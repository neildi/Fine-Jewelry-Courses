# Fine Jewelry Retail Course Architecture & Article-Generation Prompt Kit

A production blueprint for turning the research in the *Fine Jewelry Retail Career and Skills Reference* into a catalog of in-depth courses, each built from a series of long-form articles generated with Claude Sonnet 5 under human review. Part A defines personas and the course catalog with measurable outcomes. Part B is the prompt kit (system prompt, article template, QA and repurpose prompts) plus a short guide to getting better results from the model. Part C is the media sourcing and citation policy: how to find and ethically include high-quality third-party images, videos and infographics (GIA, AGS, Gem-A, museum collections, expert YouTube channels) instead of AI-generated visuals.

---

## Part A — Course Architecture

### A1. Learner personas (derived from Section 1–2 of the research)

| Persona code | Persona | Career stage (Section 5) | Typical titles (regional variants) | Primary employer types | What they need most | Success metric they are judged on |
|---|---|---|---|---|---|---|
| P1 | The New Associate | Stage 1 — Entry/IC | Sales Associate, Jewelry Consultant, Sales Executive (India/Gulf), Sales Advisor/Assistant (UK), Fine Jewelry Sales Associate (department store) | National chains, department stores, independents | Product vocabulary, a repeatable sales conversation, POS/CRM basics, security habits, financing basics | Individual sales goal, add-on/protection plan attach, client-book growth |
| P2 | The Maison Client Advisor | Stage 1–2 | Client Advisor, Brand Ambassador, Sales Professional | Luxury maisons, multi-brand luxury | Brand storytelling, HNW etiquette, appointment-based clienteling, CRM discipline | Client retention, repeat purchase, appointment conversion |
| P3 | The Cruise / Travel Retail Specialist | Stage 1–2 | Fine Jewelry Specialist, Prestige Advisor, Fine Jewellery Sales Specialist, Port Sales Associate | Cruise concessions, port-of-call operators, airport duty-free | Compressed-time selling, high-ticket closing in one visit, multi-currency/financing, security in transit | Sales per passenger/visit, average ticket, close rate within visit window |
| P4 | The Bridal Specialist | Stage 2 — Senior/Specialist | Bridal/Engagement Specialist, Luxury Bridal Manager, Diamond Sales Consultant | Bridal DTC, independents, Signet-type chains | Diamond grading depth, lab-grown vs. natural conversations, band attachment, couple dynamics, appointment follow-up | Bridal conversion, band attach rate, referral volume |
| P5 | The Estate / Pre-Owned Specialist | Stage 2 | Estate Jewelry Specialist, Jewelry Specialist (auction), Valuer (UK) | Auction houses, estate-focused independents | Period identification, hallmarks, trade-in valuation conversation, appraisal documentation, AGS vs. GIA scales | Buy/trade-in margin, consignment intake, appraisal accuracy |
| P6 | The Gemologist–Seller | Stage 2 | GIA GG on the floor, Senior Sales Specialist, Jewellery Expert | Independents, high jewelry | Translating lab knowledge into plain-language selling, treatment disclosure, custom design consultation | High-ticket close rate, custom order conversion, disclosure compliance |
| P7 | The First-Time Store Leader | Stage 3 — Management | Assistant Store Manager, Store/Boutique Manager, Showroom Manager (India), Manager Designate (UK) | All | Opening/closing SOPs, shrink control, KPI dashboards, hiring, coaching, scheduling, VM standards | Store sales vs. plan, conversion, shrink %, staff turnover |
| P8 | The Multi-Store Leader | Stage 3–4 | District Manager, Area/Regional Manager, Area Business Manager (India) | Chains, maisons, cruise fleets | Store-visit audits, comparative KPI analysis, manager coaching, compliance oversight, P&L literacy | District sales vs. plan, comp growth, manager bench strength |
| P9 | The Sales Trainer / L&D Lead | Stage 4 | Director of Sales Training, Retail Training Manager | Chains, maisons, training vendors | Curriculum design, train-the-trainer, measuring training ROI, role-play design | Ramp time of new hires, post-training KPI lift |

Personas P2, P3, P4 and P5 are "lateral" specializations of the same career stage; a learner can hold two at once (e.g., a cruise specialist who is also the bridal expert onboard).

### A2. Course catalog overview

Fifteen courses, grouped into four tracks that follow the Stage 1–4 map. Each course is delivered as a sequence of long-form articles (2,000–2,500 words each), with a capstone self-assessment. Numbers in the "Research anchor" column point to sections of the reference report and the free-resource tables (R1–R15 = Section 4 tables 1–15).

| # | Course | Track | Primary personas | Articles | Est. learner hours | Research anchor |
|---|---|---|---|---|---|---|
| C1 | Diamond & Gemstone Fluency for the Sales Floor | Foundations | P1, P2, P3 | 10 | 8–10 | R1, Section 2 Tier 1 |
| C2 | The Fine Jewelry Sales Conversation | Foundations | P1, P2, P3 | 10 | 8–10 | R2, R12, Section 2 |
| C3 | Clienteling & CRM: Building a Client Book That Compounds | Foundations | P1, P2, P3 | 8 | 6–8 | R3, Section 3.6 |
| C4 | Store Security, Loss Prevention & High-Value Transaction Protocols | Foundations | P1, P3, P7 | 8 | 6–8 | R7, R8, Section 3.1–3.3 |
| C5 | Financing, Credit & Compliance at the Counter | Foundations | P1, P4, P7 | 6 | 4–6 | R8, Section 3.4 |
| C6 | Bridal & Engagement Mastery | Specialist | P4, P1 | 10 | 8–10 | R4, Section 2 row 4 |
| C7 | Estate, Antique & Trade-In: Identification, Valuation Conversations & Appraisal Basics | Specialist | P5, P6 | 10 | 8–10 | R5, Section 2 row 5 |
| C8 | Custom Design & Repair Workflow Management | Specialist | P6, P1, P7 | 8 | 6–8 | Section 3.4–3.5 |
| C9 | Selling High-Ticket in Compressed Time: Cruise, Port & Travel Retail | Specialist | P3 | 8 | 6–8 | Section 1 (cruise dialect), Section 2 row 3 |
| C10 | Luxury Consumer Psychology & Negotiation for HNW Clients | Specialist | P2, P4, P5, P6 | 8 | 8–10 | R11, R12 |
| C11 | Running the Store: Daily, Weekly & Monthly Operating System | Leadership | P7 | 10 | 8–10 | Section 3.8, R14 |
| C12 | Retail KPIs & Reporting for Jewelry Store Leaders | Leadership | P7, P8 | 8 | 6–8 | R10, Section 2 KPI vocabulary |
| C13 | Hiring, Coaching & Performance Management in Jewelry Retail | Leadership | P7, P8 | 10 | 8–10 | R9, Section 2 Tier 3 |
| C14 | Multi-Store Leadership: Store Visits, Audits & Manager Development | Leadership | P8 | 8 | 8–10 | Section 3.7, R14 |
| C15 | Designing Jewelry Sales Training That Moves KPIs | Trainer | P9, P8 | 8 | 8–10 | R13 |

