# Correction Log (v2)

**Scope.** This log lists every material change made to the thesis working copy.

- **Working copy:** `thesis_corrected/SRH_Thesis_Template/` (compiled: `thesis_corrected/Thesis_corrected.pdf`, 93 pages).
- **Untouched originals:** `xxxx.zip` and `audit_workspace/extracted/SRH_Thesis_Template/` (SHA-256 checked unchanged).
- **Backups:** `backups/SRH_Thesis_Template_original/`, its compiled PDF `backups/original_thesis_compiled.pdf` (90 pages), and the first audit reports `backups/audit_output_v1/`.
- **Line-by-line diff:** `audit_output/thesis_changes.diff`.
- **Nothing was committed or pushed.**

**Page references.** "PDF p." refers to physical PDF pages; in the chapters, printed page = PDF page − 8.

**Basis of every change.** Each change rests on one or more of the following:

- **(i) the review data**, which are unchanged; corrections are applied only in the copy `review_data_corrected/`;
- **(ii) the OpenAlex abstracts** in `records.jsonl`;
- **(iii) the thesis's own stated rules** (Tables 3.1–3.3, Section 3.5).

**No change rests on an original full text, because none was inspected.** Issue IDs (A1, B3, …) refer to `THESIS_ISSUES.md`.

---

## 1. Data corrections (`review_data_corrected/`, produced by `audit_workspace/scripts/apply_corrections.py`)

| # | Study | Field | Old → new | Evidence | Status |
|---|---|---|---|---|---|
| D1 | Almheiri et al. 2026 (W7203683920) | `same_sample_as` | W4405869520 → none | Abstract: 400 hotel managers, UAE. The linked pair: 344 public managers. | Confirmed at abstract level |
| D2 | Mukhopadhyay 2024 | `overall_quality` | moderate → not assessable | `fulltext_used = false`. Section 3.5: abstract-only studies "cannot be assessed". Every other appraisal used a full text. | Confirmed (rule consistency) |
| D3 | Li 2026 | `categories` | H2 I, H6 I → H2 I, H4 I, H5 I | Panel A (mediator related to a dimension = indirectly relevant) and the Panel C assignment rule (separate dimension-specific indirect effects → H3–H5; "no estimate counts for both"). This is the same treatment the thesis gave Noor 2026 for H3. The abstract frames absorptive capacity as "a central seizing capability" and opportunity recognition as "a transforming pathway". | Rule consistency. The underlying estimates (0.067, 0.057) are unverified. |
| D4 | 9 title-only, 4 E5-borderline and 6 provisional-H1 studies | New annotation fields (`eligibility_status`, `e5_rationale`, `h1_direct_caveat`) | — | Records with no abstract and no full text; abstracts | Annotation only; no study was excluded |

### Recomputed values (`corrected_counts.json`)

| Quantity | Original thesis | Corrected |
|---|---|---|
| Independent studies / empirical samples | 118 "independent samples" | **119** independent studies; **94** independent empirical samples |
| Quality of the 95 empirical studies | 3 high / 9 moderate / 9 low / 74 n.a. | **3 / 8 / 9 / 75** (66 abstract only, 8 title only, 1 insufficient full text) |
| Appraisable; high or moderate | 21; 12 | **20; 11** |
| Tier 1 appraisable | 5 (4 moderate, 1 low) | **4 (3 moderate, 1 low); 18 n.a.** |
| Q4 / Q6 met among the appraisable studies | 11 / 13 (wrong denominator) | **10 / 10** |
| H1 (D / I / C) | 9 / 44 / 3 | 9* / 44 / 3 (*6 provisional; 3 unqualified) |
| H2 | 3 / 41 / 1 | 3 / **42** / 1 |
| H3 | 0 / 1 / 0 | 0 / 1 / 0 |
| H4 | 0 / 0 / 0 | 0 / **1** / 0 |
| H5 | 0 / 0 / 0 | 0 / **1** / 0 |
| H6 | 0 / 52 / 1 | 0 / **51** / 1 |
| H1 sensitivity: H/M indirect, contradictory | 8 of 12, 1 | **7 of 11**, 1 |
| H2 sensitivity: appraised with any H2 evidence; H/M among them | 13; 9 | **12; 8** |
| DC modelled as a higher-order construct | not reported | **0 of 120** |

## 2. Hypothesis reassessment (decision rules in Table 3.3 applied to the corrected data)

