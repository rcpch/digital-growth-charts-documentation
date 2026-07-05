# Quality Management System Manual

**Organisation:** Royal College of Paediatrics and Child Health (RCPCH)  
**Product scope:** RCPCH Digital Growth Charts (and any additional SaMD under RCPCH manufacture)  
**Standard:** ISO 13485:2016  
**UK regulatory framework:** UK MDR 2002 (as amended)  
**QMS version:** 1.0.0  
**Status:** Draft for management review  
**Owner:** Marcus Baw (Clinical Safety Officer / PRRC)  
**Last reviewed:** <!-- ISO date -->  
**Next review due:** <!-- ISO date, max 12 months from last review -->  

---

## 1. Purpose and Scope

This document is the Quality Manual for the RCPCH's medical device software activities. It describes the Quality Management System (QMS) maintained for the design, development, release, and post-market surveillance of Software as a Medical Device (SaMD) products under RCPCH manufacture.

The QMS is implemented primarily through Git-based version control (GitHub), supplemented by structured processes documented here. This manual maps each ISO 13485:2016 clause to the corresponding GitHub location, process, or record type, so that the entire QMS can be navigated from a single document.

**In scope:** All SaMD products registered with the MHRA under RCPCH as manufacturer, including the RCPCH Digital Growth Charts API and associated client implementations.

**Out of scope:** Non-software medical devices; activities of third parties using RCPCH open-source code under licence (they assume manufacturer responsibilities independently).

---

## 2. Normative References

| Standard | Application |
|---|---|
| ISO 13485:2016 | Quality management systems for medical devices |
| ISO 14971:2019 | Risk management for medical devices |
| IEC 62304:2006+AMD1:2015 | Software lifecycle processes for medical device software |
| IEC 62366-1:2015 | Usability engineering for medical devices |
| UK MDR 2002 (SI 2002/618, as amended) | UK regulatory framework |
| MHRA guidance on SaMD classification | Device classification |

---

## 3. Terms and Definitions

**Repository:** The canonical GitHub repository for a given product. All controlled documents, source code, issue records, and release artefacts reside here unless otherwise specified.

**Controlled document:** Any document subject to version control and approval workflow under this QMS. All controlled documents live in Git; the commit history constitutes the change record.

**Issue:** A GitHub Issue used as the formal record for complaints, CAPAs, design inputs, hazards, change requests, audit findings, or management review actions.

**PR (Pull Request):** The formal mechanism for proposing and approving changes to controlled documents or source code. Required reviewers constitute the approval record.

**Release:** A tagged Git commit constituting a formal software release, accompanied by a release note and updated technical documentation.

**PRRC:** Person Responsible for Regulatory Compliance (see Section 5.4).

**CSO:** Clinical Safety Officer.

---

## 4. Repository Structure

The QMS is distributed across the following GitHub locations. All are under version control; commit history provides the audit trail.

| Location | Contents |
|---|---|
| `github.com/rcpch/digital-growth-charts-server` | Primary product repository — source code, technical documentation, release history |
| `github.com/rcpch/digital-growth-charts-server/issues` | Complaints, CAPAs, design inputs, change requests, hazards, audit findings |
| `github.com/rcpch/digital-growth-charts-server/projects` | Design and development tracking; management review action tracking |
| `SAFETY.md` (repo root) | Clinical safety anchor document |
| `SAFETY-CASE.md` (repo root) | Clinical safety case |
| `HAZARD-LOG.md` (repo root) | ISO 14971 hazard log |
| `QMS.md` (repo root) | This document — quality manual |
| `docs/technical-file/` | Technical documentation (regulatory) |
| `docs/clinical-evaluation/` | Clinical Evaluation Report and supporting literature |
| `docs/post-market-surveillance/` | PMS plan, periodic safety update reports, trend analysis |
| `docs/supplier-register.md` | Approved supplier register |
| `docs/training-records/` | Staff qualification and training records |
| `docs/audits/` | Internal audit plans, reports, and findings |
| `docs/management-review/` | Management review minutes and action records |

---

## 5. Management Responsibilities

### 5.1 Quality Policy

The RCPCH is committed to developing and maintaining SaMD that is clinically safe, effective, and fit for purpose. Quality is achieved through transparent, open development practices; rigorous clinical safety management; and continuous improvement informed by real-world performance data and user feedback.

The quality policy is reviewed at each management review meeting (see Section 5.6).

### 5.2 Quality Objectives