Total: 130 articles. At one article per production cycle (see Part B), the full catalog is roughly 130 drafting cycles plus review.

### A3. Course-by-course outlines with outcomes

Each course uses the same skeleton so the article-generation prompt stays stable:

- **Terminal outcomes** — what the learner can *do* at the end (observable on the floor or in the back office).
- **Module list** — each module = one article.
- **Assessment** — how the learner or their manager verifies the outcome.
- **KPI link** — the metric from Section 2 the course is expected to move.
- **Free resource pairing** — the Section 4 resources to assign as pre-reading or follow-up.

#### C1 — Diamond & Gemstone Fluency for the Sales Floor

Terminal outcomes. The learner can: explain the 4Cs in plain language and connect each to visible differences in the case; read a GIA or AGS report line-by-line with a client; disclose treatments, lab-grown origin and simulants correctly; identify the ten most-sold colored stones and their care requirements; explain precious-metal marks, purity and alloys; and answer the fifteen most common product questions without a manager.

| Module | Article title | Working outcome |
|---|---|---|
| 1 | Carat, Cut, Color, Clarity — What the Client Actually Sees | Demonstrate each C with two stones from the case |
| 2 | Reading a GIA Report With a Client (and What Not to Say) | Walk a client through a report in under 3 minutes |
| 3 | AGS 0–10 vs. GIA Nomenclature: Translating Between Scales | Convert grades in a trade-in conversation |
| 4 | Lab-Grown, Natural, Simulant: The Disclosure Conversation | Deliver a compliant, non-defensive disclosure |
| 5 | Fluorescence, Inclusions and "Is This a Flaw?" | Reframe technical features as value |
| 6 | The Colored Stone Top 10: Sapphire to Tanzanite | Give species, treatment norms and care for each |
| 7 | Pearls: Types, Grading Vocabulary and Care | Sell a pearl strand with confidence |
| 8 | Metals, Marks and Alloys | Explain 14k vs. 18k vs. platinum trade-offs |
| 9 | Treatment and Origin Questions: What You Must Disclose | Apply FTC-style disclosure rules in dialogue |
| 10 | Product-Knowledge Drills: A 30-Day Self-Test | Complete and score the drill set |

Assessment: 40-question self-test plus a manager-observed "explain this stone" demonstration. KPI link: close rate on diamond inquiries; protection-plan attach. Resource pairing: GIA 4Cs site, GIA Retailer Support Program modules, NDC Diamond Learning Center, GIA Gem Encyclopedia, AGS Quick-Glance PDF.

#### C2 — The Fine Jewelry Sales Conversation

Terminal outcomes. The learner can: open without "Can I help you?"; run a discovery sequence that surfaces occasion, recipient, budget range and style; present using feature–benefit–emotion; handle the eight most common objections (price, "just looking," "I'll think about it," online comparison, lab-grown, financing hesitation, partner approval, competitor quote); ask for the sale three different ways; and add on ethically.

| Module | Article title |
|---|---|
| 1 | The First 90 Seconds: Openers That Start Conversations |
| 2 | Discovery: The Questions That Reveal the Real Purchase |
| 3 | Presenting a Piece: Feature, Benefit, Emotion, Story |
| 4 | Buying Signals and When to Stop Talking |
| 5 | Price Objections Without Discounting |
| 6 | "I'll Think About It" and the Follow-Up That Wins |
| 7 | Online Comparison and the Showrooming Client |
| 8 | Add-Ons, Protection Plans and Care Products Done Ethically |
| 9 | Three Ways to Ask for the Sale |
| 10 | Role-Play Scripts and a Weekly Practice Cadence |

Assessment: recorded or observed role-play scored against a rubric; objection-response flash cards. KPI link: conversion rate, average ticket, UPT. Resource pairing: HubSpot Inbound Sales Certification, INSTORE "100 Things," Jewelers Playbook YouTube, Shane Decker articles.

#### C3 — Clienteling & CRM: Building a Client Book That Compounds

Terminal outcomes. The learner can: capture client data at point of sale without friction; run the 2-2-2 follow-up cadence (2 days / 2 weeks / 2 months); segment a client book into VIP tiers; write occasion-based outreach that gets replies; log every interaction in the CRM; and report weekly client-book growth.

Modules: (1) Why a Client Book Is Your Career Asset; (2) Data Capture That Feels Like Service; (3) The 2-2-2 Cadence Explained; (4) Occasion Calendars: Anniversaries, Birthdays, Upgrades; (5) Writing Outreach That Gets Replies (Text, Email, Handwritten); (6) VIP Tiering and Time Allocation; (7) CRM Hygiene: Notes, Tags, Tasks; (8) Measuring Retention and Repeat Business.

Assessment: 30-day client-book audit (capture rate, follow-up completion). KPI link: repeat-client %, appointment volume. Resource pairing: Endear clienteling guide and mini-course, Salesforce Trailhead CRM trail, Endear benchmarks report.

