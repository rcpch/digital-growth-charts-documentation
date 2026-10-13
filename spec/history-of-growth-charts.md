# History of Growth Charts Content Specification

Status: proposed

This specification defines the scope, evidence model, content structure, timeline, visual treatment, accessibility requirements, and review gates for a new clinician-facing history of growth charts. It specifies future published documentation; it is not itself clinical guidance.

## Purpose

The section should explain how growth charts emerged from three related developments:

1. repeated measurement of individual children;
2. statistical modelling of selected populations; and
3. chart and software interfaces designed for clinical interpretation.

The central clinical lesson is that every chart line represents choices about who was measured, when and how they were measured, the model fitted to those measurements, and the purpose for which the resulting chart was designed. A chart is a comparison tool, not a grade, diagnosis, or timeless definition of healthy growth.

The history should be framed as **the development of methods and chart lineages that shaped current UK practice, with selected international context**. It must not claim to be a complete global history.

## Audience And Placement

The primary audience is clinicians and health staff who measure, plot, interpret, or explain childhood growth. Secondary audiences are clinical informaticians, implementers, researchers, statisticians, educators, trainees, and interested families.

The section should sit under **Clinicians**, close to the existing growth-reference and chart-information pages. It should link to current guidance rather than duplicate it:

- [Growth References](../docs/clinician/growth-references.md)
- [Growth Chart Papers](../docs/clinician/growth-chart-papers.md)
- [Information for Health Staff](../docs/clinician/chart-information-health-staff.md)

## Learning Outcomes

After reading the section, a clinician should be able to:

1. distinguish a measurement, an individual trajectory, a cross-sectional distribution, a growth reference, a growth standard, and a chart interface;
2. explain why serial measurements are needed to assess a pattern of growth;
3. identify the population, period, age range, sex model, measurement method, and statistical method represented by a reference;
4. distinguish attained size from growth velocity and recognise that joining cross-sectional centiles across age does not create a longitudinal velocity reference;
5. distinguish descriptive growth references from prescriptive growth standards;
6. explain the separate contributions of Tanner-Whitehouse growth references and Tanner-Whitehouse skeletal-maturity methods;
7. recognise that UK-WHO chart products combine more than one source model rather than representing one WHO dataset from birth to 18 years;
8. distinguish a reference epoch from a publication, product launch, recommendation, adoption, revision, manufacture date, and digital implementation;
9. explain that changing the source model can change a displayed centile without changing the child's measurement; and
10. treat centiles and thresholds as prompts for contextual clinical assessment rather than stand-alone diagnoses.

## Non-Goals

The section will not:

- provide diagnosis, referral thresholds, treatment recommendations, or a substitute for current RCPCH guidance;
- describe every anthropometric survey, cohort, specialist condition, or commercial chart;
- present a European and North American lineage as a universal global history;
- imply that the 50th centile is a target or that a historical average defines health;
- imply a simple progression in which every new chart entirely replaced its predecessor;
- use `release` as shorthand for publication, recommendation, adoption, revision, manufacture, or software deployment;
- conflate Tanner-Whitehouse height, weight, and velocity references with TW1, TW2, or TW3 skeletal-maturity scoring;
- reproduce protected charts, figures, archive scans, photographs, logos, or radiographs without an item-level reuse basis; or
- infer current software behaviour from historical papers.

## Proposed Information Architecture

A multi-page section is preferred because the history serves several distinct user tasks:

1. **History of growth charts** - a concise landing page with the central thesis, a milestones table, and the `Measurement -> Model -> Interface -> Interpretation` framework.
2. **From one child to population references** - Montbeillard and Buffon, Quetelet, Galton, Bowditch, Boas, infant welfare, and the distinction between cross-sectional and longitudinal evidence.
3. **Tanner-Whitehouse and growth through puberty** - distance, velocity, tempo, the Harpenden Growth Study, the 1966 and 1976 chart publications, and a separate skeletal-maturity explainer.
4. **Modern chart lineages** - NCHS, UK90, CDC, WHO, UK-WHO composite products, specialist references, and paperless charting.
5. **Evidence-based timeline** - a complete static chronology, optionally enhanced by filters.
6. **How to read chart provenance** - a practical checklist connecting the history to current references and digital implementations.
7. **Sources, credits, and permissions** - bibliography, image credits, review state, and corrections route.

If the first release must be one page, these items should become ordered H2 sections with a contents list. Each milestone should follow the pattern **Then / What changed / Why it matters now** and carry a visible track label: `Measurement`, `Model`, `Interface`, `Policy`, or `Digital`.

