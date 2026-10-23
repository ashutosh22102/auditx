# Data Reconciliation

Independent recalculation of the review counts from the raw files in `review_data/`. These were extracted from `xxxx.zip` into `audit_workspace/extracted/`. The originals were not modified, and the zip's SHA-256 checksum was unchanged before and after the audit.

**How this was done**

- **Scripts:**
  - `audit_workspace/scripts/reconcile.py` (raw output: `reconciliation_output.txt`)
  - `quote_check.py` (output: `QUOTE_CHECK.csv`)
  - `citation_audit.py` (output: `citation_audit_output.txt`)
- **Approach:** every number below was recomputed from `records.jsonl`, `ta_final.json`, `included_final.json`, `agreement.json` and `citation_search.json`. None was copied from the thesis or the README.

---

## 1. Identification, de-duplication and screening (PRISMA)

| Step | Thesis (Fig. 4.1 / §4.1) | Recomputed from raw data | Verdict |
|---|---|---|---|
| Records identified (OpenAlex) | 1,807 | 1,807 lines in `records.jsonl` | Reconciles |
| Duplicates removed | 10 | 1 repeated OpenAlex ID (W4400590609 appears twice) + 9 records whose title duplicates another record (different OpenAlex ID/DOI) = 10 | Reconciles |
| Records screened | 1,797 | 1,797 entries in `ta_final.json`; all exist in `records.jsonl` | Reconciles |
| Excluded at title/abstract | 1,600 | 1,600 | Reconciles |
| – E5 construct | 1,032 | 1,032 | Reconciles |
| – E4 study type | 413 | 413 | Reconciles |
| – E1 publication type | 147 | 147 (112 repository records, 22 with no source type, 13 journal records) | Reconciles |
| – E6 unit of analysis | 8 | 8 | Reconciles |
| Reports assessed for eligibility | 197 | 197 TA includes | Reconciles |
| – full text 64 / abstract only 133 | 64 / 133 | **Not recorded anywhere in the data.** Full-text status exists only for the 120 included studies: 28 full text, 83 abstract only, 9 title only (no abstract, no full text). | **Cannot be verified** |
| Reports excluded at eligibility | 77 | 77 TA includes are absent from `included_final.json` | Count reconciles |
| – E5 48 / E4 17 / E6 8 / E1 3 / E2 1 | as listed | **No file records the full-text exclusion reasons.** The 77 excluded IDs can be derived, but not why they were excluded. | **Cannot be verified** |
| Studies included | 120 | 120; all were TA includes; IDs, titles, years and DOIs match `records.jsonl` | Reconciles |
| Tier 1 / 2 / 3 | 22 / 73 / 25 | 22 / 73 / 25. Tier 3 = exactly the 25 conceptual studies. Tier 1 = studies with a DC construct plus an outcome. | Reconciles |

### De-duplication notes

**Which version was kept.** De-duplication sometimes kept a repository copy and dropped the journal version:

- *AI and competitive advantage in higher education*: the Zenodo copy was kept and screened; the journal copy W7220025114 was dropped.
- *Business intelligence for societal equity*: the Zenodo copy was kept; the GJETA journal copy was dropped.

Repository copies are then excluded as E1. This does not affect the included set, but it is a protocol weakness worth one sentence.

**Possibly mis-matched pair.** One pair is a weak duplicate match: *On the 10th anniversary of JISIB* appears as 2020 v1 and 2024 v10, with different DOIs.

**Repository record at the title/abstract stage.** One TA include had source type "repository". It is not among the 120 included studies.

## 2. Independence of samples ("120 studies, 118 independent samples")

**Arithmetic.** The thesis (§4.1, Fig. 4.1) says that two publications (Almheiri et al. 2024/2025) share one sample, and that therefore 120 studies equal 118 independent samples. Arithmetically, 120 publications with one shared pair give **119** samples.

**What the data store.** The data link *three* publications to sample W4405869520:

- almheiri2024 (JM2): 344 public managers.
- **Almheiri et al. 2026, W7203683920**: *Leveraging strategic capabilities … hotel resilience*. Its abstract reports **400 hotel managers**, a different sample.

Applying the stored links gives 118. "118" is therefore reproducible only through this erroneous link.

**Evidence the pair genuinely shares a sample.** At abstract level, the Almheiri 2024/2025 pair is consistent with one sample: both report 344 UAE public managers and the same 26-item scale development. This is partially verified. The full texts were not inspected.

**Correct figures:**

