# C16 Post-Build Verification Review

**Reviewer note:** C16 ("The GIA Diamonds Deep Dive") was built and merged to this repository through a separate coding session using local git/GitHub CLI tooling, as documented candidly in `AGENT-WORKFLOW.md` in this same folder. It was not built through the conversational six-step SOP process used for C1 and C2. This document is an independent post-build verification pass: it checks the course's own self-identified MUST VERIFY items against live, authoritative sources, and reports what was resolved, what remains open, and a full inventory of every VERIFY flag found across all 13 modules' fact-check files.

**Review date:** 2026-09-09
**Reviewer:** Perplexity, via web search against primary/official sources

## Headline items (explicitly flagged by the build's own retrospective as highest-risk)

### 1. Moses 1997 fluorescence conclusion (Modules 8 and 9) - RESOLVED

**What M08's article said:** "the handout's Moses 1997 study... its published conclusion, in the trade's shorthand, is that blue fluorescence did not measurably harm face-up appearance in the tested suite [VERIFY any numeric claim; several GG-era studies found effects small or context-dependent]."

**What the actual paper says, confirmed by locating and reading the primary source:**
Moses, T.M., Reinitz, I.M., King, J.M., et al., "A Contribution to Understanding the Effect of Blue Fluorescence on the Appearance of Diamonds," *Gems & Gemology*, Winter 1997 (GIA's own journal PDF, hosted at gia.edu, verified 2026-09-09).

The study's actual findings are more specific and more positive than the article's hedged summary suggests:
- Four sets of very similar round brilliants (colorless to faint yellow) were tested across common blue fluorescence strengths, viewed by trained graders, trade professionals, and average observers.
- **For average observers (the jewelry-buying public), no systematic negative effects of fluorescence were detected at all.**
- **Strongly blue fluorescent diamonds were perceived to have a *better* color appearance when viewed table-up (face-up)**, with no discernible trend table-down.
- This positive effect was **most noticeable at lower color grades** (the I and K color sets showed a stronger benefit than the E and G sets).
- Most observers saw no relationship between fluorescence and transparency (i.e., no support for a general "hazy/oily" effect in this study's sample).

**Resolution:** The M08/M09 articles' current hedged language ("did not measurably harm") is directionally correct but undersells the finding. The paper found a net *positive* effect on perceived color for stronger blue fluorescence, concentrated at lower color grades, not merely "no harm." Recommend updating M08 and M09 to state this more precisely and remove the VERIFY flag, citing: Moses, Reinitz, King, Gems & Gemology, Winter 1997.

### 2. 16 CFR Part 23 exact wording (Module 12) - RESOLVED

**What M12 flagged:** "VERIFY the current FTC Guides text (16 CFR Part 23) before printing the clause list - the wording above follows the GG paper's description of it."

**Confirmed exact statutory text**, cross-checked against three independent official/legal sources (govinfo.gov CFR archive, Cornell Law School's Legal Information Institute, and LawStack's CFR mirror), all showing identical text for the disclosure-of-treatments-to-gemstones provision:

> "It is unfair or deceptive to fail to disclose that a gemstone has been treated if:
> (a) The treatment is not permanent. The seller should disclose that the gemstone has been treated and that the treatment is or may not be permanent;
> (b) The treatment creates special care requirements for the gemstone. The seller should disclose that the gemstone has been treated and has special care requirements. It is also recommended that the seller disclose the special care requirements to the purchaser; or
> (c) The treatment has a significant effect on the stone's value. The seller should disclose that the gemstone has been treated."

(Note: this provision is currently numbered 23.24 in the consolidated CFR as reorganized in 2018; some sources still reference it under the older 23.22 numbering used before that reorganization. Both numberings were confirmed pointing to identical text.)

**Resolution:** M12's three-clause paraphrase ("not permanent / care-damaging / value-affecting, disclose") is confirmed accurate to the actual regulatory text. The VERIFY flag can be removed and replaced with a direct citation to 16 CFR 23.24 (or its predecessor 23.22 numbering), sourced via law.cornell.edu/cfr/text/16/23.24, verified 2026-09-09.

## Additional items resolved (found while reviewing Module 1 and Module 9)

### 3. Metric carat internationalized in 1907 (Module 1) - RESOLVED

Confirmed via multiple independent, corroborating sources (Wikipedia's "Carat (mass)" article, sizes.com, skyjems.ca gemological encyclopedia, and a gemologist's own published explainer): the 200mg metric carat was adopted at the Fourth General Conference on Weights and Measures (Conference Generale des Poids et Mesures), Paris, October 1907, and became compulsory by law in France shortly after, spreading to other countries over subsequent years. M01's flagged claim is accurate; the VERIFY flag can be removed with this citation.

### 4. De Beers' 1962 adoption of "4Cs" and the "clarity" swap (Module 1) - RESOLVED

Confirmed directly from GIA's own official page, "Diamond Quality: A Short History of the 4Cs" (gia.edu/gia-news-research, verified 2026-09-09): "While De Beers helped with the advertising campaigns that involved the 4Cs, it was not until August of 1962, when the term had become popular, that De Beers adopted the term 4Cs in its national magazine advertising campaign. It stopped using the term purity and started using Shipley's term clarity." This is a direct, word-for-word match to M01's claim, from GIA's own primary source. The VERIFY flag ("before quoting the 15-year gap rhetorically") can be removed; the underlying fact is confirmed by GIA itself, not merely inferred.

### 5. Why the D-to-Z color scale starts at D, not A (Module 9, deferred from Module 1) - RESOLVED

Confirmed directly from two separate official GIA pages (gia.edu/gia-about/4cs-color and 4cs.gia.edu/en-us/diamond-color, both verified 2026-09-09): "Because the creators of the GIA Color Scale wanted to start fresh, without any association with earlier systems, they chose to start with the letter D." Prior systems used inconsistent letters (A, B, C with multiple A's for best stones), Arabic and Roman numerals, and vague descriptive terms ("gem blue," "blue white"). GIA's own pages date the scale's introduction to 1953. This resolves M09's flagged item and confirms M01's original framing (which had deferred the question to M09) was correct all along. The VERIFY flag in both M01 and M09 can be removed with this citation.

## Full inventory of remaining VERIFY flags (lower priority, not independently resolved in this pass)

The course's own fact-check files are, on the whole, appropriately conservative: most flagged items are already hedged in the article text itself rather than stated as fact, which is the correct behavior even before independent resolution. The following remain open and are listed here for a future review pass, roughly in priority order:

| Module | Item | Current handling |
|---|---|---|
| M01 | Swindler 1949 (engagement-ring tradition) article text not fully read | Already hedged as "context," not taught as established |
| M03 | GIA handout link for Kautsky 2016 rough-grading article returns 404 | Already documented honestly in the bibliography with a dead-link note |
| M05 | Gaillou 2010 Wittelsbach-Graff "not same rough" mechanism wording | Already flagged VERIFY in text |
| M05 | Asscher family spelling/roles in the Cullinan recut account | Already flagged VERIFY in text |
| M06 | Exact wording of GIA's 2005 cut-grade system announcement | Already flagged VERIFY in text |
| M06 | Gilbertson 2009 "5x fire" diffraction-grating figure | Already flagged VERIFY in text |
| M07 | "Graining caps VVS/VS" trade folklore vs. specific study cases | Already explicitly hedged as folklore, not fact, in text |
| M09 | "100% independent grading, second-grader at boundaries" exact phrasing | Generic phrasing, PDF pointer given |
| M09 | Current GIA fancy-color report comment language | Already flagged VERIFY against current forms |
| M11 | Current GIA lab-grown report naming conventions ("Laboratory-grown" wording) | Already flagged VERIFY; conventions do evolve |
| M11 | Any specific screening-device model claims | Explicitly and correctly refused in text ("never quote device specifics") |
| M12 | "Cobalt-diffused" treatment line with no bibliography anchor | Flagged as needing a real citation or removal |
| M13 | Shor 2013 "Conway Yellow" auction price-per-carat figure | Flagged VERIFY before quoting the exact number |
| M04 | De Beers HQ move to Gaborone, Botswana, exact date (cited as 2001) | Flagged VERIFY |

None of these remaining items affect a core grading-practice claim (the kind of error that would mislead a learner about how to actually grade or sell a diamond); they are historical/citation-precision details, which the build's own fact-check discipline already surfaces rather than hides.

## Overall assessment

The course's self-critique and fact-checking discipline held up well under independent review: of the five items checked against live primary sources in this pass, all five confirmed the course's claims were substantively accurate, with the Moses 1997 summary actually understating a positive finding rather than overstating anything. The remaining ~14 open VERIFY items are consistently and honestly flagged in-text rather than silently asserted, which is the correct behavior for a course of this evidentiary density. Recommend resolving the remaining items opportunistically (most require a single targeted search each) before treating the course as fully publication-ready, but none of them block using the course for internal training in its current state.
