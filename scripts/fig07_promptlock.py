#!/usr/bin/env python3
"""
OpenClaw — Figure 07 : PromptLock
========================================
Generates Figure07_PromptLock_FR.png and Figure07_PromptLock_EN.png

EDIT: Change text directly in SVG_FR / SVG_EN below.

Usage:
    python3 fig07_promptlock.py              # FR + EN
    python3 fig07_promptlock.py fr           # FR only
    python3 fig07_promptlock.py en           # EN only

Requires: pip install cairosvg
"""

import os, sys

try:
    import cairosvg
except ImportError:
    print("pip install cairosvg")
    sys.exit(1)

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "openclaw_figures")
DPI = 300
WIDTH = 3600

# ────────────────────────────────────────────────────────────
# SVG FRANÇAIS (modifiable)
# ────────────────────────────────────────────────────────────
SVG_FR = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<svg xmlns="http://www.w3.org/2000/svg" width="750" height="520" viewBox="0 0 750 520">\n'
    '  <style>\n'
    '    text { font-family: "Times New Roman", Times, serif; }\n'
    '    .title { font-size: 11px; font-weight: bold; text-anchor: middle; }\n'
    '    .box { fill: #f5f5f5; stroke: #000; stroke-width: 1; }\n'
    '    .box-dark { fill: #ddd; stroke: #000; stroke-width: 1; }\n'
    '    .box-border { fill: none; stroke: #000; stroke-width: 1.2; stroke-dasharray: 4,2; }\n'
    '    .label { font-size: 9px; font-weight: bold; text-anchor: middle; }\n'
    '    .detail { font-size: 8px; text-anchor: middle; fill: #333; }\n'
    '    .arrow { fill: none; stroke: #000; stroke-width: 0.8; marker-end: url(#arr); }\n'
    '    .arrow-label { font-size: 7px; text-anchor: middle; fill: #555; font-style: italic; }\n'
    '    .caption { font-size: 10px; text-anchor: start; }\n'
    '    .fragility { font-size: 7.5px; text-anchor: start; fill: #555; font-style: italic; }\n'
    '    .section-label { font-size: 8px; font-weight: bold; text-anchor: start; fill: #000; }\n'
    '  </style>\n'
    '  <defs>\n'
    '    <marker id="arr" markerWidth="7" markerHeight="5" refX="7" refY="2.5" orient="auto">\n'
    '      <polygon points="0 0, 7 2.5, 0 5" fill="#000"/>\n'
    '    </marker>\n'
    '  </defs>\n'
    '\n'
    '  <text x="375" y="20" class="title">ARCHITECTURE DU RANSOMWARE PROMPTLOCK</text>\n'
    '  <line x1="30" y1="28" x2="720" y2="28" stroke="#000" stroke-width="0.6"/>\n'
    '\n'
    '  <!-- Orchestrator Go -->\n'
    '  <rect x="270" y="45" width="200" height="50" class="box-dark"/>\n'
    '  <text x="370" y="65" class="label">Orchestrateur Go</text>\n'
    '  <text x="370" y="78" class="detail">Binaire compilé — coordination des vagues</text>\n'
    '\n'
    '  <!-- LLM local (Ollama) -->\n'
    '  <rect x="50" y="140" width="180" height="60" class="box"/>\n'
    '  <text x="140" y="158" class="label">Serveur LLM local</text>\n'
    '  <text x="140" y="170" class="detail">(Ollama, modèle embarqué)</text>\n'
    '  <text x="140" y="182" class="detail">Génération de variants par cible</text>\n'
    '\n'
    '  <!-- Arrow: Orchestrator → LLM -->\n'
    '  <line x1="310" y1="95" x2="180" y2="138" class="arrow"/>\n'
    '  <text x="230" y="112" class="arrow-label">prompt de génération</text>\n'
    '\n'
    '  <!-- Arrow: LLM → Orchestrator -->\n'
    '  <line x1="200" y1="155" x2="310" y2="80" class="arrow"/>\n'
    '  <text x="270" y="130" class="arrow-label">script chiffrement</text>\n'
    '\n'
    '  <!-- Environment detection -->\n'
    '  <rect x="510" y="140" width="180" height="60" class="box"/>\n'
    '  <text x="600" y="158" class="label">Détection environnement</text>\n'
    '  <text x="600" y="170" class="detail">OS, chemins, outils disponibles</text>\n'
    '  <text x="600" y="182" class="detail">→ paramètres pour le prompt LLM</text>\n'
    '\n'
    '  <!-- Arrow: Orchestrator → Env -->\n'
    '  <line x1="430" y1="95" x2="560" y2="138" class="arrow"/>\n'
    '  <text x="510" y="112" class="arrow-label">reconnaissance locale</text>\n'
    '\n'
    '  <!-- Arrow: Env → Orchestrator -->\n'
    '  <line x1="540" y1="155" x2="430" y2="80" class="arrow"/>\n'
    '  <text x="500" y="130" class="arrow-label">contexte cible</text>\n'
    '\n'
    '  <!-- Wave 1: Servers -->\n'
    '  <rect x="50" y="250" width="180" height="50" class="box"/>\n'
    '  <text x="140" y="268" class="label">Vague 1 — Serveurs</text>\n'
    '  <text x="140" y="280" class="detail">Golden Ticket (T1558.001)</text>\n'
    '  <text x="140" y="292" class="detail">→ exécution distante</text>\n'
    '\n'
    '  <!-- Wave 2: Workstations -->\n'
    '  <rect x="280" y="250" width="180" height="50" class="box"/>\n'
    '  <text x="370" y="268" class="label">Vague 2 — Postes</text>\n'
    '  <text x="370" y="280" class="detail">GPO malveillante (T1484.001)</text>\n'
    '  <text x="370" y="292" class="detail">→ déploiement domaine</text>\n'
    '\n'
    '  <!-- Wave 3: Ransom note -->\n'
    '  <rect x="510" y="250" width="180" height="50" class="box"/>\n'
    '  <text x="600" y="268" class="label">Vague 3 — Extorsion</text>\n'
    '  <text x="600" y="280" class="detail">Note de rançon personnalisée</text>\n'
    '  <text x="600" y="292" class="detail">(T1486, T1657)</text>\n'
    '\n'
    '  <!-- Arrows from orchestrator to waves -->\n'
    '  <line x1="340" y1="95" x2="140" y2="248" class="arrow"/>\n'
    '  <line x1="370" y1="95" x2="370" y2="248" class="arrow"/>\n'
    '  <line x1="400" y1="95" x2="600" y2="248" class="arrow"/>\n'
    '\n'
    '  <!-- Timeline labels -->\n'
    '  <text x="140" y="310" class="arrow-label">T+0 à T+10</text>\n'
    '  <text x="370" y="310" class="arrow-label">T+10 à T+35</text>\n'
    '  <text x="600" y="310" class="arrow-label">T+35 à T+40</text>\n'
    '\n'
    '  <!-- Fragility box -->\n'
    '  <rect x="50" y="335" width="640" height="55" class="box-border"/>\n'
    '  <text x="60" y="350" class="section-label">Fragilités architecturales (points de détection et d\'interruption) :</text>\n'
    '  <text x="60" y="363" class="fragility">• Point de défaillance unique : si le processus LLM local (Ollama) est arrêté ou bloqué, aucun variant ne peut être généré</text>\n'
    '  <text x="60" y="375" class="fragility">• Invariants comportementaux : chiffrement en masse, suppression VSS (T1490), appels API endpoint local → détectables par EDR</text>\n'
    '  <text x="60" y="387" class="fragility">• Artefacts LLM : clés API, fichiers de configuration modèle, historique de prompts, processus serveur Ollama sur le poste</text>\n'
    '\n'
    '  <!-- Caption -->\n'
    '  <line x1="30" y1="405" x2="720" y2="405" stroke="#000" stroke-width="0.5"/>\n'
    '  <text x="30" y="423" class="caption"><tspan font-weight="bold">Figure 7.</tspan> Architecture du ransomware PromptLock. L\'orchestrateur Go coordonne la génération de variants via un LLM</text>\n'
    '  <text x="30" y="438" class="caption">local (Ollama) et le déploiement en trois vagues séquentielles. Le cadre en pointillés identifie les fragilités architecturales</text>\n'
    '  <text x="30" y="453" class="caption">exploitables par les défenseurs : la dépendance au processus LLM local constitue un point de défaillance unique, et les</text>\n'
    '  <text x="30" y="468" class="caption">invariants comportementaux (chiffrement en masse, suppression des mécanismes de restauration) restent détectables.</text>\n'
    '</svg>\n'
)

