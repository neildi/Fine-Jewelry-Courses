# C17 Verification Review

Status: **Course complete — 16/16 modules.** Capstone verification pass (Round 1 / R1) recorded 2026-09-11.

> This document is the R1 capstone verification review referred to throughout the M01–M10 fact-check tables ("MUST VERIFY — resolve by capstone"). It records what was re-checked at the capstone, what was resolved, what was corrected, and what remains open for a v1.1 polish pass.

---

## 1. Build completion audit

| Wave | Modules | Status |
|---|---|---|
| Wave 1 | M01 | ✅ Complete (merged PR #3) |
| Wave 2 | M02, M03, M04 | ✅ Complete (merged PR #3) |
| Wave 3 | M05, M06, M07 | ✅ Complete (merged PR #3) |
| Wave 4 | M08, M09, M10 | ✅ Complete (merged PR #3) |
| Wave 5 | M11 Ruby, M12 Blue Sapphire, M13 Fancy & Phenomenal Corundum, M14 Emerald | ✅ Complete (this PR) |
| Wave 6 | M15 Pearls, M16 Jade + capstone review | ✅ Complete (this PR) |

**Six-step SOP audit — all 16 modules pass:**

- [x] Step 1 outline — `production/M01–M16-outline.md` (16 files)
- [x] Step 2 media research — `production/M01–M16-media-manifest.md` (16 files); video policy observed throughout
- [x] Step 3 article — `articles/M01–M16-*.md` (16 files)
- [x] Step 4 self-critique — recorded per module in the outline and factcheck files
- [x] Step 5 fact-check — `production/M01–M16-factcheck.md` (16 files, with [VERIFY] flags and MUST VERIFY lists)
- [x] Step 6 quiz + huddle card — `production/M01–M16-quiz.md` and `-huddle-card.md` (32 files)

**Quiz audit:** all 16 modules carry 10 multiple-choice questions with a full answer key that explains the reasoning, not just the letter. 160 questions total.

**Course totals (complete):**

- 16 modules, **~61,300 words** of article text (M01–M10 ~41,800 + M11–M16 ~19,400)
- 160 quiz questions with answer keys
- 96 module support files (16 × article + outline + media-manifest + factcheck + quiz + huddle-card)
- ~260 GIA *Gems & Gemology* / Research & News citations in `references/annotated-bibliography.md`
- 10 pre-verified videos in `videos/video-library.md`, none newly promoted in Waves 5–6
- **No AI-generated imagery or video** (Prompt Kit Part C) — every media item is a real GIA or creator work, linked not re-hosted

---

## 2. Customer-facing and legal facts resolved at capstone

These are the items with the highest downside if wrong, because they are statements a client can act on or a regulator can ask about. All were re-verified on 2026-09-11.

| # | Item | Resolution | Where used |
|---|---|---|---|
| 1 | **Sunrise Ruby** — record and price | 25.59 ct Mogok ruby, Sotheby's Geneva, May 2015, CHF 28.25 million ≈ **US$30.3 million** (over $1.1M/ct). Reported as **"about $30.3 million (CHF 28.25 million)"** — individual sources vary between $30.34M and $30.42M, so a rounded figure is used | M11 article, M11 factcheck |
| 2 | **La Peregrina** | **202.24 grains ≈ 50.56 carats**; Christie's New York, December 2011, **$11,842,500** — world record for a pearl jewel | M15 article, M15 factcheck |
| 3 | **Tom Lantos Block Burmese JADE Act** | **Pub. L. 110-286, enacted 29 July 2008.** Amends the Burmese Freedom and Democracy Act of 2003 to prohibit US importation of **jadeite and rubies** (including jewelry containing them) mined or extracted from Burma, regardless of where processed. Scope is **jadeite and ruby only** — not sapphire, spinel or other Burmese gems | M11, M16 |
| 4 | **Burmese sanctions status** | The 2008 statute is only part of the picture: the broader Burma sanctions program was **terminated in 2016**, and Myanmar Gem Enterprise and associated entities were **re-sanctioned in 2021** (OFAC). Article text tells associates to **ask compliance before any Burmese-origin purchase** and never to assume an old answer is current | M11 |
| 5 | **GIA origin-determination species** | Effective **1 January 2026** GIA extended origin services to **opal, peridot and demantoid garnet**, building on alexandrite, emerald, Paraíba-type tourmaline, red spinel, ruby, sapphire, and untreated jadeite/omphacite jade from Myanmar and Guatemala — **11 species** total | M11, M13, M16 |
| 6 | **Kashmir exhaustion date** | Discovered 1880s; essentially **exhausted by the 1930s**, with only small-scale recovery since (Atkinson & Kothavala, 1983). Resolves the M10 open item | M12 |
| 7 | **Ethiopian emerald** | Shakiso/Kenticha area, Oromia; material **reached the market around 2016–2017**; chromium-dominant and low-iron, which is why it can look Colombian | M14 |
| 8 | **Ballerina "chocolate pearls"** | **Treated-color Tahitian cultured pearls** (*Pinctada margaritifera*), treated by a **bleaching-type process**, distinct from the older silver-nitrate (Ag) dyeing method. See the correction in §3 | M15 |

**Deliberately not published:** approximate figures that could not be pinned to a primary source were either rounded with the variance shown (Sunrise Ruby) or left out of the article bodies entirely (Rockefeller Emerald, Hutton-Mdivani necklace). Both are listed in §5 as open.

---

## 3. Corrections made during Waves 5–6

| # | Correction | Detail |
|---|---|---|
| C1 | **"Chocolate pearls" are Tahitian, not freshwater** | The build brief described Ballerina-process chocolate pearls as a freshwater product. GIA's published studies (Wang et al. 2006; Du Toit 2008; the 2016 "pistachio" study) describe them as **treated-color Tahitian cultured pearls**. The M15 article uses the GIA description and the fact-check logs the correction explicitly. |
| C2 | **Hpakant is jadeite, not emerald** | The build brief listed Hpakant among emerald sources. It is the premier **jadeite** locality in Kachin State, Myanmar. M14 carries an explicit note warning against conflating the two Myanmar names. |
| C3 | **"X-ray natural-pearl logic analogs" in fancy corundum** | The build brief referenced X-ray natural-pearl logic in the M13 (fancy corundum) module. That is a pearl-topic item and has no application to corundum; it was dropped from M13. The X-ray/μ-CT material appears where it belongs, in M15. |
| C4 | **Fluorescence framed as a clue, not a test** | Ruby and sapphire origin conversations are where associates most often overclaim. M11 and M12 both state explicitly that fluorescence is a clue to origin and **never** a proof, and that heat-treatment status cannot be read from a UV lamp. |
| C5 | **Price bands marked as directional** | All per-carat budget tables in M11–M14 carry a standing note that they are internal directional guidance to be checked against the store's own cost sheets, not market data. |

---

## 4. Cross-module consistency checks

- [x] **Mohs values consistent** across M04, M11 (corundum 9), M12 (corundum 9), M14 (beryl 7.5–8), M15 (pearl 2.5–4.5), M16 (jadeite 6.5–7, nephrite 6–6.5)
- [x] **Care rules consistent** — the four ultrasonic-sensitive categories (filled corundum, enhanced emerald, pearl, Type B/C jade) are stated identically wherever they appear
- [x] **Hardness ≠ toughness** stated in every module where a hard stone is also fragile (M11 filled ruby, M12 sapphire chipping, M14 emerald brittleness)
- [x] **Disclosure rule consistent** — Overton (2004) / FTC Jewelry Guides cited as the anchor in M09, M11, M12, M13, M14, M15 and M16; the "pearl" vs "cultured pearl" vocabulary rule appears in M15
- [x] **Treatment vocabulary consistent** — F0–F3 (emerald), Type A/B/C (jade), "indications of heating" / "with residues" (corundum) all used in the lab's sense throughout
- [x] **Lab list consistent** — GIA, AGL, GRS, Gübelin, SSEF, Lotus, AIGS named identically in M10, M12, M13
- [x] **Media policy** — no new video promoted from the ⏳ candidate pool in Waves 5–6; every embedded clip was verified live on 2026-09-11 and re-used at its point of use

---

## 5. Open items — deferred to v1.1 (none affect floor safety, disclosure or pricing)

Nine items of academic precision remain. Each is flagged inline in its module fact-check table. **None of them changes a care rule, a disclosure obligation, or a price band**, which is why the course is rated ready for internal staff training.

| # | Open item | Module | Why it is low risk |
|---|---|---|---|
| 1 | Exact carat weights of the **Black Prince's Ruby** (~170 ct) and **Timur Ruby** (~352 ct) from a museum catalogue | M11 | Cited as historical illustration; no client decision rests on the exact figure |
| 2 | Exact **GIA "pigeon's blood"** criteria wording | M11 | The article says GIA applies defined criteria and refers the call to the report |
| 3 | Exact GIA criteria wording for the **padparadscha** color call | M12, M13 | Both modules already instruct associates never to use the name without a report |
| 4 | Primary **G&G citation for cobalt-glass-filled sapphire** | M12 | Detection features are stated; only the citation is pending |
| 5 | Origin attribution for the **Diana/Catherine sapphire** from a museum or Garrard source | M12 | Widely reported as Ceylon; article presents it as public record |
| 6 | **Rockefeller Emerald** exact sale price and date | M10, M14 | Deliberately not quoted in any article body |
| 7 | Precise discovery vs first-market year for **Ethiopian emerald** | M14 | Article says "around 2016–2017" |
| 8 | **Hutton-Mdivani jadeite necklace** auction figures | M16 | Deliberately not quoted in any article body |
| 9 | The **1863** date for the scientific separation of jadeite and nephrite, and its attribution | M16 | Stated as history; not used in any identification guidance |

Additional standing caution recorded for future work: any **Māori-specific** statement about pounamu (M16) must be reviewed with appropriate cultural authority before publication beyond internal training use. The current text is deliberately general.

---

## 6. Read-level honesty reminder

★ entries in `references/annotated-bibliography.md` are sources whose full text was fetched and read during production; unstarred entries are title/abstract-level by design (context budget). [VERIFY] flags in the fact-check tables mark claims that depend on an unstarred citation, an approximate number, or a trade convention rather than a standard. Work the [VERIFY] flags before any public publication.

## 7. Independence disclaimer

This is an independent study companion, not an official GIA product and not endorsed by or affiliated with the Gemological Institute of America. GIA, *Gems & Gemology*, the GIA Gem Encyclopedia and related marks are the property of their respective owners. All GIA sources are cited and linked, never copied or re-hosted.
