import os

def embed_image_if_not_present(filepath, marker, image_block):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Check if this specific asset path is already in the file
    first_line_of_block = [line for line in image_block.strip().split('\n') if '<img' in line][0]
    src_match = [part for part in first_line_of_block.split() if 'src=' in part][0]
    if src_match in content:
        print(f"Already embedded {src_match} in {filepath}")
        return

    if marker in content:
        new_content = content.replace(marker, f"{marker}\n\n{image_block}\n", 1)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Successfully embedded into {filepath}")
    else:
        print(f"Marker '{marker}' not found in {filepath}")

# 1. C1 M02
c1_m02_path = "courses/C1-diamond-gemstone-fluency/articles/M02-reading-a-gia-report.md"
c1_m02_block = """<figure>
  <img src="../assets/c1-m02-gia-grading-report-annotated.svg" alt="Annotated GIA Diamond Grading Report Guide" width="100%" />
  <figcaption><strong>Figure 2.1:</strong> Annotated GIA Diamond Grading Report &amp; Dossier — Line-by-line breakdown of identification, 4Cs results, proportion diagram, clarity plot, and counter compliance rules.</figcaption>
</figure>"""
embed_image_if_not_present(c1_m02_path, "## The report, field by field", c1_m02_block)

# 2. C1 M03
c1_m03_path = "courses/C1-diamond-gemstone-fluency/articles/M03-ags-vs-gia-nomenclature.md"
c1_m03_block = """<figure>
  <img src="../assets/c1-m03-ags-vs-gia-conversion-scale.svg" alt="AGS 0-10 Scale vs GIA Nomenclature" width="100%" />
  <figcaption><strong>Figure 3.1:</strong> AGS 0–10 Numerical Scale vs. GIA Grading Nomenclature — Direct conversion matrix for Cut, Color, and Clarity grades.</figcaption>
</figure>"""
embed_image_if_not_present(c1_m03_path, "## Two labs, two philosophies, one goal", c1_m03_block)

# 3. C1 M04
c1_m04_path = "courses/C1-diamond-gemstone-fluency/articles/M04-lab-grown-natural-simulant.md"
c1_m04_block = """<figure>
  <img src="../assets/c1-m04-disclosure-decision-tree.svg" alt="Natural vs Lab-Grown vs Simulant Disclosure Decision Tree" width="100%" />
  <figcaption><strong>Figure 4.1:</strong> Counter Disclosure Decision Tree — FTC mandatory terminology, physical/chemical origins, and presentation scripts for Natural, Lab-Grown, and Simulant stones.</figcaption>
</figure>"""
embed_image_if_not_present(c1_m04_path, "## Natural, lab-grown, and simulant are three different categories", c1_m04_block)

# 4. C1 M05
c1_m05_path = "courses/C1-diamond-gemstone-fluency/articles/M05-fluorescence-inclusions.md"
c1_m05_block = """<figure>
  <img src="../assets/c1-m05-clarity-inclusion-plotting-symbols.svg" alt="Inclusion and Blemish Visual Plotting Guide" width="100%" />
  <figcaption><strong>Figure 5.1:</strong> GIA Clarity Plotting Key — Internal inclusions (Red), External blemishes (Green), and the 5 clarity grade determinants (Size, Number, Location, Relief, Nature).</figcaption>
</figure>"""
embed_image_if_not_present(c1_m05_path, "## A quick-reference table for common inclusion types", c1_m05_block)

# 5. C1 M06
c1_m06_path = "courses/C1-diamond-gemstone-fluency/articles/M06-colored-stone-top-10.md"
c1_m06_block = """<figure>
  <img src="../assets/c1-m06-colored-stone-top-10-matrix.svg" alt="Top 10 Colored Stones Reference Matrix" width="100%" />
  <figcaption><strong>Figure 6.1:</strong> Top 10 Colored Gemstones Reference Matrix — Species, Mohs hardness, toughness ratings, routine treatment norms, and ultrasonic/steam cleaning safety.</figcaption>
</figure>"""
embed_image_if_not_present(c1_m06_path, "## Hardness sets the baseline for every care conversation", c1_m06_block)

# 6. C1 M07
c1_m07_path = "courses/C1-diamond-gemstone-fluency/articles/M07-pearls.md"
c1_m07_block = """<figure>
  <img src="../assets/c1-m07-pearl-types-and-value-factors.svg" alt="Pearl Varieties and GIA 7 Value Factors" width="100%" />
  <figcaption><strong>Figure 7.1:</strong> Pearl Varieties &amp; GIA 7 Value Factors — Akoya, South Sea, Tahitian, and Freshwater characteristics, grading factors, and 'Last On, First Off' floor care rules.</figcaption>
</figure>"""
embed_image_if_not_present(c1_m07_path, "## The four major types of cultured pearls", c1_m07_block)