#### C4 — Store Security, Loss Prevention & High-Value Transaction Protocols

Terminal outcomes. The learner can: execute two-person opening/closing and all-clear signals; follow one-piece-out and case-key discipline; recognize distraction-theft and grab-and-run patterns; run the Form 8300 workflow for cash over the threshold; verify cards, checks and wires against fraud red flags; and respond correctly during and after an incident.

Modules: (1) Why Jewelry Is Targeted — The Threat Landscape; (2) Opening and Closing: The Two-Person Rule; (3) Showing High-Value Goods: Floor Discipline; (4) Distraction Theft, Switches and Grab-and-Run; (5) Cash Over the Threshold: Form 8300 Step by Step; (6) Cards, Checks, Wires and Remote-Order Fraud; (7) Cycle Counts, Case Counts and Shrink; (8) During and After an Incident.

Assessment: Jewelers Mutual Safety & Security Academy completion plus a store SOP walk-through. KPI link: shrink %, incident rate. Resource pairing: Jewelers Mutual Academy (16 courses), Partner for Protection hub, Loss Prevention Media reports, JSA crime report.

#### C5 — Financing, Credit & Compliance at the Counter

Terminal outcomes. The learner can: explain deferred-interest promotional financing accurately; present financing as a service, not a rescue; know what may and may not be said about approvals and terms; understand installment contracts and BNPL basics; and apply FTC-style representation rules to product claims.

Modules: (1) How Retail Financing Actually Works; (2) Presenting Financing Early and Ethically; (3) Deferred Interest, Promo Periods and Plain-Language Explanations; (4) What You Cannot Promise: Approvals, Terms, Credit Scores; (5) Layaway, Installments and BNPL; (6) FTC Guides and Product Representation for Sellers.

Assessment: scenario quiz on permitted statements. KPI link: financing attach rate, average ticket. Resource pairing: Synchrony Retail Orientation PDF, Synchrony "How financing works," CFPB installment and BNPL pages, JVC Essential Guides and FTC guide.

#### C6 — Bridal & Engagement Mastery

Terminal outcomes. The learner can: run a bridal appointment from research-stage inquiry to purchase; guide a couple through shape, setting and metal choices; present natural vs. lab-grown without bias; attach wedding bands and future upgrades; manage two-decision-maker dynamics; and convert online researchers into in-store appointments.

Modules: (1) The Modern Bridal Buyer's Journey; (2) Booking and Preparing the Appointment; (3) Shape, Setting, Metal: Guiding Without Overwhelming; (4) Natural vs. Lab-Grown: The Balanced Conversation; (5) Budget Conversations That Keep the Romance; (6) Band Attachment and the Upgrade Path; (7) Two Buyers, One Ring: Couple Dynamics; (8) Sizing, Timelines, Custom and Resizing Realities; (9) Post-Purchase: Proposal Follow-Up and Referral Asks; (10) Bridal Metrics: Tracking Your Own Conversion.

Assessment: appointment role-play plus a personal bridal conversion log. KPI link: bridal conversion, band attach, referrals. Resource pairing: JCK bridal articles, GIA engagement-ring content, NDC Train-the-Trainer guides.

#### C7 — Estate, Antique & Trade-In

Terminal outcomes. The learner can: identify major period styles (Georgian through Retro) and construction cues; read hallmarks and maker's marks; run a trade-in valuation conversation that protects margin and trust; know what a compliant appraisal report contains and when to refer out; and price pre-owned confidently.

Modules: (1) Why Estate Is a Growth Category; (2) Period Styles at a Glance; (3) Hallmarks, Maker's Marks and Where to Look; (4) Construction Cues, Repairs and Alterations; (5) The Trade-In Conversation: Managing Expectations; (6) Melt vs. Resale vs. Consignment Pricing Logic; (7) What an Appraisal Is (and Isn't); (8) Appraisal Report Anatomy and Credentialing Bodies; (9) Disclosure and Documentation for Pre-Owned; (10) Building an Estate Buying Program.

Assessment: identification quiz with photos; mock trade-in role-play. KPI link: trade-in margin, estate sales mix. Resource pairing: Lang Antiques university, ASA checklist and accreditation PDFs, JVC appraisal page, AGS Quick-Glance, Rapaport history article.

#### C8 — Custom Design & Repair Workflow Management

Terminal outcomes. The learner can: run a custom discovery consultation and capture it in CRM; explain CAD, approval gates and production timelines; take in a repair using a standardized envelope/form; set and communicate realistic estimates; coordinate bench handoffs; and keep clients updated on a fixed cadence.

Modules: (1) Custom as a Trust Product; (2) The Discovery Consultation; (3) CAD, Renders and the Approval Gate; (4) Timelines, Deposits and Change Orders; (5) Repair Intake: The Form Is the Legal Record; (6) Estimates, Bench Handoff and Refinement; (7) Communication Cadence During Production; (8) Presentation, Pickup and the Follow-Up Sale.

Assessment: complete a mock intake and custom order file. KPI link: custom conversion, repair-to-sale rate. Resource pairing: Section 3.4–3.5 workflows; Stuller intake sequence referenced there.

#### C9 — Selling High-Ticket in Compressed Time: Cruise, Port & Travel Retail

Terminal outcomes. The learner can: build trust in minutes with a first-time visitor; structure a one-visit close; handle duty-free, tax and shipping questions; present multi-currency and financing options; manage inventory security in a port or onboard environment; and follow up with a client who lives thousands of miles away.

Modules: (1) The Travel Retail Buyer's Mindset; (2) Trust in Ten Minutes; (3) The One-Visit Close Structure; (4) Duty-Free, Tax, Shipping and Guarantees; (5) Currency, Financing and Payment Options; (6) Security in Port and Onboard Environments; (7) Cross-Border Clienteling and Remote Repeat Sales; (8) Metrics That Matter in Travel Retail.

Assessment: timed role-play. KPI link: sales per visit, average ticket. Resource pairing: Section 1 cruise dialect; C2, C3, C4 modules as prerequisites.

#### C10 — Luxury Consumer Psychology & Negotiation for HNW Clients

