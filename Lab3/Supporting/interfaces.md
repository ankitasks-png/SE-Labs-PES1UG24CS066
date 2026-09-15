# Lab 3 — Component Interfaces

## Patient Health Record Consent Management System

The following four interfaces define the interactions between the five system components.

| Interface | Components | Interaction |
|---|---|---|
| Consent Management Interface | Patient Portal ↔ Consent Management | Grant, view, and revoke patient consent permissions. |
| Record Access Interface | Clinic Administrator ↔ Health Record Access | Request authorized access to patient health records. |
| Consent Verification Interface | Health Record Access ↔ Consent Management | Verify whether valid and non-expired consent exists before providing records. |
| Consent Audit Interface | Consent Management ↔ Audit Trail | Record consent grant and revoke events in the audit trail. |
