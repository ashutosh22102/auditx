# Thesis Issues and Suggested Corrections

**Version audited.** This is the LaTeX source in `xxxx.zip` → `SRH_Thesis_Template/`. It is the only version supplied.

- The chapter files were last modified on 23 Oct 2026 between 07:22 and 07:28, and `main.tex` at 07:25.
- **No thesis PDF exists**, and no LaTeX toolchain is installed in this environment, so **page numbers cannot be given**.
- Locations are therefore given as section number and `file:line`. Section numbers are derived from the order of `\section` and `\subsection` commands; table and figure numbers come from their order within each chapter.

**The thesis was not edited.** Suggested wording is offered only as a proposal.

**Severity levels:**

- **A** = must fix before sending to the professor: factual or integrity issue.
- **B** = should fix: inconsistency or overstatement.
- **C** = polish.

---

## A. Must fix before sending

### A1. "120 studies … 118 independent samples" is wrong

**Location:** §4.1, `Chapter4.tex:26`; Fig. 4.1 node, `Chapter4.tex:44`.

**Problem:**

- One shared pair among 120 publications gives 119.
- "118" only reproduces through a data error that also links Almheiri et al. (2026), a sample of 400 hotel managers, to the 344 public-manager sample.
- Conceptual papers have no samples.

**Fix:** "120 studies (119 after linking the two Almheiri et al. publications that use the same sample; 94 independent empirical samples)". Correct `same_sample_as` for W7203683920 in the data, then recount H2 (indirect 41 → 42; see A6).

### A2. Abstract and §5.1: "in the strongest studies, the direct effect of AI disappears"

**Location:** `main.tex:165`; §5.1 `Chapter5.tex:23`; §4.4.1 `Chapter4.tex:286`; §5.3.1 `Chapter5.tex:58`.

**Problem:** Of the three high-quality studies:

- one fits (Texeira);
- one tests AI only as a moderator (Wang);
- in one, the direct paths remain significant (Guo, β = 0.519 and 0.336).

In addition:

- Srahin's direct path has p = 0.036 even though its CI includes zero.
- Chen 2026, cited among "the strongest", is not assessable.

**Fix:** "In two studies whose quality could be appraised, the direct association became small or non-significant once related capabilities were included; other studies report both direct and indirect associations." Remove chen2026 from the "strongest" list.

### A3. Texeira (2026) moderator misnamed as "strategic flexibility"

**Location:** §4.3.4 `Chapter4.tex:242` and `:248`; §4.4.1 `:290`; §4.4.3 `:318` and Fig. 4.4 node `:341`; §5.3.1 `Chapter5.tex:62`; §5.3.2 `:71`.

**Problem:** The source abstract names the moderator **sustainable food innovation orientation**. The error also creates the "strategic flexibility" boundary condition in the revised model and the managerial implications.

**Fix:** Correct the construct name throughout. Reconsider whether this belongs among the *general* boundary conditions (it is a restaurant-specific orientation).

### A4. Statements about checks that the data show have not (yet) been documented

**"All inclusion decisions and extracted results are checked by the author"** (§3.2.2, `Chapter3.tex:186`).

- The README and the LaTeX header (`Chapter3.tex:7–10`, `Chapter4.tex:8–12`) say this **must still be done**.
- No record of manual checks exists.
- If the checks are not complete, the sentence is untrue. Complete the checks, or reword it to "will be"/"were partly", and disclose this as a limitation.

**"eligibility and data extraction rely on the abstract"** (§3.5, `Chapter3.tex:291`) and **"133 were assessed on the basis of their abstracts"** (§4.1, `Chapter4.tex:26`).

- **9 included studies have no abstract and no full text:** Hossain 2022, Htet 2026, Li 2025, Wu 2026, Anjum 2026, Ramírez 2026, Amin 2026, Samadhiya 2023 and Luo 2025.
- The header comment (`Chapter4.tex:11`) names only Wu and Li.
- **Fix:** Read the nine papers and confirm or remove each. Update 120, 95/25, 74 n.a., Appendix C and Fig. 4.2/4.3 accordingly.

**"64 full texts / 133 abstracts" and the 77 exclusion reasons** (§4.1, Fig. 4.1).

- There is no supporting record in `review_data`.
- **Fix:** Supply the full-text-stage log in the appendix or supplementary data, or state that it is unavailable.

### A5. Declaration of Honour versus AI assistance

**Location:** `main.tex:235–236`.

**Problem:** The declaration says that the thesis was written "without outside help" and with "no sources or aids other than those indicated".