- **120 publications → 119 independent publications/samples.**
- Of these, **95 empirical studies → 94 independent empirical samples.** The 25 conceptual papers have no sample, so describing them as "independent samples" is a category error.

**Knock-on effect.** The H2 "indirectly relevant = 41" figure also depends on the erroneous link (see §5).

**Two Alnofeli 2025 papers.** Two Alnofeli et al. 2025 papers are included (IJIM and JIK). Whether they share data was not assessed in the data, and I could not assess it either.

## 3. Screening agreement (Cohen's kappa)

| Item | Finding |
|---|---|
| Run-level decisions | **Not provided.** `ta_final.json` holds only the final decision, a reason code, one classification object and a `source` flag (`agreed` 1,742; `adjudicator` 55). The paired decisions of run 1 and run 2 are not in the data. |
| Observed agreement | 1,742 / 1,797 = 0.96939, matching `agreement.json` and the thesis's "96.9%" |
| Kappa 0.8436 | **Cannot be recomputed independently.** Consistency check: with 170 agreed includes and 55 disagreements, κ = 0.84357 is reproduced exactly only if the disagreements split 24/31 between the runs. Any split gives κ between 0.8436 and 0.8439, so the reported value is *arithmetically plausible*, but it is not verified. |
| Adjudication | The third run decided 27 includes and 28 excludes. 27 of the 197 TA includes (13.7%) therefore rest on a single model run, with no human check recorded. |
| Nature of the statistic | The thesis correctly says (Ch. 3 §3.2.2; §4.1; abstract) that this is agreement between two runs of the same language model, not human inter-rater reliability. The README calls the runs "two independent AI-assisted classifications", which conflicts with Ch. 3's statement that they "are not independent reviewers". The thesis wording is the accurate one. No human reliability statistic exists. |

## 4. Study characteristics (§4.1, Figs. 4.2–4.3)

| Claim | Recomputed | Verdict |
|---|---|---|
| 112 of 120 published 2024 or later; 57 in 2026 | 112; 57 (2021: 1, 2022: 3, 2023: 4, 2024: 18, 2025: 37, 2026: 57) | Reconciles |
| 95 empirical / 25 conceptual | 95 / 25 | Reconciles |
| 65 cross-sectional surveys; 1 time-lagged; 1 longitudinal panel; 13 mixed; 13 other; 2 case | Same | Reconciles. The wording "almost all empirical studies are cross-sectional surveys (65 of 95)" overstates: 65 of 95 is 68%. |
| AI use 52 / capability 46 / integration 22 | Same | Reconciles |
| DC overall 24 / dimensions 10 / related 52 / none 34 | Same | Reconciles |
| Outcome CA 74; CA and performance 20 | Same; the remaining 26 are performance 19 and other 7 | Reconciles |
| Persistence measured in 1 study (Dzreke 2025) | 1 | Reconciles |
| 105 journals; maximum 3 per journal | 105; IMM, JIK and JEIM have 3 each | Reconciles |
| 80 report n; median 312; 16 below 150 | 80; median **311.5**; 16 | Reconciles after rounding |
| PLS-SEM 39; CB-SEM 9; multiple informants 9 | 39; 9; 9 | Reconciles |
| Country not reported: 30 of 95 | 28 "not reported" + 2 partial ("CPEC, likely Pakistan"; "Europe, country not reported") = 30 | Reconciles |
| §4.1: "**Most** studies do not report the country" | 30 of 95 (32%) | **Mismatch.** This contradicts §4.4.2's own figure. |
| China most frequent (10) | 10 single-country China studies (+1 multi-country) | Reconciles |
| SE Asia 14, East Asia 13, Middle East 12 | 14, 13, 12 | Reconciles |

## 5. Quality appraisal and evidence counts

