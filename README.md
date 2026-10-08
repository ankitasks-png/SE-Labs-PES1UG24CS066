# SE-Labs-PES1UG24CS066

## Student Information

- **Name:** Ankita S
- **SRN:** PES1UG24CS066
- **Course:** Software Engineering

## Repository Description

This repository contains the deliverables for the Software Engineering Laboratory.

Each laboratory exercise is organized into a separate directory.

## Lab 1 — Requirements Engineering & UML Use-Case Modelling

### Problem Statement

**Patient Health Record Consent Management System**

**Domain:** Healthcare & Telemedicine

**Actors:**
- Patient
- Clinic Administrator

### Lab 1 Deliverables

The Lab 1 directory contains:

1. **Requirements Table**
   - Functional Requirements: FR-001 to FR-005
   - Non-Functional Requirements: NFR-001 to NFR-002

2. **UML Use-Case Diagram**
   - Represents the interactions between the Patient, Clinic Administrator, and the Patient Health Record Consent Management System.

3. **Use-Case Flow Specification**
   - Core use case: Grant Time-Bound Consent
   - Includes preconditions, postconditions, main success scenario, and alternate flow.

### Directory Structure

```text
SE-Labs-PES1UG24CS066/
│
├── README.md
│
└── Lab1/
    ├── requirements-table.md
    ├── use-case-flow.md
    └── UML_Use_Case_Diagram.png
```

## Lab 2 — Agile Project Management using Jira

### Problem Statement

Implement Agile project management for the **Patient Health Record Consent Management System** using **Jira**. The work covers organising the backlog into epics and user stories, estimating story points, running a simulated sprint, and analysing the sprint using the board and burndown chart.

**Course Code:** UE24CS341A
**Semester / Section:** 5 / B
**Jira Project:** `Ankita S` (key: `AS`)
**Jira Workspace/Project Link:** `<<paste Jira project link here>>`

### Lab 2 Deliverables

The Lab 2 directory contains a report (`Lab2_PES1UG24CS066_B.pdf`) with the following parts:

1. **Epics & User Stories / Backlog**

   Two epics were created, each broken down into user stories:

   | Epic | Story | Key | Priority |
   |---|---|---|---|
   | Consent Management (AS-4) | Grant Time-Bound Consent | AS-6 | High |
   | Consent Management (AS-4) | Revoke Active Consent | AS-7 | High |
   | Consent Management (AS-4) | View Consent Permissions | AS-8 | Medium |
   | Healthcare Provider Access Control (AS-5) | Access Records with Active Consent | AS-9 | High |
   | Healthcare Provider Access Control (AS-5) | Verify Healthcare Providers | AS-10 | Medium |

   - **Consent Management** lets patients manage time-bound consent for their health records: granting consent to verified providers, revoking active consent, and viewing existing permissions.
   - **Healthcare Provider Access Control** covers how providers are verified and how they access records only while consent is active.
   - The core consent stories were given High priority because they are essential to the system. Supporting stories (provider verification, viewing permissions) were given Medium priority.

2. **Story Points**

   | Key | Story | Story Points |
   |---|---|---|
   | AS-6 | Grant Time-Bound Consent | 8 |
   | AS-9 | Access Records with Active Consent | 8 |
   | AS-7 | Revoke Active Consent | 5 |
   | AS-10 | Verify Healthcare Providers | 5 |
   | AS-8 | View Consent Permissions | 3 |
   | | **Total** | **29** |

3. **Active Sprint Board**

   - Sprint: **AS Sprint 2**
   - All five stories were moved from To Do → In Progress → Done. At the end of the sprint, the To Do and In Progress columns were empty and all stories were in the Done column.

4. **Burndown Chart**

   - Sprint duration: **26 Aug 2026 – 2 Sep 2026**, estimated in story points.
   - Compares the remaining work against the ideal burn-down guideline, starting at 29 points and ending at 0 once all stories were completed.

5. **Reflection Answers**

   - **Did the estimations reflect the actual effort?** Largely yes. Story points helped identify which stories were complex and which were simple, and completing the sprint helped refine the sense of effort for each type of story.
   - **Was the backlog well-prioritized?** Yes. Core consent stories (Grant, Access, Revoke) were High priority; supporting stories (Verify, View) were Medium.
   - **How did the simulated sprint align with the plan?** It mostly aligned: stories were organised by priority and all planned work was completed, showing how tasks move from planning to completion in Jira.
   - **What did the burndown chart show about capacity?** Remaining story points fell to zero, showing that the amount of work planned was manageable, and it highlighted the importance of tracking progress regularly.

### Directory Structure

```text
Lab2/
└── Lab2_PES1UG24CS066_B.pdf
```

## Lab 3 — Component Modelling & Architectural Pattern Selection

### Problem Statement

**Patient Health Record Consent Management System**

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

### Lab 3 Deliverables

The Lab 3 directory contains:

