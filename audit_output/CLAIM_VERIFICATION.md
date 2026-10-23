# Claim Verification: H1–H6, the Abstract's Headline Claims, and E-Commerce/Platform Evidence

## Read this first: what "verified" means here

**No original paper was available.** None was in the repository. Every DOI resolver, OpenAlex, Unpaywall and publisher host was blocked by this environment's network policy, and the fetch tool could not resolve hosts. Web search returned only bibliographic snippets.

**What could be checked:**

- the review dataset;
- the OpenAlex **abstracts** stored in `records.jsonl`, which are the publishers' abstracts as indexed by OpenAlex;
- a few web-search snippets, used for metadata only.

**Consequences for the verdicts:**

- **No claim is marked "Verified"**, because that status requires an inspected original source.
- "Partially verified" means the claim is consistent with the source abstract, or the abstract contains the quoted words, while the estimates, methods and page numbers remain unchecked.
- All 158 quotations attributed to abstracts were found verbatim (or near-verbatim) in the abstracts.
- The 84 quotations attributed to full texts could not be checked.
- No page numbers are recorded anywhere in the extraction.

**Evidence type** is given as: **Direct** (the study reports the hypothesised relationship with the hypothesis's constructs), **Indirect** (a related construct or outcome) or **Conceptual**.

---

## A. Headline claims (abstract, §4.4.1, §5.1)

### A1. "In the strongest studies, the direct effect of AI disappears once these capabilities are considered" (abstract; §5.1 cites srahin2026 and texeira2026; §4.4.1 adds chen2026)

**Verdict: Mismatch (overgeneralised).**

**The three high-quality studies:**

| Study | What the data/abstract show |
|---|---|
| Texeira 2026 | Direct B = 0.071, p = 0.070 with mediators in the model. Full-text quote, unchecked. Fits the claim. |
| Wang 2026 | AI capability is a *moderator*. There is no mediation of an AI effect, so it does not illustrate the claim. |
| **Guo 2025** | The direct paths **remain significant** (β = 0.519 and 0.336) alongside the IMC indirect effects. This contradicts the claim. |

**The moderate-quality studies used:**

- **Srahin 2026:** the direct effect has a BCa CI of [−0.005, 0.179], but t = 2.108, p = 0.036. The source is ambiguous, not "disappeared".
- **Malik 2021:** the abstract says innovation capability "*partially* mediates".

**The third study cited (§4.4.1):** Chen 2026 is **not assessable** (abstract only). It concerns AI *infrastructure*, and its abstract says two of the routes from AI infrastructure were non-significant. It cannot be counted among "the strongest studies".

**Counter-evidence elsewhere:**

- Tu 2026: direct effect on competitiveness.
- Ayoub 2026: significant direct effect.
- Kokash 2026: AI "directly improve[s] firm performance"; no DC mediation.
- Giang 2026: partial mediation.

**Suggested wording:** "In one high-quality and one moderate-quality study, the direct association became small or non-significant once related capabilities were modelled; in other studies a direct association remained."

### A2. "Four of the six hypotheses are partly supported, and none is fully supported" (abstract, §4.4.1, Table 4.2, §5.1)

**Verdict: Partially verified against the decision rules, but two judgements are fragile.**

**"None supported" is correct.** No hypothesis has direct moderate- or high-quality evidence from the focal context (Panel B and the Context rule).

**H3 "partly supported" is applied inconsistently with H4 and H5.** It rests on Noor 2026, where:

- the AI construct is *adoption*;
- the outcome is *marketing performance*;
- the effect is a *serial* indirect effect through market sensing **and** brand visibility.

Li 2026 is the counterpart for H4 and H5: its authors frame absorptive capacity as "seizing" and opportunity recognition as "transforming", and it also reports estimated indirect effects. Yet those are reassigned to H6 because they are "distinct constructs", and H4 and H5 are judged "not yet examined".

Either both studies count as indirect dimension evidence, which would make H3, H4 and H5 all "partly supported (one indirect study)", or neither does, which would make H3 "not yet examined". The headline "four of six" depends on this asymmetric choice.

**H6 "partly supported" conflicts with the thesis's own reasoning.** In §4.3.4 and RQ4 the thesis concludes that the evidence supports mediation "through other organisational capabilities, but **not specifically through dynamic capabilities as a higher-order construct**". The underlying evidence:

- There is no direct evidence.
- **No included study specifies DC as a higher-order construct** (0 of 120 in the data).
- The only explicit test of DC mediation found none (Kokash 2026). That is contradictory evidence on the core claim.

The label is permitted literally by Panel B ("mainly indirectly relevant evidence"), but it reads as more support than the thesis's own analysis grants. Options: "inconclusive (for DC); consistent indirect evidence for related capabilities", or keep "partly supported" with an explicit qualifier in the abstract and Table 4.2.

### A3. "Only seven concern e-commerce or platform-based business" (abstract, §4.4.2, §4.5, §5.1)

**Verdict: Partially verified (count) / overstated (description).**

**The seven are coded in the data as:**

| Study | Data coding | What the abstract shows |
|---|---|---|
| Guo 2025 | Complementor | — |
| Noor 2026 | E-commerce retailer | — |
| Bunea 2026 | E-commerce retailer | — |
| Awamleh 2022 | Other e-commerce/digital | Its abstract does say "e-commerce enterprises" |
| Firmansyah 2025 | Other e-commerce/digital | Does not mention e-commerce or digital business |
| Adamu 2026 | Other e-commerce/digital | "digitally active sectors" (FinTech, banking, technology) |
| Dzreke 2025b | Platform owner | Conceptual |

§4.4.2 itself calls Firmansyah and Adamu "digitally active firms more broadly". Strictly, 4 empirical e-commerce/platform studies exist (1 of them about complementors), plus 1 conceptual platform-owner paper. The abstract and §5.1 phrase this as "seven concern e-commerce or platform-based business", which overstates.

**Coding inconsistencies:**

- The TA-stage flag `ecommerce_platform` was set for 11 of the 197 reports; only 4 of these were included. The 7 excluded flagged reports include *Algorithm-Centric Business Development … AI-Dominated E-Commerce* and *Causal Factors of Competitive Advantages … E-commerce*. Their full-text exclusion reasons are not recorded.
- Three included studies were coded as focal only after screening.
- Kambara 2026 (fashion retail, conceptual) and Wasesa 2025 (multi-sector including e-commerce) are coded "none".

---

## B. H1: AI capability is positively associated with sustainable competitive advantage

**Thesis judgement:** partly supported. Nine direct, 44 indirect, 3 contradictory.

| Study | Thesis claim | Source location checked | Evidence type | Verdict | Explanation |
|---|---|---|---|---|---|
| Shao 2026 | 546 Chinese SMEs; AI capability → CA; "partly mediated" by BMI (Ch. 2) | Abstract | Direct (association) | Partially verified | The abstract confirms the sample, the positive influence and BMI mediation. "Partly" is **not** in the abstract. The authors frame AI capability as a dynamic capability, so it overlaps with the mediator (the thesis notes this). |
| Kim 2026 | 400 Korean exporters; AI capability → differentiation and low-cost CA | Abstract (Korean) | Direct | Partially verified | The abstract states that both capabilities significantly raised both CA types. |
| Tu 2026 | 304 Chinese manufacturers; AI capability → competitiveness | Abstract | Direct ("competitiveness" ≈ CA) | Partially verified | Direct and serial indirect effects are stated. |
| Firmansyah 2025 | 0.361 in 70 digital MSMEs; low quality; the only digital-context direct study | Abstract ("36.1%"); 0.361 / t = 3.072 from the full text, unchecked | Direct | **Needs checking** | No DOI. The abstract contains a stray fragment from another text. AI capability is modelled as a *mediator* of KMC→SCA. The "digital MSME" context is not in the abstract. Peer review is unverified. |
| Waqas 2024 | AI capability (with BDA and IoT) → green CA | Abstract | Direct, but only jointly reported | Partially verified | The abstract gives no AI-specific result. The thesis acknowledges this. |
| Giang 2026 | AI capability → CA (jointly reported) | Abstract | Direct, but only jointly reported | Partially verified | No AI-specific estimate. Classifying it as "directly reported" is generous. |
| Almereb 2026 | Generative AI → cost and differentiation CA | Abstract | Direct only if GenAI = capability | Partially verified | GenAI is a *mediator* of GSCM→CA. The checker re-coded the construct from "use" to "capability". |
| Al-Mamary 2025 | AI capabilities → CA and venture success | Abstract | Ambiguous | Partially verified | CA appears to be one of several AI-capability "effect areas" that predict venture success. The role of CA (outcome or dimension) is unclear. |
| **Gafsi 2026** | AI capabilities → "competitive performance" | Abstract | **Indirect** | **Mismatch** | The abstract reports the result as "significantly enhance **firm performance**". Under Table 3.3's Outcome rule this is indirectly relevant, not direct. |
| Wang 2026 (contradictory) | "Only high-quality study that tests the relationship directly finds no significant effect" (b = 0.05) | Abstract; b = 0.05 from a full-text table that the extraction calls "garbled" | Not a direct test | **Needs checking** | The abstract presents AI capability **only as a moderator** of SEO→disruptive innovation. b = 0.05 is a coefficient inside an interaction model. AI capability and disruptive innovation were measured in the same wave. Calling this *the* decisive high-quality test of H1 overstates. |
| Chen 2026 (contradictory) | AI infrastructure has no direct effect; works only via green innovation | Abstract | Indirect (AI infrastructure) | Partially verified | Consistent with the abstract, which adds that two AI-infrastructure routes were also non-significant. |
| Mashi 2024 (mixed) | Adoption n.s.; applications significant | Abstract | Direct/mixed (use facets) | Partially verified | Consistent. The sample is reported as both 315 and 346. |
| Guo 2025 (high, indirect) | β = 0.519 / 0.336 | Abstract and web snippet of the publisher record; estimates full text only | Indirect (AI adoption + strategic agility; complementors) | Partially verified | The predictor bundles *platform* AI use with strategic agility, itself a DC. It is not a firm AI capability. |
| Srahin 2026 (moderate) | Total effect 0.542; direct CI includes zero; indirect 0.445 | Abstract ("operates mainly through firm agility") | Indirect (augmented analytics adoption) | Partially verified | Omits that p = 0.036 for the direct path. |
| Texeira 2026 (high) | Not significant once mediators are included | Abstract (null direct effect is full text only) | Indirect | Partially verified on this point | See the H6 table for the moderator mismatch. |

**Overstatement check:**

- **Causality.** The thesis mostly uses "associated" correctly. Exceptions: Ch. 2 says "AI capability had a positive effect on competitive advantage" (Shao), and §2.3.2 says "AI capability has been found to enhance dynamic capabilities".
- **Sustained competitive advantage.** The thesis correctly states (§4.2.1) that even the direct evidence concerns perceived CA at one point in time, not *sustainable* CA. Only Dzreke 2025 measured persistence, and its credibility is doubtful.
- **Robust direct count.** After the corrections above, the robust direct H1 evidence is Shao, Kim, Tu and (doubtfully) Firmansyah, all unappraisable or low quality. The "partly supported" judgement survives, but "nine independent studies report … directly" should be revised to roughly 4–8 with explicit caveats.

## C. H2: AI capability is positively associated with dynamic capabilities

**Thesis judgement:** partly supported. Three direct samples, 41 indirect, 1 contradictory.

| Study | Thesis claim | Source checked | Evidence type | Verdict | Explanation |
|---|---|---|---|---|---|
| Almheiri 2024 + 2025 (one sample) | AI capability enhances DC; 344 UAE public managers | Both abstracts | Direct | Partially verified | Both abstracts state the positive AI-capability→DC relationship, with 344 public managers and the same scale development. Same sample: plausible. Outcome: public-sector performance. |
| Fano 2025 | AI ambidexterity "fostered sensing, seizing and transforming" | Abstract | Direct (DC overall; AI ambidexterity) | Partially verified | The abstract reports that AI ambidexterity "fosters dynamic capabilities". No dimension-level results appear, so the thesis wording slightly overstates. The bib year (2026) differs from the key and Appendix C (2025). |
| Neira-Fernández 2026 | AI readiness related to dynamic digital capabilities | Abstract | Direct only if readiness = capability; the link is inferred from a mediation sentence | Partially verified | The "direct" quote infers AIR→DDC from "DDC mediates this relationship". n not reported. |
| Malik 2021 | β = 0.68 and 0.62 | Abstract | Indirect | **Needs checking** | The abstract confirms both estimates. But the publication metadata are inconsistent (year 2021 vs a recent-range Zenodo DOI), CB-SEM fit indices are reported for a PLS model, and there are reporting inconsistencies. Check the year and peer review before relying on it. |
| Srahin 2026 | Adoption → agility β = 0.625 | Full text, unchecked | Indirect | Partially verified | Abstract-level consistency only. |
| Li 2026 | AI orientation → absorptive capacity β = 0.312 in "502 … firms" | Abstract | Indirect | Partially verified | The abstract says "502 managerial respondents", not firms. The study is borderline under E5. |
| Noor 2026 | GenAI adoption → market sensing β = 0.571 | Full text, unchecked | Indirect (adoption) | Partially verified | No DOI; journal peer review unverified; n unreported ("400–500"). |
| Mukhopadhyay 2024 | AI-enabled marketing "strengthened dynamic capabilities" | Abstract | Qualitative | **Needs checking** | The abstract speaks of DC "through AI technologies" enhancing marketing, so the direction is reversed or unclear. It is rated "moderate" from the abstract alone, unlike every other appraised study. |
| Sofiyan 2026 (contradictory) | No direct AIC→change capacity effect; only under transformational leadership | Abstract | Contradictory/indirect | Partially verified | Consistent. Military setting; borderline under E5. |
| Deng 2025 | DC → GenAI adoption (β = 0.453) | Abstract | Reverse direction | Partially verified | The β is confirmed in the abstract. |

**H2 count.** The "41 indirect" figure depends on the erroneous Almheiri 2026 same-sample link; it should be 42 (DATA_RECONCILIATION §5). The direction ("AI builds DC") is unresolved; the thesis states this correctly.

**Overstatement.** The judgement is justified. The thesis's own sensitivity check shows that **no appraisable study reports AI capability→DC directly**.

## D. H3–H5: dimension-specific mediation

**H3 (sensing).** The judgement rests solely on Noor 2026's serial indirect effect of 0.110 on marketing performance. It is from the full text and unverified.

- The thesis correctly labels it indirectly relevant.
- See A2 for the asymmetry with H4 and H5.
- Maune 2026 (qualitative: AI enhanced sensing) and Siaw 2024 (conceptual) are context only.
- **Siaw's abstract contradicts itself.** Its Findings say AI substitution suits external scanning; its Limitations say AI may be ineffective for external scanning. §4.3.1 uses only the second reading. **Needs checking.**

**H4 and H5.** "Not yet examined" is consistent with the assignment rule, but not with the H3 treatment (see A2).

Li 2026's indirect estimates (0.067; 0.057; serial 0.009) are full-text quotes and unverified. The abstract does confirm that the authors frame AC as seizing and EOR as transforming, and that bootstrapping with 5,000 resamples was used.

**§4.3 breakdown of the 10 dimension studies: Mismatch** (DATA_RECONCILIATION §5). Corrected breakdown:

- 3 quantitative studies, not 4. Deng 2025 is coded DC "overall".
- Ghobakhloo 2025 is a Delphi study, not conceptual.
- Wei 2025 and Arowolo 2026 are omitted from the list.

**The thesis does not overclaim here.** It correctly states that no study estimates a dimension-specific indirect effect on CA, and that "theorising … runs well ahead of testing".

## E. H6: DC as a higher-order mediator

| Study | Thesis claim | Source checked | Verdict | Explanation |
|---|---|---|---|---|
| Malik 2021 | Indirect 0.31 (innovation capability) and 0.27 (organisational capability) | Abstract confirms 0.31 | Needs checking | See H2. 0.27 is from the full text. |
| Srahin 2026 | Indirect 0.445 via agility, "with no remaining direct effect" | Abstract consistent | Partially verified | "No remaining direct effect" ignores p = 0.036. |
| Guo 2025 | IMC indirect 0.346 / 0.242 | Abstract confirms the IMC mediation | Partially verified | The extraction notes the table gives .255, not .242. |
| **Texeira 2026** | "indirect effect increased with **strategic flexibility**" (§4.3.4, §4.4.1, Fig. 4.4, §5.3) | Abstract | **Mismatch** | The abstract names the moderator **sustainable food innovation orientation** (the extraction's "SFIO"). "Strategic flexibility" does not appear. This error has spread into the revised model's boundary conditions and the managerial implications. |
| Tu 2026 | Learning and resilience | Abstract | Partially verified | The serial mediation is stated in the abstract. |
| Dzreke 2025 | Orchestration capability (58%) | Abstract | Partially verified | Serious credibility concerns are recorded in the extraction. The thesis notes "doubts". |
| Kokash 2026 | DC mediation not found | Abstract | Partially verified | It is the only explicit test of DC mediation, and it is contradictory. |
| Ayoub 2026; Shao 2026 | Merge AI and DC constructs | Abstracts | Partially verified | Consistent. |

**Overstatement.** "AI capability works through organisational capabilities" is supported as an *association* pattern; §4.3.4 correctly warns against reading it causally. Two problems remain:

- The **H6 label** overstates. No higher-order DC specification exists in any study, and the only DC-mediation test is null.
- Ch. 2 §2.4.2's statement that the higher-order specification "corresponds to how most empirical studies model dynamic capabilities" is contradicted by the data.

## F. E-commerce and platform claims (§1.4, §2.3.1, §4.4.2, §5.3)

| Claim | Verdict | Explanation |
|---|---|---|
| Complementor studies are treated as "closely related evidence … labelled as such and not taken as evidence about platform owners" (§1.4, §2.3.1) | Consistent in §4.4.2 | Guo is labelled "complementors". |
| §5.1: "only one of them [the seven] is of high quality (guo2025)" | Needs a label | That one high-quality study concerns complementors. Say so. |
| §5.3: "**For platform firms**, the evidence on sellers using cross-border platforms suggests …" | **Mismatch with §1.4** | Complementor evidence is applied to "platform firms". The next paragraph labels complementors correctly. Rephrase to "For sellers on platforms (complementors) …". |
| §4.4.2: "The only study of platform owners is conceptual" (Dzreke 2025b) | Partially verified | The abstract makes unsupported quantitative claims ("71% of market dominance"). The thesis flags its "uncertain peer-review status". |
| §4.4.2: Dzreke 2025 effects "stronger in … FinTech and e-commerce" | Source unavailable | Full-text quote. The abstract says nothing on sectors. Correctly treated as a hypothesis only. |
| §4.4.2 geography: 30 of 95 not reported; SE Asia 14 … | Reconciles | — |
| §4.4.2: "only three studies each come from North America and Europe" | Needs checking | It depends on how multi-region studies are counted. |

## G. Methodology claims to correct

- **Ch. 3 §3.2.2:** "All inclusion decisions and extracted results **are checked** by the author." The README and the LaTeX comments state this still **must** be done before submission. If it has not been done, the sentence is currently untrue and must be changed (e.g. "were checked …" only after doing it, or "should be checked" with the limitation disclosed).
- **Ch. 3 §3.5 and §4.1:** "eligibility and data extraction rely on the abstract" / "the other 133 were assessed on the basis of their abstracts". 9 included studies had no abstract.
- **Ch. 5 §5.4:** "verify every extraction against a quotation from its source". 92 studies were abstract-only, and the "source" for the full-text quotes cannot be audited. There are no page numbers.
- **Ch. 3 §3.4:** "credibility is supported by … the re-screening check". No re-screening check is described anywhere.

---

## Update v2: how each claim was handled in the corrected thesis

- **A1 (direct effect disappears):** rewritten. The thesis now reports a non-uniform pattern. Chen 2026 has been removed from the "strongest" list.
- **A2 (four of six):** the rules were applied consistently, so H4 and H5 are now partly supported (one indirect study each). H6 is qualified as "related capabilities only". Supervisor confirmation is advised.
- **A3 (seven studies):** the thesis now says four empirical e-commerce/platform studies, plus closely related ones.
- **H1 Gafsi 2026:** the verdict is revised from Mismatch to **Needs checking**. The abstract names "competitive performance" as the dependent variable, so the evidence is ambiguous rather than contradictory. The classification is kept as provisional.
- **H1 Wang 2026:** reworded as a moderation model; still Needs checking.
- **H6 Texeira 2026:** the moderator name has been corrected to "sustainable food innovation orientation" everywhere.
- **F (complementors):** the §5.1 and §5.3.2 wording is fixed.
- **G (methodology claims):** the manual-check sentence is reworded with a note for the author; "re-screening check" and "documented script" are corrected; title-only studies are disclosed.

**No claim has been verified against an original full text.** All verdicts above remain at abstract level.