Terminal outcomes. The learner can: explain status-signalling and self-expression motives in luxury purchases; recognize which motive is driving a given client; use tactical empathy (labeling, mirroring) in price and trade-in conversations; prepare a negotiation with BATNA thinking; and preserve margin without damaging the relationship.

Modules: (1) Why People Buy Luxury: The Research; (2) Reading the Motive in the Room; (3) Scarcity, Provenance and Story as Value; (4) Tactical Empathy on the Sales Floor; (5) Preparing a Negotiation: Anchors and Alternatives; (6) Trade-In and Price Negotiations That Hold Margin; (7) Recovering From a Stalled Deal; (8) Long-Game Relationship Economics.

Assessment: negotiation role-play scored on margin retained and relationship signals. KPI link: discount rate, average ticket. Resource pairing: INSEAD luxury psychology PDF, Coursera Successful Negotiation (audit), Chris Voss videos, Bocconi luxury management course.

#### C11 — Running the Store: Daily, Weekly & Monthly Operating System

Terminal outcomes. The manager can: run the daily open/huddle/close sequence; execute weekly cycle counts and case audits; run the monthly reporting and planning cycle; maintain VM standards; manage scheduling to traffic; and document every recurring workflow as an SOP.

Modules: (1) The Store as an Operating System; (2) The Daily Rhythm: Open, Huddle, Floor, Close; (3) Weekly: Counts, Coaching, Client-Book Review; (4) Monthly: Reporting, Planning, Inventory Reconciliation; (5) Visual Merchandising Standards and Case Zoning; (6) Scheduling to Traffic and Peak Coverage; (7) Vendor, Repair and Custom Pipeline Management; (8) Writing SOPs Your Team Will Actually Use; (9) Compliance Calendar: Insurance, Records, Filings; (10) The Manager's Own Weekly Scorecard.

Assessment: produce the store's SOP binder and 30-day calendar. KPI link: sales vs. plan, shrink, VM audit score. Resource pairing: Alison Diploma in Retail Management, GoAudits checklists, Alison Visual Merchandising, GIA Retailer display assets.

#### C12 — Retail KPIs & Reporting for Jewelry Store Leaders

Terminal outcomes. The manager can: define and calculate conversion, ATV, UPT, sales per hour, sell-through, GMROI, shrink and retention; build a weekly dashboard; diagnose a sales miss by KPI; set individual targets from store targets; and present results upward.

Modules: (1) The KPI Vocabulary of Jewelry Retail; (2) Conversion and Traffic: Measuring What You Can't See; (3) Average Ticket, UPT and Mix; (4) Inventory KPIs: Sell-Through, Turn, GMROI; (5) Retention and Client-Book KPIs; (6) Building the Weekly Dashboard; (7) Diagnosing a Miss; (8) Reporting Up: The One-Page Store Review.

Assessment: build and populate a dashboard from sample data. KPI link: all. Resource pairing: Shopify Retail Metrics guide, Retail Ops Toolkit KPI dashboard and scorecards, Endear benchmarks.

#### C13 — Hiring, Coaching & Performance Management in Jewelry Retail

Terminal outcomes. The manager can: write a role profile and interview guide; run structured interviews; onboard a new associate in 30 days; coach using observation and role-play; run performance reviews with documented evidence; and manage underperformance within policy.

Modules: (1) What Great Jewelry Sellers Have in Common; (2) Role Profiles and Sourcing; (3) Structured Interviews and Auditions; (4) The 30-Day Onboarding Plan; (5) Floor Coaching: Observe, Debrief, Practice; (6) Weekly One-on-Ones; (7) Performance Reviews With Evidence; (8) Managing Underperformance; (9) Recognition, Incentives and Commission Fairness; (10) Building Bench Strength for Your Own Promotion.

Assessment: interview guide, onboarding plan and a recorded coaching debrief. KPI link: ramp time, turnover, per-associate productivity. Resource pairing: NHPA Hiring Toolkit and Train the Trainer, HubSpot Sales Management Certification, Alison Performance Management, OpenLearn Managing People.

#### C14 — Multi-Store Leadership: Store Visits, Audits & Manager Development

Terminal outcomes. The district leader can: run a structured store visit; compare stores on normalized KPIs; coach managers rather than associates; enforce compliance across sites; and build a district talent pipeline.

Modules: (1) From Running a Store to Running Managers; (2) The Store Visit: Agenda, Audit, Debrief; (3) Comparative KPI Analysis Across Stores; (4) Coaching Managers on Coaching; (5) Compliance and Risk Oversight at Scale; (6) District Communication Cadence; (7) Talent Pipeline and Succession; (8) Presenting District Results to Executives.

Assessment: store-visit report and district scorecard. KPI link: district comp growth, manager retention. Resource pairing: GoAudits retail audit library, OpenLearn Leadership and Followership, Retail Ops Toolkit chain scorecards.

#### C15 — Designing Jewelry Sales Training That Moves KPIs

Terminal outcomes. The trainer can: write behavioral learning outcomes; design a module with practice built in; run train-the-trainer sessions for store managers; build role-play libraries; measure training with pre/post KPI comparison; and maintain a curriculum roadmap by career stage.

Modules: (1) Outcomes Before Content; (2) Designing for the Sales Floor, Not the Classroom; (3) Role-Play Libraries and Scenario Banks; (4) Train the Trainer for Store Managers; (5) Microlearning and Huddle Content; (6) Measuring Training: Pre/Post KPI Design; (7) Curriculum Roadmaps by Career Stage; (8) Keeping Content Current With the Trade Press.

Assessment: a complete module design with measurement plan. KPI link: new-hire ramp, post-training KPI lift. Resource pairing: NHPA Path to Success and Trainer's Toolbox, ATD Workshop Series and webinars, HubSpot Sales Management.

### A4. Persona-to-course learning paths

