"""Independent recalculation of the review counts reported in the thesis.

Usage: python3 -I reconcile.py <review_data_dir>
Reads only; writes nothing. Output is captured into audit_output/reconciliation_output.txt.
"""
import json
import re
import statistics
import sys
import collections as C
from pathlib import Path

d = Path(sys.argv[1])
raw_lines = (d / "records.jsonl").read_text(encoding="utf-8").splitlines()
records = [json.loads(l) for l in raw_lines if l.strip()]
ta = json.loads((d / "ta_final.json").read_text(encoding="utf-8"))
inc = json.loads((d / "included_final.json").read_text(encoding="utf-8"))
agr = json.loads((d / "agreement.json").read_text(encoding="utf-8"))
cit = json.loads((d / "citation_search.json").read_text(encoding="utf-8"))
rec_by_id = {}
for r in records:
    rec_by_id.setdefault(r["id"], r)


def h(title):
    print("\n## " + title)


def show(label, value, thesis=None):
    flag = ""
    if thesis is not None:
        flag = "  [thesis: %s] %s" % (thesis, "OK" if str(value) == str(thesis) else "DIFFERS")
    print("%-70s %s%s" % (label, value, flag))


h("A. Identification and de-duplication")
show("Lines in records.jsonl", len(records), 1807)
show("Unique OpenAlex IDs in records.jsonl", len(rec_by_id))
show("Records in ta_final.json (screened)", len(ta), 1797)
show("Records not carried into screening (duplicates removed)", len(records) - len(ta), 10)
not_in_ta = [i for i in rec_by_id if i not in ta]
show("  of which unique IDs absent from ta_final", len(not_in_ta))
show("  of which repeated OpenAlex ID lines", len(records) - len(rec_by_id))
show("ta_final IDs absent from records.jsonl", len([k for k in ta if k not in rec_by_id]))

h("B. Title/abstract screening")
dec = C.Counter(v["decision"] for v in ta.values())
show("Included at TA", dec["include"], 197)
show("Excluded at TA", dec["exclude"], 1600)
reasons = C.Counter(v["reason"] for v in ta.values() if v["decision"] == "exclude")
for code, thesis in [("E5", 1032), ("E4", 413), ("E1", 147), ("E6", 8)]:
    show("  TA exclusions " + code, reasons.get(code, 0), thesis)
show("  Other TA exclusion codes", {k: v for k, v in reasons.items() if k not in ("E5", "E4", "E1", "E6")})
src = C.Counter(v["source"] for v in ta.values())
show("Records where both runs agreed (source=agreed)", src["agreed"])
show("Records resolved by third run (source=adjudicator)", src["adjudicator"], 55)
show("Adjudicated -> include / exclude", dict(C.Counter(v["decision"] for v in ta.values() if v["source"] == "adjudicator")))
show("Run-level decisions stored for each pass?", "NO (only final decision + source flag)")

h("C. Agreement statistic (consistency check only - paired run data absent)")
n = len(ta)
ag_inc = sum(1 for v in ta.values() if v["source"] == "agreed" and v["decision"] == "include")
po = src["agreed"] / n
show("Observed agreement recomputed = agreed/screened", round(po, 6), round(agr["agreement"], 6))
show("Reported kappa (agreement.json)", round(agr["kappa"], 6))
splits = []
for d1 in range(0, src["adjudicator"] + 1):
    d2 = src["adjudicator"] - d1
    p1 = (ag_inc + d1) / n
    p2 = (ag_inc + d2) / n
    pe = p1 * p2 + (1 - p1) * (1 - p2)
    k = (po - pe) / (1 - pe)
    splits.append((d1, d2, k))
exact = [(a, b) for a, b, k in splits if abs(k - agr["kappa"]) < 1e-9]
show("Disagreement splits (run1-only incl, run2-only incl) reproducing kappa", exact)
show("Kappa range over all possible splits", "%.4f-%.4f" % (min(s[2] for s in splits), max(s[2] for s in splits)))