1. **Component Diagram** - in PNG and PDF formats, plus an editable `.drawio` source.
2. **Architecture Justification** - explains why Microservices Architecture was chosen (PDF and DOCX).
3. **Architecture Analysis** - analysis of the selected architecture (`architecture-analysis.md`, `architecture-selection.md`).
4. **Component and Interface Documentation** - `components.md` and `interfaces.md`.
5. **Supporting Documentation**
   - Analysis and Traceability
   - Verification Report
   - SHA-256 Checksums

### Directory Structure

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
```

## Lab 4 — Vibe Coding: Fishing Game

### Problem Statement

Use a Vibe Coding tool to inspect, fix, and extend a Python/Pygame fishing game. The original game contained a deliberate catch-detection bug and required three additional features to be implemented.

**Game Repository:** `ankitasks-png/03_fishing`

### Tasks Completed

**Task 1 — Fix the Fish Catch Detection Bug**

The original check only compared the hook's and the fish's vertical (depth) position, so a fish could be caught even when the hook was not horizontally overlapping it. Catch detection now uses Pygame rectangle collision, so a catch happens only when the hook and fish actually overlap.

```python
hook_rect = hook.get_rect()

for fish in fish_list:
    if hook_rect.colliderect(fish.get_rect()):
        return fish
```

**Task 2 — Add Multiple Fish Types** (commit `792949c`)

Two fish types were added, differing in movement speed, size, colour, and point value:

| Fish Type | Speed | Size | Points | Colour |
|---|---|---|---|---|
| `SlowFish` | 1.5 | 32 × 16 | 10 | Blue |
| `FastFish` | -4 | 44 × 22 | 25 | Orange |

Catching each type awards its own score.

**Task 3 — Player-Controlled Casting**

Casting is now controlled by the player instead of happening automatically:

- Press **Spacebar** to start a cast.
- A cast starts only when the hook is idle.
- The hook travels down and returns on reaching maximum depth or catching a fish.
- Pressing Spacebar during an active cast does not interrupt it.

```python
def start_cast(self):
    if self.hook.state == IDLE:
        self.hook.start_cast()
```

**Task 4 — 30-Second Round Timer** (commit `6974aa8`)

A round system was added with `ROUND_DURATION = 30`:

- 30-second countdown with remaining time displayed on screen
- No catches possible once the timer reaches zero
- Round-over state with a clear final score display
- Press **R** to start a new round, which resets the score, timer, fish, and hook

**Additional Fix During Task 4**

Fish were becoming invisible while the hook was casting. This was corrected so fish stay visible and keep moving during a cast, while the hook behaviour and the Task 1 catch-detection logic remained unchanged.

### Controls

| Key | Action |
|---|---|
| **Spacebar** | Start casting the hook |
| **R** | Start a new round after the round ends |
| **Close Window** | Exit the game |

### Vibe Coding Prompts Used

The prompts were entered in a separate ChatGPT conversation, one task at a time, with each prompt telling the tool to keep earlier fixes working and not to implement later tasks yet.

1. **Fix catch detection** - the hook should only catch a fish when they actually overlap, not just when they are at the same depth.
2. **Add multiple fish types** - at least two types with different speeds and point values, visually distinct, with correct points awarded; keep the Task 1 fix working.
3. **Player-controlled casting** - a key starts the cast when the hook is idle; the hook returns at maximum depth or on a catch; a new cast must not interrupt an active one.
4. **Fix fish visibility and add the round timer** - fish must stay visible and move while casting, then add a 30-second countdown, round end, final score, and a way to start a new round with score and timer reset.

### Evidence

- **Before video (10 s, original game):** `<<paste Before video link here>>`
- **After video (10 s, completed Tasks 1-4):** `<<paste After video link here>>`
- **Chat history (ChatGPT):** `<<paste ChatGPT conversation link here>>`
- **Commits:** separate commits were made for each task, including `792949c` (Task 2) and `6974aa8` (Task 4).

### Project Setup

**Requirements:** Python 3.10+ and Pygame.

```bash
pip install -r requirements.txt
python main.py
```

### Directory Structure

```text
Lab4_Fishing_VibeCoding/
└── README.md
```

## Complete Repository Structure

```text
SE-Labs-PES1UG24CS066/
│
├── README.md
├── SE-Labs-PES1UG24CS066.pdf
│
├── Lab1/
│   ├── requirements-table.md
│   ├── use-case-flow.md
│   └── UML_Use_Case_Diagram.png
│
├── Lab2/
│   └── Lab2_PES1UG24CS066_B.pdf
│
├── Lab3/
│   ├── Supporting/
│   │   ├── Analysis_and_Traceability.md
│   │   ├── SHA256SUMS.txt
│   │   ├── VERIFICATION_REPORT.md
│   │   ├── Architecture_Justification.docx
│   │   ├── Architecture_Justification.pdf
│   │   ├── README.md
│   │   ├── Patient_Health_Record_Component_Diagram.drawio
│   │   ├── Patient_Health_Record_Component_Diagram.png
│   │   └── Patient_Health_Record_Component_Diagram.pdf
│   ├── architecture-analysis.md
│   ├── architecture-selection.md
│   ├── components.md
│   └── interfaces.md
│
└── Lab4_Fishing_VibeCoding/
    └── README.md
```