| Persona | Required courses (in order) | Elective |
|---|---|---|
| P1 New Associate | C1 → C2 → C4 → C3 → C5 | C6 |
| P2 Maison Client Advisor | C1 → C2 → C3 → C10 | C7 |
| P3 Cruise/Travel Specialist | C1 → C2 → C4 → C9 → C5 | C3, C10 |
| P4 Bridal Specialist | C1 → C2 → C6 → C5 → C10 | C8 |
| P5 Estate Specialist | C1 → C7 → C10 → C5 | C8 |
| P6 Gemologist–Seller | C2 → C8 → C10 → C7 | C6 |
| P7 First-Time Store Leader | C11 → C12 → C13 → C4 | C5 |
| P8 Multi-Store Leader | C12 → C14 → C13 → C10 | C15 |
| P9 Sales Trainer | C15 → C13 → C2 → C12 | any |

---

## Part B — Article-Generation Prompt Kit for Claude Sonnet 5

### B1. How to get better results (read this first)

1. **Give the model the evidence, not the topic.** Paste the relevant rows from the research files (job-posting quotes, KPI definitions, workflow steps) into the prompt. Sonnet writes far better from supplied facts than from its own recall, and it will stop inventing statistics.
2. **Separate the stable from the variable.** Put brand voice, format rules and prohibitions in a system prompt you reuse. Put course, module, persona and evidence in the user message. This keeps quality consistent across 130 articles.
3. **Use labeled sections (XML-style tags).** Tags like `<evidence>`, `<persona>`, `<format>` make it unambiguous what is instruction vs. source material and reduce the model blending the two.
4. **Run a chain, not a single shot.** Outline → draft → self-critique → revision produces markedly better long-form work than one prompt. Each step below is a separate turn.
5. **Demand a structured skeleton, then prose.** Ask for the section headings and the one-sentence purpose of each section first; approve; then ask for the full draft. Fixing an outline costs seconds, fixing a draft costs minutes.
6. **Show one exemplar.** Include one finished article (or a 300-word excerpt) that represents the target voice. One good example beats three paragraphs of style description.
7. **Name the prohibitions explicitly.** "No invented statistics, no named competitors' internal data, no legal or financial advice framed as certain, no filler transitions, no emoji, no exclamation points." Models comply well with negative constraints when they are concrete.
8. **Ask for a confidence flag.** Require the model to mark any claim it is not certain of with `[VERIFY]` so a human reviewer knows where to look. This is the single highest-value quality control for factual content.
9. **Keep temperature-equivalent settings default; vary the input instead.** If drafts feel same-y across articles, change the scenario hook, the persona's specific situation and the evidence — not the sampling settings.
10. **Human-in-the-loop checkpoints.** Review at outline, after draft, after QA pass. Never publish straight from generation.

### B2. Master system prompt (reuse for every article)

```
You are a senior instructional writer for a fine jewelry retail sales training platform. You write long-form training articles for people who work on the sales floor, run stores, or lead districts in fine jewelry retail (luxury maisons, national chains, department-store counters, cruise and travel retail, e-commerce brands, auction houses, independents).

VOICE
- Friendly, authoritative, practical. Write like an experienced trainer talking to a capable colleague.
- Floor-ready: every concept ends in something the reader can say or do this week.
- Scannable: short paragraphs (2–5 sentences), descriptive H2/H3 headings, tables for comparisons, numbered steps for procedures, bullet lists for checklists.
- Use example dialogues in the form  Client: ... / Associate: ...  when teaching conversation skills.
- No exclamation points. No emoji. No italics for emphasis. No marketing hype. No academic jargon without a plain-language gloss.

FACTUAL DISCIPLINE
- Use only the facts supplied in <evidence>. Do not add statistics, survey results, percentages, prices, legal thresholds or named-company practices that are not in <evidence>.
- Where general industry practice is described without a source, phrase it as common practice ("many stores...", "a typical approach...") rather than as fact.
- Mark any statement you are not certain is accurate with [VERIFY] immediately after it.
- Never give legal, tax, credit or appraisal advice as certain; frame these as "check your store policy and local regulations."
- Do not mention any real employee, client or specific store by name unless it appears in <evidence>.

STRUCTURE (unless <format> overrides)
1. Title (H1)
2. Scenario hook (150–250 words): a realistic sales-floor or back-office situation the persona recognizes
3. Why this matters (link to the KPI or risk named in <persona>)
4. Core content (3–6 H2 sections; the technical or procedural breakdown)
5. On the floor: applying it this week (scripts, steps, checklists)
6. Objections, mistakes and edge cases
7. Self-check (5–8 questions or a short checklist)
8. Go deeper (list the free resources supplied in <resources>, with a one-line note on what each is for)

MEDIA
- Do not describe or invent images, videos or infographics. Do not generate URLs for media from memory.
- Use only the media items supplied in <media>. Insert each at the most instructive point in the article using this exact block:

  > **[MEDIA: {type} | {id}]**
  > **Watch/View:** {title} — {creator/organization}
  > **Why here:** {one sentence on what the learner should look for}
  > **Source:** {URL}
  > **Use:** {embed | link-out | licensed-download}

- If a section would clearly benefit from a visual that is not in <media>, insert the placeholder  [MEDIA REQUEST: {what is needed, e.g. "macro video of jardin inclusions in Colombian emerald"}]  so the media researcher can source it. Never fill the gap with a description of an imaginary image.
- Every media block must be followed by one sentence of the article's own words explaining what the learner should notice. Media supports the text; it does not replace it.

LENGTH: 2,000–2,500 words unless <format> says otherwise.
OUTPUT: Markdown only. No preamble, no closing remarks about the article itself.
```

### B3. Step 1 — Outline prompt

```
Create an outline for one training article.

<course>C{n} — {course title}</course>
<module>Module {m} — {article title}</module>
<persona>
Persona: {P-code and name}
Career stage: {stage}
Typical titles: {titles}
Employer type: {employer type}
KPI this article should move: {KPI}
What they already know: {prerequisites}
</persona>
<terminal_outcome>
By the end of this article the reader can: {one observable behavior}
</terminal_outcome>
<evidence>
{Paste relevant rows/quotes from the research files here — job posting language, workflow steps, KPI definitions, regional notes. Include source URLs.}
</evidence>
<resources>
{Paste the 2–4 free resources to feature, with URLs and time estimates}
</resources>

Return:
1. A working title and two alternates.
2. The scenario hook in one sentence (who, where, what goes wrong or what is at stake).
3. Section-by-section outline: for each H2, give the heading and one sentence stating what the reader will be able to do after that section.
4. A list of every fact from <evidence> you plan to use, and where.
5. Any gaps: information you would need to write this well that is not in <evidence>.
```

