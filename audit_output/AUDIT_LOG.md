# Audit Log

**Audit date:** 23 Oct 2026.
**Auditor:** Claude Code session, with no human reviewer.
**Constraint:** the originals were not modified.

## 1. File inventory (Stage A)

### Repository root (`/home/user/auditx`)

| File | Notes |
|---|---|
| `README.md` | 13 bytes ("# auditx / new") |
| `xxxx.zip` | 1.83 MB; SHA-256 recorded in `audit_workspace/zip_sha256_before.txt` and re-checked unchanged after the audit |

### Inside `xxxx.zip`

Extracted to `audit_workspace/extracted/`; `__MACOSX` metadata was skipped.

| Path | Modified (zip time) | Role |
|---|---|---|
| `SRH_Thesis_Template/main.tex` | 2026-10-23 07:25 | Thesis master file (title page, abstract, declaration) |
| `Chapters/Chapter1–5.tex` | 23 Oct 07:22–07:28 | Thesis chapters (latest edits) |
| `Appendices/AppendixA–C.tex` | 23 Oct 07:04–07:17 | Search log, extraction form, included studies |
| `bibliography.bib` | 22 Oct 21:08 | 114 entries |
| `Thesis.cls`, `vector.sty`, `lstpatch.sty`, `SRH_Logo.png`, `Tables/HEIreg.tex`, `Chapters/Dataset.png`, `.DS_Store` | — | Template files. `HEIreg.tex` and `Dataset.png` are not referenced by the chapters |
| `review_data/README.txt` | 22 Oct 21:00 | Data description |
| `review_data/query.json` | 22 Oct 21:00 | OpenAlex filter, run date 2026-10-22 |
| `review_data/records.jsonl` | 22 Oct 21:00 | 1,807 records |
| `review_data/ta_final.json` | 22 Oct 21:00 | 1,797 final TA decisions |
| `review_data/agreement.json` | 22 Oct 21:00 | Agreement statistics |
| `review_data/included_final.json` | 22 Oct 21:00 | 120 extraction records |
| `review_data/citation_search.json` | 22 Oct 21:00 | Citation-search counts |

### Latest thesis version

Only one version exists: the LaTeX source above. It is identified as current because it is the only copy, its chapter timestamps (23 Oct) post-date the review data (22 Oct), and its content cites the 22 Oct review run.

### Missing (recorded explicitly, not assumed)

- Thesis PDF; DOCX or Markdown versions.
- Original research-paper PDFs: **none of the 120**.
- Run-level screening outputs (run 1 and run 2), and the adjudication outputs.
- The full-text eligibility log (64/133 split; the 77 exclusion reasons).
- The search script; the citation-search records and the seed list.
- The model prompts for screening, extraction and verification.
- Any record of the author's manual checks; previous audit reports; screening spreadsheets.

## 2. Actions taken (chronological)

1. Listed the repository, inspected the zip, recorded its SHA-256, and extracted it to `audit_workspace/extracted/`.
2. Read the complete thesis source: `main.tex`, Chapters 1–5 and Appendices A–C.
3. Profiled every field of `records.jsonl`, `ta_final.json` and `included_final.json`.
4. Wrote and ran `audit_workspace/scripts/reconcile.py`, which recomputes every reported count → `reconciliation_output.txt`.
5. Investigated the discrepancies with ad-hoc scripts (all read-only):
   - duplicates and the de-duplication choices;
   - possible kappa splits;
   - independence groupings, comparing three counting schemes to reproduce 44/41/52;
   - country, mediation and dimension-study lists;
   - E5 conformity, tier rules and focal-context coding;
   - a keyword search of included abstracts for e-commerce and platform terms.
6. Wrote and ran `quote_check.py`, which compares all 248 extracted quotations with the OpenAlex abstracts using normalised substring matching plus a ≥ 0.90 sequence-match fallback → `QUOTE_CHECK.csv`.
7. Dumped the extraction records and abstracts of all 38 thesis-cited included studies, plus 5 others, and compared each thesis statement with the extraction and the abstract manually.
8. Attempted to access the original sources:
   - `curl` to api.openalex.org, doi.org, api.unpaywall.org, semanticscholar.org and europepmc.org → **HTTP 403 from the environment's network proxy (policy denial)**;
   - WebFetch → DNS failure (`ENOTFOUND`).
9. Ran 5 web searches for bibliographic metadata:
   - Guo 2025: found the publisher/repository record; the snippet confirms 322 SMEs, China, cross-border platforms.
   - Wang 2026: found the bibliographic record and DOI; no results.
   - Srahin 2026 and Texeira 2026: not found.
   - TPM/tpmap.org: no evidence of hijacking; tpmap.org is listed as the journal's site.

   These are secondary sources only. They were used for metadata, never as verification of results.
10. Wrote and ran `citation_audit.py`, which compares `\cite` keys with `bibliography.bib`, the bib metadata with the review data, and the retrieval status of the key prior studies → `citation_audit_output.txt`.
11. Parsed Appendix C against the data: 120 of 120 present; tiers and quality ratings match.
12. Wrote and ran `build_study_audit.py` → `STUDY_EVIDENCE_AUDIT.csv`/`.xlsx` and `MISSING_SOURCES.csv`.
13. Wrote the reports: DATA_RECONCILIATION, CLAIM_VERIFICATION, THESIS_ISSUES and AUDIT_SUMMARY.

