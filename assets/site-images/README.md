# jewelswell.com course imagery

Photographic course images generated for the live site, at **1600×900 (16:9)**.

- `*.png` — primary files, matching the site's existing `.png` upload convention
- `jpg/*.jpg` — same images at quality 86, roughly **8× smaller**. Prefer these
  for the homepage grid and hero, where a 1.5–2 MB PNG measurably hurts
  Largest Contentful Paint. PNG offers no benefit for photographic content with
  no transparency.

## Why these were made

A site audit on 2026-09-27 found **7 stock images serving all 16 courses**.
Several were doing triple duty:

| Existing file | Currently reused by |
|---|---|
| `pillar-1-gemstone-education-hero.png` | C1, C8, C16 |
| `pillar-2-jewelry-sales-psychology-hero.png` | C2, C10, flagship Closer System |
| `pillar-3-cruise-port-jewelry-sales-hero.png` | C6, C9, C17 |
| `pillar-4-jewelry-industry-knowledge-hero.png` | C4, C7, Store Manager track |
| `p2-01-seven-steps-to-a-jewelry-sale.png` | C5, C12, closing field guide |
| `p2-03-building-trust-with-jewelry-buyers.png` | C3, C13, objection playbook |
| `manager-daily-sales-huddle.png` | C11, huddle field guide |

Every course now gets imagery specific to its own subject.

## Upload map

Replace the featured image on each course with the file below. Filenames are
already slug-aligned with the course URLs.

| Course | New file | Replaces | Subject |
|---|---|---|---|
| Homepage hero | `hero-jewelswell-master-academy.png` | `pillar-2-…-hero.png` | Diamond in tweezers, dark atelier, gold bokeh |
| C1 Diamond & Gemstone Fluency | `c1-diamond-gemstone-fluency.png` | `pillar-1-…-hero.png` | Loose brilliant on a grading tray, loupe, report |
| C2 Fine Jewelry Sales Conversation | `c2-fine-jewelry-sales-conversation.png` | `pillar-2-…-hero.png` | Associate presenting a ring across the counter |
| C3 Clienteling & CRM | `c3-clienteling-and-crm.png` | `p2-03-building-trust…png` | Handwritten client note, ribboned boxes, client book |
| C4 Store Security & Loss Prevention | `c4-store-security-loss-prevention.png` | `pillar-4-…-hero.png` | Vault door, combination dial, after-hours light |
| C5 Financing, Credit & Compliance | `c5-financing-credit-compliance.png` | `p2-01-seven-steps…png` | POS terminal, card, agreement paperwork |
| C6 Bridal & Engagement Mastery | `c6-bridal-engagement-mastery.png` | `pillar-3-…-hero.png` | Platinum solitaire with matching pavé band on silk |
| C7 Estate, Antique & Trade-In | `c7-estate-antique-trade-in.png` | `pillar-4-…-hero.png` | Art Deco brooch, Victorian locket, loupe, ledger |
| C8 Custom Design & Repair Workflow | `c8-custom-design-repair-workflow.png` | `pillar-1-…-hero.png` | Jeweler's bench, ring clamp, torch, gold shavings |
| C9 Selling in Compressed Time | `c9-selling-high-ticket-compressed-time.png` | `pillar-3-…-hero.png` | Cruise-port boutique, ship and harbour behind |
| C10 Luxury Psychology & Negotiation | `c10-luxury-consumer-psychology-negotiation.png` | `pillar-2-…-hero.png` | Private VIP salon, high jewelry tray, champagne |
| C11 Running the Store | `c11-running-the-store-operations.png` | `manager-daily-sales-huddle.png` | Morning team huddle before opening |
| C12 Retail KPIs & Reporting | `c12-retail-kpis-reporting.png` | `p2-01-seven-steps…png` | Analytics dashboards on the store counter |
| C13 Hiring, Coaching & Performance | `c13-hiring-coaching-performance.png` | `p2-03-building-trust…png` | One-on-one coaching at a consultation table |
| C14 Multi-Store Leadership | `c14-multi-store-leadership.png` | *(no image today)* | Regional director walking a flagship floor |
| C16 GIA Diamonds Deep Dive | `c16-gia-diamonds-deep-dive.png` | `pillar-1-…-hero.png` | Rough octahedron beside a polished brilliant, under the scope |
| C17 GIA Colored Stones Deep Dive | `c17-gia-colored-stones-deep-dive.png` | `pillar-3-…-hero.png` | Ruby, sapphire, emerald and jade on a lab tray |

## The second image slot

Course pages also carry an in-page **"Figure 0.1"** hero with a caption — C16
currently uses `p1-four-cs-realistic.png` captioned *"Mantle genesis,
ray-tracing cut evaluation, lab-grown detection, and international bourses."*

That slot is a better home for the **branded diagram covers** in
`assets/frontpage/`, which state the curriculum claims as legible text. The
photographic files here are intended for the card/featured slot, where text in
an image would be redundant against the card's own heading.

## Provenance

These are **AI-generated photographic images**, not licensed stock and not
photographs of real people, places, or merchandise. Per the Part C rules in
`courses/media-sources.md`, AI-generated visuals are prohibited *inside course
articles as evidentiary or instructional media* — nothing here is embedded in a
module article. They are marketing imagery for course cards and hero banners
only. Do not present them as photographs of actual inventory, stores, staff, or
clients.

Regenerate or re-normalize with:

```bash
python3 scripts/normalize_site_images.py
```