### B3a. Step 1b — Media request list (run right after the outline)

```
Using the approved outline, list the visual or video support each section needs to teach its outcome. For each item give:
- Section it belongs to
- Media type (still image / macro photo / diagram or infographic / short video under 5 min / long video / interactive tool)
- Exactly what it must show (e.g. "side-by-side of VS1 vs SI1 clarity at 10x", "jardin inclusions in a Colombian emerald under magnification", "GIA cut grade proportions diagram")
- Preferred authoritative sources to search first (see Part C tier list)
- Whether a text-only fallback is acceptable if nothing suitable is found

Limit to the 3–6 items that most change comprehension. Do not propose decorative imagery.
```

The output of this step goes to the media researcher (a person, or a search-enabled tool such as Perplexity or Claude with web search). See Part C for the research prompt and verification rules. The verified result becomes the `<media>` block in Step 2.

### B4. Step 2 — Draft prompt (after approving the outline)

```
Write the full article from the approved outline below. Follow the system prompt for voice, structure, factual discipline, media handling and length.

<approved_outline>
{paste outline, with your edits}
</approved_outline>
<evidence>
{same evidence block}
</evidence>
<resources>
{same resources block}
</resources>
<media>
{paste the verified media manifest from Part C — one entry per item with id, type, title, creator, URL, license/use status, and the section it belongs to}
</media>
<exemplar>
{300–500 words from a finished article in the target voice}
</exemplar>

Additional instructions for this article:
- Include at least {2} example dialogues.
- Include one table comparing {x}.
- Address the regional variation for {US / UK / India-Gulf / cruise} where relevant, in one short callout.
- Mark uncertain claims with [VERIFY].
```

### B5. Step 3 — Self-critique and revision prompt

```
Review the draft below against the system prompt and the rubric. Then produce a revised version.

<draft>
{paste draft}
</draft>

RUBRIC — score each 1–5 and give one sentence of justification:
1. Outcome alignment: does every section serve the terminal outcome?
2. Factual discipline: any statistic, price, threshold or practice not traceable to <evidence>? List each.
3. Floor readiness: can the reader do something specific this week from each H2?
4. Voice: any hype, filler transitions, exclamation points, emoji, italics, jargon without gloss?
5. Scannability: paragraph length, heading quality, use of tables and steps.
6. Persona fit: does the scenario and language match the persona's actual job and employer type?
7. Length within 2,000–2,500 words?
8. Media discipline: is every media block taken verbatim from <media>? Any invented URL, described-but-unsourced image, or media used without the required attribution block? Is each media item placed where it teaches, with a sentence telling the learner what to notice?

Then output the revised article in full, with a short change log (bullets) at the top listing what you changed and why. Keep all [VERIFY] flags in place for the human reviewer.
```

### B6. Step 4 — Fact-check extraction prompt (for the human reviewer)

```
From the article below, extract every checkable claim into a table with columns: Claim | Type (statistic / legal-regulatory / product-technical / company practice / procedure) | Source in <evidence> (URL or "none") | Risk if wrong (low / medium / high).

Flag any claim with source "none" and risk medium or high as MUST VERIFY.

<article>
{paste article}
</article>
```

### B7. Repurposing prompts

**Huddle card (5-minute team briefing):**
```
Condense the article below into a one-page huddle card for a store manager to read aloud in a 5-minute morning huddle: 1 headline, 3 key points, 1 script to practice today, 1 question to ask the team. Plain text, under 200 words.
```

**Self-assessment quiz:**
```
Write 10 multiple-choice questions (4 options each, one correct) testing the terminal outcome of the article below. Mix recall, application and scenario questions. Provide an answer key with a one-sentence explanation per item. Do not test trivia; test what changes behavior on the floor.
```

**Manager's coaching guide:**
```
Write a 400-word coaching guide for a store manager using this article with an associate: what to observe on the floor, three debrief questions, one role-play scenario with a scoring rubric (3 criteria, 1–3 scale).
```

**Course landing-page copy:**
```
Using the course outline below, write landing-page copy: a 40-word summary, 6 outcome bullets starting with a verb, a "who this is for" paragraph naming the persona's typical titles, and a "what you will need" line (time, prerequisites). No hype language.
```

### B8. Production checklist per article

1. Select course, module, persona from Part A.
2. Assemble the `<evidence>` block from the four research files (copy rows verbatim with URLs).
3. Assemble `<resources>` from the free-resource tables.
4. Run B3 (outline). Human review: approve or edit.
5. Run B3a (media request list).
6. Run the Part C media research prompt (C4) in a search-enabled tool; a human opens every URL and completes the verification checklist (C5). Produce the `<media>` manifest.
7. Run B4 (draft) with exemplar and `<media>`.
8. Run B5 (critique and revise).
9. Run B6 (fact-check table). Human resolves every MUST VERIFY.
10. Resolve any `[MEDIA REQUEST]` placeholders (source it or delete it — never leave a placeholder in a published article).
11. Remove `[VERIFY]` flags once resolved.
12. Run B7 repurposing prompts as needed.
13. Log article, persona, KPI link, media manifest and publication date in the course tracker.

---

## Part C — Media Sourcing & Citation Policy

AI-generated images and video are a poor fit for gemological and product training: they cannot accurately render inclusions, cut proportions, hallmarks or treatment evidence, and a learner who trusts a fabricated "emerald" image learns the wrong thing. The policy below replaces generated visuals with real, expert-produced media, sourced and credited in a way that respects the creators.

### C1. Principles