h("D. Eligibility (full-text) stage")
incl_ids = [x["id"] for x in inc]
ta_inc = {k for k, v in ta.items() if v["decision"] == "include"}
show("Studies in included_final.json", len(inc), 120)
show("Included studies that were not TA-includes", len([i for i in incl_ids if i not in ta_inc]))
show("TA-includes with no record in included_final (FT exclusions)", len(ta_inc - set(incl_ids)), 77)
show("Exclusion reasons for these 77 stored in any file?", "NO")
show("Full-text vs abstract status for the 197 stored?", "NO (only for the 120 included)")
ft = C.Counter(x["fulltext_used"] for x in inc)
show("Included with fulltext_used = True", ft[True])
show("Included with fulltext_used = False", ft[False])
noabs = [x for x in inc if not (rec_by_id[x["id"]].get("abstract") or "").strip()]
show("Included with no abstract in records.jsonl AND fulltext_used False",
     len([x for x in noabs if not x["fulltext_used"]]))
for x in noabs:
    print("    title-only: %s %s (%s) %s" % (x["first"], x["yr"], x["id"], x["title"][:70]))

h("E. Independence of samples")
links = [(x["id"], x["first"], x["yr"], x.get("same_sample_as"), x["sample_size"]) for x in inc if x.get("same_sample_as")]
for l in links:
    print("    same_sample_as link:", l)
groups = {}
for x in inc:
    groups[x["id"]] = x.get("same_sample_as") or x["id"]
show("Independent samples if data links applied as stored", len(set(groups.values())), 118)
show("Independent samples counting only the Almheiri 2024/2025 pair", len(inc) - 1, 118)

h("F. Study characteristics")
show("Design distribution", dict(C.Counter(x["design"] for x in inc)))
emp = [x for x in inc if x["design"] != "conceptual"]
show("Empirical (non-conceptual) studies", len(emp), 95)
show("Conceptual studies", len(inc) - len(emp), 25)
show("Cross-sectional surveys", sum(x["design"] == "cross_sectional_survey" for x in inc), 65)
show("Tier distribution", dict(sorted(C.Counter(x["tier"] for x in inc).items())), "{1: 22, 2: 73, 3: 25}")
show("Tier 3 == conceptual?", sorted(C.Counter((x["tier"], x["design"] == "conceptual") for x in inc).items()))
show("Year distribution", dict(sorted(C.Counter(x["yr"] for x in inc).items())))
show("Published 2024 or later", sum(x["yr"] >= 2024 for x in inc), 112)
show("Published 2026", sum(x["yr"] == 2026 for x in inc), 57)
show("AI construct", dict(C.Counter(x["ai_construct_type"] for x in inc)), "{'use': 52, 'capability': 46, 'integration': 22}")
show("DC construct", dict(C.Counter(x["dc_construct"] for x in inc)))
show("Outcome type", dict(C.Counter(x["outcome_type"] for x in inc)))
show("Persistence measured", [x["first"] + " " + str(x["yr"]) for x in inc if x["persistence_measured"]])
show("Distinct journals", len({x["journal"] for x in inc}), 105)
show("Max studies per journal", C.Counter(x["journal"] for x in inc).most_common(3))
ss = [x["sample_size"] for x in emp if isinstance(x["sample_size"], (int, float))]
show("Empirical studies with numeric sample size", len(ss), 80)
show("Median sample size", statistics.median(ss) if ss else None, 312)
show("Sample size < 150", sum(s < 150 for s in ss), 16)
am = C.Counter(x["analysis_method"] for x in inc)
pls = sum(v for k, v in am.items() if k.startswith("PLS-SEM"))
show("analysis_method starting 'PLS-SEM'", pls, 39)
show("analysis_method containing 'PLS'", sum(v for k, v in am.items() if "PLS" in k))
show("analysis_method containing 'CB-SEM'", sum(v for k, v in am.items() if "CB-SEM" in k), 9)
show("Respondents containing 'multiple'", sum("multiple" in x["respondents"] for x in inc), 9)
show("Country not reported (empirical)", sum(x["country"] in ("not reported", "", None) for x in emp), 30)
show("Country not reported (all 120)", sum(x["country"] in ("not reported", "", None) for x in inc))
ctry = C.Counter()
for x in inc:
    for c in re.split(r"[;,/]| and ", x["country"] or ""):
        c = c.strip()
        if c and c != "not reported":
            ctry[c] += 1