# 7. C1 M08
c1_m08_path = "courses/C1-diamond-gemstone-fluency/articles/M08-metals-marks-alloys.md"
c1_m08_block = """<figure>
  <img src="../assets/c1-m08-precious-metals-hallmarks.svg" alt="Precious Metals, Alloys and Hallmarks Guide" width="100%" />
  <figcaption><strong>Figure 8.1:</strong> Precious Metals &amp; International Hallmarks Guide — Gold karatage fineness, Platinum PT950 vs. White Gold trade-offs, and UK/US/EU hallmark stamps.</figcaption>
</figure>"""
embed_image_if_not_present(c1_m08_path, "## Gold karat purity, in one table", c1_m08_block)

# 8. C2 M01
c2_m01_path = "courses/C2-fine-jewelry-sales-conversation/articles/M01-first-90-seconds.md"
c2_m01_block = """<figure>
  <img src="../assets/c2-m01-first-90-seconds-flow.svg" alt="The First 90 Seconds Floor Protocol" width="100%" />
  <figcaption><strong>Figure 1.1:</strong> The First 90 Seconds Approach Map — 10-foot proximity buffer, eliminating 'Can I help you?', and the tactile transition to the presentation pad.</figcaption>
</figure>"""
embed_image_if_not_present(c2_m01_path, "## The Luxury Decompression Zone: The First Ten Seconds", c2_m01_block)

# 9. C2 M02
c2_m02_path = "courses/C2-fine-jewelry-sales-conversation/articles/M02-discovery-real-purchase.md"
c2_m02_block = """<figure>
  <img src="../assets/c2-m02-discovery-questioning-tree.svg" alt="The 4-Pillar Discovery Questioning Tree" width="100%" />
  <figcaption><strong>Figure 2.1:</strong> The 4-Pillar Discovery Questioning Tree — Uncovering Occasion, Recipient Lifestyle, Aesthetic Taste, and Investment Range.</figcaption>
</figure>"""
embed_image_if_not_present(c2_m02_path, "## 3. The seven discovery areas", c2_m02_block)

# 10. C2 M03
c2_m03_path = "courses/C2-fine-jewelry-sales-conversation/articles/M03-presenting-piece-story-craft-value.md"
c2_m03_block = """<figure>
  <img src="../assets/c2-m03-feature-benefit-emotion-bridge.svg" alt="Feature Benefit Emotion Storytelling Bridge" width="100%" />
  <figcaption><strong>Figure 3.1:</strong> Feature → Benefit → Emotion Storytelling Bridge — Connecting technical specs to functional customer benefits and lasting emotional milestone narratives.</figcaption>
</figure>"""
embed_image_if_not_present(c2_m03_path, "## 3. Translate features into client meaning", c2_m03_block)

# 11. C2 M05
c2_m05_path = "courses/C2-fine-jewelry-sales-conversation/articles/M05-price-objections-without-discounting.md"
c2_m05_block = """<figure>
  <img src="../assets/c2-m05-price-objection-ladder.svg" alt="The 4-Step Price Objection Ladder" width="100%" />
  <figcaption><strong>Figure 5.1:</strong> The 4-Step Price Objection Ladder — Acknowledging without flinching, isolating price vs. style, re-engineering 4Cs levers, and offering promotional financing.</figcaption>
</figure>"""
embed_image_if_not_present(c2_m05_path, "## Diagnose before you answer", c2_m05_block)

# 12. C2 M09
c2_m09_path = "courses/C2-fine-jewelry-sales-conversation/articles/M09-three-ways-to-ask-for-the-sale.md"
c2_m09_block = """<figure>
  <img src="../assets/c2-m09-three-closing-pathways.svg" alt="Three Natural Closing Pathways" width="100%" />
  <figcaption><strong>Figure 9.1:</strong> Three Natural Closing Pathways — Assumptive Next Step, Alternative Choice, and Direct Milestone closing architectures for fine jewelry.</figcaption>
</figure>"""
embed_image_if_not_present(c2_m09_path, "## Recognize the moment first", c2_m09_block)