1. **Real over generated.** Every visual in a course must be a real photograph, diagram, or video produced by a credible gemological, trade, museum or expert source. No AI-generated stones, jewelry, people or "infographics."
2. **Link or embed; do not copy.** The default way to include third-party media is an official embed (YouTube, Instagram) or a link-out to the source page, so the creator keeps control, analytics and any revenue. Downloading and re-hosting a file is permitted only when the license explicitly allows it (see C3).
3. **Attribute every time, in the same format.** The MEDIA block in the system prompt is the single attribution format. Creator or organization, title, URL and use type are mandatory.
4. **Do not rely on "fair use" or "educational use" as a blanket permission.** A commercial training platform is not a classroom. Treat fair-use arguments as a last resort to be reviewed by counsel, not a default. (This policy is operational guidance, not legal advice.)
5. **Never alter the creator's work.** No cropping out watermarks, no removing logos, no re-captioning that changes meaning, no downloading a YouTube video to re-upload.
6. **Discovery platforms are not sources.** Pinterest, Google Images and most Instagram reposts are aggregators. Use them to find media, then trace to the original creator and cite that.
7. **Media must teach, not decorate.** Each item is placed where it changes comprehension and is followed by a sentence telling the learner what to notice.
8. **A human opens every URL before publication.** Language models, including search-enabled ones, produce plausible but dead or wrong links. No media URL goes live unverified.

### C2. Source-quality tiers (search in this order)

