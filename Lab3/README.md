# Lab 3 — Component Modelling & Architectural Pattern Selection

## Patient Health Record Consent Management System

### Problem Statement

A patient-centric electronic health data gateway where patients explicitly manage granular, time-bound consent permissions for clinics, diagnostic labs, and consulting doctors to access their medical history.

### Selected Architecture

**Microservices Architecture**

The architecture was selected because the system requires secure handling of sensitive health information, controlled consent management, service isolation, scalability, and fault isolation.

### Components

The system contains exactly five components:

1. **Patient Portal Component**
   - Allows patients to view health records and manage consent permissions.

2. **Consent Management Component**
   - Creates, updates, and revokes time-bound consent permissions.

3. **Health Record Access Component**
   - Verifies active consent and provides authorized access to medical records.

4. **Clinic Access Component**
   - Handles requests from verified clinic personnel for patient health-record access.

5. **Audit Trail Component**
   - Records consent grants, revocations, and health-record access events.

### Interfaces

Exactly four interfaces are represented in the component diagram:

1. **Consent Management Interface**
   - Patient Portal ↔ Consent Management

2. **Record Access Interface**
   - Clinic Access ↔ Health Record Access

3. **Consent Verification Interface**
   - Health Record Access ↔ Consent Management

4. **Consent Audit Interface**
   - Consent Management ↔ Audit Trail

### Deliverables

- Component Diagram — PNG
- Component Diagram — PDF
- Editable Component Diagram — `.drawio`
- Architecture Justification — PDF
- Architecture Analysis
- Supporting Documentation
- Verification Report
- SHA-256 Checksums

### Repository Structure

```text
Lab3/
├── Supporting/
│   ├── Analysis_and_Traceability.md
│   ├── SHA256SUMS.txt
│   ├── VERIFICATION_REPORT.md
│   ├── Architecture_Justification.docx
│   ├── Architecture_Justification.pdf
│   ├── README.md
│   ├── Patient_Health_Record_Component_Diagram.drawio
│   ├── Patient_Health_Record_Component_Diagram.png
│   └── Patient_Health_Record_Component_Diagram.pdf
│
├── architecture-analysis.md
├── architecture-selection.md
├── components.md
└── interfaces.md
