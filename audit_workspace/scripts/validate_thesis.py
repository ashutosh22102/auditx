"""Validate the compiled corrected thesis against the corrected review data.

Usage: python3 -I validate_thesis.py <corrected_thesis_dir>
Requires pdftotext. Checks that corrected values appear, superseded values are gone,
and reports the PDF page of each check.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

root = Path(sys.argv[1])
C = json.loads((root / "review_data_corrected/corrected_counts.json").read_text(encoding="utf-8"))
txt = subprocess.run(["pdftotext", "-layout", str(root / "main.pdf"), "-"], capture_output=True, text=True).stdout
pages = txt.split("\f")
norm = lambda s: re.sub(r"\s+", " ", s.replace("­", "").replace("-\n", ""))
header = re.compile(r"^\s*(\d+ [A-Z][^\n]*?|[A-Z][^\n]*?)\s{5,}[ivxlc\d]+\s*$")
npages = [norm("\n".join(l for l in p.split("\n")[:2] if not header.match(l)) + "\n" + "\n".join(p.split("\n")[2:])) for p in pages]
alltext = " ".join(npages)


def where(pat):
    hits = [i + 1 for i, p in enumerate(npages) if re.search(pat, p)]
    if not hits:  # text broken across a page boundary
        hits = ["%d-%d" % (i + 1, i + 2) for i in range(len(npages) - 1)
                if re.search(pat, norm(npages[i][-400:] + " " + npages[i + 1][:400]))]
    return hits


ok = fail = 0


def must(pat, label):
    global ok, fail
    w = where(pat)
    status = "PASS" if w else "FAIL"
    ok, fail = (ok + 1, fail) if w else (ok, fail + 1)
    print("%-4s present  %-60s pdf pages %s" % (status, label, w[:8]))


def mustnot(pat, label):
    global ok, fail
    w = where(pat)
    status = "PASS" if not w else "FAIL"
    ok, fail = (ok + 1, fail) if not w else (ok, fail + 1)
    print("%-4s absent   %-60s %s" % (status, label, ("found on pdf pages %s" % w[:8]) if w else ""))


print("PDF pages:", len(pages) - 1)
must(r"119 independent studies", "119 independent studies (sec 4.1)")
must(r"94 independent samples", "94 independent empirical samples (sec 4.1) = %d" % C["independent_empirical_samples"])
must(r"119 independent; 9 provisional", "PRISMA box: 119 independent, 9 provisional")
mustnot(r"118 independent", "superseded '118 independent samples'")
must(r"28 were assessed in full text, 83 on their abstract and 9 on their title", "access split 28/83/9 = %s" % C["access_included"])
must(r"3 were rated high, 8 moderate and 9 low", "quality 3/8/9 = %s" % C["quality_empirical"])
must(r"For the other 75", "75 not assessable")
must(r"66 were accessible only as an abstract, 8 only as a title", "n.a. breakdown 66/8/1 = %s" % C["not_assessable_breakdown"])
must(r"Among the 20 studies that could be appraised", "appraised = %d" % C["appraised"])
must(r"met in 10 studies, and an indirect effect was estimated directly in 10", "Q4/Q6 among appraised = %d/%d" % (C["Q4_met_appraised"], C["Q6_met_appraised"]))
must(r"only four could be appraised: three were rated moderate and one low", "Tier 1 = %s" % C["tier1_quality"])
must(r"among the eleven studies of high or moderate quality, seven", "H1 sensitivity 11 H/M, 7 indirect = %d/%d" % (C["high_moderate"], C["sens_H1_indirect_in_HM"]))
must(r"all 12 relevant studies in this subset, 8 of them", "H2 sensitivity 12/8 = %d/%d" % (C["sens_H2_any_in_appraised"], C["sens_H2_any_in_HM"]))
must(r"The 42 studies with indirectly relevant evidence", "H2 indirect 42 = %s" % C["H2"])
must(r"and 42 studies relate AI", "RQ2 42")
mustnot(r"\b41 studies\b", "superseded H2 '41 studies'")
must(r"The 51 studies with indirectly relevant evidence", "H6 indirect 51 = %s" % C["H6"])
must(r"Fifty-one studies", "RQ4 fifty-one")
mustnot(r"Fifty-two|52 studies with indirectly", "superseded H6 '52'")
must(r"H2 3 42 1", "Table 4.2 H2 row")
must(r"H4 0 1 0", "Table 4.2 H4 row = %s" % C["H4"])
must(r"H5 0 1 0", "Table 4.2 H5 row = %s" % C["H5"])
must(r"H6 0 51 1", "Table 4.2 H6 row")
mustnot(r"strategic flexibility", "superseded Texeira moderator 'strategic flexibility'")
must(r"sustainable food innovation orientation", "corrected Texeira moderator")
mustnot(r"[Ff]our of the six hypotheses", "superseded 'four of the six'")
mustnot(r"direct effect of AI disappears", "superseded 'direct effect disappears'")
mustnot(r"strongest studies, the direct", "superseded 'strongest studies' claim")
mustnot(r"only seven concern", "superseded 'only seven concern'")
must(r"only four empirical studies concern", "four empirical e-commerce/platform studies")
mustnot(r"Most studies do not report the country", "superseded country statement")
must(r"Thirty of the 95 empirical studies do not report", "country 30 of 95 = %d" % C["country_not_reported_empirical"])
mustnot(r"Almost all empirical studies are cross-sectional", "superseded 'almost all cross-sectional'")
mustnot(r"74 of the 95", "superseded '74 of the 95'")
must(r"75 of the 95", "75 of the 95 (sec 5.4)")
mustnot(r"For platform firms, the evidence on sellers", "complementor evidence applied to platform firms")
mustnot(r"are checked by the author", "unsupported 'are checked by the author'")
mustnot(r"re-screening check", "undefined 're-screening check'")
mustnot(r"documented script", "unsupported 'documented script'")
must(r"Only three are quantitative", "dimension studies: three quantitative")
must(r"Kabir et al\. \(2025\)", "Appendix C missing author restored")
mustnot(r"^- et al\.|\s- et al\. \(2025\)", "Appendix C '- et al.'")
must(r"Claude, Anthropic\), which supported the screening", "declaration AI disclosure")
must(r"no hypothesis is supported, and all six are at most partly supported", "abstract judgement wording")
must(r"none specifies dynamic capabilities as a higher-order construct", "RQ4 higher-order statement (dc_order higher = %d)" % C["dc_higher_order"])
must(r"Almheiri et al\. \(2024\)", "Almheiri 2024 citation")
must(r"Almheiri et al\. \(2025\)", "Almheiri 2025 citation (Appendix C now matches bibliography)")
mustnot(r"\?\?|\[\?\]", "unresolved references (?? or [?])")
mustnot(r"Citation .* undefined", "undefined citations in text")
print("\nPASS %d  FAIL %d" % (ok, fail))
