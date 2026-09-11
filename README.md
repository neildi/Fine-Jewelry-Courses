# Fine Jewelry Courses

A catalog of fine jewelry retail training courses built from the *Fine Jewelry Retail Career and Skills Reference* and the *Global Fine Jewelry Retail Career, Operations, and Competency Framework*, produced with the *Fine Jewelry Retail Course Architecture & Article-Generation Prompt Kit*.

## Source documents

- `Fine-Jewelry-Retail-Prompt-Kit.md` - course architecture, prompt chain, media policy
- `Fine-Jewelry-Retail-Career-and-Skills-Reference.md` - the primary research evidence base (job titles, KPIs, responsibilities, free-resource library, career progression map)
- `Fine-Jewelry-Career-Guide.md` - supplementary research file: compensation benchmarks by sector, AML/Form 8300/G7 sanctions compliance detail, dual-custody operational workflows, clienteling cadence timing, and an expanded free-resources directory

## Structure

- `courses/<Cn-slug>/README.md` - course outcomes, module status
- `courses/<Cn-slug>/articles/` - published-ready long-form articles
- `courses/<Cn-slug>/production/` - per-article outline, media manifest, fact-check table, huddle card, quiz

## Catalog progress

| Course | Track | Articles | Done |
|---|---|---|---|
| C1 Diamond & Gemstone Fluency for the Sales Floor | Foundations | 10 | 10 (complete, retroactive cleanup complete) |
| C2 The Fine Jewelry Sales Conversation | Foundations | 10 | 1 |
| C3 Clienteling & CRM | Foundations | 8 | 0 |
| C4 Store Security & Loss Prevention | Foundations | 8 | 0 |
| C5 Financing, Credit & Compliance | Foundations | 6 | 0 |
| C6 Bridal & Engagement Mastery | Specialist | 10 | 0 |
| C7 Estate, Antique & Trade-In | Specialist | 10 | 0 |
| C8 Custom Design & Repair Workflow | Specialist | 8 | 0 |
| C9 Selling High-Ticket in Compressed Time | Specialist | 8 | 0 |
| C10 Luxury Consumer Psychology & Negotiation | Specialist | 8 | 0 |
| C11 Running the Store | Leadership | 10 | 0 |
| C12 Retail KPIs & Reporting | Leadership | 8 | 0 |
| C13 Hiring, Coaching & Performance Management | Leadership | 10 | 0 |
| C14 Multi-Store Leadership | Leadership | 8 | 0 |
| C15 Designing Jewelry Sales Training | Trainer | 8 | 0 |
| C16 The GIA Diamonds Deep Dive (companion to GIA's D&DG further-reading bibliography) | Advanced/Specialist | 13 | 13 |
| C17 The GIA Colored Stones Deep Dive (companion to GIA's Colored Stones further-reading bibliography) | Advanced/Specialist | 16 | 0 (Wave 1 in progress) |

**Total: 159 articles (130 original catalog + 13 in C16 + 16 in C17). C1 is fully complete; C2 is underway; C16 complete (13/13 modules, 65 production artifacts), independently built and verified per `courses/C16-gia-diamonds-deep-dive/production/VERIFICATION-REVIEW.md`. C17 complete (16/16 modules, 96 production artifacts, 160 quiz questions), independently built and verified per `courses/C17-gia-colored-stones-deep-dive/production/VERIFICATION-REVIEW.md`.**

**Note on C16:** independent study companion, not a GIA product, built from GIA's own "For Further Reading for Diamonds and Diamond Grading" bibliography (~260 *Gems & Gemology* / GIA Research citations). It adds a `references/` folder (full annotated bibliography) and a `videos/` folder (verified video index) to the standard layout. See its README for the module-to-assignment map and wave log, and `production/VERIFICATION-REVIEW.md` for the post-build fact-check review.

**Note on C17:** independent study companion, not a GIA product, built on the same model as C16 from GIA's "For Further Reading: Colored Stones" bibliography (~260 *Gems & Gemology* / GIA Research citations spanning ruby, sapphire, emerald, pearl and jade). Same repository layout (articles/ + production/ + references/annotated-bibliography.md + videos/video-library.md). See its README for the module-to-assignment map and wave log.

## Production rules (six-step SOP)

Every article is produced one at a time, with a full review/revision cycle between each, not batched:
1. **Review the draft** - 8-part structure, tone, sourcing check, VERIFY flags resolved against research.
2. **Self-critique and revise** - scored 1-5 against outcome alignment, factual discipline, floor readiness, voice, scannability, persona fit, and length; revised version with a change log.
3. **Fact-check extraction** - every checkable claim tabled with type, source, and risk; MUST VERIFY items flagged.
4. **Media handling** - real expert-produced media only (GIA, AGS, NDC, trade press, museums, credentialed channels), verified before use; no AI-generated imagery.
5. **Repurposing** - a one-page huddle card and a 10-question quiz per article (omitted only for modules that are themselves an assessment, e.g. capstones).
6. **Move to the next module** - only after the above are complete.

Word length is need-driven, not capped: articles may run well past the original 2,000-2,500 word guide, up to roughly 10,000 words, whenever the added depth genuinely helps the learner.