Quality objectives are set and reviewed at management review. Current objectives are tracked as GitHub Issues labelled `quality-objective` in the management review Project.

Minimum objectives:
- Zero unmitigated high or unacceptable risks in the Hazard Log at any release
- All serious incidents reported to MHRA within required timelines
- Management review conducted at least annually
- Internal audit conducted at least annually
- All CAPA actions closed within agreed timescales

### 5.3 Organisational Roles

| Role | Responsibility | Current postholder |
|---|---|---|
| PRRC / CSO | Overall regulatory compliance; DCB0129 clinical safety officer; ISO 14971 risk management ownership; MHRA liaison | Marcus Baw |
| Technical Lead | IEC 62304 software lifecycle; release management; security | <!-- name --> |
| Clinical Lead | Clinical evaluation; usability; intended use definition | <!-- name --> |
| QMS Administrator | Document control; audit scheduling; training records | <!-- name --> |

### 5.4 Person Responsible for Regulatory Compliance (PRRC)

Under UK MDR 2002, the PRRC is responsible for ensuring:
- Technical documentation is prepared and kept up to date
- Post-market surveillance obligations are fulfilled
- Reporting obligations (vigilance, PSUR) are met
- The Declaration of Conformity is accurate

The PRRC is Marcus Baw. Contact: marcus@bawmedical.co.uk

### 5.5 Resource Management

Staff involved in regulated activities must have documented qualifications relevant to their role. Records are maintained in `docs/training-records/`, with one file per person, recording:
- Role and responsibilities
- Relevant qualifications and experience
- Training completed (with dates and evidence)
- Competency assessments (where applicable)

New starters with regulated responsibilities must complete onboarding before acting independently on any regulated task. Onboarding checklist is at `docs/training-records/onboarding-checklist.md`.

### 5.6 Management Review

Management review is conducted at least **annually**, or following any significant quality event (serious incident, major CAPA, significant regulatory change).

**Process:**
1. QMS Administrator opens a GitHub Issue using the `management-review` template at least 4 weeks in advance
2. Review agenda is attached to the Issue
3. Review is conducted (in person or remote); minutes are recorded
4. Minutes and action items are committed to `docs/management-review/YYYY-MM-DD-management-review.md`
5. Action items are created as linked GitHub Issues and tracked to closure

**Mandatory agenda items:**
- Quality policy review
- Quality objectives — status and adequacy
- Audit findings and status of corrective actions
- CAPA log review
- Complaints and feedback summary
- Post-market surveillance data summary
- Regulatory changes affecting the QMS
- Resource adequacy
- Actions from previous review — closure status

**GitHub label:** `management-review`  
**Record location:** `docs/management-review/`

---

## 6. Document and Record Control

### 6.1 Controlled Documents

All controlled documents are maintained in Git. The following rules apply:

- Documents reside in the repository at a defined path (see Section 4)
- Changes to controlled documents are made via Pull Request
- PRs require at least one approving review from a person with appropriate authority (defined by the CODEOWNERS file)
- Commit messages for controlled document changes must reference the reason for change
- Documents must not be force-pushed or history-rewritten after approval

The Git commit history constitutes the complete change log for every controlled document. No separate change log table is required within documents themselves, as this would create a duplicate record.

### 6.2 External Documents

Externally-sourced documents (standards, MHRA guidance, published clinical literature) are referenced by URL or DOI. Specific versions used in clinical evaluations or risk assessments are recorded at the point of use. External documents are not stored in the repository.

### 6.3 Records

Quality records are created and maintained in GitHub Issues and committed documents. Records must not be deleted. Closed Issues remain accessible. Repository history must not be rewritten.

Retention: all quality records are retained indefinitely in the GitHub repository. In the event of a platform migration, records are exported and maintained in the successor platform.

---

## 7. Design and Development

Design and development activities follow IEC 62304 software lifecycle processes. The software safety class is determined at project initiation and recorded in the technical file.

### 7.1 Design Planning

Each significant development effort (new feature, major change, new product) begins with a design input Issue using the `design-input` template. This records:
- Clinical or user need driving the change
- Intended functionality
- Relevant regulatory implications (classification, risk management, clinical evaluation impact)
- Acceptance criteria

Design planning is tracked in GitHub Projects.

### 7.2 Design Inputs

Design inputs are formal requirements derived from clinical need, user research, regulatory requirements, and risk management outputs. Each design input is a GitHub Issue labelled `design-input`.

