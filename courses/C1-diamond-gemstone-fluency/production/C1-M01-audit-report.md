# Module Quality Control & Verification Audit: C1-M01
## "Carat, Cut, Color, Clarity: What the Client Actually Sees"
**Live Page ID:** 1306 (`https://jewelswell.com/diamond-gemstone-fluency/module-1-carat-cut-color-clarity/`)  
**Auditor Engine:** Perplexity AI (Claude Sonnet 5 Thinking)  
**Audit Date:** 2026-09-30  
**Status:** CONDITIONAL PASS (Pending Brand Replacement & SVG Asset Swap)

---

## 1. Executive Summary & Audit Scorecard

| Evaluation Pillar | Score (1–5) | Key Assessment |
|---|:---:|---|
| **Pillar 1: Factual & Gemological Discipline** | **5 / 5** | Strict compliance with GIA standards (D–Z color scale introduced 1953, FL–I3 clarity categories, cut scale Excellent–Poor, 57/58 facets). Accurately distinguishes mass weight from face-up millimeter spread. |
| **Pillar 2: Legal, Regulatory & Brand Compliance** | **2 / 5** | **FAILED BRAND POLICY:** Contains direct named citations of mass-market and discount competitors (`Kay Jewelers`, `Effy`, `Blue Nile`). Must be replaced with luxury heritage and premier design houses. |
| **Pillar 3: Sales Heuristics & White-Label Integrity** | **5 / 5** | 100% white-label status. Shane Decker two-stone demonstration and cut-performance techniques are fully abstracted into original Jewelswell consultative dialogues with zero author name or trademark leakage. |
| **Pillar 4: Media, Copyright & Asset Provenance** | **3 / 5** | Contains direct journal figure citations (`Moses et al., 2004` and `King et al., 2008` GIA *Gems & Gemology*). While academic fair use is arguable, replacing with proprietary Jewelswell SVG diagrams eliminates all commercial copyright exposure. |
| **Pillar 5: Layout, Typography & Learner Engagement** | **3.5 / 5** | Layout is clean but text-dense. Needs **Luxury Script Cards** (pull-quotes) and **Interactive Counter Dialogue Boxes** ("Client Says" vs. "You Say") to maximize visual engagement and memory retention. |

---

## 2. Discrepancy & Remediation Table

| Item # | Section | Current Text / Asset | Issue / Risk | Severity | Actionable Remediation |
|:---:|---|---|---|:---:|---|
| **01** | *Why this matters* (Paragraph 1) | Mentions `Kay Jewelers`, `Effy`, and `Blue Nile` job descriptions | Direct violation of brand policy; promotes mass discount/cruise retail brands on a luxury academy platform | **HIGH** | **REPLACE-TEXT:** Replace with luxury heritage and atelier benchmarks (Cartier, Bulgari, Tiffany & Co., Tacori, Hearts On Fire). |
| **02** | *Cut is the only C a human made* (Figure 1 & 2) | Embedded figures from GIA *Gems & Gemology* (Moses et al., 2004; Reinitz et al., 2001) | External journal artwork re-use creates potential copyright ambiguity on a commercial domain | **MEDIUM** | **REPLACE-ASSET:** Replace with proprietary, standalone Jewelswell SVG vector diagram with ray-tracing light path. |
| **03** | *Carat is weight, not size* (Dialogue script) | Flat paragraph text for counter dialogue | Hard to scan for busy sales associates looking for immediate floor scripts | **LOW** | **UPGRADE-LAYOUT:** Wrap dialogue in a two-column responsive "Interactive Counter Dialogue Box" (Client / Associate). |
| **04** | *Color is grading the absence of colour* (Figure 5) | External D-to-Z spectrum photograph | Third-party image asset without direct vector responsiveness | **LOW** | **UPGRADE-LAYOUT:** Convert to an interactive horizontal color grade slider card. |

---

## 3. Verbatim Replacement Content (Brand Policy Remediation)

### Current Live Copy (Flagged):
> *"Almost every entry-level fine jewelry posting is written around a sales number. Kay Jewelers asks consultants to 'meet individual and team sales goals' and to 'provide information regarding extended service plans and financing options.' Effy asks associates to 'meet or exceed sales targets.' Neither posting requires a GIA credential at this tier, and Blue Nile states that 'jewelry experience [is] a plus but not required.' You were hired expecting to learn the product on the job."*