| Claim | Recomputed | Verdict |
|---|---|---|
| Of 95 empirical: 3 high, 9 moderate, 9 low, 74 not assessable | Same | Reconciles |
| 74 not assessable "because only the abstract was accessible" (§4.1) | 65 abstract only; **8 title only** (Hossain 2022, Htet 2026, Li 2025, Wu 2026, Anjum 2026, Ramírez 2026, Samadhiya 2023, Luo 2025); **1 full text available but not assessable** (Nikzat 2025) | **Partly inaccurate.** Ch. 5 §5.4 ("mostly because …") is the accurate wording. |
| Appraisable = 21 | 21 (20 rated from full text; **Mukhopadhyay 2024 rated "moderate" from the abstract only**) | Reconciles, with one inconsistency |
| Studies marked "not assessable" described as low quality? | No. §4.1 explicitly says n.a. ≠ low, and n.a. studies are never counted as low in Table 4.2. | Correctly handled |
| Tier 1: 5 appraisable (4 moderate, 1 low), 17 n.a. | Same | Reconciles |
| "Among the studies that could be appraised", CMB addressed in **11**, indirect effect estimated in **13** | Among the 21 appraised: Q4 met in **10**, Q6 met in **10**. The figures 11 and 13 count all 120 studies, including ratings given to "not assessable" studies (Q4: Sofiyan; Q6: Sharma, Gafsi, Tu). | **Mismatch (denominator)** |
| Only 2 separated measures in time; 3 fully met sampling; 2 controls | 2; 3; 2 | Reconciles |
| Overall-quality rule (note under Table 3.2) applied correctly | All 21 ratings follow the stated rule | Reconciles |
| H1: 9 direct / 44 indirect / 3 contradictory | 9 / 46 raw. **44** is reproduced when a study coded both "direct" and "indirect" (Al-Mamary) or both "contradictory" and "indirect" (Mashi) is counted once under its stronger category. | Reconciles under that undocumented rule |
| H2: 3 direct / 41 indirect / 1 contradictory | Direct 3 after merging the Almheiri pair. **Indirect 41 reproduces only if the erroneous Almheiri 2026 link is applied**; with the pair-only rule used for H1, it is **42**. | **Mismatch** (inconsistent independence handling) |
| H3: 0 / 1 / 0 | 0 / 1 (Noor 2026) / 0 | Reconciles |
| H4, H5: none | None | Reconciles |
| H6: 0 / 52 / 1 | 0 / 52 / 1 (Kokash) | Reconciles |
| Sensitivity: of 12 high/moderate, 8 H1-indirect and 1 contradictory; 13 appraised with H2 evidence, 9 of them high/moderate | Same | Reconciles |
| AI→CA results: 70; 57 positive, 7 null, 5 mixed, 1 negative | Same | Reconciles |
| 13 estimated indirect effects vs 38 inferred | 13 and 38 among empirical non-qualitative studies (plus 3 qualitative and 10 conceptual) | Reconciles |
| 28 AI-use studies provide H1-indirect evidence | 28 | Reconciles |
| 10 studies address DC dimensions: "4 conceptual, 2 qualitative/mixed, 4 quantitative (Deng, Fano, Neira-Fernández, Noor)" | The data list **Wei 2025, Arowolo 2026, Siaw 2024, Karami 2026** (conceptual), **Ghobakhloo 2025** (Delphi, coded empirical "other"), **Feroz 2024, Maune 2026** (mixed), **Fano 2025, Neira-Fernández 2026, Noor 2026** (quantitative). Deng 2025 is coded DC "overall". | **Mismatch:** there are 3 quantitative studies, not 4. Ghobakhloo is not conceptual, and Wei and Arowolo are omitted. |
| DC as a higher-order construct | **0 of 120** studies are coded as higher-order (6 first-order, 114 n/a). Ch. 2 §2.4.2 says the higher-order specification "corresponds to how most empirical studies model dynamic capabilities". | **Mismatch** |
| Focal context: 7 studies | 7 coded non-"none": Guo (complementor), Noor, Bunea (e-commerce retailer), Awamleh, Firmansyah, Adamu (other e-commerce/digital), Dzreke 2025b (platform owner, conceptual) | Count reconciles. However, Firmansyah's abstract does not mention e-commerce or digital business, and Adamu concerns FinTech, banking and tech sectors. Strictly e-commerce/platform: **4 empirical + 1 conceptual**. |

## 6. Included studies that may conflict with the stated criteria

**E5 (neither DC nor CA examined).** These are coded with outcome = performance/other and DC = related/none:

- **Li 2026**: cited for H2, H4, H5 and H6.
- **Sofiyan 2026**: the H2 contradictory study.
- **Shore 2024** and **Tian 2023**: Tian is coded H1-indirect.

The authors frame their mediators (absorptive capacity, change capacity, resilience) as dynamic capabilities. Each inclusion decision needs a documented justification.

**Title-only inclusions.** The thesis says eligibility rests on at least the abstract (Ch. 3 §3.5), but **9 included studies have neither an abstract nor a full text**. The LaTeX comments acknowledge only Wu 2026 and Li 2025. None of the 9 has extracted results; they inflate the 120 total and the "not assessable" count.

## 7. Citation search (678 records)

**What the data show.** `citation_search.json`: 527 backward + 476 forward = 1,003; 826 unique; **678 new**.

**Disclosure in the thesis.** No screening decisions exist. The thesis discloses the 678 as unscreened in four places:

