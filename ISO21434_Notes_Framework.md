# ISO/SAE 21434 Study Notes & Interpretation

## 📌 Overview
**Goal:** Map the cybersecurity engineering requirements to my existing Quality Management (QM) experience.
**Status:** In Progress 🚧

## 🟢 Clause 5: Organizational Cybersecurity Management
> **My Insight:** This is the foundation. Without Clause 5, you cannot pass a UN R155 Audit. It maps directly to existing Quality Management Systems.

### 1. Cybersecurity Governance
* **Policy:** The organization must have a specific policy for cybersecurity, approved by top management. It's not just "IT's problem", it's a Board-level issue.
* **Roles:** Distinct roles must be defined.
    * *Example:* A "Cybersecurity Manager" must have the authority to stop a release if security requirements aren't met (Independence of authority).

### 2. Cybersecurity Culture
* This is a favorite topic for German auditors (TÜV).
* **Key Question:** "How do you ensure every engineer cares about security?"
* **Evidence:** Training records, awareness newsletters, clear escalation channels for reporting vulnerabilities.

### 3. Management of the CSMS (Audit Ready)
* **Process Definition:** You must have written procedures for TARA, Testing, and Incident Response.
* **Tool Management:** If you use tools (like my Python scripts or Jira), they must be managed and validated.

### 🎯 Connection to My CQM Experience
* **IATF 16949 Analogy:** Just like we have a "Quality Manual", we need a "Cybersecurity Manual".
* **Action Item:** When auditing a supplier, ask for their "Cybersecurity Policy" first. If they don't have one, they fail Clause 5 immediately.

## 🟡 Clause 15: Distributed Cybersecurity Activities (Supplier Management)
> *Critical for Tier-1s.* This connects directly to UN R155 requirements for supply chain management.

* **CIAD (Cybersecurity Interface Agreement for Development):** * What it is: The "contract" between OEM and Supplier regarding security.
    * *My Template Idea:* Create a CIAD generator using Python.
* **Supplier Capability Check:** How to audit a software supplier?

## 🔴 Clause 8: Risk Assessment Methods (TARA)
> *The Core Engine.* This is where I am building the AI Agent.

* **Asset Identification:** What are we protecting? (e.g., Cryptographic Keys, User Privacy).
* **Threat Scenarios:** * *Example:* Attacker spoofs CAN bus message to unlock door.
* **Impact Rating (SFOP):**
    * S: Safety (ISO 26262 link)
    * F: Financial
    * O: Operational
    * P: Privacy (GDPR link)
* **Attack Path Analysis:** [TODO: Upload my threat tree diagram here]

## 📝 Integration with Quality (My Insights)
* **Gate Reviews:** Cybersecurity checks must be added to existing APQP Gates.
* **Traceability:** Requirements -> TARA -> Testing (Must be linked, just like V-Model).
