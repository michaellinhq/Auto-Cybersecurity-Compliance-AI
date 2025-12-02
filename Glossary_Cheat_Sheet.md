# 📚 ISO/SAE 21434 & UN R155 Vocabulary Cheat Sheet

> **Purpose:** Quick reference for the most critical terms in Automotive Cybersecurity.
> **Target Audience:** Certification Exams (Level 1) & Customer Interviews.

## 🔹 Core Concepts (TARA)

| Term | Definition (Simplified) | Example |
| :--- | :--- | :--- |
| **Asset** | Something of value that needs protection. | Cryptographic keys, User privacy data, Braking function. |
| **Threat Scenario** | A potential cause of an unwanted incident. | "Attacker spoofs CAN message to stop braking." |
| **Damage Scenario** | The adverse consequence to the road user. | "Collision with vehicle in front due to loss of braking." |
| **Impact Rating** | The severity of the damage (SFOP). | **S**afety (Severe), **F**inancial (Major), **O**perational, **P**rivacy. |
| **Attack Path** | The steps an attacker takes to realize a threat. | Bluetooth -> Infotainment -> Gateway -> CAN Bus -> Brake ECU. |
| **Attack Feasibility** | How hard is it to attack? (Based on Time, Expertise, Equipment, Window of opportunity). | **High** (Easy to hack), **Low** (Hard to hack). |
| **Risk Value** | Combination of **Impact** and **Feasibility**. | Critical (1) to Negligible (5). |

## 🔹 Management Terms (The "CQM" Language)

| Term | Definition | Connection to Quality |
| :--- | :--- | :--- |
| **CSMS** | **C**yber**s**ecurity **M**anagement **S**ystem. The "Rules & Processes". | Equivalent to QMS in IATF 16949. Mandatory for UN R155. |
| **SUMS** | **S**oftware **U**pdate **M**anagement **S**ystem. | Managing OTA updates (UN R156). |
| **Distributed Activities** | Managing Suppliers (Tier 1/2). | Supply Chain Quality Management (Clause 15). |
| **CIAD** | **C**ybersecurity **I**nterface **A**greement for **D**evelopment. | The "Contract" defining who does what security task. |
| **Post-Development** | Production, Operations, Maintenance, Decommissioning. | What happens after SOP (Start of Production). |

## 🔹 Tech Acronyms

* **TARA:** Threat Analysis and Risk Assessment (The heart of ISO 21434).
* **OTA:** Over-The-Air (Wireless updates).
* **V-Model:** The standard development lifecycle (Design on left, Test on right).
* **PSIRT:** Product Security Incident Response Team (The firefighters).