| H | Evidence (D / I / C) | Rule applied | Original judgement | New judgement | Changed? |
|---|---|---|---|---|---|
| H1 | 9* / 44 / 3 | Panel B *Supported* needs ≥ 2 independent direct studies, at least one of moderate or high quality and from the focal context. No direct study is of moderate or high quality. Context rule. | Partly supported | Partly supported | No. Basis clarified: 6 of 9 direct classifications are provisional; the judgement is the same with only the 3 unqualified studies. |
| H2 | 3 / 42 / 1 | As above; no appraisable direct study | Partly supported | Partly supported | No (count 41 → 42) |
| H3 | 0 / 1 / 0 | Panel B *Partly supported* ("mainly indirectly relevant evidence"). *Not yet examined* applies only when no eligible evidence exists. | Partly supported (one study) | Partly supported (one indirect study) | No |
| H4 | 0 / 1 / 0 | Same as H3 (Li 2026, absorptive capacity framed by its authors as seizing) | Not yet examined | **Partly supported (one indirect study)** | **Yes.** The thesis had assigned this result to H6, contrary to its own assignment rule, which sends separate dimension-specific effects to H3–H5 and only overall effects to H6. |
| H5 | 0 / 1 / 0 | Same (Li 2026, opportunity recognition framed as transforming) | Not yet examined | **Partly supported (one indirect study)** | **Yes**, for the same reason |
| H6 | 0 / 51 / 1 | *Partly supported* (indirectly relevant evidence). *Inconclusive* requires supporting **direct** evidence (none). *Contradicted* requires contradictory direct evidence predominating among moderate- or high-quality studies (Kokash 2026 is not assessable). | Partly supported | Partly supported (related capabilities only) | Label qualified. The text now states: 0 of 120 studies specify DC as a higher-order construct; the only explicit DC-mediation test was null. |

**Consequence.** The headline "four of six partly supported, two not yet examined" becomes "**no hypothesis supported; all six at most partly supported, on very different bases**".

**This is the literal outcome of the stated rules.** The alternatives (amending the rules for H3–H5, or a separate category for H6) are recorded in `UNRESOLVED_ISSUES.md` (U23, U24). **The author chose to keep option (a) for both**, the current text, so no further change was made.

## 3. Thesis text changes