Design inputs must be:
- Unambiguous and verifiable
- Traceable to the clinical or user need
- Reviewed and approved (PR or Issue comment from Technical Lead and Clinical Lead)

### 7.3 Design Outputs

Design outputs are the artefacts that satisfy design inputs: source code, API specifications, configuration files, documentation. The traceability between design inputs and outputs is maintained through Issue and PR cross-references.

A release is a formal design output. The release notes must reference the design input Issues addressed.

### 7.4 Design Review

Design reviews are conducted at:
- Feature specification stage (before development begins)
- Pre-release (before a tagged release)

Design reviews are recorded as comments on the relevant Issue or PR, with explicit sign-off from the Technical Lead and Clinical Lead.

### 7.5 Design Verification

Verification demonstrates that design outputs meet design inputs. For SaMD this means:
- Automated test suite (unit, integration, regression) — results recorded in CI/CD pipeline
- Code review — PR review comments constitute the verification record
- Clinical algorithm validation — results recorded in `docs/technical-file/verification/`

All verification must pass before a release is tagged.

### 7.6 Design Validation

Validation demonstrates that the device meets user needs in its intended environment. Methods include:
- Clinical user testing (usability evaluation under IEC 62366-1)
- Real-world performance monitoring (post-market)
- Clinical expert review

Validation records are in `docs/technical-file/validation/`.

### 7.7 Design Transfer

Release process (transfer to production) is documented in `docs/technical-file/release-process.md`. It includes:
- Pre-release checklist (all verification passed; Hazard Log reviewed; SAFETY.md version updated; release notes complete)
- Deployment steps
- Post-deployment smoke test
- Rollback procedure

### 7.8 Design Changes

All changes to controlled source code or documentation are made via Pull Request. For changes with potential regulatory significance (intended use, safety-relevant functionality, clinical algorithm), the PR must:
- Reference a design input Issue
- Include an assessment of the impact on risk management and clinical evaluation
- Be approved by the PRRC in addition to the Technical Lead

---

## 8. Risk Management

Risk management follows **ISO 14971:2019** throughout the product lifecycle.

**Risk management file:** `HAZARD-LOG.md` contains the structured hazard log. `SAFETY-CASE.md` contains the safety argument. `SAFETY.md` is the root anchor.

The risk management process is:

1. **Hazard identification** — conducted at design input stage and reviewed at every release. Sources: clinical expert review, user feedback, incident reports, literature, comparable device analysis
2. **Risk estimation** — severity (1–5) and likelihood (1–5) per DCB0129 scales, recorded in `HAZARD-LOG.md` YAML frontmatter
3. **Risk evaluation** — risk acceptability determined by risk matrix; unacceptable risks block release
4. **Risk control** — controls documented in `HAZARD-LOG.md`; implementation verified in code/documentation
5. **Residual risk assessment** — post-control severity and likelihood recorded; benefit-risk analysis in `SAFETY-CASE.md`
6. **Risk management review** — mandatory at each release; PRRC sign-off required

No release may proceed with unmitigated risks rated `high` or `unacceptable` without explicit PRRC and Clinical Lead documented justification.

---

## 9. Purchasing and Supplier Management

Suppliers whose products or services could affect device quality are assessed and monitored. The approved supplier register is at `docs/supplier-register.md`.

For SaMD, relevant suppliers include:
- Cloud infrastructure provider (hosting, availability)
- CI/CD platform
- Third-party libraries with safety-relevant functions (algorithm dependencies)
- Clinical data sources (reference datasets)

Each entry in the supplier register records: supplier name, service/product, criticality classification, last assessment date, assessment outcome, and monitoring approach.

Critical suppliers (those where failure could affect device safety or availability) are reviewed annually and at the management review.

---

## 10. Complaints and Post-Market Surveillance

### 10.1 Complaint Handling

A complaint is any expression of dissatisfaction with the device or any report of a potential safety issue, regardless of source.

**Process:**
1. Complaint received (GitHub Issue, email, user report, clinical incident)
2. QMS Administrator opens a GitHub Issue using the `complaint` template within 2 working days
3. Initial assessment: is this a reportable serious incident? (see Section 10.3)
4. Investigation conducted; root cause documented in Issue
5. CAPA raised if required (see Section 10.2)
6. Response to complainant (if identified)
7. Issue closed with resolution documented

**GitHub label:** `complaint`

### 10.2 Corrective and Preventive Action (CAPA)

