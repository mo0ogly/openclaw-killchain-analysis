# Operation OpenClaw — Kill Chain Analysis of an AI Agent-Driven Cyberattack

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Status: Active Research](https://img.shields.io/badge/Status-Active%20Research-orange.svg)]()
[![Language: EN / FR](https://img.shields.io/badge/Language-EN%20%2F%20FR-blue.svg)]()

<p align="center">
  <img src="figures/openclaw_operation.png" alt="Operation OpenClaw — Kill Chain Overview" width="700"/>
</p>

> **This repository is an active research project. Documents are updated regularly. See the [CHANGELOG](CHANGELOG.md) for corrections.**

---

## Quick Access — No Git Required

**You don't need to install anything.** Click any link below to read or download the documents directly in your browser.

### Start Here

| Document | FR | EN |
|----------|----|----|
| **Summary note** (~10 pages) | [Note academique (PDF)](ACADEMIC_NOTE.pdf) | [Academic note (PDF)](ACADEMIC_NOTE_en.pdf) |
| **Summary note** (markdown) | [NOTE_ACADEMIQUE.md](NOTE_ACADEMIQUE.md) | [ACADEMIC_NOTE.md](ACADEMIC_NOTE.md) |
| **Master 2 course** — AI & Cybersecurity introduction for non-specialists | [Cours M2 Sorbonne (FR v6 PDF)](S1-ISI5_IA_et_Cybersecurite%20v6.pdf) | [M2 Course Sorbonne (EN v6 PDF)](S1-ISI5_IA_et_Cybersecurite%20v6_en.pdf) |

### Detailed Phase Analyses (~25-30 pages each)

| Phase | Title | FR (Report) | EN (Report) | FR (Infographie) | EN (Infographic) |
|-------|-------|-------------|-------------|------------------|------------------|
| **1** | Reconnaissance | [PDF](phases/Phase1_Reconnaissance.pdf) | [PDF](phases/Phase1_Reconnaissance_en.pdf) | [SVG](figures/phase1_infographic.svg) | [SVG](figures/phase1_infographic_en.svg) |
| **2** | Weaponization | [PDF](phases/Phase2_Weaponization.pdf) | [PDF](phases/Phase2_Weaponization_EN.pdf) | [SVG](figures/phase2_infographic.svg) | [SVG](figures/phase2_infographic_en.svg) |
| **3** | Delivery & Exploitation | [PDF](phases/Phase3_Installation_Exécution.pdf) | [PDF](phases/Phase3_Installation_Execution_EN.pdf) | [SVG](figures/phase3_infographic.svg) | [SVG](figures/phase3_infographic_en.svg) |
| **4** | Lateral Movement & Persistence | [PDF](phases/Phase4_Mouvement_Latéral_Persistance.pdf) | [PDF](phases/Phase4_Lateral_Movement_Persistence_EN.pdf) | [SVG](figures/phase4_infographic.svg) | [SVG](figures/phase4_infographic_en.svg) |
| **5** | Exfiltration & Double Extortion | [PDF](phases/Phase5_PromptLock_Exfiltration-RD_Double%20Extorsion.pdf) | [PDF](phases/Phase5_PromptLock_Exfiltration_Double_Extortion_EN.pdf) | [SVG](figures/phase5_infographic.svg) | [SVG](figures/phase5_infographic_en.svg) |

### Download Everything

> **[Download all files as ZIP](https://github.com/mo0ogly/openclaw-killchain-analysis/archive/refs/heads/main.zip)** — one click, no Git needed.

---

## Reading Guide

| Time available | Start here |
|---------------|-----------|
| **5 min** | This README + [key figures](#key-figures) below |
| **20 min** | Summary note: [FR (PDF)](ACADEMIC_NOTE.pdf) / [EN (PDF)](ACADEMIC_NOTE_en.pdf) |
| **1 hour** | Summary note + one phase of your choice (see table above) |
| **Full study** | All 5 phases in order |
| **New to AI security?** | Start with the [Master 2 course (FR v6)](S1-ISI5_IA_et_Cybersecurite%20v6.pdf) / [(EN v6)](S1-ISI5_IA_et_Cybersecurite%20v6_en.pdf) |

---

## Abstract

This repository presents a **comprehensive threat model of a fictional multi-phase cyberattack** exploiting an autonomous AI coding agent (OpenClaw) as both attack vector and force multiplier against a mid-size pharmaceutical company. The study models a complete **agentic kill chain spanning 36 days**, from LLM-augmented OSINT reconnaissance through supply chain compromise, lateral movement via AI agent impersonation, to ransomware deployment and double extortion.

All vulnerabilities, tools and techniques are documented in the public literature (February 2026).

**Key findings:**
- **13 of 14 MITRE ATT&CK Enterprise tactics** are covered across the five phases
- **Phase 4 (lateral movement) — not Phase 5 (ransomware)** — is the technical center of gravity
- A compromised AI agent acts with **system permissions, automation speed, and natural language adaptability**
- **Foundational controls** (patching, MFA, segmentation, immutable backups) would have disrupted the majority of the kill chain
- AI-specific controls (tool allowlists, sandboxing, egress monitoring) are **complementary but not substitute** protection

A **five-layer defense-in-depth model** specific to agentic AI threats is proposed.

---

<details>
<summary><strong>Resume en francais</strong></summary>

Ce depot presente la modelisation complete d'une cyberattaque fictive multi-phases exploitant un agent IA de codage autonome (OpenClaw) comme vecteur d'attaque et multiplicateur de force contre une entreprise pharmaceutique. L'etude couvre une kill chain agentique de 36 jours, de la reconnaissance OSINT augmentee par LLM jusqu'au deploiement d'un rancongiciel et a la double extorsion. Un modele de defense en profondeur en cinq couches specifique aux menaces agentiques est propose.

La note de synthese en francais est disponible : [NOTE_ACADEMIQUE.md](NOTE_ACADEMIQUE.md) | [PDF](ACADEMIC_NOTE.pdf)

Le cours de Master 2 Sorbonne (introduction a l'IA et cybersecurite) : [v6 PDF](S1-ISI5_IA_et_Cybersecurite%20v6.pdf)

</details>

---

## The 5 Phases

| Phase | Title | Timeline | Key Findings |
|-------|-------|----------|-------------|
| **1** | [Reconnaissance](phases/Phase1_Reconnaissance_en.pdf) | D-30 to D-15 | LLM-augmented OSINT, social graph reconstruction, 40,000+ exposed OpenClaw agents via Shodan |
| **2** | [Weaponization](phases/Phase2_Weaponization_EN.pdf) | D-15 to D-7 | Malicious ClawHub skill, PromptLock ransomware (Go), prompt injection payloads, audio deepfake |
| **3** | [Delivery & Exploitation](phases/Phase3_Installation_Execution_EN.pdf) | D-7 to D | 3 simultaneous vectors: skill supply chain, infostealer (token theft per Hudson Rock), CVE-2024-55591 VPN |
| **4** | [Lateral Movement](phases/Phase4_Lateral_Movement_Persistence_EN.pdf) | D to D+5 | Shadow agent, Slack prompt injection, DCSync to Golden Ticket, PoisonGPT chatbot poisoning |
| **5** | [Actions on Objectives](phases/Phase5_PromptLock_Exfiltration_Double_Extortion_EN.pdf) | D+5 to D+6 | Full R&D exfiltration, PromptLock deployed, double extortion, 2.5M EUR ransom / 7.5M EUR est. total impact |

## Infographics / Infographies

<details>
<summary><strong>Phase 1: Reconnaissance</strong></summary>

**English**: <br><img src="figures/phase1_infographic_en.svg" width="800"/>

**Français**: <br><img src="figures/phase1_infographic.svg" width="800"/>
</details>

<details>
<summary><strong>Phase 2: Weaponization</strong></summary>

**English**: <br><img src="figures/phase2_infographic_en.svg" width="800"/>

**Français**: <br><img src="figures/phase2_infographic.svg" width="800"/>
</details>

<details>
<summary><strong>Phase 3: Delivery & Exploitation</strong></summary>

**English**: <br><img src="figures/phase3_infographic_en.svg" width="800"/>

**Français**: <br><img src="figures/phase3_infographic.svg" width="800"/>
</details>

<details>
<summary><strong>Phase 4: Lateral Movement & Persistence</strong></summary>

**English**: <br><img src="figures/phase4_infographic_en.svg" width="800"/>

**Français**: <br><img src="figures/phase4_infographic.svg" width="800"/>
</details>

<details>
<summary><strong>Phase 5: Exfiltration & Double Extortion</strong></summary>

**English**: <br><img src="figures/phase5_infographic_en.svg" width="800"/>

**Français**: <br><img src="figures/phase5_infographic.svg" width="800"/>
</details>

<details>
<summary><strong>Taxonomy of Attacks ON AI Systems (S1-ISI5)</strong></summary>

**Français**: <br><img src="figures/taxonomy_ai_attacks_fr.svg" width="800"/>
</details>

## Defense-in-Depth Model

| Layer | Principle | Key Controls |
|-------|----------|-------------|
| **C1** — Agent Governance | The LLM is an advisor, not an executor | Tool allowlists, sandbox, human-in-the-loop |
| **C2** — Input Control | All ingested content is untrusted | Data/instruction separation, need-to-know access |
| **C3** — Output Control | Legitimate HTTPS can mask logical abuse | Egress proxy by app identity, DLP, destination allowlists |
| **C4** — Impact Reduction | Compromised agent must not inherit SI-wide permissions | Segmentation, 3-2-1-1-0 backups, AD hardening |
| **C5** — Basic Hygiene | Agentic controls don't replace fundamentals | Accelerated patching, MFA, minimal exposure |

**Core insight**: Layers C4-C5 (fundamentals) would have disrupted the majority of the kill chain. Layers C1-C3 (AI-specific) are complementary, not substitute.

## Key Figures

<table>
<tr>
<td><img src="figures/fig12_trifecta_en.png" width="300"/><br/><em>Fig. 12 — Willison's Lethal Trifecta</em></td>
<td><img src="figures/fig22_mitre_heatmap_en.png" width="400"/><br/><em>Fig. 22 — MITRE ATT&CK Density Matrix</em></td>
</tr>
</table>

## Introductory Course — AI & Cybersecurity (Master 2, Sorbonne)

For readers unfamiliar with AI security concepts, a **Master 2 course from Universite Paris Sorbonne** is included as an introduction:

- [S1-ISI5 — IA et Cybersecurite (FR v6, PDF)](S1-ISI5_IA_et_Cybersecurite%20v6.pdf)
- [S1-ISI5 — AI and Cybersecurity (EN v6, PDF)](S1-ISI5_IA_et_Cybersecurite%20v6_en.pdf)

This course covers foundational concepts needed to understand the kill chain analysis and is recommended as a starting point for non-specialists.

## Repository Structure

```
openclaw-killchain-analysis/
│
├── README.md                              ← this file
├── CHANGELOG.md                           ← corrections & version history
├── LICENSE                                ← CC BY-NC-SA 4.0
│
├── ACADEMIC_NOTE.md                       ← Summary note (EN, markdown)
├── ACADEMIC_NOTE_en.pdf                   ← Summary note (EN, PDF)
├── NOTE_ACADEMIQUE.md                     ← Note de synthese (FR, markdown)
├── ACADEMIC_NOTE.pdf                      ← Note de synthese (FR, PDF)
│
├── S1-ISI5_IA_et_Cybersecurite v6.pdf     ← Master 2 course (FR) NEW
├── S1-ISI5_IA_et_Cybersecurite v6_en.pdf  ← Master 2 course (EN) NEW
│
├── phases/                                ← Detailed phase analyses (FR + EN)
│   ├── Phase1_Reconnaissance.pdf / _en.pdf
│   ├── Phase2_Weaponization.pdf / _EN.pdf
│   ├── Phase3_Installation_Execution.pdf / _EN.pdf
│   ├── Phase4_Mouvement_Lateral.pdf / _EN.pdf
│   └── Phase5_PromptLock.pdf / _EN.pdf
│
├── figures/                               ← Academic figures (EN + FR, 21 figures)
│
└── scripts/                               ← Figure generation scripts
    └── gen_figures.py
```

## Disclaimer

> **This work is an academic analysis based on an entirely fictional scenario.** PharmEurys SA does not exist. No actual attack was conducted. All vulnerabilities and techniques described are documented in the public literature. The purpose is exclusively defensive: identifying risks associated with autonomous AI agents to improve security postures.

## Citation

```bibtex
@techreport{pizzi2026openclaw,
  title     = {Operation OpenClaw: Modeling an Agentic Kill Chain Against Enterprise Infrastructure},
  author    = {Pizzi, Fabrice},
  year      = {2026},
  month     = {February},
  institution = {Universite Paris Sorbonne},
  type      = {Technical Report},
  url       = {https://github.com/mo0ogly/openclaw-killchain-analysis}
}
```

## Contact

- **Author**: Fabrice Pizzi
- **GitHub**: [@mo0ogly](https://github.com/mo0ogly)
- **LinkedIn**: https://www.linkedin.com/in/fpizzi/

## License

[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
