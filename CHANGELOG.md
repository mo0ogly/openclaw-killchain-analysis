# Changelog — Operation OpenClaw Analysis

All notable changes to this project will be documented in this file.

## [v7.1] — 2026-02-23

### UI/UX "Modern Threat Intel" Upgrade
- **Premium Aesthetics**: Upgraded `docs/index.html` with a modern "Glassmorphism" design, subtle radial background gradients, and sleek Neon Glow hover effects.
- **Typography & Animations**: Integrated Google Fonts (Inter, JetBrains Mono) and added smooth fade-in and slide-up CSS animations for a highly professional reading experience.

## [v7.0] — 2026-02-22

### Documentation & UI Improvements
- **Media Presentation**: Integrated 6 podcast links (FR, EN, BR) and 3 non-technical explainer videos into new sophisticated collapsible accordion UI (`<details>`).
- **License Disclaimer**: Added explicit CC BY-NC-SA 4.0 license and usage disclaimer to `README.md` and `docs/index.html` footer.

### Master 2 Course Content Expansion (S1-ISI5)
- **Section 2.5 Expanded:** Grown from a single paragraph to 10 structured sub-sections.
  - *Part A*: Offensive autonomous agents featuring Claude Code (Sept 2025 case), LotL lateral movement, adaptive C2 via LLM APIs, and 14 MITRE ATLAS/Zenity techniques.
  - *Part B*: Data poisoning (4 variants), model poisoning/Pickle, indirect prompt injection (6 vectors). Converges OpenClaw with Lethal Trifecta OWASP 2026. Added a consolidated defense table. Includes 15 references (8 from 2025-2026).
- **New Section 2.6:** Taxonomy of attacks mapped to the OECD lifecycle (7 phases). 
  - Features the DICF quantitative scoring framework + Technical Feasibility.
  - Added 5 structured Attack Profiles: data poisoning, indirect prompt injection, MCP ecosystem, Claude Code autonomous espionage, and LLMjacking.
  - Comparative table of 5 security frameworks: NIST, ATLAS, OWASP LLM, OWASP ML, and ANSSI.
  - Embedded cross-mapping: Kill Chain ↔ Lifecycle ↔ NIST ↔ ATLAS.
  - Provided a "What Changed 2024→2026" summary table.
  - Assorted with 4 graded student exercises and 27 references.

## [v0.8.1] — 2026-02-22

### Added
- English version of the Master 2 course (v6) PDF and its LinkedIn infographic.
- Interactive toggle in GitHub Pages (`index.html`) to switch between French and English versions of the phase infographics and the V6 course infographic.
- Explicit side-by-side FR/EN PDF download buttons for the V6 course.

### Fixed
- Replaced problematic HTML minus entities in the `index.html` timeline to ensure numbers render correctly across all browsers.
- Updated `README.md` repository structure to accurately reflect the correct PDF filenames for all phases and explicitly included the `docs/` directory.

## [v0.8] — 2026-02-19

### Initial Release
- 5-phase analysis documents (Phase 1–5)
- Academic summary note
- 27 academic figures (FR + EN)
- Defense-in-depth model (5 layers)
- MITRE ATT&CK/ATLAS mapping per phase
- Kill chain defense matrix

### Known Issues (to be corrected)
- 

## Versioning Policy

This is an active research project. Documents may be updated after initial publication.
Each change is tracked in this file with date and description.
Major corrections affecting conclusions are flagged with ⚠️.