## 3. Methods and decision rules used by the auditor

**Verdict statuses.** Only the five requested statuses are used.

- **Verified** requires an inspected original paper. Because none was available, **no row is Verified**.
- **Partially verified:** the claim or quotation is consistent with, or found in, the OpenAlex abstract, or is otherwise supported by the data and abstract, while the full-text details remain unchecked.
- **Mismatch:** the abstract or the data contradict the thesis or the extraction.
- **Needs checking:** the available evidence is insufficient, or internally inconsistent, to judge a claim the thesis relies on.
- **Source unavailable:** nothing beyond the title/metadata was available. This applies to the 9 title-only inclusions and to `li2025`.

**Abstracts are treated as part of the source but not as the paper.** Everything verified against an abstract is labelled as such.

**Page numbers.** None are recorded in the extraction, and none were invented.

## 4. Calculations performed

- All PRISMA, tier, year, design, construct, outcome, journal, sample-size, method, country and quality counts.
- Quality-rule recomputation for the 21 appraised studies.
- Hypothesis category counts under three independence schemes.
- AI→CA direction counts; mediation-type counts; the dimension-study list.
- Kappa feasibility: all 56 possible disagreement splits.
- Bib/data/OpenAlex year and DOI comparisons.
- Quote-to-abstract matching (248 quotations).

## 5. Checks that could not be completed

- **Verification of any study against its full text:** 0 of 120. The 84 full-text quotations and all numeric estimates taken from full texts (e.g. 0.519, 0.336, 0.445, 0.071, 0.05, 0.110, 0.067) remain unchecked, and page numbers are unknown.
- **Independent recomputation of Cohen's kappa:** paired run decisions are absent.
- **The full-text-stage PRISMA breakdown** (64/133; 48/17/8/3/1): no data.
- **Re-running the OpenAlex query and the benchmark filter test** (1,188 records): network blocked.
- **The citation-search records:** not supplied.
- **Peer-review/legitimacy checks of flagged journals:** Firmansyah, Noor, Malik/TPM, Dzreke ×2, Wei, Arowolo and others.
- **Whether the two Alnofeli 2025 papers share data.**
- **Thesis page numbers, layout, and the rendering of the figures and tables:** no PDF and no TeX compiler.

## 6. Output files

```
audit_output/
  AUDIT_SUMMARY.md
  DATA_RECONCILIATION.md
  CLAIM_VERIFICATION.md
  THESIS_ISSUES.md
  AUDIT_LOG.md
  STUDY_EVIDENCE_AUDIT.csv   (120 rows; one per included study)
  STUDY_EVIDENCE_AUDIT.xlsx  (sheets: Study audit, Quote check, Missing sources)
  QUOTE_CHECK.csv            (248 rows; one per extracted quotation)
  MISSING_SOURCES.csv        (120 rows, prioritised: 22 critical, 28 high, 70 normal)
  reconciliation_output.txt, quote_check_output.txt, citation_audit_output.txt (raw script output)
audit_workspace/
  scripts/  reconcile.py, quote_check.py, citation_audit.py, build_study_audit.py
  extracted/ (copy of zip contents; not committed)
  cited_extractions.txt, PROGRESS_LOG.md, zip_sha256_before.txt
```

## 7. How to reproduce

```
python3 -I audit_workspace/scripts/reconcile.py audit_workspace/extracted/SRH_Thesis_Template/review_data
python3 -I audit_workspace/scripts/quote_check.py audit_workspace/extracted/SRH_Thesis_Template/review_data audit_output/QUOTE_CHECK.csv
python3 -I audit_workspace/scripts/citation_audit.py audit_workspace/extracted/SRH_Thesis_Template
python3 -I audit_workspace/scripts/build_study_audit.py audit_workspace/extracted/SRH_Thesis_Template audit_output
```

First extract the zip with `unzip -q xxxx.zip -d audit_workspace/extracted -x '__MACOSX/*'`.

---

## v2 correction pass (actions)

1. Created the working copy `thesis_corrected/SRH_Thesis_Template/` and the backups (`backups/SRH_Thesis_Template_original/`, `backups/audit_output_v1/`). Recorded the original file hashes (`backups/original_source_sha256.txt`). No git operations.
2. Installed TeX Live and biber with apt. Compiled the unmodified original as a baseline (90 pages, clean) and saved `backups/original_thesis_compiled.pdf`.
3. Wrote `apply_corrections.py`, which applies corrections D1–D3 to a copy of the data, annotates the provisional cases and recomputes all counts.
4. Edited `main.tex`, Chapters 2–5, Appendix C and `bibliography.bib` (two name commas). Full diff: `audit_output/thesis_changes.diff`.
5. Compiled the corrected thesis (93 pages, clean) and visually checked Fig. 4.1, Table 4.2 and Fig. 4.4.
6. Wrote `validate_thesis.py`: 49/49 checks pass. Re-ran `reconcile.py` (counts unchanged; made deterministic) and `citation_audit.py` on the corrected source.
7. Rebuilt `STUDY_EVIDENCE_AUDIT.csv`/`.xlsx`, adding the column "Thesis correction (v2)". Gafsi verdict revised.
8. Wrote CORRECTION_LOG.md, UNRESOLVED_ISSUES.md and VALIDATION_SUMMARY.md, and appended v2 sections to the existing reports.

**Still not possible:** verification against any original paper (network policy unchanged; no PDFs supplied).
