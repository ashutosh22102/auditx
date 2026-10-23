# Audit Summary

**Thesis:** *From AI Capabilities to Sustainable Competitive Advantages: A Dynamic Capabilities Perspective in E-Commerce and Platform-Based Digital Business*. The version audited is the LaTeX source in `xxxx.zip`, last edited 23 Oct 2026. No PDF was supplied.

## Overall assessment

The **review dataset is internally coherent**, and the **title/abstract-stage PRISMA counts reconcile exactly** with the raw files. Most descriptive statistics in Chapter 4 recompute correctly. The thesis is also commendably candid about:

- the use of a language model;
- the meaning of kappa (agreement between model runs, not human reviewers);
- unassessable quality;
- the unscreened citation search.

However, the thesis **cannot yet be described as verified against its sources**. Three reasons:

1. **No original paper was available.** None was in the repository, and the network policy blocked every publisher, DOI and OA host. 0 of 120 studies were checked against full text.
   - 83 studies were checked against their OpenAlex abstract.
   - 28 rely on full-text extractions that could not be checked.
   - 9 were included **on title only**.
2. **Several numbers and claims in the abstract and conclusions contradict the data or the source abstracts** (major issues below).
3. **Key methodological records are missing:** run-level screening decisions, the full-text eligibility log, the search script and the record of manual checks. The thesis currently states that the author has checked all inclusion decisions and extracted results. The README and the LaTeX notes say this still has to be done.

## Major issues (most serious first)

1. **"118 independent samples" is wrong.** One shared pair in 120 publications gives 119; there are 94 independent *empirical* samples. 118 is reproducible only through a data error that links Almheiri et al. (2026), 400 hotel managers, to the 344 public-manager sample. The same error makes the H2 count 41 instead of 42.
2. **Abstract and §5.1: "in the strongest studies, the direct effect of AI disappears"** is overgeneralised. Of the three high-quality studies:
   - only one fits;
   - one treats AI only as a moderator;
   - in one (Guo 2025) the direct paths remain significant.

   Chen 2026, listed among "the strongest", is not assessable.
3. **Texeira (2026)'s moderator is misreported as "strategic flexibility"** throughout §4.3–§5.3 and in the revised model. The source abstract names it *sustainable food innovation orientation*.
4. **Nine included studies have no abstract and no full text.** The thesis says eligibility rested at least on abstracts.
5. **H1 "nine direct studies".** One (Gafsi 2026) measures firm performance, so it is indirect under the thesis's own Outcome rule. Four more are borderline: Giang, Waqas, Almereb, Al-Mamary.
6. **Hypothesis judgements are applied asymmetrically.**
   - **H3 versus H4/H5:** H3 is "partly supported" on one indirectly relevant study (Noor 2026), while the analogous seizing and transforming evidence (Li 2026) is reassigned to H6.
   - **H6:** "partly supported" contradicts the thesis's own conclusion ("not specifically through dynamic capabilities"). No study models DC as a higher-order construct, and the only DC-mediation test was null.
   - The headline "four of six partly supported" depends on these choices.
7. **"Only seven studies concern e-commerce or platform-based business" overstates.** Firmansyah 2025 and Adamu 2026 are not e-commerce or platform studies by their abstracts. That leaves 4 empirical e-commerce/platform studies, one of them on complementors, plus 1 conceptual paper.
8. **§5.3.2 applies complementor evidence (Guo 2025) to "platform firms"**, contrary to §1.4's scope rule.
9. **Wang 2026 is presented as "the only high-quality study that tests [H1] directly"**, but AI capability is only a moderator in that study.
10. **The Declaration of Honour** ("without outside help … no aids other than those indicated") must be reconciled with the AI assistance used and with SRH's AI-use rules.
11. **Smaller numeric and description errors:**
    - "most studies do not report the country" (actually 30 of 95);
    - "almost all … cross-sectional" (65 of 95);
    - 11 and 13 should be 10 and 10 "among appraised studies";
    - the list of DC-dimension studies is wrong (3 quantitative, not 4);
    - "74 because only the abstract was accessible" (8 were title-only, 1 had a full text);
    - one appraisal (Mukhopadhyay) was made from the abstract only;
    - inconsistent citation years (fano2025, almheiri2025, kemp2024);
    - a missing author in Appendix C;
    - Malik "2021" has inconsistent metadata (a recent-range Zenodo DOI) despite being key H2/H6 evidence.

## Is any key hypothesis or conclusion overstated?

**H1: yes, in degree.** The judgement ("partly supported") stands, but the robust direct count is about 4–8, not 9. The abstract's mechanism claim (the direct effect "disappears") overstates the evidence.