| Tier | Source type | Examples (verify each URL at time of use) | Typical use type | Notes |
|---|---|---|---|---|
| **1 — Authoritative, explicitly licensed for retailer use** | Gem labs and industry bodies that publish assets *for* retailers | [GIA Retailer Support Program](https://retailer.gia.edu/) (downloadable 4Cs videos, images, interactive scales, brochures); [NDC free downloadable trade assets](https://www.naturaldiamonds.com/trade/free-downloadable-assets-4cs/); [NDC Diamond Learning Center](https://www.naturaldiamonds.com/trade/) videos | licensed-download or embed | Best possible source: made for exactly this purpose. Read the program terms; some assets are for in-store use only, so confirm online-training use is covered. |
| **2 — Authoritative reference, link or embed only** | Gem labs, gemmological associations, appraisal bodies, trade compliance bodies | [GIA 4Cs](https://4cs.gia.edu/en-us/) articles and interactive scales; [GIA Gem Encyclopedia](https://www.gia.edu/gem-encyclopedia) (species photos, video); [GIA Knowledge Sessions YouTube playlist](https://www.youtube.com/playlist?list=PLWlzLnp9A9J0dF3TjLYqpqQ3hAZ0pNC9s); AGS grading standards ([Quick-Glance PDF](https://cdn.ymaws.com/members.americangemsociety.org/resource/collection/2D290953-2F77-40D0-B4B0-B42F5A66F6A5/AGS-Diamond-Grading-Standards-Quick-Glance-160.pdf)); [Gem-A Gem Hub](https://gem-a.com/resources/gem-hub/); official GIA, Gem-A and AGS YouTube channels | link-out or YouTube embed | Do not download and re-host their images; embed the video or link to the encyclopedia page with a caption describing what to look at. |
| **3 — Open-license and public-domain collections** | Museum open-access programs and Creative Commons repositories | Smithsonian Open Access (National Gem Collection), The Met Open Access, Wikimedia Commons (check the license on each file page), Cooper Hewitt open access | licensed-download (with license stated) | Excellent for historical/estate jewelry (C7), famous stones, period styles. Record the exact license (CC0, CC BY, CC BY-SA) and the required attribution string. |
| **4 — Expert practitioner channels (YouTube)** | Gemologists, bench jewelers, appraisers, sales trainers with a demonstrable track record | Channels of credentialed gemologists demonstrating inclusions, treatments and cut under magnification; bench jewelers showing repair and custom processes; sales trainers such as [The Jewelers Playbook](https://www.youtube.com/@jewelersplaybook) | YouTube embed only | Verify the creator's credentials (GG, FGA, bench experience) in their channel "About" or website. Prefer videos with visible magnification, stated stone identity and no product sales pitch. Embedding must be enabled on the video. |
| **5 — Trade press** | Free-to-read industry publications | [JCK](https://www.jckonline.com/), National Jeweler, INSTORE, Rapaport articles with photos or infographics | link-out | Cite the article; do not lift the image. Useful for market and merchandising visuals. |
| **6 — Social discovery (Instagram, Pinterest)** | Individual creators, brands, labs posting on social | Instagram accounts of gem labs, mines, cutters, dealers, museums | Instagram official embed (never a screenshot); Pinterest = discovery only | Instagram embeds keep the creator's control and attribution intact and disappear if the post is deleted, which is the ethically correct behavior. Trace Pinterest pins to the original creator before citing. Brand content from maisons is typically not licensed for third-party training; link-out only. |

Excluded: stock-photo sites without a confirmed license, image-search thumbnails, reposted "gem facts" infographics with no traceable author, and any AI-generated visual regardless of source.

### C3. Use types and what each requires

| Use type | When allowed | Required in the MEDIA block | Required in the platform |
|---|---|---|---|
| **embed** | YouTube video with embedding enabled; Instagram post via official embed code | Creator, title, URL, "embed" | Use the platform's official embed code; never download and re-upload |
| **link-out** | Any credible page (GIA encyclopedia, AGS PDF, trade article) | Creator/org, page title, URL, "link-out" | Open in new tab; add a caption in the article's own words describing what the learner should look for |
| **licensed-download** | Only when the license or program terms explicitly permit re-hosting for this use: GIA Retailer Support assets (confirm scope), NDC free trade assets, CC0/CC BY/CC BY-SA museum files | Creator/org, title, URL of the source page, license name, attribution string exactly as the license requires, "licensed-download" | Keep a copy of the license text or program terms in the course asset folder; do not crop credits or watermarks; CC BY-SA content must carry the same license notice |
| **permission-obtained** | Creator has granted written permission for a specific image or video | As licensed-download, plus "used with permission" and the date | File the permission email with the asset |

If none of the four use types applies, the item is not used. Replace it with a text explanation and a `[MEDIA REQUEST]` for the researcher to find an alternative.

### C4. Media research prompt (run in a search-enabled tool)

This step requires web access. Run it in Perplexity, in Claude with web search enabled, or hand the request list to a human researcher. Claude Sonnet 5 without web access must not be asked to "find" media; it will invent URLs.

```
You are a media researcher for a fine jewelry retail training platform. Find real, high-quality, expert-produced media for the items in <media_requests>. No AI-generated imagery. Follow the source tiers in order: (1) GIA Retailer Support Program and Natural Diamond Council trade assets, (2) GIA / AGS / Gem-A reference pages and official YouTube channels, (3) museum open-access collections (Smithsonian, The Met) and Wikimedia Commons with a stated license, (4) YouTube channels of credentialed gemologists or bench jewelers, (5) trade press (JCK, National Jeweler, INSTORE, Rapaport), (6) Instagram posts from labs, cutters or museums via official embed. Pinterest is for discovery only — trace to the original creator.

<media_requests>
{paste the Step 1b list}
</media_requests>

For each request return up to 3 candidates, best first, as a table with columns:
Request | Candidate title | Creator / organization | Creator credentials or authority (one line) | Direct URL | Media type | Duration or dimensions | Exactly what it shows | Tier | Proposed use type (embed / link-out / licensed-download) | License or terms found (quote or "not stated") | Embedding enabled? (for video) | Date published | Concerns

Rules:
- Only return URLs you actually opened and confirmed show the described content. If you could not open a page, do not list it.
- Quote the license or terms text you found; do not paraphrase it as permissive.
- Prefer content that names the stone, magnification and treatment status on screen or in the description.
- Reject anything with a sales pitch as the main content, anything with no identifiable creator, and anything that appears to be a repost.
- If nothing meets the bar, say so for that request and suggest a text-only fallback.
```

### C5. Human verification checklist (before an item enters `<media>`)

- [ ] Opened the URL; it loads and shows what the researcher described.
- [ ] Creator identified and credible for this subject (lab, association, museum, credentialed gemologist, established bench jeweler, recognized trainer).
- [ ] Content is accurate: stone identity, grade or treatment shown matches the article's claim (spot-check against GIA/AGS references).
- [ ] Use type is legitimate: embedding is enabled (video), or the license/terms explicitly permit re-hosting (download), or it is a link-out.
- [ ] For downloads: license text or program terms saved to the asset folder; attribution string recorded exactly.
- [ ] No watermark, credit or logo will be removed or cropped.
- [ ] Not a maison's or brand's marketing asset being repurposed without permission.
- [ ] No AI-generated content (check descriptions, creator disclosures, and obvious render artifacts).
- [ ] Date noted; standards-based content (GIA/AGS grading) may be older and still valid; market or pricing visuals should be within 24 months.
- [ ] Added to the `<media>` manifest with a stable id (e.g. `C1-M04-V2`) and the section it belongs to.

### C6. `<media>` manifest format (paste into Step 2)

```
<media>
id: C1-M04-V1
section: "Lab-Grown, Natural, Simulant" (H2 #2)
type: video
title: {exact video title}
creator: {channel or organization} — {credential, e.g. GIA GG}
url: {URL, human-verified on YYYY-MM-DD}
use: embed
license: YouTube standard license; embedding enabled
shows: {one sentence}
learner_should_notice: {one sentence the article can build on}

id: C1-M04-I1
section: "Carat, Cut, Color, Clarity" (H2 #1)
type: diagram
title: {asset name}
creator: Gemological Institute of America — Retailer Support Program
url: https://retailer.gia.edu/
use: licensed-download
license: {quote the program terms line that permits this use; date checked}
attribution: "Image courtesy of GIA" (or the exact string the terms require)
shows: {one sentence}
learner_should_notice: {one sentence}
</media>
```

### C7. Citation style for media inside articles

Media attribution uses the MEDIA block (system prompt) at the point of use. In addition, each article ends its "Go deeper" section with a **Media credits** list, one line per item, in this form:

`{Type}: "{Title}" by {Creator/Organization}, {URL}. {License or "Embedded via YouTube" / "Linked with permission of the publisher's terms"}.`

Text sources continue to be cited inline as markdown links, as in the research report. No separate bibliography is needed for text; the media credits list exists because embedded and downloaded media carry license obligations that inline links do not.

### C8. Priority media requests by course (starting list for the researcher)

| Course | High-value visuals to source first | Best tier to start |
|---|---|---|
| C1 Diamond & Gemstone Fluency | 4Cs interactive scales; clarity grade comparison at 10x; cut proportion diagram; fluorescence under UV; natural vs. lab-grown identification features; inclusion types in emerald (jardin), sapphire (silk), ruby; pearl surface and luster comparison | Tier 1 (GIA RSP, NDC), Tier 2 (GIA Gem Encyclopedia video), Tier 4 for magnified inclusion video |
| C6 Bridal | Ring shape and setting style comparison; band stacking; sizing demonstration | Tier 1 (GIA/NDC), Tier 2 (GIA 4Cs engagement content) |
| C7 Estate & Antique | Period-style exemplars (Georgian → Retro); hallmark close-ups; hand-fabrication vs. cast cues | Tier 3 (Smithsonian, The Met, Wikimedia Commons), Tier 2 (Lang Antiques university — link-out) |
| C8 Custom & Repair | CAD-to-cast sequence; prong retipping; sizing; stone setting | Tier 4 (credentialed bench jewelers on YouTube, embed) |
| C4 Security & LP | Distraction-theft and grab-and-run footage used for training; two-person open/close demonstration | Tier 2 (Jewelers Mutual, JSA educational videos — link-out or embed) |
| C11–C14 Leadership | KPI dashboard examples; store-visit checklist samples; VM case-zoning diagrams | Tier 1/2 (Retail Ops Toolkit templates, GoAudits samples — link-out), Tier 5 (trade press) |

Every URL in this table's underlying sources must still pass C5 before use; the table is a search plan, not a manifest.
