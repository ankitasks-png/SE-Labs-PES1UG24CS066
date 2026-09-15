# Lab 3 — Architecture Selection

## Patient Health Record Consent Management System

### Selected Architecture: Microservices Architecture

The selected architecture for the Patient Health Record Consent Management System is **Microservices Architecture**.

### Reason 1 — Security and Isolation

The system handles sensitive patient health records and consent permissions. Microservices allow security-sensitive responsibilities such as consent management, authentication, health-record access, and audit logging to be separated into independent services. This provides better isolation between critical functions and helps restrict access to only the required service.

### Reason 2 — Scalability and Fault Isolation

The system may receive different levels of demand for consent management and health-record access. Microservices allow individual services to scale independently. Fault isolation also helps prevent a failure in one service from affecting the entire system.

### Security Advantage

Microservices can isolate access-control and consent-management functionality from other parts of the system. This supports enforcing authorization before a clinic or doctor can access a patient's records and helps protect sensitive health information.

### Performance Benefit

Individual services can be independently scaled according to demand. Consent verification can therefore be handled by a dedicated service, helping the system respond efficiently when multiple access requests occur.

### Conclusion

Microservices Architecture is selected because it provides strong service isolation, scalability, and fault isolation, which are appropriate for a patient-centric healthcare system that requires controlled access to sensitive health records.