- Ch. 3 §3.2.1
- Fig. 3.2 (dashed box)
- Fig. 4.1
- Appendix A

It also lists them among the limitations (Ch. 3 §3.5; Ch. 5 §5.4).

**Two details to check.**

- **Seed set.** Appendix A says the citation search was seeded from "the 121 studies eligible before the final language check". That is consistent with one E2 exclusion at full text (197 − 77 = 120), but the seed list itself is not in the data.
- **Filter.** The relaxed filter (AI AND (capability OR outcome)) differs from the main query. This is disclosed in Appendix A.

## 8. Search dates, filters and the 2026 cut-off

**Search date.** `query.json`: run 22 Oct 2026. This is consistent across the README, Ch. 3, Ch. 4, Appendix A and Fig. 4.2.

**Date filter.** The filter is `from 2015-01-01` / `to 2026-12-31`, which is disclosed in Appendix A with a rationale. Table 3.1 says "January 2015 to the date of the search", and Fig. 4.2 says "*2026 until 22 October".

- These are consistent in intent.
- Note, however, that 2026 records dated to later 2026 issues can be included. Fig. 4.2's "until 22 October" refers to when records were *available*, not to publication dates.

**Record years.** Records span 2015–2026. No E3 exclusions were needed, because the filter enforced the start date. The earliest included study is 2021: Malik "2021", whose year is itself doubtful (see CLAIM_VERIFICATION.md).

**Search filters.** Type article, English, no subject filter, as stated. The benchmark claim (business filter → 1,188 records, which would drop Chen 2022) could not be re-run, because OpenAlex is blocked from this environment.

**Year conventions.** Year conventions differ between the bibliography (issue year) and Appendix C/Fig. 4.2 (OpenAlex year) for:

- fano2025 (bib 2026)
- almheiri2025 (OpenAlex 2024)
- kemp2024 (OpenAlex 2023)
- siaw2024 (bib 2025)
- krakowski2023, rana2022 and neiroukh2025

## 9. What the data do not support (missing files)

These are referenced by the thesis or README but were not supplied:

- The two run-level screening outputs, and the adjudication prompts.
- Full-text eligibility decisions and exclusion reasons for the 77 excluded reports.
- The full-text/abstract status of the 197 reports.
- The search script (Ch. 3 §3.4 says "a documented script").
- The 121-study seed list and the citation-search records.
- The extraction and verification prompts, including the "separate verification run".
- Any record of the author's manual checks (Ch. 3 states that "All inclusion decisions and extracted results are checked by the author").
- Any original research-paper PDFs.
- A compiled thesis PDF.

---

## 10. Corrected values (v2)

**Source.** `audit_workspace/scripts/apply_corrections.py` writes `thesis_corrected/SRH_Thesis_Template/review_data_corrected/included_final_corrected.json` and `corrected_counts.json`. The original `review_data/` is unchanged.

**Data corrections:**

- **D1:** the Almheiri 2026 same-sample link was removed.
- **D2:** Mukhopadhyay 2024 → not assessable.
- **D3:** Li 2026 → H4 and H5 indirectly relevant, and no longer counted for H6.

**Recomputed values:**

- Independent studies **119**; independent empirical samples **94**.
- Empirical quality: 3 high / **8** moderate / 9 low / **75** n.a. (66 abstract only, 8 title only, 1 insufficient full text). Appraisable **20**; high or moderate **11**; Tier 1: 3 moderate, 1 low, 18 n.a.
- Q4 and Q6 met among the appraisable studies: **10 / 10**.
- Hypothesis counts:

  | H | D / I / C |
  |---|---|
  | H1 | 9* / 44 / 3 |
  | H2 | 3 / **42** / 1 |
  | H3 | 0 / 1 / 0 |
  | H4 | 0 / **1** / 0 |
  | H5 | 0 / **1** / 0 |
  | H6 | 0 / **51** / 1 |

- Sensitivity: H1, 7 of 11 high/moderate studies indirect and 1 contradictory; H2, 12 appraised studies with H2 evidence, 8 of them high/moderate.
- Higher-order DC specifications: **0**.

**Unchanged** (still reconciling): all PRISMA title/abstract counts, years, designs, construct counts, the AI→CA direction counts, and the 13 vs 38 mediation counts.

**Still unverifiable:** the full-text stage (64/133; the 77 reasons) and κ (see UNRESOLVED U13, U14).

All corrected values appear consistently in the compiled corrected PDF (`validation_output.txt`: 49/49 checks pass).
