"""Check every extracted quotation in included_final.json against the OpenAlex abstract.

Usage: python3 -I quote_check.py <review_data_dir> <out_csv>
A quote 'found in abstract' is verified against the abstract only (not the full paper).
A quote not found in the abstract may still be in the full text, which is not available here.
"""
import csv
import json
import re
import sys
import unicodedata
from difflib import SequenceMatcher
from pathlib import Path

d = Path(sys.argv[1])
inc = json.loads((d / "included_final.json").read_text(encoding="utf-8"))
recs = {}
for line in (d / "records.jsonl").read_text(encoding="utf-8").splitlines():
    if line.strip():
        r = json.loads(line)
        recs.setdefault(r["id"], r)


def norm(s):
    s = unicodedata.normalize("NFKC", s or "")
    s = s.replace("‐", "-").replace("‑", "-").replace("–", "-").replace("—", "-")
    s = s.replace("‘", "'").replace("’", "'").replace("“", '"').replace("”", '"')
    s = re.sub(r"-\s+", "-", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


def best_ratio(q, a):
    if not q or not a:
        return 0.0
    sm = SequenceMatcher(None, a, q, autojunk=False)
    m = sum(b.size for b in sm.get_matching_blocks())
    return m / len(q)


rows = []
for x in inc:
    ab = norm(recs[x["id"]].get("abstract"))
    for i, p in enumerate(x["paths"]):
        q = norm(p.get("quote"))
        q_core = q.strip(" .\"'")
        if not q_core:
            status = "no quote"
        elif not ab:
            status = "no abstract available"
        elif q_core in ab:
            status = "verbatim in abstract"
        else:
            r = best_ratio(q_core, ab)
            status = "near-verbatim in abstract (%.2f)" % r if r >= 0.9 else "not in abstract"
        if status == "not in abstract" and x["fulltext_used"]:
            status = "not in abstract (full text claimed; unchecked)"
        rows.append({
            "study_id": x["id"], "bibkey": x.get("bibkey", ""), "first_author": x["first"], "year": x["yr"],
            "fulltext_used": x["fulltext_used"], "path_no": i + 1, "path": p["path"], "direction": p["direction"],
            "estimate": p["estimate"], "result_type": p["result_type"], "quote": p.get("quote", ""),
            "quote_check": status,
        })

with open(sys.argv[2], "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)

from collections import Counter
print("quotes:", len(rows))
print(Counter(r["quote_check"].split(" (")[0] for r in rows))
print("by fulltext_used:")
print(Counter((r["fulltext_used"], r["quote_check"].split(" (")[0]) for r in rows))
for r in rows:
    if r["quote_check"] == "not in abstract":
        print("  ABSTRACT-ONLY STUDY, QUOTE NOT FOUND:", r["first_author"], r["year"], r["bibkey"], r["path"], "|", r["quote"][:160])