# 13. C4 M01
c4_m01_path = "courses/C4-store-security-loss-prevention/articles/M01-opening-and-closing-the-two-person-rule-and-alarm-response.md"
c4_m01_block = """<figure>
  <img src="../assets/c4-m01-dual-custody-opening-closing-sop.svg" alt="Dual-Custody Store Opening and Closing Protocol" width="100%" />
  <figcaption><strong>Figure 1.1:</strong> Dual-Custody Store Opening &amp; Closing SOP — 4-phase entry sequence, physical all-clear signals, dual safe combination control, and empty showcase display protocols.</figcaption>
</figure>"""
embed_image_if_not_present(c4_m01_path, "## The Two-Person Rule and the All-Clear Signal", c4_m01_block)

# 14. C4 M06
c4_m06_path = "courses/C4-store-security-loss-prevention/articles/M06-large-cash-transactions-and-form-8300-compliance.md"
c4_m06_block = """<figure>
  <img src="../assets/c4-m06-form-8300-cash-compliance-tree.svg" alt="IRS Form 8300 Cash Compliance Decision Tree" width="100%" />
  <figcaption><strong>Figure 6.1:</strong> IRS Form 8300 &amp; FinCEN Compliance Decision Tree — Cash definition, 24-hour transaction aggregation, 15-day e-filing clock, and anti-structuring rules.</figcaption>
</figure>"""
embed_image_if_not_present(c4_m06_path, "## What Triggers a Filing", c4_m06_block)

# 15. C8 M02
c8_m02_path = "courses/C8-custom-design-repair-workflow/articles/M02-intake-documenting-condition-setting-expectations-and-the-job-ticket.md"
c8_m02_block = """<figure>
  <img src="../assets/c8-m02-jewelry-intake-condition-map.svg" alt="Jewelry Intake Condition Mapping Template" width="100%" />
  <figcaption><strong>Figure 2.1:</strong> Jewelry Intake Condition Mapping Template &amp; 6-Point Checklist — 10x magnification flaw documentation, stone tightness testing, and pre-existing damage disclosure.</figcaption>
</figure>"""
embed_image_if_not_present(c8_m02_path, "## Inspect Before You Accept: The Pre-Existing Condition Check", c8_m02_block)

# 16. C8 M03
c8_m03_path = "courses/C8-custom-design-repair-workflow/articles/M03-the-cad-to-casting-workflow-how-a-custom-piece-actually-gets-made.md"
c8_m03_block = """<figure>
  <img src="../assets/c8-m03-cad-to-casting-7-stage-pipeline.svg" alt="The 7-Stage CAD-to-Casting Custom Workflow" width="100%" />
  <figcaption><strong>Figure 3.1:</strong> The 7-Stage CAD-to-Casting Custom Jewelry Pipeline — From initial sketch to 3D CAD, CAM wax model, lost-wax casting, stone setting, and final QC delivery.</figcaption>
</figure>"""
embed_image_if_not_present(c8_m03_path, "## Stage One: From CAD File to Physical Pattern", c8_m03_block)

# 17. C3 M02
c3_m02_path = "courses/C3-clienteling-and-crm/articles/M02-clienteling-calendar-cadences-that-feel-personal.md"
c3_m02_block = """<figure>
  <img src="../assets/c3-m02-2-2-2-clienteling-cadence.svg" alt="The 2-2-2 Client Retention and Outreach Cadence" width="100%" />
  <figcaption><strong>Figure 2.1:</strong> The 2-2-2 Relationship Cadence — Day 2 gratitude SMS, Week 2 reaction check-in, and Month 2 complimentary ultrasonic cleaning invitation.</figcaption>
</figure>"""
embed_image_if_not_present(c3_m02_path, "## The post-sale sequence: 30, 90, 365", c3_m02_block)

# 18. C12 M01
c12_m01_path = "courses/C12-retail-kpis-reporting/articles/M01-the-kpi-vocabulary-of-jewelry-retail.md"
c12_m01_block = """<figure>
  <img src="../assets/c12-m01-retail-kpi-hierarchy-pyramid.svg" alt="Jewelry Retail KPI Cascade Hierarchy" width="100%" />
  <figcaption><strong>Figure 1.1:</strong> Jewelry Retail KPI Cascade Hierarchy — Connecting top-line GMROI and margin dollars down to traffic, conversion %, ATV, and UPT floor drivers.</figcaption>
</figure>"""
embed_image_if_not_present(c12_m01_path, "## Conversion Rate: The Percentage That Explains Everything Else", c12_m01_block)

print("All asset embeddings processed!")