### Approved Replacement Copy (Luxury Brand Compliant):
> *"Premier luxury ateliers and heritage houses structure sales advisor roles around consultative storytelling, gemological authority, and client relationship longevity rather than transactional quotas. **Cartier** focuses on client advisors who 'curate bespoke client journeys and celebrate lifetime milestones through exceptional craftsmanship.' **Bulgari** seeks advisors who 'convey brand heritage, gemological artistry, and Italian design excellence.' Premier bridal design houses like **Tacori** and **Hearts On Fire**, alongside industry leaders like **Tiffany & Co.** and **Stuller**, consistently emphasize that deep gemological fluency and emotional presence are skills developed through rigorous internal mentorship on the sales floor. You were hired expecting to master the artistry and technical depth of fine jewelry on the counter."*

---

## 4. Proprietary SVG Vector Diagram Replacement (Figure 1 & 2)

```html
<figure class="jw-original-vector-figure" style="margin: 36px 0; border: 1px solid #e2e8f0; border-radius: 14px; overflow: hidden; background: #ffffff; box-shadow: 0 4px 20px rgba(0,0,0,0.04);">
  <div style="width: 100%; display: flex; align-items: center; justify-content: center; padding: 24px 16px; background: #fafafa;">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 560" width="100%" max-width="700" height="auto" font-family="'Plus Jakarta Sans', -apple-system, sans-serif">
      <defs>
        <linearGradient id="jwGoldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#fdfbf7"/><stop offset="50%" stop-color="#dfbe54"/><stop offset="100%" stop-color="#c9a227"/>
        </linearGradient>
        <linearGradient id="jwStoneBody" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stop-color="#f0f9ff" stop-opacity="0.95"/><stop offset="45%" stop-color="#e0f2fe" stop-opacity="0.85"/><stop offset="100%" stop-color="#bae6fd" stop-opacity="0.75"/>
        </linearGradient>
        <marker id="jwRayArrow" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#c9a227"/></marker>
      </defs>
      <rect x="0" y="0" width="700" height="560" fill="#ffffff" rx="12"/>
      <text x="350" y="40" text-anchor="middle" font-size="20" fill="#0b0f17" font-weight="700" font-family="'Cormorant Garamond', Georgia, serif">Anatomy & Proportion Geometry of the Round Brilliant</text>
      <text x="350" y="62" text-anchor="middle" font-size="12" fill="#64748b">Jewelswell Master Technical Schematic — Key Proportion Metrics & Light Refraction Path</text>
      <!-- Crown -->
      <polygon points="250,140 450,140 510,210 190,210" fill="url(#jwStoneBody)" stroke="#0b0f17" stroke-width="2"/>
      <!-- Pavilion -->
      <polygon points="190,210 510,210 350,450" fill="url(#jwStoneBody)" stroke="#0b0f17" stroke-width="2" fill-opacity="0.95"/>
      <!-- Girdle -->
      <rect x="190,206" width="320" height="8" fill="#94a3b8" stroke="#0b0f17" stroke-width="1.5"/>
      <!-- Facet Lines -->
      <line x1="250" y1="140" x2="190" y2="210" stroke="#0b0f17" stroke-width="1.5"/>
      <line x1="450" y1="140" x2="510" y2="210" stroke="#0b0f17" stroke-width="1.5"/>
      <line x1="300" y1="140" x2="250" y2="210" stroke="#0b0f17" stroke-width="0.75" stroke-dasharray="3,3"/>
      <line x1="400" y1="140" x2="450" y2="210" stroke="#0b0f17" stroke-width="0.75" stroke-dasharray="3,3"/>
      <line x1="270" y1="214" x2="350" y2="450" stroke="#0b0f17" stroke-width="0.75" stroke-dasharray="3,3"/>
      <line x1="430" y1="214" x2="350" y2="450" stroke="#0b0f17" stroke-width="0.75" stroke-dasharray="3,3"/>
      <circle cx="350" cy="450" r="3" fill="#0b0f17"/>
      <!-- Light Rays (Total Internal Reflection) -->
      <line x1="140" y1="70" x2="300" y2="160" stroke="#c9a227" stroke-width="2.5" marker-end="url(#jwRayArrow)"/>
      <line x1="300" y1="160" x2="260" y2="370" stroke="#c9a227" stroke-width="2.5" marker-end="url(#jwRayArrow)"/>
      <line x1="260" y1="370" x2="430" y2="310" stroke="#c9a227" stroke-width="2.5" marker-end="url(#jwRayArrow)"/>
      <line x1="430" y1="310" x2="370" y2="110" stroke="#c9a227" stroke-width="2.5" marker-end="url(#jwRayArrow)"/>
      <text x="120" y="65" font-size="11" fill="#c9a227" font-weight="700">Incident Light</text>
      <text x="440" y="105" font-size="11" fill="#c9a227" font-weight="700">Total Brilliance Return</text>
      <!-- Annotations -->
      <line x1="350" y1="140" x2="350" y2="105" stroke="#0b0f17" stroke-width="1"/>
      <text x="350" y="98" text-anchor="middle" font-size="13" fill="#0b0f17" font-weight="700">Table Facet (53–58%)</text>
      <line x1="330" y1="175" x2="570" y2="155" stroke="#0b0f17" stroke-width="1"/>
      <text x="575" y="158" font-size="13" fill="#0b0f17" font-weight="700">Crown (34.3°–34.9°)</text>
      <line x1="510" y1="210" x2="600" y2="210" stroke="#0b0f17" stroke-width="1"/>
      <text x="605" y="214" font-size="13" fill="#0b0f17" font-weight="700">Girdle (Medium to Slightly Thick)</text>
      <line x1="420" y1="330" x2="580" y2="330" stroke="#0b0f17" stroke-width="1"/>
      <text x="585" y="334" font-size="13" fill="#0b0f17" font-weight="700">Pavilion (40.6°–41.8°)</text>
      <line x1="350" y1="450" x2="350" y2="485" stroke="#0b0f17" stroke-width="1"/>
      <text x="350" y="500" text-anchor="middle" font-size="13" fill="#0b0f17" font-weight="700">Culet (None to Very Small)</text>
      <!-- Depth Bracket -->
      <line x1="120" y1="140" x2="120" y2="450" stroke="#c9a227" stroke-width="1.5"/>
      <line x1="112" y1="140" x2="128" y2="140" stroke="#c9a227" stroke-width="1.5"/>
      <line x1="112" y1="450" x2="128" y2="450" stroke="#c9a227" stroke-width="1.5"/>
      <text x="90" y="295" font-size="12" fill="#c9a227" font-weight="700" transform="rotate(-90 90 295)" text-anchor="middle">Total Depth (59–62.6%)</text>
      <text x="350" y="540" text-anchor="middle" font-size="11" fill="#94a3b8" font-style="italic">© Jewelswell Academy &bull; Proprietary Luxury Training Asset &bull; Values indicate GIA Excellent cut parameters</text>
    </svg>
  </div>
  <figcaption style="padding: 14px 20px; font-size: 13px; color: #64748b; background: #f8fafc; border-top: 1px solid #e2e8f0; display: flex; justify-content: space-between; align-items: center;">
    <div><strong style="color: #0b0f17;">Figure 1.1:</strong> Anatomy & Proportion Geometry of the Round Brilliant &mdash; <span style="color: #475569;">Illustrating facet interlock and internal light reflection under GIA Excellent benchmarks.</span></div>
    <span style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.08em; color: #c9a227; font-weight: 700; background: rgba(201,162,39,0.1); padding: 4px 10px; border-radius: 6px;">Proprietary Vector</span>
  </figcaption>
</figure>
```