A CAPA is raised in response to:
- Confirmed complaints indicating a systemic issue
- Audit findings
- Non-conformities identified in internal review
- Serious incidents
- Trend analysis indicating adverse signal

**CAPA record (GitHub Issue using `capa` template) must contain:**
- Description of the non-conformity or potential non-conformity
- Root cause analysis
- Corrective action (what will be done to fix the current problem)
- Preventive action (what will be done to prevent recurrence)
- Implementation owner and due date
- Verification of effectiveness (how will we know it worked, and by when)

CAPAs are reviewed at management review. Open CAPAs with overdue actions are escalated to the PRRC.

**GitHub label:** `capa`

### 10.3 Vigilance — Serious Incident Reporting

A serious incident is any malfunction or deterioration in characteristics or performance, or any inadequacy in labelling or instructions for use, which has led or could lead to:
- Death
- Serious deterioration in health
- Serious public health threat

Serious incidents must be reported to the MHRA. Timelines:
- Serious public health threat: **2 calendar days**
- Death or unanticipated serious deterioration in health: **10 calendar days**
- Other serious incidents: **30 calendar days**

The PRRC is responsible for MHRA reporting. All incidents are recorded as GitHub Issues labelled `serious-incident` and cross-referenced to the MHRA report reference number once submitted.

### 10.4 Post-Market Surveillance (PMS)

The PMS plan is at `docs/post-market-surveillance/pms-plan.md`. It describes:
- Data sources monitored (user feedback, GitHub Issues, clinical incident reports, published literature, comparable device data)
- Monitoring frequency
- Trend analysis methodology
- Triggers for CAPA or risk management review

A **Periodic Safety Update Report (PSUR)** is produced at least annually and committed to `docs/post-market-surveillance/YYYY-psur.md`. The PSUR covers:
- Summary of PMS data collected
- Conclusions on safety and performance
- Any benefit-risk ratio changes
- Actions taken or planned

---

## 11. Internal Audit

Internal audits are conducted at least **annually** to verify that the QMS conforms to ISO 13485:2016 and is effectively implemented.

**Process:**
1. QMS Administrator opens a GitHub Issue using the `internal-audit` template at least 6 weeks in advance
2. Audit scope and plan committed to `docs/audits/YYYY-audit-plan.md`
3. Audit conducted; auditor must be independent of the area being audited
4. Findings recorded as GitHub Issues labelled `audit-finding`
5. Audit report committed to `docs/audits/YYYY-audit-report.md`
6. Non-conformities trigger CAPAs (see Section 10.2)
7. Audit closure confirmed when all findings are resolved

**GitHub label:** `internal-audit`, `audit-finding`  
**Record location:** `docs/audits/`

---

## 12. Non-conformity and Corrective Action

Non-conformities identified outside the complaint and audit process (e.g. during development review, supplier assessment, or management review) are recorded as GitHub Issues labelled `non-conformity` and handled via the CAPA process (Section 10.2).

---

## 13. GitHub Issue Templates

The following Issue templates must be maintained in `.github/ISSUE_TEMPLATE/` to support this QMS:

| Template file | Purpose | Required fields |
|---|---|---|
| `complaint.md` | Complaint intake | Source, description, date received, initial severity assessment |
| `capa.md` | CAPA record | Non-conformity description, root cause, corrective action, preventive action, owner, due date, verification method |
| `design-input.md` | Design input | Clinical/user need, functional requirement, acceptance criteria, regulatory impact |
| `serious-incident.md` | Serious incident | Date, description, patient impact, reportability assessment, MHRA reference |
| `internal-audit.md` | Audit planning | Scope, planned date, auditor, clauses to be covered |
| `audit-finding.md` | Audit finding | Clause reference, finding description, evidence, classification (major/minor/observation) |
| `management-review.md` | Management review | Date, attendees, agenda items, decisions, actions |
| `hazard.md` | New hazard | Hazard description, cause, effect, initial risk estimate, proposed controls |

---

## 14. GitHub Labels

The following labels must be maintained in the repository to support QMS process tracking:

| Label | Colour (suggested) | Purpose |
|---|---|---|
| `complaint` | Red | Complaint records |
| `capa` | Orange | CAPA records |
| `serious-incident` | Dark red | Serious incident records |
| `audit-finding` | Yellow | Audit finding records |
| `internal-audit` | Yellow | Audit planning records |
| `management-review` | Blue | Management review records |
| `design-input` | Green | Design input records |
| `non-conformity` | Orange | Non-conformity records |
| `quality-objective` | Blue | Quality objective tracking |
| `pms` | Purple | Post-market surveillance observations |
| `regulatory` | Purple | Regulatory change tracking |