show("Top countries (all studies, split on separators)", ctry.most_common(8))
show("Studies with country containing 'China'", sum("China" in (x["country"] or "") for x in inc), 10)

h("G. Quality appraisal")
show("Overall quality (all)", dict(C.Counter(x["overall_quality"] for x in inc)))
show("Overall quality (empirical)", dict(C.Counter(x["overall_quality"] for x in emp)), "3 high, 9 moderate, 9 low, 74 n.a.")
na = [x for x in emp if x["overall_quality"] == "not assessable"]
show("'not assessable' with fulltext_used False", sum(not x["fulltext_used"] for x in na), 74)
show("'not assessable' with fulltext_used True", sum(x["fulltext_used"] for x in na))
appr = [x for x in emp if x["overall_quality"] in ("high", "moderate", "low")]
show("Appraised empirical studies", len(appr), 21)
show("Appraised with fulltext_used True", sum(x["fulltext_used"] for x in appr))
show("Full text used but conceptual", sum(x["fulltext_used"] for x in inc if x["design"] == "conceptual"))
t1 = [x for x in inc if x["tier"] == 1]
show("Tier 1 quality", dict(C.Counter(x["overall_quality"] for x in t1)), "4 moderate, 1 low, 17 n.a.")
for q, lab, th in [("Q5", "Q5 temporal ordering met", 2), ("Q4", "Q4 CMB met", 11), ("Q6", "Q6 indirect effect met", 13),
                   ("Q2", "Q2 sampling met", 3), ("Q7", "Q7 alternative explanations met", 2)]:
    show(lab + " (appraised studies)", sum(x["quality"].get(q) == "met" for x in appr), th)
    show(lab + " (all studies)", sum(x["quality"].get(q) == "met" for x in inc))
# check the overall-quality rule from Table 3.3
keys = ["Q3", "Q4", "Q6", "Q8"]
rule_mismatch = []
for x in appr:
    q = x["quality"]
    applicable_keys = [k for k in keys if q.get(k) not in ("na", None)]
    others = [k for k in q if k not in keys and q.get(k) not in ("na", None)]
    if any(q[k] == "not_met" for k in applicable_keys):
        expect = "low"
    elif all(q[k] == "met" for k in applicable_keys) and sum(q[k] == "not_met" for k in others) <= 1:
        expect = "high"
    else:
        expect = "moderate"
    if expect != x["overall_quality"]:
        rule_mismatch.append((x["first"], x["yr"], x.get("bibkey"), x["overall_quality"], expect, q))
show("Appraised studies whose rating differs from the stated rule", len(rule_mismatch))
for m in rule_mismatch:
    print("    ", m)

h("H. Hypothesis evidence categories (study-level)")
for H in ["H1", "H2", "H3", "H4", "H5", "H6"]:
    cats = C.Counter()
    for x in inc:
        for c in set(x["categories"].get(H, [])):
            cats[c] += 1
    show(H + " studies per category (raw, 120 publications)", dict(cats))
    # with independence: collapse Almheiri pair only
    pair = {"W4391349566", "W4405869520"}
    cats2 = C.Counter()
    seen_pair = set()
    for x in inc:
        for c in set(x["categories"].get(H, [])):
            if x["id"] in pair:
                if c in seen_pair:
                    continue
                seen_pair.add(c)
            cats2[c] += 1
    show(H + " per category (Almheiri pair collapsed)", dict(cats2))
