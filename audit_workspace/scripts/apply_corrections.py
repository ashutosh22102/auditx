"""Create a corrected copy of included_final.json and recompute every count used in the thesis.

Usage: python3 -I apply_corrections.py <original_review_data_dir> <out_dir>
The original files are read only. Writes:
  <out_dir>/included_final_corrected.json
  <out_dir>/corrections_applied.json
  <out_dir>/corrected_counts.json
and prints a human-readable summary.
"""
import copy
import json
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path

src = Path(sys.argv[1])
out = Path(sys.argv[2])
out.mkdir(parents=True, exist_ok=True)
orig = json.loads((src / "included_final.json").read_text(encoding="utf-8"))
recs = {}
for line in (src / "records.jsonl").read_text(encoding="utf-8").splitlines():
    if line.strip():
        r = json.loads(line)
        recs.setdefault(r["id"], r)
data = copy.deepcopy(orig)
by_id = {x["id"]: x for x in data}
log = []


def change(sid, field, new, reason, evidence, status):
    old = by_id[sid].get(field)
    by_id[sid][field] = new
    log.append(dict(study=sid, author_year="%s %s" % (by_id[sid]["first"], by_id[sid]["yr"]), field=field,
                    old=old, new=new, reason=reason, evidence=evidence, status=status))


# C1 Almheiri et al. (2026) is not the same sample as Almheiri et al. (2024/2025)
change("W7203683920", "same_sample_as", None,
       "Incorrect same-sample link to the Almheiri 2024/2025 public-manager sample.",
       "OpenAlex abstract of W7203683920: survey data from 400 hotel managers in the UAE; abstracts of W4391349566 and "
       "W4405869520: 344 public managers. Different populations and sample sizes.",
       "confirmed (abstract level)")

# C2 Mukhopadhyay 2024 was rated from the abstract only; the thesis rule says such studies cannot be appraised
mid = next(x["id"] for x in data if x.get("bibkey") == "mukhopadhyay2024")
change(mid, "overall_quality", "not assessable",
       "Rated 'moderate' although fulltext_used=False; Section 3.5 states that the quality of abstract-only studies cannot be assessed.",
       "included_final.json: fulltext_used=false; every other appraised study used the full text.",
       "confirmed (rule consistency)")

# C3 Li 2026: author-assigned seizing (absorptive capacity) and transforming (opportunity recognition) mediators
lid = next(x["id"] for x in data if x.get("bibkey") == "li2026")
newcat = {"H2": ["indirectly relevant"], "H4": ["indirectly relevant"], "H5": ["indirectly relevant"]}
change(lid, "categories", newcat,
       "Apply Panel A and the assignment rule as for Noor 2026 (H3): an estimated indirect effect through a mediator that the "
       "study itself assigns to one DC dimension is 'indirectly relevant' for that dimension's hypothesis; such estimates are "
       "not also counted for H6 ('no estimate counts for both').",
       "Abstract of Li 2026 frames absorptive capacity as 'a central seizing capability' and entrepreneurial opportunity "
       "recognition as 'a transforming pathway'; extraction records specific indirect effects 0.067 and 0.057 (full-text "
       "values, not verified by the auditor).",
       "rule consistency; estimates unverified")

title_only = [x["id"] for x in data if not (recs[x["id"]].get("abstract") or "").strip() and not x["fulltext_used"]]
for sid in title_only:
    by_id[sid]["eligibility_status"] = "provisional: retained on title only (no abstract or full text accessible)"
e5_borderline = {
    "li2026": "measures opportunity sensing capability and frames absorptive capacity/opportunity recognition as seizing/transforming",
    "sofiyan2026": "measures dynamic managerial capability (DMC) alongside AI capability",
    ("Shore", 2024): "grounded in the contingent view of dynamic capability; entrepreneurial resilience as DC-type outcome",
    ("Tian", 2023): "abstract defines supply chain resilience as a dynamic capability",
}
for x in data:
    k = x.get("bibkey")
    key = k if k in e5_borderline else (x["first"], x["yr"])
    if key in e5_borderline:
        x["e5_rationale"] = e5_borderline[key]
provisional_h1 = {"giang2026": "AI effect reported jointly with four other capabilities",
                  "waqas2024": "AI effect reported jointly with BDA and IoT capabilities",
                  "almereb2026": "generative AI coded as capability by the verification run",
                  "almamary2025": "role of competitive advantage (outcome vs. dimension) ambiguous",
                  "gafsi2026": "dependent variable 'competitive performance'; finding worded as 'firm performance'",
                  "firmansyah2025": "low quality; AI capability modelled as mediator of KMC; journal peer review unverified"}