## Editorial Invariants

- A date is meaningful only when paired with a date kind.
- Observation, plotting, publication, launch, recommendation, adoption, revision, manufacture, and software implementation are separate events unless evidence explicitly proves otherwise.
- Historical titles must be quoted accurately, but explanatory text should apply the modern distinction between growth references and growth standards.
- Historical fact and present-day interpretation must be visibly distinct.
- A DOI proves a publication identity and date, not clinical adoption.
- `UK 1990` identifies a reference epoch or target date, not a 1990 publication or launch.
- `British children, 1965` in the Tanner-Whitehouse-Takaishi title is not the papers' 1966 publication date.
- The WHO 2006 Child Growth Standards and WHO 2007 5-19 growth reference are different products with different methods and meanings.
- Digital implementation of an existing model does not create a new growth reference or standard.
- Claims of `first`, `introduced`, `adopted`, `current`, and `superseded` require a stated scope and source.

## Timeline Record Model

Each timeline event should be maintained as structured data or equivalent consistently formatted content with these fields:

| Field | Requirement |
|---|---|
| `claim_id` | Stable, never-reused editorial identifier. |
| `display_date` | Most precise defensible date or range. |
| `date_start`, `date_end` | Machine-sortable values where known; unknown components must not be invented. |
| `date_precision` | `day`, `month`, `year`, `range`, or `approximate-period`. |
| `date_kind` | `observation-period`, `reference-epoch`, `publication`, `release`, `recommendation`, `adoption`, `revision`, `manufacture`, `commissioning`, `development`, `deployment`, or `communication`. |
| `event_type` | One or more of `measurement`, `growth-reference`, `growth-standard`, `statistical-method`, `chart-product`, `policy`, `specialist-reference`, or `digital-implementation`. |
| `geography` | Named jurisdiction or `international`; use nation-specific adoption where rollout differed. |
| `population_and_age` | Population, selection, age or gestational range, and represented sex categories. |
| `study_design` | `individual-longitudinal`, `cohort-longitudinal`, `cross-sectional`, `mixed`, `reconstruction`, or `not-applicable`. |
| `underlying_data` | Named source-data lineage, including composite source bands. |
| `what_changed` | Concise factual description. |
| `why_it_matters` | Clinician-facing interpretation, clearly distinguished from historical fact. |
| `confidence` | `high`, `medium`, or `provisional`, with a rationale. |
| `publication_status` | `ready` or `review-required`. |
| `sources` | At least one authoritative source; prefer a primary source plus a synthesis or current authority. |
| `review` | Historical, clinical, rights, and accessibility reviewer and date fields where applicable. |

## Candidate Core Timeline

This chronology is the baseline for authoring, not final publication copy. `Ready` means the date and event type have authoritative support but still require normal editorial and clinical review. `Review required` means the uncertainty stated in the entry must remain visible until resolved.