show("Studies with no hypothesis category", sum(1 for x in inc if not x["categories"]))
show("  of which non-conceptual", [(x["first"], x["yr"], x["design"]) for x in inc if not x["categories"] and x["design"] != "conceptual"])

def lst(H, c):
    return sorted("%s%s(%s,%s)" % (x["first"], x["yr"], x.get("bibkey"), x["overall_quality"]) for x in inc if c in x["categories"].get(H, []))

for H, c in [("H1", "directly reported"), ("H1", "contradictory"), ("H2", "directly reported"), ("H2", "contradictory"),
             ("H3", "indirectly relevant"), ("H6", "contradictory")]:
    print("    %s %s: %s" % (H, c, lst(H, c)))
hm = [x for x in appr if x["overall_quality"] in ("high", "moderate")]
show("High/moderate studies", len(hm), 12)
show("H/M with H1 indirectly relevant", sum("indirectly relevant" in x["categories"].get("H1", []) for x in hm), 8)
show("H/M with H1 contradictory", sum("contradictory" in x["categories"].get("H1", []) for x in hm), 1)
show("Appraised with any H2 category", sum(bool(x["categories"].get("H2")) for x in appr), 13)
show("H/M with any H2 category", sum(bool(x["categories"].get("H2")) for x in hm), 9)
show("Appraised with H1 directly reported", [x["first"] for x in appr if "directly reported" in x["categories"].get("H1", [])])

h("I. Extracted paths")
ca = [p for x in inc for p in x["paths"] if p["path"] == "AI->CA"]
show("AI->CA results", len(ca), 70)
show("AI->CA direction", dict(C.Counter(p["direction"] for p in ca)), "57 positive, 7 null, 5 mixed, 1 negative")
med = [x for x in inc if any(p["path"].startswith("indirect") for p in x["paths"])]
show("Studies with any indirect_* path", len(med))
est = [x for x in inc if any(p["path"].startswith("indirect") and p["result_type"] == "estimated_indirect_effect" for p in x["paths"])]
inf = [x for x in med if x not in est]
show("  with an estimated indirect effect", len(est), 13)
show("  only inferred / untested mediation", len(inf), 38)
dims = [x for x in inc if x["dc_construct"] == "dimensions"]
show("Studies with DC dimensions", len(dims), 10)
show("  by design", dict(C.Counter(x["design"] for x in dims)), "4 conceptual, 2 qual/mixed, 4 quantitative")
for x in dims:
    print("    %s %s %s %s %s" % (x["first"], x["yr"], x.get("bibkey"), x["design"], x["analysis_method"]))
s_paths = [(x["first"], x["yr"], p["path"], p["result_type"]) for x in inc for p in x["paths"] if p["path"] in ("AI->sensing", "AI->seizing", "AI->transforming")]
show("Dimension-level paths (study, path, type)", s_paths)

h("J. Focal context (e-commerce / platform)")
show("context field", dict(C.Counter(x["context"] for x in inc)))
foc = [x for x in inc if x["context"] != "none"]
show("Studies with focal/closely related context", len(foc), 7)
for x in foc:
    print("    %s %s %s context=%s quality=%s design=%s cats=%s" % (x["first"], x["yr"], x.get("bibkey"), x["context"], x["overall_quality"], x["design"], x["categories"]))
ta_eflag = [k for k in sorted(ta_inc) if ta[k]["class"].get("ecommerce_platform")]
show("TA classification ecommerce_platform=True among 197", len(ta_eflag))
show("  of which included", len([k for k in ta_eflag if k in set(incl_ids)]))
for k in ta_eflag:
    print("    ", k, k in set(incl_ids), rec_by_id[k]["title"][:90])

h("K. Citation search")
show("Backward + forward", cit["counts"]["backward"] + cit["counts"]["forward"])
show("Unique", cit["unique"])
show("New (not in database search)", cit["new"], 678)
show("Screening decisions stored for citation records?", "NO")
