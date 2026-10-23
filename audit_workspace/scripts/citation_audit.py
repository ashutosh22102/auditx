"""Cross-check thesis citations, bibliography.bib and the review data.

Usage: python3 -I citation_audit.py <thesis_dir>
"""
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

root = Path(sys.argv[1])
tex_files = [root / "main.tex"] + sorted((root / "Chapters").glob("*.tex")) + sorted((root / "Appendices").glob("*.tex"))
cite_re = re.compile(r"\\(?:paren|text|foot|auto)?cite[s]?\*?(?:\[[^\]]*\])*\{([^}]*)\}")
cites = defaultdict(list)
for f in tex_files:
    for ln, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
        if line.lstrip().startswith("%"):
            continue
        for m in cite_re.finditer(line):
            for k in m.group(1).split(","):
                cites[k.strip()].append("%s:%d" % (f.relative_to(root), ln))

bib = (root / "bibliography.bib").read_text(encoding="utf-8")
entries = {}
for m in re.finditer(r"@(\w+)\{([^,]+),(.*?)\n\}", bib, re.S):
    body = m.group(3)
    fields = dict((k.lower(), v.strip()) for k, v in re.findall(r"(\w+)\s*=\s*\{(.*?)\}\s*,?\s*$", body, re.M))
    entries[m.group(2).strip()] = dict(type=m.group(1), **fields)

dup_keys = [k for k, v in Counter(re.findall(r"@\w+\{([^,]+),", bib)).items() if v > 1]
print("Bibliography entries:", len(entries), "| duplicate keys:", dup_keys)
print("Distinct cited keys:", len(cites))
missing = sorted(k for k in cites if k not in entries)
print("\nCITED BUT NOT IN BIBLIOGRAPHY:", missing)
for k in missing:
    print("   ", k, cites[k][:5])
uncited = sorted(k for k in entries if k not in cites)
print("\nIN BIBLIOGRAPHY BUT NEVER CITED (biblatex prints only cited entries unless \\nocite):", uncited)
print("\\nocite present:", "\\nocite" in "".join(f.read_text(encoding="utf-8") for f in tex_files))

data = json.loads((root / "review_data" / "included_final.json").read_text(encoding="utf-8"))
recs = {}
for line in (root / "review_data" / "records.jsonl").read_text(encoding="utf-8").splitlines():
    if line.strip():
        r = json.loads(line)
        recs.setdefault(r["id"], r)
by_doi = {}
for r in recs.values():
    if r.get("doi"):
        by_doi[r["doi"].lower()] = r

def nt(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())

print("\nINCLUDED STUDIES WITH BIBKEY: bib vs review data")
for x in data:
    k = x.get("bibkey")
    if not k:
        continue
    e = entries.get(k)
    if not e:
        print("  %-20s NO BIB ENTRY" % k)
        continue
    probs = []
    if str(e.get("year")) != str(x["yr"]):
        probs.append("year bib=%s data=%s" % (e.get("year"), x["yr"]))
    if (e.get("doi") or "").lower() != (x["doi"] or "").lower():
        probs.append("doi bib=%s data=%s" % (e.get("doi"), x["doi"]))
    if nt(e.get("title")) != nt(x["title"]):
        probs.append("title differs")
    if not k in cites:
        probs.append("NOT CITED")
    print("  %-20s %s" % (k, "; ".join(probs) if probs else "consistent"))

print("\nOTHER BIB ENTRIES (not included studies) found in records.jsonl by DOI:")
inc_keys = {x.get("bibkey") for x in data}
ta = json.loads((root / "review_data" / "ta_final.json").read_text(encoding="utf-8"))
for k, e in sorted(entries.items()):
    if k in inc_keys:
        continue
    r = by_doi.get((e.get("doi") or "").lower())
    if r:
        t = ta.get(r["id"])
        print("  %-20s %s -> TA %s %s" % (k, r["id"], t["decision"] if t else "not screened (dup)", t["reason"] if t else ""))

print("\nBIB ENTRIES WITHOUT DOI:", sorted(k for k, e in entries.items() if not e.get("doi")))
print("\nCITATIONS PER FILE")
per = Counter(loc.split(":")[0] for v in cites.values() for loc in v)
print(dict(per))