---

## 15. Branch Protection and Approval Workflow

The following branch protection rules must be configured on the main branch to enforce document control:

- Require pull request reviews before merging: **minimum 1 approving review**
- For changes to `SAFETY.md`, `SAFETY-CASE.md`, `HAZARD-LOG.md`, `QMS.md`, or any file in `docs/technical-file/` or `docs/clinical-evaluation/`: require review from **Code Owner** (PRRC)
- Dismiss stale reviews when new commits are pushed
- Require status checks to pass (CI/CD pipeline)
- Do not allow force pushes
- Do not allow branch deletion

A `CODEOWNERS` file must be maintained at the repository root specifying the PRRC as required reviewer for regulated documents.

Example `CODEOWNERS` entry:
```
SAFETY.md @pacharanero
SAFETY-CASE.md @pacharanero
HAZARD-LOG.md @pacharanero
QMS.md @pacharanero
docs/technical-file/ @pacharanero
docs/clinical-evaluation/ @pacharanero
```

---

## 16. QMS Review and Improvement

This document is a controlled document under this QMS. Changes are made via Pull Request with PRRC approval.

The QMS is reviewed:
- At each management review
- Following any significant regulatory change
- Following any internal audit finding relating to the QMS itself
- When a new product is brought into scope

Version history is the Git commit history of this file.

---

## Appendix A — ISO 13485:2016 Clause Mapping

| ISO 13485 Clause | Title | Evidence location |
|---|---|---|
| 4.1 | General QMS requirements | This document |
| 4.2.1 | Documentation requirements — general | Section 6, this document |
| 4.2.2 | Quality manual | This document |
| 4.2.3 | Medical device file | `docs/technical-file/` |
| 4.2.4 | Document control | Section 6, branch protection rules |
| 4.2.5 | Record control | GitHub Issues, commit history |
| 5.1 | Management commitment | Section 5.1 |
| 5.2 | Customer focus | Section 10, PMS plan |
| 5.3 | Quality policy | Section 5.1 |
| 5.4 | Planning | Section 5.2, management review records |
| 5.5 | Responsibility, authority, communication | Section 5.3 |
| 5.6 | Management review | Section 5.6, `docs/management-review/` |
| 6.1 | Resource provision | Section 5.5 |
| 6.2 | Human resources | `docs/training-records/` |
| 6.3 | Infrastructure | `docs/supplier-register.md` (infrastructure suppliers) |
| 6.4 | Work environment | Not applicable (software only) |
| 7.1 | Planning of product realisation | Section 7.1 |
| 7.2 | Customer-related processes | Section 7.2, design inputs |
| 7.3 | Design and development | Section 7 |
| 7.4 | Purchasing | Section 9, `docs/supplier-register.md` |
| 7.5 | Production and service provision | IEC 62304 lifecycle, release process |
| 7.6 | Control of monitoring and measuring equipment | Not applicable (software only) |
| 8.1 | Measurement, analysis, improvement | Sections 10–12 |
| 8.2.1 | Feedback | Section 10.1, PMS plan |
| 8.2.2 | Complaints handling | Section 10.1 |
| 8.2.3 | Reporting to regulatory authorities | Section 10.3 |
| 8.2.4 | Internal audit | Section 11 |
| 8.2.6 | Monitoring and measurement of product | Section 10.4, PSUR |
| 8.3 | Control of nonconforming product | Section 12 |
| 8.4 | Analysis of data | Section 10.4, management review |
| 8.5 | Improvement — CAPA | Section 10.2 |

---

## Appendix B — Scheduled QMS Activities

| Activity | Frequency | Owner | GitHub trigger |
|---|---|---|---|
| Management review | Annual (minimum) | PRRC | Recurring Issue, January |
| Internal audit | Annual (minimum) | QMS Administrator | Recurring Issue, October |
| PSUR | Annual | PRRC | Recurring Issue, on release anniversary |
| Supplier review | Annual | QMS Administrator | Recurring Issue, January |
| Quality objectives review | At management review | PRRC | Management review agenda |
| Hazard log review | At each release | PRRC | Pre-release checklist |
| PMS data review | Quarterly | QMS Administrator | Recurring Issue |
