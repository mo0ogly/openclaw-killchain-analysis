#!/usr/bin/env python3
"""
OpenClaw — Figure 02 : Timeline
========================================
Generates Figure02_Timeline_FR.png and Figure02_Timeline_EN.png

EDIT: Change text directly in SVG_FR / SVG_EN below.

Usage:
    python3 fig02_timeline.py              # FR + EN
    python3 fig02_timeline.py fr           # FR only
    python3 fig02_timeline.py en           # EN only

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
    '<svg xmlns="http://www.w3.org/2000/svg" width="900" height="400" viewBox="0 0 900 400">\n'
    '  <style>\n'
    '    text { font-family: "Times New Roman", Times, serif; }\n'
    '    .title { font-size: 11px; font-weight: bold; text-anchor: middle; }\n'
    '    .axis-label { font-size: 8px; text-anchor: middle; fill: #333; }\n'
    '    .phase-label { font-size: 9px; font-weight: bold; text-anchor: middle; fill: #000; }\n'
    '    .phase-detail { font-size: 7.5px; text-anchor: middle; fill: #444; }\n'
    '    .caption { font-size: 10px; text-anchor: start; }\n'
    '    .detect-label { font-size: 7px; text-anchor: middle; fill: #666; font-style: italic; }\n'
    '    .bar-light { fill: #e8e8e8; stroke: #000; stroke-width: 0.8; }\n'
    '    .bar-medium { fill: #ccc; stroke: #000; stroke-width: 0.8; }\n'
    '    .bar-dark { fill: #999; stroke: #000; stroke-width: 0.8; }\n'
    '    .bar-black { fill: #666; stroke: #000; stroke-width: 0.8; }\n'
    '    .bar-final { fill: #444; stroke: #000; stroke-width: 0.8; }\n'
    '  </style>\n'
    '\n'
    '  <text x="450" y="20" class="title">CHRONOLOGIE DE L\'OPÉRATION OPENCLAW (J−30 À J+6)</text>\n'
    '  <line x1="30" y1="28" x2="870" y2="28" stroke="#000" stroke-width="0.6"/>\n'
    '\n'
    '  <!-- Time axis -->\n'
    '  <line x1="80" y1="290" x2="850" y2="290" stroke="#000" stroke-width="1"/>\n'
    '  <!-- Tick marks -->\n'
    '  <line x1="80" y1="287" x2="80" y2="293" stroke="#000" stroke-width="0.8"/>\n'
    '  <text x="80" y="303" class="axis-label">J−30</text>\n'
    '  <line x1="185" y1="287" x2="185" y2="293" stroke="#000" stroke-width="0.8"/>\n'
    '  <text x="185" y="303" class="axis-label">J−15</text>\n'
    '  <line x1="290" y1="287" x2="290" y2="293" stroke="#000" stroke-width="0.8"/>\n'
    '  <text x="290" y="303" class="axis-label">J−7</text>\n'
    '  <line x1="430" y1="287" x2="430" y2="293" stroke="#000" stroke-width="0.8"/>\n'
    '  <text x="430" y="303" class="axis-label">Jour J</text>\n'
    '  <line x1="500" y1="287" x2="500" y2="293" stroke="#000" stroke-width="0.8"/>\n'
    '  <text x="500" y="303" class="axis-label">J+1</text>\n'
    '  <line x1="780" y1="287" x2="780" y2="293" stroke="#000" stroke-width="0.8"/>\n'
    '  <text x="780" y="303" class="axis-label">J+5</text>\n'
    '  <line x1="850" y1="287" x2="850" y2="293" stroke="#000" stroke-width="0.8"/>\n'
    '  <text x="850" y="303" class="axis-label">J+6</text>\n'
    '  <!-- Arrow -->\n'
    '  <polygon points="850,290 856,287 856,293" fill="#000"/>\n'
    '\n'
    '  <!-- Phase 1: Reconnaissance J-30 to J-15 -->\n'
    '  <rect x="80" y="45" width="105" height="35" class="bar-light"/>\n'
    '  <text x="132" y="60" class="phase-label">Phase 1</text>\n'
    '  <text x="132" y="72" class="phase-detail">Reconnaissance OSINT</text>\n'
    '  <text x="132" y="88" class="detect-label">Signaux : consultations LinkedIn,</text>\n'
    '  <text x="132" y="96" class="detect-label">scans Shodan/Censys</text>\n'
    '\n'
    '  <!-- Phase 2: Weaponization J-15 to J-7 -->\n'
    '  <rect x="185" y="110" width="105" height="35" class="bar-medium"/>\n'
    '  <text x="237" y="125" class="phase-label">Phase 2</text>\n'
    '  <text x="237" y="137" class="phase-detail">Armement (skill, PromptLock)</text>\n'
    '  <text x="237" y="153" class="detect-label">Signaux : publication skill ClawHub,</text>\n'
    '  <text x="237" y="161" class="detect-label">activité registre communautaire</text>\n'
    '\n'
    '  <!-- Phase 3: Delivery/Exploitation/Installation J-7 to J+1 -->\n'
    '  <rect x="290" y="175" width="210" height="35" class="bar-dark"/>\n'
    '  <text x="395" y="190" class="phase-label" style="fill:#fff;">Phase 3</text>\n'
    '  <text x="395" y="202" class="phase-detail" style="fill:#eee;">Livraison + Exploitation + Installation</text>\n'
    '  <text x="395" y="218" class="detect-label">Signaux : install. skill non validée, connexion VPN anormale,</text>\n'
    '  <text x="395" y="226" class="detect-label">exfiltration credentials, écriture HEARTBEAT.md</text>\n'
    '\n'
    '  <!-- Sub-events in Phase 3 -->\n'
    '  <line x1="290" y1="235" x2="290" y2="245" stroke="#000" stroke-width="0.5"/>\n'
    '  <text x="290" y="253" class="detect-label">Supply chain skill</text>\n'
    '  <line x1="370" y1="235" x2="370" y2="245" stroke="#000" stroke-width="0.5"/>\n'
    '  <text x="370" y="253" class="detect-label">Infostealer</text>\n'
    '  <line x1="430" y1="235" x2="430" y2="245" stroke="#000" stroke-width="0.5"/>\n'
    '  <text x="430" y="253" class="detect-label">CVE-2024-55591</text>\n'
    '  <line x1="480" y1="235" x2="480" y2="245" stroke="#000" stroke-width="0.5"/>\n'
    '  <text x="480" y="253" class="detect-label">Persistance</text>\n'
    '\n'
    '  <!-- Phase 4: C2/Lateral Movement J+1 to J+5 -->\n'
    '  <rect x="500" y="110" width="280" height="35" class="bar-black"/>\n'
    '  <text x="640" y="125" class="phase-label" style="fill:#fff;">Phase 4</text>\n'
    '  <text x="640" y="137" class="phase-detail" style="fill:#ddd;">Mouvement latéral + C2 + Exfiltration R&amp;D</text>\n'
    '  <text x="640" y="153" class="detect-label">Signaux : auth. Kerberos anormale, accès séquentiel fichiers R&amp;D,</text>\n'
    '  <text x="640" y="161" class="detect-label">volumétrie HTTPS sortante, injection prompt Slack, neutralisation sauvegardes</text>\n'
    '\n'
    '  <!-- Phase 5: Actions on Objectives J+6 -->\n'
    '  <rect x="780" y="45" width="70" height="35" class="bar-final"/>\n'
    '  <text x="815" y="60" class="phase-label" style="fill:#fff;">Phase 5</text>\n'
    '  <text x="815" y="72" class="phase-detail" style="fill:#ddd;">PromptLock</text>\n'
    '  <text x="815" y="88" class="detect-label">Signaux : chiffrement en masse,</text>\n'
    '  <text x="815" y="96" class="detect-label">modif. GPO, note de rançon</text>\n'
    '\n'
    '  <!-- Connecting lines to axis -->\n'
    '  <line x1="80" y1="80" x2="80" y2="290" stroke="#bbb" stroke-width="0.5" stroke-dasharray="2,2"/>\n'
    '  <line x1="185" y1="80" x2="185" y2="290" stroke="#bbb" stroke-width="0.5" stroke-dasharray="2,2"/>\n'
    '  <line x1="290" y1="145" x2="290" y2="175" stroke="#bbb" stroke-width="0.5" stroke-dasharray="2,2"/>\n'
    '  <line x1="500" y1="145" x2="500" y2="175" stroke="#bbb" stroke-width="0.5" stroke-dasharray="2,2"/>\n'
    '  <line x1="780" y1="80" x2="780" y2="290" stroke="#bbb" stroke-width="0.5" stroke-dasharray="2,2"/>\n'
    '  <line x1="850" y1="80" x2="850" y2="290" stroke="#bbb" stroke-width="0.5" stroke-dasharray="2,2"/>\n'
    '\n'
    '  <!-- Y-axis label -->\n'
    '  <text x="40" y="55" class="axis-label" style="font-weight:bold;">Attaque</text>\n'
    '  <text x="40" y="200" class="axis-label" style="font-weight:bold;">Multi-</text>\n'
    '  <text x="40" y="210" class="axis-label" style="font-weight:bold;">vecteurs</text>\n'
    '\n'
    '  <!-- Caption -->\n'
    '  <line x1="30" y1="320" x2="870" y2="320" stroke="#000" stroke-width="0.5"/>\n'
    '  <text x="30" y="338" class="caption"><tspan font-weight="bold">Figure 2.</tspan> Chronologie de l\'Opération OpenClaw. Les barres représentent la durée de chaque phase ; leur intensité</text>\n'
    '  <text x="30" y="353" class="caption">croissante reflète la progression du niveau de privilège de l\'attaquant. Les signaux de détection identifiés sous chaque</text>\n'
    '  <text x="30" y="368" class="caption">phase constituent autant de fenêtres d\'intervention pour les équipes défensives. La Phase 3 couvre trois étapes de la Kill</text>\n'
    '  <text x="30" y="383" class="caption">Chain (Delivery, Exploitation, Installation) avec des vecteurs parallèles. La temporalité est illustrative (cf. section 2.3).</text>\n'
    '</svg>\n'
)

# ────────────────────────────────────────────────────────────
# SVG ANGLAIS (modifiable)
# ────────────────────────────────────────────────────────────
SVG_EN = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<svg xmlns="http://www.w3.org/2000/svg" width="900" height="400" viewBox="0 0 900 400">\n'
    '  <style>\n'
    '    text { font-family: "Times New Roman", Times, serif; }\n'
    '    .title { font-size: 11px; font-weight: bold; text-anchor: middle; }\n'
    '    .axis-label { font-size: 8px; text-anchor: middle; fill: #333; }\n'
    '    .phase-label { font-size: 9px; font-weight: bold; text-anchor: middle; fill: #000; }\n'
    '    .phase-detail { font-size: 7.5px; text-anchor: middle; fill: #444; }\n'
    '    .caption { font-size: 10px; text-anchor: start; }\n'
    '    .detect-label { font-size: 7px; text-anchor: middle; fill: #666; font-style: italic; }\n'
    '    .bar-light { fill: #e8e8e8; stroke: #000; stroke-width: 0.8; }\n'
    '    .bar-medium { fill: #ccc; stroke: #000; stroke-width: 0.8; }\n'
    '    .bar-dark { fill: #999; stroke: #000; stroke-width: 0.8; }\n'
    '    .bar-black { fill: #666; stroke: #000; stroke-width: 0.8; }\n'
    '    .bar-final { fill: #444; stroke: #000; stroke-width: 0.8; }\n'
    '  </style>\n'
    '\n'
    '  <text x="450" y="20" class="title">OPERATION OPENCLAW TIMELINE (D−30 TO D+6)</text>\n'
    '  <line x1="30" y1="28" x2="870" y2="28" stroke="#000" stroke-width="0.6"/>\n'
    '\n'
    '  <line x1="80" y1="290" x2="850" y2="290" stroke="#000" stroke-width="1"/>\n'
    '  <line x1="80" y1="287" x2="80" y2="293" stroke="#000" stroke-width="0.8"/>\n'
    '  <text x="80" y="303" class="axis-label">D−30</text>\n'
    '  <line x1="185" y1="287" x2="185" y2="293" stroke="#000" stroke-width="0.8"/>\n'
    '  <text x="185" y="303" class="axis-label">D−15</text>\n'
    '  <line x1="290" y1="287" x2="290" y2="293" stroke="#000" stroke-width="0.8"/>\n'
    '  <text x="290" y="303" class="axis-label">D−7</text>\n'
    '  <line x1="430" y1="287" x2="430" y2="293" stroke="#000" stroke-width="0.8"/>\n'
    '  <text x="430" y="303" class="axis-label">Day D</text>\n'
    '  <line x1="500" y1="287" x2="500" y2="293" stroke="#000" stroke-width="0.8"/>\n'
    '  <text x="500" y="303" class="axis-label">D+1</text>\n'
    '  <line x1="780" y1="287" x2="780" y2="293" stroke="#000" stroke-width="0.8"/>\n'
    '  <text x="780" y="303" class="axis-label">D+5</text>\n'
    '  <line x1="850" y1="287" x2="850" y2="293" stroke="#000" stroke-width="0.8"/>\n'
    '  <text x="850" y="303" class="axis-label">D+6</text>\n'
    '  <polygon points="850,290 856,287 856,293" fill="#000"/>\n'
    '\n'
    '  <rect x="80" y="45" width="105" height="35" class="bar-light"/>\n'
    '  <text x="132" y="60" class="phase-label">Phase 1</text>\n'
    '  <text x="132" y="72" class="phase-detail">OSINT Reconnaissance</text>\n'
    '  <text x="132" y="88" class="detect-label">Signals: LinkedIn lookups,</text>\n'
    '  <text x="132" y="96" class="detect-label">Shodan/Censys scans</text>\n'
    '\n'
    '  <rect x="185" y="110" width="105" height="35" class="bar-medium"/>\n'
    '  <text x="237" y="125" class="phase-label">Phase 2</text>\n'
    '  <text x="237" y="137" class="phase-detail">Weaponization (skill, PromptLock)</text>\n'
    '  <text x="237" y="153" class="detect-label">Signals: skill published on ClawHub,</text>\n'
    '  <text x="237" y="161" class="detect-label">community registry activity</text>\n'
    '\n'
    '  <rect x="290" y="175" width="210" height="35" class="bar-dark"/>\n'
    '  <text x="395" y="190" class="phase-label" style="fill:#fff;">Phase 3</text>\n'
    '  <text x="395" y="202" class="phase-detail" style="fill:#eee;">Delivery + Exploitation + Installation</text>\n'
    '  <text x="395" y="218" class="detect-label">Signals: unvetted skill install, anomalous VPN login,</text>\n'
    '  <text x="395" y="226" class="detect-label">credential exfiltration, HEARTBEAT.md write</text>\n'
    '\n'
    '  <line x1="290" y1="235" x2="290" y2="245" stroke="#000" stroke-width="0.5"/>\n'
    '  <text x="290" y="253" class="detect-label">Skill supply chain</text>\n'
    '  <line x1="370" y1="235" x2="370" y2="245" stroke="#000" stroke-width="0.5"/>\n'
    '  <text x="370" y="253" class="detect-label">Infostealer</text>\n'
    '  <line x1="430" y1="235" x2="430" y2="245" stroke="#000" stroke-width="0.5"/>\n'
    '  <text x="430" y="253" class="detect-label">CVE-2024-55591</text>\n'
    '  <line x1="480" y1="235" x2="480" y2="245" stroke="#000" stroke-width="0.5"/>\n'
    '  <text x="480" y="253" class="detect-label">Persistence</text>\n'
    '\n'
    '  <rect x="500" y="110" width="280" height="35" class="bar-black"/>\n'
    '  <text x="640" y="125" class="phase-label" style="fill:#fff;">Phase 4</text>\n'
    '  <text x="640" y="137" class="phase-detail" style="fill:#ddd;">Lateral Movement + C2 + R&amp;D Exfiltration</text>\n'
    '  <text x="640" y="153" class="detect-label">Signals: anomalous Kerberos auth, sequential R&amp;D file access,</text>\n'
    '  <text x="640" y="161" class="detect-label">outbound HTTPS volumetry, Slack prompt injection, backup neutralization</text>\n'
    '\n'
    '  <rect x="780" y="45" width="70" height="35" class="bar-final"/>\n'
    '  <text x="815" y="60" class="phase-label" style="fill:#fff;">Phase 5</text>\n'
    '  <text x="815" y="72" class="phase-detail" style="fill:#ddd;">PromptLock</text>\n'
    '  <text x="815" y="88" class="detect-label">Signals: mass encryption,</text>\n'
    '  <text x="815" y="96" class="detect-label">GPO modification, ransom note</text>\n'
    '\n'
    '  <line x1="80" y1="80" x2="80" y2="290" stroke="#bbb" stroke-width="0.5" stroke-dasharray="2,2"/>\n'
    '  <line x1="185" y1="80" x2="185" y2="290" stroke="#bbb" stroke-width="0.5" stroke-dasharray="2,2"/>\n'
    '  <line x1="290" y1="145" x2="290" y2="175" stroke="#bbb" stroke-width="0.5" stroke-dasharray="2,2"/>\n'
    '  <line x1="500" y1="145" x2="500" y2="175" stroke="#bbb" stroke-width="0.5" stroke-dasharray="2,2"/>\n'
    '  <line x1="780" y1="80" x2="780" y2="290" stroke="#bbb" stroke-width="0.5" stroke-dasharray="2,2"/>\n'
    '  <line x1="850" y1="80" x2="850" y2="290" stroke="#bbb" stroke-width="0.5" stroke-dasharray="2,2"/>\n'
    '\n'
    '  <text x="40" y="55" class="axis-label" style="font-weight:bold;">Attack</text>\n'
    '  <text x="40" y="200" class="axis-label" style="font-weight:bold;">Multi-</text>\n'
    '  <text x="40" y="210" class="axis-label" style="font-weight:bold;">vector</text>\n'
    '\n'
    '  <line x1="30" y1="320" x2="870" y2="320" stroke="#000" stroke-width="0.5"/>\n'
    '  <text x="30" y="338" class="caption"><tspan font-weight="bold">Figure 2.</tspan> Operation OpenClaw timeline. Bar intensity reflects the attacker\'s escalating privilege level across phases.</text>\n'
    '  <text x="30" y="353" class="caption">Detection signals identified beneath each phase represent intervention windows for defensive teams. Phase 3 spans three</text>\n'
    '  <text x="30" y="368" class="caption">Kill Chain stages (Delivery, Exploitation, Installation) with parallel attack vectors. Timeline is illustrative (cf. §2.3).</text>\n'
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
        name = f"Figure02_Timeline_{suffix}.png"
        path = os.path.join(OUTPUT_DIR, name)
        cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=path, dpi=DPI, output_width=WIDTH)
        print(f"  \u2713 {name} ({os.path.getsize(path)//1024} KB)")


if __name__ == "__main__":
    lang = sys.argv[1].lower() if len(sys.argv) > 1 else None
    generate(lang)