for x in data:
    if x.get("bibkey") in provisional_h1:
        x["h1_direct_caveat"] = provisional_h1[x["bibkey"]]

(out / "included_final_corrected.json").write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
(out / "corrections_applied.json").write_text(json.dumps(dict(changes=log, title_only=title_only,
                                                              e5_borderline=[x["id"] for x in data if "e5_rationale" in x],
                                                              provisional_h1=list(provisional_h1)), ensure_ascii=False, indent=1),
                                               encoding="utf-8")

# ---------------- recompute -----------------
C = {}
emp = [x for x in data if x["design"] != "conceptual"]
groups = {x["id"]: (x.get("same_sample_as") or x["id"]) for x in data}
C["publications"] = len(data)
C["independent_publications"] = len(set(groups.values()))
C["empirical"] = len(emp)
C["independent_empirical_samples"] = len({groups[x["id"]] for x in emp})
C["conceptual"] = len(data) - len(emp)
C["title_only"] = len(title_only)
C["access_included"] = dict(Counter("full text" if x["fulltext_used"] else ("abstract" if (recs[x["id"]].get("abstract") or "").strip() else "title only") for x in data))
C["quality_empirical"] = dict(Counter(x["overall_quality"] for x in emp))
appr = [x for x in emp if x["overall_quality"] in ("high", "moderate", "low")]
hm = [x for x in appr if x["overall_quality"] in ("high", "moderate")]
C["appraised"] = len(appr)
C["high_moderate"] = len(hm)
na = [x for x in emp if x["overall_quality"] == "not assessable"]
C["not_assessable_breakdown"] = dict(Counter("full text, insufficient reporting" if x["fulltext_used"] else ("abstract only" if (recs[x["id"]].get("abstract") or "").strip() else "title only") for x in na))
t1 = [x for x in data if x["tier"] == 1]
C["tier1_quality"] = dict(Counter(x["overall_quality"] for x in t1))
for q in ["Q2", "Q4", "Q5", "Q6", "Q7"]:
    C["%s_met_appraised" % q] = sum(x["quality"].get(q) == "met" for x in appr)


def hcounts(H):
    g = defaultdict(set)
    for x in data:
        for c in x["categories"].get(H, []):
            g[groups[x["id"]]].add(c)
    cnt = Counter()
    for s in g.values():
        for c in ("directly reported", "contradictory", "indirectly relevant"):
            if c in s:
                cnt[c] += 1
                break
    return dict(cnt)


for H in ["H1", "H2", "H3", "H4", "H5", "H6"]:
    C[H] = hcounts(H)
C["H1_direct_robust"] = sorted(x["bibkey"] for x in data if "directly reported" in x["categories"].get("H1", []) and x.get("bibkey") not in provisional_h1)
C["sens_H1_direct_in_appraised"] = [x["first"] for x in appr if "directly reported" in x["categories"].get("H1", [])]
C["sens_H1_indirect_in_HM"] = sum("indirectly relevant" in x["categories"].get("H1", []) for x in hm)
C["sens_H1_contra_in_HM"] = sum("contradictory" in x["categories"].get("H1", []) for x in hm)
C["sens_H2_any_in_appraised"] = sum(bool(x["categories"].get("H2")) for x in appr)
C["sens_H2_any_in_HM"] = sum(bool(x["categories"].get("H2")) for x in hm)
C["sens_H2_direct_in_appraised"] = sum("directly reported" in x["categories"].get("H2", []) for x in appr)
C["hm_list"] = sorted("%s %s (%s)" % (x["first"], x["yr"], x["overall_quality"]) for x in hm)
C["dc_higher_order"] = sum(x["dc_order"] == "higher_order" for x in data)
C["focal_context"] = dict(Counter(x["context"] for x in data if x["context"] != "none"))
C["years"] = dict(sorted(Counter(x["yr"] for x in data).items()))
C["country_not_reported_empirical"] = sum(x["country"].startswith("not reported") or "country not reported" in x["country"] for x in emp)
ss = [x["sample_size"] for x in emp if isinstance(x["sample_size"], (int, float))]
C["n_reported"] = len(ss)
C["median_n"] = statistics.median(ss)
(out / "corrected_counts.json").write_text(json.dumps(C, ensure_ascii=False, indent=1), encoding="utf-8")
for k, v in C.items():
    print("%-32s %s" % (k, v))
print("\nchanges:", len(log), "| title-only:", len(title_only))