# ────────────────────────────────────────────────────────────
# SVG ANGLAIS (modifiable)
# ────────────────────────────────────────────────────────────
SVG_EN = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<svg xmlns="http://www.w3.org/2000/svg" width="750" height="520" viewBox="0 0 750 520">\n'
    '  <style>\n'
    '    text { font-family: "Times New Roman", Times, serif; }\n'
    '    .title { font-size: 11px; font-weight: bold; text-anchor: middle; }\n'
    '    .box { fill: #f5f5f5; stroke: #000; stroke-width: 1; }\n'
    '    .box-dark { fill: #ddd; stroke: #000; stroke-width: 1; }\n'
    '    .box-border { fill: none; stroke: #000; stroke-width: 1.2; stroke-dasharray: 4,2; }\n'
    '    .label { font-size: 9px; font-weight: bold; text-anchor: middle; }\n'
    '    .detail { font-size: 8px; text-anchor: middle; fill: #333; }\n'
    '    .arrow { fill: none; stroke: #000; stroke-width: 0.8; marker-end: url(#arr); }\n'
    '    .arrow-label { font-size: 7px; text-anchor: middle; fill: #555; font-style: italic; }\n'
    '    .caption { font-size: 10px; text-anchor: start; }\n'
    '    .fragility { font-size: 7.5px; text-anchor: start; fill: #555; font-style: italic; }\n'
    '    .section-label { font-size: 8px; font-weight: bold; text-anchor: start; fill: #000; }\n'
    '  </style>\n'
    '  <defs><marker id="arr" markerWidth="7" markerHeight="5" refX="7" refY="2.5" orient="auto"><polygon points="0 0, 7 2.5, 0 5" fill="#000"/></marker></defs>\n'
    '\n'
    '  <text x="375" y="20" class="title">PROMPTLOCK RANSOMWARE ARCHITECTURE</text>\n'
    '  <line x1="30" y1="28" x2="720" y2="28" stroke="#000" stroke-width="0.6"/>\n'
    '\n'
    '  <rect x="270" y="45" width="200" height="50" class="box-dark"/>\n'
    '  <text x="370" y="65" class="label">Go Orchestrator</text>\n'
    '  <text x="370" y="78" class="detail">Compiled binary — wave coordination</text>\n'
    '\n'
    '  <rect x="50" y="140" width="180" height="60" class="box"/>\n'
    '  <text x="140" y="158" class="label">Local LLM Server</text>\n'
    '  <text x="140" y="170" class="detail">(Ollama, embedded model)</text>\n'
    '  <text x="140" y="182" class="detail">Per-target variant generation</text>\n'
    '\n'
    '  <line x1="310" y1="95" x2="180" y2="138" class="arrow"/>\n'
    '  <text x="230" y="112" class="arrow-label">generation prompt</text>\n'
    '  <line x1="200" y1="155" x2="310" y2="80" class="arrow"/>\n'
    '  <text x="270" y="130" class="arrow-label">encryption script</text>\n'
    '\n'
    '  <rect x="510" y="140" width="180" height="60" class="box"/>\n'
    '  <text x="600" y="158" class="label">Environment Detection</text>\n'
    '  <text x="600" y="170" class="detail">OS, paths, available tools</text>\n'
    '  <text x="600" y="182" class="detail">→ parameters for LLM prompt</text>\n'
    '\n'
    '  <line x1="430" y1="95" x2="560" y2="138" class="arrow"/>\n'
    '  <text x="510" y="112" class="arrow-label">local reconnaissance</text>\n'
    '  <line x1="540" y1="155" x2="430" y2="80" class="arrow"/>\n'
    '  <text x="500" y="130" class="arrow-label">target context</text>\n'
    '\n'
    '  <rect x="50" y="250" width="180" height="50" class="box"/>\n'
    '  <text x="140" y="268" class="label">Wave 1 — Servers</text>\n'
    '  <text x="140" y="280" class="detail">Golden Ticket (T1558.001)</text>\n'
    '  <text x="140" y="292" class="detail">→ remote execution</text>\n'
    '\n'
    '  <rect x="280" y="250" width="180" height="50" class="box"/>\n'
    '  <text x="370" y="268" class="label">Wave 2 — Workstations</text>\n'
    '  <text x="370" y="280" class="detail">Malicious GPO (T1484.001)</text>\n'
    '  <text x="370" y="292" class="detail">→ domain-wide deployment</text>\n'
    '\n'
    '  <rect x="510" y="250" width="180" height="50" class="box"/>\n'
    '  <text x="600" y="268" class="label">Wave 3 — Extortion</text>\n'
    '  <text x="600" y="280" class="detail">Personalized ransom note</text>\n'
    '  <text x="600" y="292" class="detail">(T1486, T1657)</text>\n'
    '\n'
    '  <line x1="340" y1="95" x2="140" y2="248" class="arrow"/>\n'
    '  <line x1="370" y1="95" x2="370" y2="248" class="arrow"/>\n'
    '  <line x1="400" y1="95" x2="600" y2="248" class="arrow"/>\n'
    '\n'
    '  <text x="140" y="310" class="arrow-label">T+0 to T+10</text>\n'
    '  <text x="370" y="310" class="arrow-label">T+10 to T+35</text>\n'
    '  <text x="600" y="310" class="arrow-label">T+35 to T+40</text>\n'
    '\n'
    '  <rect x="50" y="335" width="640" height="55" class="box-border"/>\n'
    '  <text x="60" y="350" class="section-label">Architectural fragilities (detection and disruption points):</text>\n'
    '  <text x="60" y="363" class="fragility">• Single point of failure: if the local LLM process (Ollama) is stopped or blocked, no variant can be generated</text>\n'
    '  <text x="60" y="375" class="fragility">• Behavioral invariants: mass encryption, VSS deletion (T1490), API calls to local endpoint → detectable by EDR</text>\n'
    '  <text x="60" y="387" class="fragility">• LLM artifacts: API keys, model config files, prompt history, Ollama server process on host</text>\n'
    '\n'
    '  <line x1="30" y1="405" x2="720" y2="405" stroke="#000" stroke-width="0.5"/>\n'
    '  <text x="30" y="423" class="caption"><tspan font-weight="bold">Figure 7.</tspan> PromptLock ransomware architecture. The Go orchestrator coordinates variant generation via a local LLM</text>\n'
    '  <text x="30" y="438" class="caption">(Ollama) and sequential three-wave deployment. The dashed box identifies architectural fragilities exploitable by</text>\n'
    '  <text x="30" y="453" class="caption">defenders: the dependency on the local LLM process constitutes a single point of failure, and behavioral invariants</text>\n'
    '  <text x="30" y="468" class="caption">(mass encryption, recovery mechanism deletion) remain detectable regardless of syntactic variability.</text>\n'
    '</svg>\n'
)


def generate(lang=None):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    targets = []
    if lang != "en":
        targets.append(("FR", SVG_FR))
    if lang != "fr":
        targets.append(("EN", SVG_EN))
    for suffix, svg in targets:
        name = f"Figure07_PromptLock_{suffix}.png"
        path = os.path.join(OUTPUT_DIR, name)
        cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=path, dpi=DPI, output_width=WIDTH)
        print(f"  \u2713 {name} ({os.path.getsize(path)//1024} KB)")


if __name__ == "__main__":
    lang = sys.argv[1].lower() if len(sys.argv) > 1 else None
    generate(lang)