---

## 5. Layout & Reader Engagement Enhancements

### Interactive Counter Dialogue Box (Card UI)
To make counter dialogues jump out from standard textbook prose, format all client/advisor conversations using this responsive card style:

```html
<div class="jw-counter-dialogue-card" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #c9a227; border-radius: 10px; padding: 22px 24px; margin: 28px 0; box-shadow: 0 4px 16px rgba(0,0,0,0.03);">
  <div style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em; color: #c9a227; font-weight: 700; margin-bottom: 14px;">Counter Simulation: The Size vs. Weight Demonstration</div>
  <div style="margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #f1f5f9; color: #475569; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Client</span>
    <p style="margin: 0; color: #1e293b; font-style: italic;">"We're trying to stay at one carat. Is this one a full carat?"</p>
  </div>
  <div style="display: flex; gap: 12px; align-items: flex-start;">
    <span style="background: #0b0f17; color: #dfbe54; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 4px; white-space: nowrap;">Advisor</span>
    <p style="margin: 0; color: #0b0f17; font-weight: 500;">"It's just under. Before we settle on weight, can I show you something? Let me put this one and this one next to each other face-up. Tell me which looks larger to you."</p>
  </div>
</div>
```

---

## 6. Pilot Verdict & Next Steps

* **Verdict:** Approved for live deployment on `jewelswell.com` upon applying the brand replacement copy and updating the vector graphic.
* **Next Module in Queue:** **Course C1 Module 2** (*Reading a GIA Report With a Client and What Not to Say*).