- Ch. 3 discloses language-model use for screening and extraction.
- Every chapter header contains "Rewrite the text in your own words".
- The Ch. 3 header asks the author to "check SRH rules on declaring AI assistance".

**Fix:** Before submission, check the SRH AI-use policy with the supervisor. Make the declaration and §3.4 consistent with the actual use of AI tools, including any drafting assistance.

### A6. H2 count and the inconsistent independence rule

**Location:** §4.2.2; Table 4.2 `Chapter4.tex:274`; RQ2 `Chapter5.tex:39`.

**Problem:** "41 studies with indirectly relevant evidence" reproduces only with the erroneous Almheiri 2026 link. With the pair-only rule (the one that gives H1's 44), the figure is **42**.

**Fix:** Correct the link and recount. Document the "count once under the stronger category" rule used for H1 and H2.

### A7. H1 "Nine independent studies report … directly" (§4.2.1 `Chapter4.tex:189`; Table 4.1; Table 4.2; RQ1 `Chapter5.tex:35`)

**Gafsi 2026:** the abstract reports *firm performance*. Under the Outcome rule (Table 3.3, Panel C) this is indirectly relevant.

**Further borderline studies:**

- Giang 2026 and Waqas 2024: AI effect only reported jointly with other capabilities.
- Almereb 2026: generative AI, re-coded from "use" to "capability".
- Al-Mamary 2025: role of CA ambiguous.

**Fix:** Reclassify Gafsi (9 → 8), or justify keeping it. Add a footnote listing the borderline cases. The "partly supported" judgement survives either way.

### A8. Focal-context claim: "only seven concern e-commerce or platform-based business"

**Location:** `main.tex:165`; §4.4.2 `Chapter4.tex:303`; §4.5 `:370`; §5.1 `Chapter5.tex:23`.

**Problem:** Two of the seven are not e-commerce or platform studies:

- Firmansyah 2025: the abstract does not mention e-commerce or digital business.
- Adamu 2026: FinTech, banking and technology firms.

One is conceptual (Dzreke 2025b), and one concerns complementors (Guo).

**Fix (abstract):** "only seven concern e-commerce, platform or closely related digital contexts (four empirical e-commerce or platform studies, one of them on complementors)". Keep §4.4.2's own description, "focal and closely related context".

### A9. H3 versus H4/H5 asymmetry, and the H6 label

**Location:** §4.3.1–4.3.4; Table 4.2; abstract "four of the six".

**The asymmetry:**

- Noor 2026 has an adoption construct, a marketing-performance outcome and a serial effect through an extra mediator. It is counted for H3.
- Li 2026's indirect effects, through constructs its authors call seizing and transforming, are reassigned to H6.

**Fix:** Apply one rule to both. Either both count as indirectly relevant dimension evidence, or H3 becomes "not yet examined". If the rule changes, the headline "four of six" changes too.

**The H6 label:** "partly supported" conflicts with the thesis's own conclusion that the evidence is "not specifically through dynamic capabilities as a higher-order construct":

- no study specifies DC as a higher-order construct;
- the only DC-mediation test was null (Kokash).

**Fix:** Qualify the label wherever it appears, e.g. "partly supported for related capabilities; not supported for DC as a higher-order construct".

## B. Should fix (inconsistencies, overstatements, wrong descriptions)

| # | Location | Issue | Suggested correction |
|---|---|---|---|
| B1 | §4.1 `Chapter4.tex:83` vs §4.4.2 `:311` | "Most studies do not report the country", but 30 of 95 (32%) do not | "About a third of the empirical studies (30 of 95) do not report …" |
| B2 | §4.1 `:83`; abstract; §5.1/5.4 | "Almost all empirical studies are cross-sectional surveys (65 of 95)": 68% | "Most (65 of 95) …; only two separated measures in time" |
| B3 | §4.1 `:122` | "Among the studies that could be appraised … CMB … in 11 … indirect effect … in 13": among the 21 appraised, both are **10**; 11 and 13 include ratings of not-assessable studies | Use 10 and 10, or change the denominator |
| B4 | §4.1 `:122`; §5.4 `Chapter5.tex:81` | 74 n.a. "because only the abstract was accessible": 65 abstract-only, 8 title-only, 1 full text but insufficient (Nikzat 2025) | Use §5.4's "mostly because"; give the breakdown |
| B5 | §4.1 `:122` / Appendix C | Mukhopadhyay 2024 is rated "moderate" from the abstract only, unlike all other appraisals | Mark n.a. until the full text is read |
| B6 | §4.3 `Chapter4.tex:220`; RQ3 `Chapter5.tex:43` | The 10 dimension studies are mis-listed: Deng 2025 is not a dimension study in the data; Ghobakhloo 2025 is a Delphi study, not conceptual; Wei 2025 and Arowolo 2026 are omitted; there are 3 quantitative studies, not 4 | Correct the list and numbers |
| B7 | §4.4.1 `:288`; §5.1 | "only 10 of the 120 studies **measure** these dimensions": 4 are conceptual | "address" instead of "measure" |
| B8 | §2.4.2 `Chapter2.tex:314` | The higher-order specification "corresponds to how most empirical studies model dynamic capabilities": 0 of 120 included studies are coded higher-order | Delete, or support with the cited prior studies only |
| B9 | §4.2.1 `:193`, `:201`; §5.2 `Chapter5.tex:35` | Wang 2026 "the only high-quality study that tests the relationship directly": the abstract presents AI only as a moderator; b = 0.05 is a coefficient in an interaction model; AI capability and disruptive innovation were measured in the same wave | "a high-quality study in which AI capability was modelled as a moderator found no significant main effect" |
| B10 | §4.3.4 `:242`, `:248` | Srahin: "with no remaining direct effect"; the source reports p = 0.036 with a CI including zero | Report both |
| B11 | §4.2.2 `:206` | Fano: "fostered sensing, seizing and transforming": the abstract reports DC overall, not dimension results | "fostered dynamic capabilities (sensing, seizing, transforming)" |
| B12 | §4.2.2 `:210` | Li 2026 "502 Chinese tourism firms": the abstract says 502 managerial respondents | "502 managers of tourism businesses" |
| B13 | §4.2.2 `:210` | Mukhopadhyay: "AI-enabled marketing practices strengthened dynamic capabilities": the abstract frames DC *through* AI enhancing marketing | Rephrase direction |
| B14 | §4.4.1 `:290` | Li 2025 listed among studies where dynamism "shaped the role of AI", but it was included on title only | Remove until read |
| B15 | §4.3.1 `:227` | Siaw 2024: its abstract contradicts itself on external scanning | Check the full text; state the proposition precisely |
| B16 | §5.3.2 `Chapter5.tex:71` | "For platform firms, the evidence on sellers using cross-border platforms …": complementor evidence applied to platform firms, contrary to §1.4 | "For sellers on platforms (complementors) …" |
| B17 | §5.1 `Chapter5.tex:23` | "only one of them is of high quality (guo2025)": not labelled as complementor evidence | Add "(a study of complementors)" |
| B18 | Ch. 2 `Chapter2.tex:171`, `:202`; Ch. 1 `Chapter1.tex:36` | Shao: "partly mediated" is not in the abstract; "positive effect" and "enhance" are causal wording | Check the full text; use "associated with" |
| B19 | §2.3.2 `Chapter2.tex:200` | "AI capability has been found to enhance dynamic capabilities" (Almheiri): cross-sectional | "is positively associated with" |
| B20 | §3.4 `Chapter3.tex:283` | "the re-screening check": no such check is described | Describe it, or delete |
| B21 | §3.4 `Chapter3.tex:285` | "a documented script": not provided in `review_data` | Add it to the supplementary material, or remove the claim |
| B22 | Table 4.1 caption text `Chapter4.tex:122` | Claims to list "all studies from e-commerce or platform contexts", but Dzreke 2025b (platform owner, conceptual) is absent | Add it, or qualify "empirical" |
| B23 | Table 4.1 `Chapter4.tex:151` | The Almheiri row omits the H1 "indirectly relevant" code that the data hold for almheiri2024 | Align with the data |
| B24 | Abstract `main.tex:163` | "120 studies were included, appraised against nine quality criteria": only 21 could be appraised | "… of which 21 could be appraised against nine quality criteria" |
| B25 | §3.2.2 vs README | The README calls the screening runs "independent"; the thesis correctly says they are not | Keep the thesis wording; align the README if it is submitted |
| B26 | Included set vs E5 (Table 3.1) | Li 2026, Sofiyan 2026, Shore 2024 and Tian 2023 have neither a DC nor a CA construct as coded (mediators framed as DC by their authors) | Document why each passes E5 |
| B27 | Malik 2021 (key H2/H6 evidence; §4.2.2, §4.3.4, §5.3.2) | OpenAlex year 2021 conflicts with a recent-range Zenodo DOI; reporting inconsistencies | Verify the year, issue and peer-review status with the publisher before citing |

## C. Citations, bibliography and appendices

| # | Location | Issue | Suggested correction |
|---|---|---|---|
| C1 | `bibliography.bib` | All 112 cited keys exist. `wu2026` and `martinmartin2021` are never cited. biblatex will omit them, so this is harmless, but Wu 2026 is an included title-only study | Remove the entries, or cite them deliberately |
| C2 | `fano2025` | Bib year **2026**; key, data and Appendix C say 2025. The text will print "Fano et al. (2026)" next to Appendix C's "(2025)" | Choose one year (issue vs online) consistently |
| C3 | `almheiri2025` | Bib 2025, Appendix C 2024, so Appendix C shows **two** "Almheiri et al. (2024)" rows | Use the same year in Appendix C, or add 2024a/2024b |
| C4 | `kemp2024`, `siaw2024`, `krakowski2023`, `rana2022`, `neiroukh2025` | Bib year ≠ OpenAlex year (online-first vs issue). Kemp appears as 2023 in Appendix C and 2024 in the text | Adopt one convention |
| C5 | Appendix C `AppendixC.tex:27` | First row: "- et al. (2025)", with the author missing | Fill in the author of *Deep Learning-Enabled Business Models for Competitive Advantage* (IJSAT) |
| C6 | `firmansyah2025`, `noor2026` | No DOI; peer-review status of the journals unverified (extraction notes) | Add a stable URL; confirm peer review |
| C7 | All chapters | No citation has a page number (SRH 4.2.1; LaTeX headers repeat this) | Add pages for direct claims and quotations |
| C8 | Appendix C vs data | All 120 included studies are present; tiers and quality ratings match the data | No action |
| C9 | Appendix A `AppendixA.tex:23` | "121 studies eligible before the final language check": the seed list is not supplied | Supply it, or describe it |
| C10 | `main.tex:127`, `:133` | Empty author e-mail; `\submissiondate{\today}` | Fill in before submission |

## D. Checks that came out clean (no action)

- The PRISMA counts reconcile with `ta_final.json`: 1,807 → 10 duplicates → 1,797 → 1,600 excluded (1,032 / 413 / 147 / 8) → 197 → 120 included.
- Tiers, years, designs, construct counts, the AI→CA direction counts, the sensitivity checks, and the 13 vs 38 mediation counts all reconcile (see DATA_RECONCILIATION.md).
- The 678 citation-search records are consistently disclosed as unscreened: Ch. 3 §3.2.1, Fig. 3.2, Fig. 4.1, Appendix A, §3.5 and §5.4.
- Kappa is consistently described as agreement between model runs, not human inter-rater reliability: abstract, §3.2.2, §4.1. No wording implies human reviewers.
- "Not assessable" is consistently distinguished from "low quality": §4.1, Table 4.1 legend, Appendix C note.
- The 2015 start and 22 Oct 2026 search date are consistent across the thesis and the data. The 2026-12-31 upper filter is disclosed and explained (Appendix A).
- The limitations (single database, incomplete citation search, LLM-assisted screening and extraction, inaccessible full texts) are disclosed consistently in §3.5 and §5.4. The abstract mentions the LLM runs and the unassessable quality, but not the single database or the unscreened citation records; consider adding one clause.
- The §4.4.1 statement about which key prior studies were retrieved, excluded or missed (4 / 4 / 7) is verified against `records.jsonl` and `ta_final.json`.
- Abstract, RQs, hypotheses, results and conclusion are otherwise aligned: the same six judgements appear in Table 4.2, §4.5, §5.1, §5.2 and the abstract.

---

## Resolution status (v2)

**Fixed in the working copy** (see CORRECTION_LOG.md for locations and evidence):

- A1, A2, A3, A6, A8.
- A4: wording fixed; the checks themselves are still to be done.
- A5: disclosure added; the SRH policy check is still to be done.
- A7: classifications qualified; Gafsi is not reclassified.
- A9: rules applied consistently.
- B1–B24, B26, B27; C1 (partly), C2–C5.

**Unresolved** (see UNRESOLVED_ISSUES.md):

- the A4 manual checks (U17);
- the A5 SRH policy (U18);
- A7 Gafsi and the other provisional classifications (U6);
- B9 Wang (U4); B15 Siaw content (U9); B25 data README (U27);
- C2 `fano2025` year (U21); C6 missing DOIs and peer review (U8); C7 page numbers (U20); C9 seed list (U15); C10 e-mail and date (U19).