**H6: yes.** The label overstates relative to the thesis's own analysis.

**H3: the label rests on an asymmetric rule.**

**H2: the judgement is reasonable.** The thesis correctly notes that the direction is unresolved and that no appraisable study reports the relationship directly.

**Causality and sustained advantage are mostly handled well.** The text repeatedly says the evidence shows associations, and that it concerns perceived competitive advantage at a point in time rather than *sustained* advantage. Exceptions: causal wording in Ch. 2 (Shao: "effect", "partly mediated"; Almheiri: "enhance").

## Must fix before sending to the professor

1. Correct 118 → 119 (and 94 empirical samples). Fix the Almheiri 2026 link and the H2 count.
2. Rewrite the "direct effect disappears / strongest studies" sentence in the abstract, §4.4.1, §5.1 and §5.3.1.
3. Replace "strategic flexibility" with "sustainable food innovation orientation" everywhere, including Fig. 4.4 and the managerial implications.
4. Read the 9 title-only studies, then confirm or remove each and update every total. At minimum, disclose them.
5. Either complete and document the manual checks of the 120 inclusion decisions and extracted results, or change §3.2.2's statement that they "are checked". Prioritise the 22 "critical" papers in `MISSING_SOURCES.csv`.
6. Reclassify Gafsi 2026 (or justify it). Make the H3/H4/H5 rule consistent, and qualify the H6 label in the abstract, Table 4.2 and §5.1.
7. Fix the "seven e-commerce/platform studies" wording, and the complementor-as-platform-firm sentence in §5.3.2.
8. Align the Declaration of Honour and §3.4 with the actual AI assistance and the SRH policy.
9. Fix the B-list inconsistencies in THESIS_ISSUES.md (country, "almost all", 11/13, the dimension-study list, Wang 2026 wording).

## Recommended next steps

1. Obtain the PDFs for the 22 critical studies in `MISSING_SOURCES.csv`, through the library or the OA links listed there. Re-run the claim checks with page numbers. With network access to doi.org and OpenAlex, this audit's scripts can be extended to do so.
2. Export and archive the missing review records:
   - the run-level screening decisions (so kappa can be recomputed);
   - the full-text eligibility log with reasons;
   - the search script;
   - the citation-search seed list.
3. After the corrections, recompile the PDF and re-run `audit_workspace/scripts/*.py` to confirm that the counts still reconcile.

All details: DATA_RECONCILIATION.md, CLAIM_VERIFICATION.md, THESIS_ISSUES.md, STUDY_EVIDENCE_AUDIT.csv/.xlsx, MISSING_SOURCES.csv, AUDIT_LOG.md.

---

## Update v2: corrections applied

A corrected working copy now exists: `thesis_corrected/SRH_Thesis_Template/`, compiled to `thesis_corrected/Thesis_corrected.pdf`. The originals are unchanged.

**Where to find the details:**

- `CORRECTION_LOG.md`: every change, with its evidence.
- `UNRESOLVED_ISSUES.md`: what still needs papers, the author or the supervisor.
- `VALIDATION_SUMMARY.md`: compilation and the 49 consistency checks.

**Status of the major issues above:**

| Item | Status after v2 |
|---|---|
| 1. 118 samples | **Fixed:** 119 independent studies, 94 empirical samples; H2 indirect 42 |
| 2. "direct effect disappears" | **Fixed:** wording now reflects Guo (direct and indirect both significant) and Srahin (p = 0.036); Chen 2026 is no longer "strongest" |
| 3. Texeira moderator | **Fixed** throughout, including Fig. 4.4 and the implications |
| 4. Nine title-only studies | **Disclosed and marked (T)**; eligibility **unresolved** (needs papers) |
| 5. H1 nine direct studies | **Qualified:** 6 marked provisional; Gafsi re-assessed as ambiguous (not reclassified) |
| 6. H3/H4/H5 asymmetry; H6 label | **Fixed by applying the rules consistently:** H4 and H5 are now partly supported (one indirect study each, Li 2026); H6 51 studies, label qualified. **Author decision: option (a) kept for U23 and U24.** |
| 7. "Only seven e-commerce/platform studies" | **Fixed:** four empirical e-commerce/platform studies, plus closely related ones |
| 8. Complementors as "platform firms" | **Fixed** |
| 9. Wang 2026 | **Reworded**; classification **unresolved** |
| 10. Declaration | **AI-use sentence added**; SRH policy check **unresolved** (author/supervisor) |
| 11. Smaller errors | **Fixed**, except `fano2025` year and Malik metadata (unresolved, marked †) |

**Headline judgement after correction:** no hypothesis supported; all six at most partly supported, on very different evidential bases. **The thesis is still not verified against original papers.**
