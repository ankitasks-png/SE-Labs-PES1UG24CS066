# Lab 3 — Component Identification

## Patient Health Record Consent Management System

The system is designed using a Microservices Architecture. The following five components are identified based on the responsibilities of the patient, clinic administrator, consent management, health-record access, and audit requirements.

| Component | Responsibility |
|---|---|
| Patient Portal Component | Allows patients to view their health records and manage consent permissions. |
| Consent Management Component | Creates, updates, and revokes time-bound consent permissions. |
| Health Record Access Component | Verifies active consent and provides authorized access to medical records. |
| Clinic Administrator Component | Allows verified clinic personnel to request and access patient health records according to granted permissions. |
| Audit Trail Component | Records consent grants, revocations, and health-record access events in an append-only audit trail. |
