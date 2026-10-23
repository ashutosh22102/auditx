# Validation Summary (v2)

## Compilation

**Toolchain.** TeX Live 2023 (`pdflatex`) and `biber`, installed in this session from the Ubuntu archive.

**Sequence.** `pdflatex` → `biber` → `pdflatex` → `pdflatex`.

| Build | Result |
|---|---|
| Original source (baseline, unmodified copy) | Compiled: 90 pages, 0 LaTeX errors, 0 undefined references, 2 biber name warnings. Saved as `backups/original_thesis_compiled.pdf`. |
| Corrected source | **Compiled: `thesis_corrected/Thesis_corrected.pdf`, 93 pages.** 0 LaTeX errors (`^!` lines), 0 undefined references or citations, 0 biber warnings, no "rerun" warning after the final pass. 5 overfull boxes (6 in the original), all ≤ 4.9 pt, in Table 4.1. |

## Data and count checks

1. **`reconcile.py` on the unchanged review data.** All counts are identical to the first audit. The script was made deterministic (sorted set iteration).
2. **`apply_corrections.py`.** Writes `review_data_corrected/` and `corrected_counts.json` (`audit_output/corrected_counts_output.txt`).
3. **`validate_thesis.py`.** Compares the text of the compiled PDF with `corrected_counts.json` and checks that superseded statements are gone. **49 of 49 checks pass** (`audit_output/validation_output.txt`). These include:
   - present: 119 / 94; 28/83/9; 3/8/9/75; 66/8/1; 20 appraised; 10/10; Tier 1 3/1/18; 11 high/moderate, 7 indirect; 12/8; H2 42; H6 51; the Table 4.2 rows for H2, H4, H5 and H6; 30 of 95; three quantitative dimension studies; "Kabir et al. (2025)"; the AI disclosure in the declaration;
   - absent: "118 independent", "strategic flexibility", "four of the six", "direct effect … disappears", "only seven concern", "41 studies", "Fifty-two", "74 of the 95", "For platform firms, the evidence on sellers", "are checked by the author", "re-screening check", "documented script", unresolved `??` references.
4. **`citation_audit.py` on the corrected source.**
   - All 113 cited keys exist in the bibliography. Previously there were 112; `wu2026` is now cited through Appendix C.
   - One bibliography entry is uncited (`martinmartin2021`, harmless).
   - Remaining bibliography-vs-OpenAlex year differences: `fano2025` (2026 vs 2025) and `almheiri2025` (2025 vs 2024). Appendix C now prints the bibliography year, so text and appendix agree.
5. **Appendix C.**
   - All 120 studies are listed. 42 rows are generated with `\textcite`.
   - Markers: T = 9, E = 4, † = 5.
   - Ratings: 3 high / 8 moderate / 9 low / 75 n.a. / 25 conceptual; Tier 1 = 3 moderate, 1 low, 18 n.a. These match the corrected data.
6. **Visual check.** The rendered pages show Fig. 4.1 (PRISMA), Table 4.2 and Fig. 4.4 (revised model) laid out correctly. Labels in Fig. 4.4 sit slightly close to the arrows but are legible.

## Integrity checks

- **`xxxx.zip`:** SHA-256 unchanged.
- **`audit_workspace/extracted/SRH_Thesis_Template/`** (original source and review data): all 23 files match the hashes recorded before editing (`backups/original_source_sha256.txt`).
- **`thesis_corrected/.../review_data/`:** byte-identical to the original. Corrections exist only in `review_data_corrected/`.
- **No git commit or push was made.**

## What validation does *not* establish

- **No claim in the thesis has been verified against an original full text.** The corrections rest on the review data, the OpenAlex abstracts and the thesis's own rules.
- **Passing checks show internal consistency only.** The prose, tables, figures and appendices now agree with the corrected data. That does not make the data correct; see `UNRESOLVED_ISSUES.md`.
- **The thesis must not be described as fully verified.**
