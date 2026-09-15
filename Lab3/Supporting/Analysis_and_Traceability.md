# Analysis and Traceability

## Patient Health Record Consent Management System

### Requirements to Architecture Traceability

| Requirement / Concern | Architectural Response | Component |
|---|---|---|
| Patients manage consent | Presentation and business logic separation | Patient Portal + Consent Management |
| Time-bound consent | Consent validation before access | Consent Management |
| Authorized record access | Consent verification | Health Record Access |
| Clinic record requests | Controlled presentation interface | Clinic Access |
| Consent grant/revoke logging | Append-only audit trail | Audit Trail |
| Security of health records | Business-layer authorization | Consent Management |
| Maintainability | Separation of layers | All components |

### Architecture

**Selected:** Layered Architecture

### Layers

1. **Presentation Layer**
   - Patient Portal Component
   - Clinic Access Component

2. **Business Logic Layer**
   - Consent Management Component

3. **Data Layer**
   - Health Record Access Component
   - Audit Trail Component

### Component Count

Exactly **5 components**.

### Interface Count

Exactly **4 interfaces**.

### Actors

- Patient
- Clinic Administrator

### Verification Points

- Consent must be validated before record access.
- Expired consent must not permit access.
- Consent grant and revoke events must be recorded.
- Components must remain within the defined five-component scope.