| Date | Event and date meaning | Publication status; confidence | Core sources |
|---|---|---|---|
| 1759-1776 | Gueneau de Montbeillard repeatedly measured his son's height from birth to age 17 years 7 months. This is an observation period, not publication of a graph or population reference. | Ready; high | [Buffon 1777, pp. 376-382](https://archive.org/details/histoirenaturel41buff); [Cole 2012](https://doi.org/10.3109/03014460.2012.694475); [Miller 2018](https://doi.org/10.1002/ajpa.23426) |
| 1777 | Buffon published Montbeillard's measurements as a table with commentary. The familiar curve was not printed in this volume. | Ready; high | [Buffon scan](https://gallica.bnf.fr/ark:/12148/bpt6k10705425) |
| 1832 | Quetelet published cross-sectional heights and weights across ages and developed population-average thinking. | Ready; high | [Royal Academy of Belgium catalogue](https://academieroyale.be/fr/publications-academie-toutes-publications-detail/oeuvres-2/recherches-sur-le-poids-de-lhomme-aux-differents-ages/); [Sandler 2021](https://doi.org/10.1016/j.ssmph.2021.100865) |
| 1875 | Galton published percentile grades and ranking by cumulative distribution. His statistical contribution must be presented beside its eugenic context. | Ready; high | [Galton primary scan](https://pdf.galton.org/essays/1870-1879/galton-1875-intercomparison.pdf); [Cole 2012](https://pmc.ncbi.nlm.nih.gov/articles/PMC3920659/) |
| 1875-1883 | The British Association Anthropometric Committee collected and reported measurements from a large but uneven and incomplete set of returns organised through national, occupational, classed, and racialised categories. | Ready; high | [Final report, 1883](https://pdf.galton.org/essays/1880-1889/galton-1883-rba-anthro-report-final.pdf) |
| 1877 | Bowditch published cross-sectional Boston schoolchild height and weight observations. Each child was measured once. | Ready; high | [Bowditch 1877](https://archive.org/details/b22279647) |
| 1891 | Bowditch reanalysed the Boston observations using percentile grades. Plate 8 is a forerunner of modern age-by-measurement centile charts, not an unqualified `first ever growth chart`. | Ready; high | [NLM catalogue and public-domain scan](https://collections.nlm.nih.gov/catalog/nlm:nlmuid-101485029-bk); [NLM scan](https://resource.nlm.nih.gov/101485029) |
| 1892 | Boas criticised inference about individual growth from cross-sectional age groups and argued for repeated measurement. | Ready; high | [Boas primary text](https://archive.org/stream/jstor-1764956/1764956_djvu.txt) |
| 1890s-1905 | Infant-welfare services in France and British milk depots embedded repeated weighing and weight curves into follow-up. This was distributed practice, not one national launch. | Ready; medium | [Weaver 2010](https://doi.org/10.1353/bhm.0.0315) |
| 1927 | Scammon plotted Montbeillard's tabulated individual record. Later paired distance-and-velocity figures are later representations again. | Ready; high | [Scammon 1927](https://doi.org/10.1002/ajpa.1330100303); [Miller 2018](https://doi.org/10.1002/ajpa.23426) |
| 1929 | The Fels Longitudinal Study began repeated measurement from at or near birth. | Ready; high | [Fels collection history](https://medicine.wright.edu/population-and-public-health-sciences/fels-longitudinal-study-collection) |
| 1948; measurements 1949-1969 | The Harpenden Growth Study was established in 1948 and repeatedly measured a socially and ethnically narrow institutional cohort from 1949 in exceptional detail. | Ready; high | [Cole 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7391859/) |
| October 1966 | Tanner, Whitehouse, and Takaishi published Part I of `Standards from birth to maturity ... British children, 1965`. | Ready; high | [Part I](https://doi.org/10.1136/adc.41.219.454) |
| December 1966 | Tanner, Whitehouse, and Takaishi published Part II, including the companion velocity reference material. | Ready; high | [Part II](https://doi.org/10.1136/adc.41.220.613) |
| March 1976 | Tanner and Whitehouse published clinical longitudinal charts, including tempo-specific velocity centiles, using the same underlying data as the British 1965 references. | Ready; high | [Tanner and Whitehouse 1976](https://doi.org/10.1136/adc.51.3.170) |
| 1 November 1977 | NCHS published growth curves from birth to 18 years, later used in the former NCHS/WHO reference and WHO 2007 reconstruction. | Ready; high | [CDC Stacks](https://stacks.cdc.gov/view/cdc/12687) |
| 1992 | Cole and Green published the LMS method for modelling age-varying skewness, median, and spread. This is a method publication, not a chart launch. | Ready; high | [Cole and Green 1992](https://doi.org/10.1002/sim.4780111005) |
| 5 March 1994 | Cole published `Do growth chart centiles need a face lift?`, proposing nine curves spaced by two-thirds of an SDS. This was a design proposal, not a new dataset, guideline, or outcomes study. | Ready; high | [BMJ DOI](https://doi.org/10.1136/bmj.308.6929.641); [lawful full text in PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC2539730/); [UCL copy](https://discovery.ucl.ac.uk/id/eprint/3682/) |
| July 1995 | The principal UK90 stature and weight reference paper was published. `1990` is the reference date, not publication or adoption. | Ready; high | [Stature and weight](https://doi.org/10.1136/adc.73.1.17) |
| July 1995 | The separate UK90 BMI reference paper was published. | Ready; high | [BMI](https://doi.org/10.1136/adc.73.1.25) |
| Mid-1990s | UK90 charts entered UK clinical practice, but an exact national introduction date has not been established. | Review required; medium | [Wright et al. 2002](https://doi.org/10.1136/adc.86.1.11) |
| 28 February 1998 | Revised maximum-penalised-likelihood LMS centiles consolidated the UK90 reference family. This was a method revision, not a new population or adoption event. | Ready; high | [Cole, Freeman, and Preece 1998](https://doi.org/10.1002/%28SICI%291097-0258%2819980228%2917%3A4%3C407%3A%3AAID-SIM742%3E3.0.CO%3B2-L) |
| 30 May 2000 | CDC released the 2000 US Growth Charts, a descriptive US reference and chart set. | Ready; high | [CDC data and release history](https://www.cdc.gov/growthcharts/cdc-data-files.htm) |
| August 2002 | The UK and Republic of Ireland Down syndrome growth-reference paper was published. | Ready; high | [Styles et al. 2002](https://doi.org/10.1136/adc.87.2.104) |
| 27 April 2006 | WHO released the prescriptive Child Growth Standards for birth to five years. | Ready; high | [WHO release](https://www.who.int/news/item/27-04-2006-world-health-organization-releases-new-child-growth-standards) |
| September 2007 | WHO published its 5-19 growth reference, reconstructed from NCHS 1977 data and supplemented near age five with WHO under-five data. | Ready; high | [WHO 5-19 reference](https://www.who.int/tools/growth-reference-data-for-5to19-years); [de Onis et al. 2007](https://doi.org/10.2471/BLT.07.043497) |
| 15 September 2007 | SACN and RCPCH published recommendations on applying WHO standards in the UK. This was a recommendation, not adoption. | Ready; high | [GOV.UK record](https://www.gov.uk/government/publications/sacn-application-of-who-growth-standards-in-the-uk) |
| 11 May 2009 | England introduced the composite UK-WHO 0-4 charts for babies born from this date. The product uses reanalysed UK90 birth and preterm data and WHO 2006 standards from two weeks to four years. | Ready; high | [Scottish Government CEL 35 (2009)](https://www.publications.scot.nhs.uk/files/cel2009-35.pdf); [GOV.UK guidance](https://www.gov.uk/government/publications/using-the-new-uk-world-health-organization-0-4-years-growth-charts); [current source mapping](../docs/clinician/growth-references.md) |
| 1 January 2010 | Scotland implemented WHO charts in its new Personal Child Health Record. | Ready; high | [Scottish Government CEL 49 (2009)](https://www.publications.scot.nhs.uk/files/cel2009-49.pdf) |
| January 2010 | Wales adopted the early-years charts; the primary implementation instrument still needs retrieval. | Review required; medium | [UCL REF impact record](https://impact.ref.ac.uk/casestudies/CaseStudy.aspx?Id=41839) |
| October 2010 | Northern Ireland adopted the early-years charts; the primary implementation instrument still needs retrieval. | Review required; medium | [UCL REF impact record](https://impact.ref.ac.uk/casestudies/CaseStudy.aspx?Id=41839) |
| 2011 | RCPCH and DSMIG revised and reissued UK Down syndrome charts using the existing dataset in a format aligned with UK-WHO and UK90 presentation. | Ready; high | [RCPCH chart page](https://www.rcpch.ac.uk/resources/uk-who-growth-charts-down-syndrome-0-18-years); [DSMIG history](https://www.dsmig.org.uk/information-resources/growth-charts/) |
| May 2012 | Extended UK-WHO and UK90 school-age products were launched to age 18. The 2-18 product includes a UK90 birth scale, WHO 2006 from ages 2-4, and UK90 thereafter. | Ready; medium | [RCPCH 2-18 chart](https://www.rcpch.ac.uk/sites/default/files/Boys_2-18_years_growth_chart.pdf); [UCL REF impact record](https://impact.ref.ac.uk/casestudies/CaseStudy.aspx?Id=41839) |
| 4 January 2013 | The current UK 2-18 issue 2 artefact records this manufacture date. It is not the May 2012 chart-family launch date. | Ready; high | [RCPCH 2-18 chart](https://www.rcpch.ac.uk/sites/default/files/Boys_2-18_years_growth_chart.pdf) |
| January 2013 | RCPCH identifies the UK-WHO 0-4 product as second edition. This is edition metadata, not adoption or the family launch. | Ready; high | [RCPCH 0-4 product](https://www.rcpch.ac.uk/resources/uk-who-growth-charts-0-4-years) |
| Early 2020 | NHS commissioning of the RCPCH Digital Growth Charts minimum viable product occurred in this approximate period. This is not a production launch or adoption date. | Ready; high | [Project history](../docs/about/about.md) |
| May 2020 | Development work on RCPCH Digital Growth Charts began. This is not a production launch or a new reference. | Ready; high | [Project history](../docs/about/about.md) |
| 2022 | The UK Down syndrome reference was added to RCPCH Digital Growth Charts. | Ready; medium | [DSMIG history](https://www.dsmig.org.uk/information-resources/growth-charts/) |
| 2023 | The paperless-age review was published online. This is a publication milestone, not a product release. | Ready; high | [Wright, Chapman, and Cole](https://doi.org/10.1136/archdischild-2023-325363) |
| 1 February 2024 | The paperless-age review appeared in the February 2024 journal issue. This is the issue-publication date for the same article, not a product release. | Ready; high | [PubMed](https://pubmed.ncbi.nlm.nih.gov/37463736/) |

Optional context may include the 1985 Turner syndrome reference, Fenton preterm references, INTERGROWTH-21st newborn-size standards, and later international Down syndrome charts. They should appear in a secondary specialist or international lane and must not be implied to be routine UK adoption. Size at birth and postnatal growth must remain distinct.

## Montbeillard And Bowditch Source Treatment

The local presentation `2023.11.10 RCPCH dGC Platform @ BCS PHCSG Annual Conference.odp` is evidence of how this history was communicated at the 2023 conference and a useful lead to primary material. It is not final historical authority and does not establish image-reuse rights.

The public history must not repeat the shorthand `first ever growth chart` without qualification:

- **Montbeillard and Buffon:** describe an early sustained longitudinal record of one child's height, observed from 1759 to 1776 and published as a table by Buffon in 1777. Scammon plotted the record in 1927. The familiar paired distance-and-velocity reproduction is later again.
- **Bowditch:** distinguish the cross-sectional Boston school observations published in 1877 from the percentile analysis and chart forms published in 1891. Plate 8 may be called a forerunner of most modern growth charts, but the source data were not longitudinal.

The presentation's slide 6 image is a low-resolution, unattributed modern graphic with no recoverable reuse basis and must not be republished. Replace it with an original reconstruction from Buffon's table after independent transcription and calculation checks.

The slide 7 image is recognisable as Bowditch's Plate 8 but should be replaced by a new high-resolution crop from the [National Library of Medicine public-domain object](https://resource.nlm.nih.gov/101485029), retaining its heading, legend, catalogue identity, and required institutional credit.

## Tanner-Whitehouse Treatment

Tanner-Whitehouse requires a dedicated two-branch explanation.

### Growth-reference branch

First use should identify **the Tanner-Whitehouse-Takaishi British 1965 height, weight, and velocity standards, published in two parts in 1966**, followed by **the Tanner-Whitehouse 1976 clinical longitudinal charts**. Modern explanatory text should call the 1966 product a descriptive British growth reference while preserving `Standards` in the historical title.

The section should explain attained size, velocity, early or average or late pubertal tempo, and why unsynchronised pubertal spurts flatten a cross-sectional average. It should credit the Harpenden Growth Study's unusually detailed repeated measurements without presenting its selected institutional cohort as nationally representative or as the sole basis of every 1966 curve.

### Skeletal-maturity branch

TW1, TW2, and TW3 should be reserved for the separate skeletal-maturity systems. The explanatory sequence is:

`hand and wrist radiograph -> staged bones -> skeletal maturity score -> reference-specific bone age or adult-height prediction`

The history must not imply that TW methods are current advice to order radiographs. Exact TW1 and TW2 manual-edition dates remain review-required pending inspection of authoritative title pages or publisher records.

## Required Terminology

The published content should define and consistently distinguish:

- measurement and serial measurement;
- attained size or distance and growth velocity;
- growth monitoring and screening;
- growth reference and growth standard;
- growth chart and underlying source model;
- centile and standard deviation score or z-score;
- cross-sectional and longitudinal study designs;
- conditional reference;
- growth tempo;
- skeletal maturity score and bone age;
- secular trend;
- reference epoch;
- chart revision or edition; and
- digital implementation.

Historical sex categories should be described as variables in the original datasets without implying that historical binary categorisation resolves current inclusive-care requirements. Final wording requires clinical and equality or inclusion review.

## Ethical And Social Context

Ethical history must be integrated alongside the methods it shaped rather than placed in a detached disclaimer.

- Galton's statistical contribution must be presented beside his eugenic programme.
- Historical reference populations should be described as constructed and selected, with geography, collection period, recruitment setting, socioeconomic and institutional selection, categories used by the source, and missing voices identified where evidence permits.
- The page should acknowledge that measurement has served care and public health, but also administration, labour regulation, surveillance, commerce, colonial power, and racialised classification.
- Harmful historical terminology should appear only where necessary for accurate quotation or interpretation, with attribution and context.
- The Harpenden cohort consisted of children in institutional care. The absence of located consent or ethics records must be reported as an evidence gap rather than converted into an assertion.
- Identifiable participant photographs, unclothed or puberty-stage images, and historical radiographs are excluded unless exceptional educational need, lawful reuse, ethics review, and documented consent or provenance are established.

## Visual Requirements

The first release should favour original explanatory graphics over portraits or copied chart pages:

1. `measurement -> selected population and data -> statistical model -> chart interface -> clinical interpretation`;
2. individual serial measurement compared with cross-sectional and cohort-longitudinal data;
3. an original Montbeillard attained-height and velocity reconstruction from Buffon's table;
4. a rights-recorded Bowditch Plate 8 reproduction or an original redraw;
5. a Tanner-Whitehouse tempo schematic showing early, average, and late pubertal peaks;
6. a schematic separating Tanner-Whitehouse growth charts from TW skeletal-maturity scoring;
7. an original nine-line SDS or centile explainer for Cole's 1994 proposal;
8. a UK-WHO source-band diagram showing the model transitions by age;
9. a lineage diagram separating dataset, reference or standard, chart product, policy adoption, and digital implementation; and
10. a text or table equivalent for every graphic.

The Montbeillard reconstruction must record source rows, historical-unit conversion, observation intervals, velocity calculations, rounding, omissions, and independent verification. It must be captioned as a modern reconstruction from measurements published in 1777, not as an eighteenth-century graph.

Every visual needs a stable ID, visible credit, concise alt text, adjacent takeaway, detailed description or data table, and a claim-data ledger recording every encoded fact and transformation.

## Timeline Interaction And Accessibility

The static HTML must contain the complete chronology in linear DOM order. Filters for geography or track may progressively enhance it but must not contain the only copy of any event.

- Use semantic headings and an ordered list or article sequence.
- Express date kind, event type, confidence, and status in text, not only through colour, icon, position, or line style.
- Keep real HTML text for dates, labels, and captions; transcribe facsimile text nearby.
- Do not use tabs, carousels, parallax, auto-scrolling, hover-only detail, or scroll-triggered animation for essential content.
- Preserve chronological keyboard order and visible focus.
- Collapse to one column on mobile and remove decorative rails where necessary.
- Reflow without page-level horizontal scrolling at 320 CSS pixels and 400% zoom.
- Respect reduced-motion preferences.
- Produce a complete, linear, readable PDF representation.
- Meet WCAG 2.2 AA for the new content and components without implying a changed whole-site conformance claim.

Manual validation should include keyboard-only use, CSS disabled, JavaScript disabled, mobile and tablet layouts, 320 CSS pixels, 400% zoom, text and meaningful non-text contrast, target sizing, print and PDF, NVDA with Firefox or Chrome, JAWS with Chrome or Edge, and VoiceOver with Safari. User testing should include at least one screen-reader user, one magnification or reflow user, one keyboard-only user, and clinicians scanning under time pressure.

## Evidence And Rights Controls

### Source hierarchy

1. Original papers, datasets, contemporaneous policy or release records, archive catalogues, and chart artefacts establish what happened and when.
2. Peer-reviewed historical syntheses explain connections and help identify primary sources.
3. Current RCPCH, WHO, CDC, UK government, and W3C guidance establishes current product lineage, terminology, policy, rights, and accessibility.
4. University, museum, archive, and specialist-society interpretation may provide bounded institutional context.
5. Popular histories, search snippets, and unattributed reposts are discovery leads only.

Each significant claim should have a stable claim ID and at least one primary source where available. The source record should include the citation, DOI or catalogue ID, full-text route, evidence tier, claims supported, exact pages or sections reviewed, reviewer and date, licence or reuse status, and access date for mutable pages.

### Cole 1994

The bibliographic facts and attributed design proposal in [Cole's 1994 BMJ article](https://doi.org/10.1136/bmj.308.6929.641) are ready for drafting. The lawful [PubMed Central full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC2539730/) and [UCL copy](https://discovery.ucl.ac.uk/id/eprint/3682/) permit review but do not establish a blanket reuse licence.

The section must not claim that the article introduced a new dataset, established outcome benefit, supplied current universal policy, or alone caused subsequent UK chart revisions. Direct quotation, figure reproduction, or body-level causal interpretation requires a recorded full-text and rights review.

### Asset-rights ledger

Before design work begins, every proposed third-party asset must record:

- filename, title, creator, and date;
- holding institution, collection, and item ID;
- canonical catalogue and source-file URLs;
- copyright owner and licence or rights statement;
- permitted transformations and required credit;
- permission correspondence and expiry where applicable;
- allowed web, PDF, and print uses;
- alt text, transcription, and long description; and
- reviewer and review date.

Public web access, inclusion in PubMed Central, age of the underlying work, or prior use in an RCPCH presentation does not by itself establish permission. Prefer original SVG or HTML explanations with fully documented source data. Link rather than embed where rights remain uncertain.

## Open Questions

| ID | Question or evidence gap | Publication effect |
|---|---|---|
| HG-01 | Confirm that the intended scope is UK lineage with selected international context rather than a global history. | Blocks final title and scope wording. |
| HG-02 | Select the canonical Buffon scan and independently verify table transcription, historical-unit conversion, intervals, velocity calculations, and rounding. | Blocks the Montbeillard reconstruction, not the prose history. |
| HG-03 | Verify whether Roberts's 1876 child data warrant a core milestone from the primary publication. | Keep out of the core timeline meanwhile. |
| HG-04 | Decide whether Bayer and Bayley's 1959 distance and velocity chart belongs in the core timeline after primary review. | Keep in a secondary lane meanwhile. |
| HG-05 | Extract source datasets, sample sizes, dates, and weighting for each Tanner-Whitehouse 1966 age segment. | Blocks a detailed population table. |
| HG-06 | Verify TW1 and TW2 manual and edition chronology from title pages or publisher catalogues. | Blocks exact skeletal-method timeline dates. |
| HG-07 | Determine whether consent and ethics records survive for the Harpenden Growth Study. | Do not infer consent status; exclude participant imagery. |
| HG-08 | Find the national introduction mechanism and exact adoption period for UK90 charts. | Publish only `mid-1990s`. |
| HG-09 | Retrieve primary Welsh and Northern Irish UK-WHO implementation records. | Retain month-level qualified entries. |
| HG-10 | Distinguish current chart issue or edition numbers from printed manufacture dates. | Use precise artefact wording only. |
| HG-11 | Decide which event should anchor the Digital Growth Charts product history: commissioning, first code release, production deployment, first NHS integration, or medical-device registration. | Do not invent a general launch date. |
| HG-12 | Agree wording for historical sex variables and current inclusive clinical practice. | Blocks final glossary and relevant captions. |
| HG-13 | Select a clinically safe explanatory scenario showing how reference choice changes a displayed centile. | No patient-like scenario before clinical review. |
| HG-14 | Confirm which historical assets justify their rights and ethics costs. | Default to original schematics. |
| HG-15 | Prototype the timeline and complex figures in the pinned Zensical version and generated PDF. | Blocks bespoke interaction. |
| HG-16 | Name historical, clinical, rights, equality or inclusion, and accessibility reviewers. | Blocks publication. |
| HG-17 | Record page-level review of Cole 1994 and any proposed quotations or causal claims. | Attributed design-proposal summary may proceed. |
| HG-18 | Identify and review the exact Tanner 1962 object containing the later paired Montbeillard distance and velocity reproduction. | Do not reuse or assign a precise timeline date yet. |

## Acceptance Criteria

### Scope And Content

- [ ] The published section states its UK-lineage scope and does not claim global completeness.
- [ ] The content delivers the clinician learning outcomes and links rather than duplicates current clinical guidance.
- [ ] The narrative uses the `Measurement -> Model -> Interface -> Interpretation` frame rather than a portrait-led inventor sequence.
- [ ] Historical content cannot be mistaken for current diagnostic or referral guidance.
- [ ] The section contains a complete static timeline with stable claim IDs.

### Historical Accuracy

- [ ] Every event records date precision, date kind, event type, geography, source lineage, confidence, publication status, and sources.
- [ ] Montbeillard's observations, Buffon's table, Scammon's graph, and later reproductions remain separate objects.
- [ ] Bowditch's 1877 survey and 1891 percentile-chart publication remain separate, and the source data are correctly described as cross-sectional.
- [ ] `British children, 1965`, UK90, WHO 2006, WHO 2007, and the four-nation UK-WHO rollout are not collapsed into misleading dates.
- [ ] Cole 1994 appears as an attributed chart-design proposal with DOI `10.1136/bmj.308.6929.641`, not as a new dataset, guideline, or outcomes study.
- [ ] Provisional claims retain visible uncertainty and a stated evidence task.

### Tanner-Whitehouse And Terminology

- [ ] Tanner-Whitehouse growth references and TW skeletal-maturity methods are presented as separate branches.
- [ ] Harpenden is described as an important intensive longitudinal study but not a nationally representative cohort or the sole source of all 1966 curves.
- [ ] Attained size, velocity, tempo, skeletal maturity score, and bone age are clearly distinguished.
- [ ] Historical uses of `standard` are quoted accurately and explained using modern terminology.

### Ethics, Rights, And Accessibility

- [ ] Eugenics, classed and racialised categorisation, institutional selection, surveillance, and missing participant voices are integrated beside the relevant methods.
- [ ] No identifiable, intimate, radiographic, or institution-derived child image is included without exceptional rights, ethics, and provenance clearance.
- [ ] The presentation's unattributed Montbeillard image is not reused.
- [ ] Any Bowditch Plate 8 reproduction is newly sourced from the NLM object and records its catalogue provenance and transformations.
- [ ] Every visual has an asset-rights record, claim-data ledger, credit, alt text, adjacent takeaway, and detailed text or table equivalent.
- [ ] The chronology remains complete without CSS or JavaScript, works by keyboard, reflows at 320 CSS pixels and 400% zoom, and produces a linear PDF.
- [ ] Contrast and target sizing are verified, named assistive-technology and browser combinations are recorded, and testing includes screen-reader, magnification or reflow, keyboard-only, and clinician participants.
- [ ] Historical, clinical, rights, equality or inclusion, and accessibility review are recorded before publication.

## Core Bibliography

- Bowditch HP. *The Growth of Children*. Boston; 1877. [Primary scan](https://archive.org/details/b22279647).
- Bowditch HP. *The Growth of Children: Studied by Galton's Method of Percentile Grades*. 1891. [NLM catalogue and scan](https://collections.nlm.nih.gov/catalog/nlm:nlmuid-101485029-bk).
- Buffon G-L Leclerc, Comte de. *Histoire naturelle, generale et particuliere, servant de suite a l'Histoire naturelle de l'homme*, supplement 4. 1777:376-382. [Primary scan](https://archive.org/details/histoirenaturel41buff).
- Cole TJ. The development of growth references and growth charts. *Annals of Human Biology*. 2012;39(5):382-394. [DOI 10.3109/03014460.2012.694475](https://doi.org/10.3109/03014460.2012.694475). [Full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC3920659/).
- Cole TJ. Do growth chart centiles need a face lift? *BMJ*. 1994;308(6929):641-642. [DOI 10.1136/bmj.308.6929.641](https://doi.org/10.1136/bmj.308.6929.641). [Full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC2539730/).
- Cole TJ, Green PJ. Smoothing reference centile curves: the LMS method and penalized likelihood. *Statistics in Medicine*. 1992;11:1305-1319. [DOI 10.1002/sim.4780111005](https://doi.org/10.1002/sim.4780111005).
- Freeman JV, Cole TJ, Chinn S, Jones PRM, White EM, Preece MA. Cross-sectional stature and weight reference curves for the UK, 1990. *Archives of Disease in Childhood*. 1995;73(1):17-24. [DOI 10.1136/adc.73.1.17](https://doi.org/10.1136/adc.73.1.17).
- Miller EM. The first Seriatum study of growth by R. E. Scammon. *American Journal of Physical Anthropology*. 2018;165(3):415-420. [DOI 10.1002/ajpa.23426](https://doi.org/10.1002/ajpa.23426).
- Sandler AD. The rise and fall of the normal child: Growth assessment and the historical construction of normality. *SSM - Population Health*. 2021;15:100865. [DOI 10.1016/j.ssmph.2021.100865](https://doi.org/10.1016/j.ssmph.2021.100865).
- Tanner JM, Whitehouse RH, Takaishi M. Standards from birth to maturity for height, weight, height velocity, and weight velocity: British children, 1965. I and II. *Archives of Disease in Childhood*. 1966. [Part I](https://doi.org/10.1136/adc.41.219.454). [Part II](https://doi.org/10.1136/adc.41.220.613).
- Tanner JM, Whitehouse RH. Clinical longitudinal standards for height, weight, height velocity, weight velocity, and stages of puberty. *Archives of Disease in Childhood*. 1976;51(3):170-179. [DOI 10.1136/adc.51.3.170](https://doi.org/10.1136/adc.51.3.170).
- Weaver LT. In the balance: weighing babies and the birth of the infant welfare clinic. *Bulletin of the History of Medicine*. 2010;84(1):30-57. [DOI 10.1353/bhm.0.0315](https://doi.org/10.1353/bhm.0.0315).
- WHO. [Child Growth Standards](https://www.who.int/tools/child-growth-standards).
- WHO. [Growth reference data for 5-19 years](https://www.who.int/tools/growth-reference-data-for-5to19-years).
- Wright CM, Chapman S, Cole TJ. How can we best chart children's growth in the paperless age? The UK experience. *Archives of Disease in Childhood*. 2024;109(2):78-82. [DOI 10.1136/archdischild-2023-325363](https://doi.org/10.1136/archdischild-2023-325363).

The implementation bibliography should preserve complete citations, identifiers, exact pages reviewed, evidence tier, access date, and rights status rather than relying only on this selected list.