| ID | Issue | Location(s) in corrected PDF | Change | Evidence |
|---|---|---|---|---|
| A1 | 118 independent samples | §4.1 p. 45; Fig. 4.1 p. 46 | "120 publications represent 119 independent studies; … 95 empirical studies … based on 94 independent samples"; PRISMA box "119 independent; 9 provisional, title only" | D1; arithmetic |
| A2 | "strongest studies: direct effect disappears" | Abstract p. 2; §4.2.1 pp. 50–51; §4.4.1 p. 58; §5.1 p. 65; §5.2 RQ1 p. 66; §5.3.1 | Replaced with: in two appraised studies the direct association became small or non-significant; in the high-quality platform-seller study the direct and indirect paths were both significant; other studies report both. Chen 2026 removed from "strongest" and described as an abstract-level AI-infrastructure study. Srahin's p = 0.036 reported alongside its CI. | Extraction for Guo (direct 0.519 and 0.336; abstract: coupling "positively influences … product innovation and brand upgrading, while IMCs serve as a mediating mechanism"); Srahin extraction (p = 0.036, CI includes 0); Chen quality n.a. and abstract |
| A3 | Texeira moderator | §4.3.4 pp. 56–57; §4.4.1 p. 59; §4.4.3 + Fig. 4.4 p. 64; §5.3.1; §5.3.2 p. 70; §5.4 | "strategic flexibility" → "sustainable food innovation orientation" (or "innovation orientation" in summaries and the figure) | Texeira abstract: "sustainable food innovation orientation strengthens the conditional indirect relationships" |
| A4 | Manual-check claim; title-only studies; "133 abstracts" | §3.2.2 p. 38; §3.5 p. 43; §4.1 p. 45; Fig. 4.1; Appendix C; §5.4 p. 71; abstract | "are checked by the author" → "remain subject to checking … against the original papers" (+ LaTeX note to the author). Nine title-only studies disclosed as provisional and marked **T**. "133 … abstracts" → "abstracts or, where the record contained no abstract, their titles". Access split of the 120 (28/83/9) added. | records.jsonl (no abstract), `fulltext_used`; README and LaTeX notes (checks still to be done) |
| A5 | Declaration of Honour | Declaration p. 93 | Added: "The aids used include a large language model (Claude, Anthropic), which supported the screening …, the extraction of data and its verification …" + LaTeX note asking the author to check SRH rules and disclose any further AI assistance | Ch. 3 §3.2.2 and §3.4 disclosures |
| A6 | H2 count | §4.2.2 p. 53; Table 4.2 p. 59; §5.2 RQ2 | 41 → 42 | D1; recount |
| A7 | H1 direct classification | §4.2.1 p. 50; Table 4.1 (D*); Table 4.2 (9*); §5.2 RQ1 | Six studies' direct classification described as provisional, with reasons; "only three … without such a qualification"; judgement shown to be robust. **Gafsi not reclassified** (see note below). | Abstracts; extraction notes |
| A8 | "only seven concern e-commerce or platform business" | Abstract p. 2; §4.4.2 p. 61; §4.5 p. 64; §5.1 p. 65 | "only four empirical studies concern e-commerce or platform-based business, one of them on complementors"; the seven are described as "focal and closely related". Firmansyah's context is qualified as not confirmed by its abstract. | Abstracts of Firmansyah and Adamu; context coding |
| A9 | H3/H4/H5 asymmetry; H6 label | §4.3.2–4.3.4 pp. 55–57; Table 4.2; §4.4.1 p. 58; §4.4.2 (focal: H4/H5 not examined *within* the focal context); §4.4.3 + Fig. 4.4; §4.5; §5.1; §5.2 RQ3/RQ4; abstract | See §2 above. H6: "51 studies"; new sentence "none of the 120 included studies specifies dynamic capabilities as a higher-order construct"; judgement wording qualified | D3; Table 3.3 |
| B1 | "Most studies do not report the country" | §4.1 p. 47 | "Thirty of the 95 empirical studies do not report …" | Data (30) |
| B2 | "Almost all … cross-sectional" | §4.1 p. 46 | "Most empirical studies are cross-sectional surveys (65 of 95)" | Data |
| B3 | 11 / 13 among appraised | §4.1 p. 48 | "Among the 20 studies that could be appraised … met in 10 … estimated directly in 10" | Data (after D2) |
| B4 | "74 … because only the abstract was accessible" | §4.1 p. 47; §5.4 p. 71 | 75 = 66 abstract only + 8 title only + 1 insufficient full text | Data |
| B5 | Mukhopadhyay rated from abstract | Table 4.1 (moved to "other studies", n.a.); Appendix C | See D2 | D2 |
| B6 | List of DC-dimension studies | §4.3 p. 54; §5.2 RQ3 | 4 conceptual (2 cited, 2 "listed in Appendix C"), 1 Delphi, 2 qualitative/mixed, **3** quantitative; Deng 2025 described separately | Data |
| B7 | "measure these dimensions" | §4.4.1; §5.1 | "address … only three of them quantitatively" | Data |
| B8 | "how most empirical studies model DC" | §2.4.2 p. 30 | "corresponds to studies that model dynamic capabilities as an overall construct" | dc_order = 0 higher-order |
| B9 | Wang 2026 "only high-quality study that tests …" | §4.2.1 p. 51; §5.2 RQ1 | Described as a moderation model, with AIC and DI measured in the same wave; the null coefficient is "not … a test designed for H1". Classification kept (contradictory). | Wang abstract; extraction notes |
| B10 | Srahin "no remaining direct effect" | §4.2.1; §4.3.4 | "only a small remaining direct effect"; p = 0.036 reported | Extraction |
| B11 | Fano wording | §4.2.2 p. 53 | "fostered dynamic capabilities, measured as sensing, seizing and transforming" | Fano abstract |
| B12 | Li 2026 "502 … firms" | §4.2.2; §4.3.2–4.3.4 | "502 managers of Chinese tourism businesses" / "tourism businesses" | Li abstract |
| B13 | Mukhopadhyay direction | §4.2.2 | "describe how dynamic capabilities, exercised through AI technologies, enhance marketing practices"; "without establishing a direction" | Abstract |
| B14 | Li 2025 (title only) used for a finding | §4.4.1 p. 59 | Removed from the boundary-condition claim | Title only |
| B15 | Siaw abstract inconsistency | §4.3.1 p. 55 | Cautious wording; states that the abstract is inconsistent and the proposition needs full-text checking | Siaw abstract |
| B16 | "For platform firms, the evidence on sellers …" | §5.3.2 p. 70 | "For firms that sell through platforms …" | §1.4 scope rule |
| B17 | Unlabelled complementor study | §5.1 p. 65 | "the only one of high quality examines complementors that sell through cross-border platforms rather than platform owners or retailers" | §1.4 |
| B18 | Shao causal and "partly" wording | §2.3.2 p. 25 | "was positively associated with … with business model innovation acting as a mediator" | Shao abstract (no "partial") |
| B19 | Almheiri "enhance" | §2.3.2 p. 25 | "positively associated with" | Cross-sectional design |
| B20 | "re-screening check" | §3.4 p. 41 | "the second screening run"; appraisal "of every included study whose full text was accessible" | No re-screening described |
| B21 | "documented script" | §3.4 | "OpenAlex API with the query documented in Appendix A" | query.json |
| B22 | Table 4.1 caption scope | §4.1 p. 48 | "all empirical studies from e-commerce, platform or closely related digital contexts … and one further study discussed in the text" | Table content |
| B23 | Almheiri row missing H1 I | Table 4.1 | "H1 I; H2 D; H6 I" | Data |
| B24 | Abstract "120 … appraised against nine criteria" | Abstract p. 2 | "Twenty of the 95 empirical studies could be appraised …" | Data |
| B26 | E5 borderline studies | §3.2.2 p. 37; Appendix C (**E**) | The construct criterion is clarified (authors' explicit DC definition); four studies are marked **E** | Abstracts of Li 2026, Sofiyan 2026, Shore 2024, Tian 2023 |
| B27 | Publication details unconfirmed | Table 4.1 and Appendix C (**†**); §4.2.1, §4.2.2 | Markers for Malik 2021, Firmansyah 2025, Noor 2026, Dzreke 2025, 2025b; text caveats | Records metadata; extraction notes |
| C2–C4 | Year mismatches between text and Appendix C | Appendix C; Fig. 4.2 note | Appendix C now uses `\textcite` for all 42 studies in the bibliography, so text and appendix print the same year. Fig. 4.2 note explains that years are OpenAlex first-publication years. | Bibliography |
| C5 | "- et al. (2025)" | Appendix C p. 86 | "Kabir et al. (2025)" | OpenAlex record authors (first: Md Firoz Kabir) |
| C1 | `wu2026` uncited | Appendix C | Now cited via Appendix C. `martinmartin2021` is still uncited (biblatex omits it; harmless). | — |
| — | Biber "comma at end of name" warnings (2) | `bibliography.bib` (sofiyan2026, firmansyah2025) | Removed the stray commas after the single-name authors "Sabar" and "Firmansyah". Biber warnings: 2 → 0. | Biber log |
| — | Draft note | `Chapter4.tex` header comment | Lists all nine title-only studies, not two | Data |

## 4. Audit findings revised by this pass

- **Gafsi 2026.** The first audit called this a "Mismatch". On re-reading, the abstract names *competitive performance* as the dependent variable and reports the finding as *firm performance*. The evidence is therefore ambiguous, not contradictory.
  - **Status:** downgraded to "Needs checking".
  - **Thesis:** the classification was kept and marked provisional, rather than changed without the full text.
- **E5-borderline studies.** Each of the four measures a construct that its authors define as a dynamic capability:
  - Li 2026: opportunity sensing capability;
  - Sofiyan 2026: dynamic managerial capability;
  - Tian 2023: supply chain resilience;
  - Shore 2024: contingent DC view.

  They are therefore retained, with the rule now stated in §3.2.2. No study was excluded.

## 5. What was deliberately *not* changed

- **No study was excluded.** This includes the nine title-only studies, Gafsi, Wang and the E5-borderline studies.
- **No estimate, quotation, page number or bibliographic detail was added** that is not in the review data or the OpenAlex records.
- **The original review data are unchanged.** The data README's word "independent" remains as it is.
- **The full-text-stage figures are retained but unverified:** 64/133 and the 77 exclusion reasons (48/17/8/3/1).
- **The `fano2025` bibliography year (2026)** was not changed. The correct year cannot be confirmed without the publisher record.
- **The LaTeX notes "Rewrite the text in your own words"** and the empty author e-mail and submission date are left for the author.
