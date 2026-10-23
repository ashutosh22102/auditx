# Unresolved Issues

These items could not be resolved with the material available: no original papers, no compiled source of the review pipeline, and no access to publisher sites.

They need original papers, the author's judgement or the supervisor's guidance. The thesis wording has been made cautious wherever these items are mentioned.

**Priority:** **1** = affects a hypothesis judgement or headline claim; **2** = affects a count, description or method statement; **3** = presentation.

## Needs original papers

| ID | P | Issue | What is needed | Where it matters |
|---|---|---|---|---|
| U1 | 1 | **No study has been verified against its full text** (0 of 120). 84 full-text quotations and all estimates taken from full texts (e.g. 0.519, 0.336, 0.445, 0.071, 0.05, 0.110, 0.067, 0.057) are unchecked; there are no page numbers. | Obtain the PDFs, starting with the 22 "1-critical" rows of `MISSING_SOURCES.csv`. Check each quote and estimate and add page numbers. | All of Ch. 4–5 |
| U2 | 1 | **Nine title-only inclusions** (Hossain 2022, Htet 2026, Li 2025, Wu 2026, Anjum 2026, Ramírez 2026, Amin 2026, Samadhiya 2023, Luo 2025) | Read each paper and confirm or exclude it. If any is excluded: update 120/119, 95/94, 25, 75 n.a., the Tier counts, the year and design figures, and Appendix C. Re-run `apply_corrections.py` and `validate_thesis.py`. | §3.5, §4.1, Fig. 4.1–4.3, Appendix C |
| U3 | 1 | **H3, H4 and H5 each rest on one study** (Noor 2026; Li 2026) whose estimates are unverified | Verify the indirect estimates and their framing as sensing, seizing and transforming in the full texts | Table 4.2, §4.3, abstract |
| U4 | 1 | **Wang 2026**: is AI capability's null main effect a legitimate "contradictory" result for H1? | Check the model specification (Table 5) in the full text | §4.2.1, §5.2 |
| U5 | 1 | **Texeira 2026**: null direct effect (B = 0.071, p = 0.070) and the "high" rating despite a recorded sample inconsistency (449 vs 803 administered) | Full text | §4.2.1, §4.4.1, §5.1 |
| U6 | 2 | **Provisional H1 direct classifications**: Gafsi 2026 (outcome measure), Giang 2026 and Waqas 2024 (AI-specific path), Almereb 2026 (GenAI measured as use or capability), Al-Mamary 2025 (role of CA), Firmansyah 2025 | Full texts. If Gafsi measures firm performance, H1 direct 9 → 8. | §4.2.1, Tables 4.1–4.2 |
| U7 | 2 | **Srahin 2026** (p = 0.036 vs a CI including 0) and **Guo 2025** (text 0.242 vs table .255) | Full text | §4.2.1, §4.3.4 |
| U8 | 2 | **Publication legitimacy**: Malik "2021" (Zenodo DOI in a recent range; CB-SEM fit for a PLS model), Firmansyah 2025 and Noor 2026 (no DOI), Dzreke 2025 and 2025b (credibility concerns) | Publisher pages, ISSN and indexing checks; correct the year and volume | Table 4.1 †, Appendix C † |
| U9 | 2 | **Siaw 2024**: its abstract contradicts itself on external scanning | Full text | §4.3.1 |
| U10 | 2 | **Firmansyah 2025**: is the sample "digital MSMEs"? | Full text | §4.2.1, §4.4.2 (focal count) |
| U11 | 3 | **Two Alnofeli 2025 papers**: overlapping data? | Full texts | Independence count |
| U12 | 3 | **Almheiri 2024/2025 shared sample** is supported only at abstract level | Full texts | 119 / 94 |

## Needs missing review records

| ID | P | Issue | What is needed |
|---|---|---|---|
| U13 | 2 | **Full-text stage**: 64 full texts vs 133 abstracts or titles, and the 77 exclusion reasons (48/17/8/3/1) are not documented anywhere | Export the full-text eligibility log and add it to the supplementary material |
| U14 | 2 | **Cohen's κ** (0.84) cannot be recomputed. It is arithmetically plausible: an exact match requires a 24/31 split of the 55 disagreements. | Export the run-1 and run-2 decisions |
| U15 | 3 | Search script, model prompts, verification-run outputs, the 121-study citation seed list and the 678 citation records | Archive them with the thesis data |
| U16 | 3 | Benchmark claim: a business subject filter gives 1,188 records and drops Chen 2022 | Re-run the query (OpenAlex was blocked here) |

## Needs the author

| ID | P | Issue | Action |
|---|---|---|---|
| U17 | 1 | **§3.2.2** now says inclusion decisions and results "remain subject to checking by the author" (LaTeX note in the source) | Do the checks (U1, U2), then reword the sentence to describe what was actually done |
| U18 | 1 | **Declaration of Honour**: an AI-use sentence was added, but the SRH form and AI policy were not available. Drafting assistance, if any, is not disclosed. The source still contains "Rewrite the text in your own words" notes in every chapter. | Check the official SRH wording and AI rules with the supervisor; disclose all AI assistance; remove the draft notes |
| U19 | 3 | Empty author e-mail; `\submissiondate{\today}` | Fill in |
| U20 | 3 | Citations have no page numbers (SRH 4.2.1) | Add them after reading the papers |
| U21 | 3 | `fano2025` bibliography year 2026 vs OpenAlex 2025; whether to use online or issue years throughout | Check the publisher record; the bibliography convention is now explained in the Appendix C and Fig. 4.2 notes |
| U22 | 3 | `martinmartin2021` is in the bibliography but uncited | Cite or delete (biblatex omits it either way) |

## Needs supervisor guidance

| ID | P | Issue | Options |
|---|---|---|---|
| U23 | — | **RESOLVED by author decision: option (a) kept.** **H3–H5 judgements.** Applying Table 3.3 consistently makes H3, H4 and H5 each "partly supported (one indirect study)". Before, H3 was partly supported while H4 and H5 were not yet examined. | (a) Keep the literal rule outcome (current text). (b) Amend the rules, e.g. "an indirect effect on an outcome other than CA through a framed mediator counts as *no eligible evidence*", which would make H3–H5 all "not yet examined". Either way, apply it to all three. |
| U24 | — | **RESOLVED by author decision: option (a) kept.** **H6 label.** By the rules it is "partly supported", although no study models DC as a higher-order construct and the only DC-mediation test was null | Keep the qualified label (current text), or introduce an explicit category such as "inconclusive for DC" (this would be a rule change) |
| U25 | 2 | **E5 interpretation**: a construct counts as DC when its authors define it as one. Four studies depend on this; it is stated in §3.2.2, but it was documented after screening. | Confirm the interpretation, or exclude the four (and recount) |
| U26 | 2 | **Focal context**: the seven "focal and closely related" studies include two digital-sector studies and one conceptual paper | Confirm whether "closely related" is acceptable, or restrict to the four empirical e-commerce/platform studies |
| U27 | 3 | The data README describes the screening runs as "independent"; the thesis says they are not | If the data are submitted, align the README (the original was kept unchanged) |

## Decisions recorded

- **U23 and U24: option (a) kept, by author decision.**
  - H3, H4 and H5 stay "partly supported (one indirectly relevant study each)", the literal outcome of Table 3.3.
  - H6 stays "partly supported (related capabilities only)", with the qualification in the text.
  - No thesis text was changed by this decision, because the corrected working copy already used option (a).
  - The supervisor may still raise these points. The alternatives are kept above for reference.
