# Lab 3 — Architecture Analysis

## Patient Health Record Consent Management System

### 1. Layered Architecture

**Structure:**  
The system can be organized into Presentation, Business Logic, and Data Access layers.

**Pros:**
- Clear separation of concerns.
- Easy to understand and maintain.
- Suitable for a structured healthcare application.

**Cons:**
- Requests may need to pass through multiple layers.
- Changes in one layer can affect dependent layers.
- Scaling individual functionality can be difficult.

**Suitability:**  
Suitable because the system has clear user-interface, consent-management, and data-storage responsibilities. However, strict layer traversal may introduce unnecessary overhead for time-sensitive consent verification.

---

### 2. Microservices Architecture

**Structure:**  
The system can be divided into independently deployable services such as Consent Management, Patient Records, Authentication, Audit Logging, and Access Control.

**Pros:**
- Independent scaling of services.
- Fault isolation between services.
- Individual services can be developed and deployed independently.
- Suitable for separating security-sensitive healthcare functions.

**Cons:**
- Higher operational complexity.
- Network communication can introduce latency.
- Maintaining consistency across services can be challenging.

**Suitability:**  
Highly suitable for a healthcare system because consent management, authentication, health-record access, and audit logging can be isolated into separate services. However, it may be more complex than necessary for a small-scale academic implementation.

---

### 3. Client-Server Architecture

**Structure:**  
Patients and clinic administrators act as clients that communicate with a centralized server containing the application's business logic and data.

**Pros:**
- Centralized control of patient consent and health-record access.
- Simple deployment and management.
- Easier to maintain consistent consent and access data.

**Cons:**
- The centralized server can become a single point of failure.
- The server can become a scalability bottleneck.
- Limited fault tolerance compared with distributed architectures.

**Suitability:**  
Suitable for a centralized patient health-record system because consent permissions and health-record data can be controlled from one server. However, the centralized architecture may create availability and scalability concerns as usage increases.

---

## Comparison

| Architecture | Main Advantage | Main Disadvantage | Suitability |
|---|---|---|---|
| Layered | Clear separation of concerns | Layer traversal overhead | High |
| Microservices | Scalability and fault isolation | Operational complexity | Very High |
| Client-Server | Centralized control | Single point of failure | High |
