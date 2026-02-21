#!/usr/bin/env python3
"""
OpenClaw — Figure 17 : WAVES
========================================
Generates Figure17_WAVES_FR.png and Figure17_WAVES_EN.png

EDIT: Change text directly in SVG_FR / SVG_EN below.

Usage:
    python3 fig17_waves.py              # FR + EN
    python3 fig17_waves.py fr           # FR only
    python3 fig17_waves.py en           # EN only

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
    '<svg xmlns="http://www.w3.org/2000/svg" width="750" height="250" viewBox="0 0 750 250">\n'
    '<style>\n'
    'text{font-family:"Times New Roman",Times,serif}.title{font-size:11px;font-weight:bold;text-anchor:middle}\n'
    '.box{fill:#f5f5f5;stroke:#000;stroke-width:1}.box2{fill:#eee;stroke:#000;stroke-width:1}.box3{fill:#ddd;stroke:#000;stroke-width:1}\n'
    '.boxd{fill:none;stroke:#000;stroke-width:1;stroke-dasharray:4,2}.lbl{font-size:9px;font-weight:bold;text-anchor:middle}\n'
    '.det{font-size:8px;text-anchor:middle;fill:#333}.det2{font-size:7.5px;text-anchor:middle;fill:#555}\n'
    '.sm{font-size:7px;text-anchor:middle;fill:#666;font-style:italic}\n'
    '.arr{fill:none;stroke:#000;stroke-width:0.8;marker-end:url(#a)}\n'
    '.col{stroke:#000;stroke-width:0.8}\n'
    '</style>\n'
    '<defs><marker id="a" markerWidth="7" markerHeight="5" refX="7" refY="2.5" orient="auto"><polygon points="0 0,7 2.5,0 5" fill="#000"/></marker></defs>\n'
    '<text x="375" y="20" class="title">DÉPLOIEMENT PROMPTLOCK EN TROIS VAGUES</text>\n'
    '<line x1="20" y1="28" x2="730" y2="28" stroke="#000" stroke-width="0.6"/>\n'
    '\n'
    '    <line x1="80" y1="130" x2="680" y2="130" stroke="#000" stroke-width="1"/>\n'
    '    <text x="80" y="145" class="sm">T+0</text>\n'
    '    <text x="280" y="145" class="sm">T+10 min</text>\n'
    '    <text x="500" y="145" class="sm">T+35 min</text>\n'
    '    <text x="680" y="145" class="sm">T+40 min</text>\n'
    '    \n'
    '    <rect x="80" y="55" width="200" height="65" class="box2"/>\n'
    '    <text x="180" y="72" class="lbl">Vague 1 : Serveurs</text>\n'
    '    <text x="180" y="86" class="det">Golden Ticket → exéc. distante</text>\n'
    '    <text x="180" y="108" class="sm">Chiffrement masse, conso. CPU</text>\n'
    '    \n'
    '    <rect x="280" y="55" width="220" height="65" class="box"/>\n'
    '    <text x="390" y="72" class="lbl">Vague 2 : Postes</text>\n'
    '    <text x="390" y="86" class="det">GPO malveillante → domaine</text>\n'
    '    <text x="390" y="108" class="sm">Modification GPO (4739)</text>\n'
    '    \n'
    '    <rect x="500" y="55" width="180" height="65" class="box3"/>\n'
    '    <text x="590" y="72" class="lbl">Vague 3 : Extorsion</text>\n'
    '    <text x="590" y="86" class="det">Note rançon personnalisée</text>\n'
    '    <text x="590" y="108" class="sm">Fichier ransom note, beacon C2</text>\n'
    '    \n'
    '    <line x1="80" y1="127" x2="80" y2="133" stroke="#000" stroke-width="1"/>\n'
    '    <line x1="280" y1="127" x2="280" y2="133" stroke="#000" stroke-width="1"/>\n'
    '    <line x1="500" y1="127" x2="500" y2="133" stroke="#000" stroke-width="1"/>\n'
    '    <line x1="680" y1="127" x2="680" y2="133" stroke="#000" stroke-width="1"/>\n'
    '    <text x="80" y="105" class="det2" style="text-anchor:start;font-weight:bold;">Signaux de détection :</text>\n'
    '\n'
    '<line x1="20" y1="200" x2="730" y2="200" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="20" y="218" style="font-family:Times New Roman,serif;font-size:10px;"><tspan font-weight="bold">Figure 17.</tspan> Séquence de déploiement PromptLock en trois vagues (T+0 à T+40 minutes). Chaque vague</text>\n'
    '<text x="20" y="233" style="font-family:Times New Roman,serif;font-size:10px;">produit des signaux de détection spécifiques (italique), offrant des fenêtres d\'intervention décroissantes.</text>\n'
    '\n'
    '</svg>\n'
)

# ────────────────────────────────────────────────────────────
# SVG ANGLAIS (modifiable)
# ────────────────────────────────────────────────────────────
SVG_EN = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<svg xmlns="http://www.w3.org/2000/svg" width="750" height="250" viewBox="0 0 750 250">\n'
    '<style>\n'
    'text{font-family:"Times New Roman",Times,serif}.title{font-size:11px;font-weight:bold;text-anchor:middle}\n'
    '.box{fill:#f5f5f5;stroke:#000;stroke-width:1}.box2{fill:#eee;stroke:#000;stroke-width:1}.box3{fill:#ddd;stroke:#000;stroke-width:1}\n'
    '.boxd{fill:none;stroke:#000;stroke-width:1;stroke-dasharray:4,2}.lbl{font-size:9px;font-weight:bold;text-anchor:middle}\n'
    '.det{font-size:8px;text-anchor:middle;fill:#333}.det2{font-size:7.5px;text-anchor:middle;fill:#555}\n'
    '.sm{font-size:7px;text-anchor:middle;fill:#666;font-style:italic}\n'
    '.arr{fill:none;stroke:#000;stroke-width:0.8;marker-end:url(#a)}\n'
    '.col{stroke:#000;stroke-width:0.8}\n'
    '</style>\n'
    '<defs><marker id="a" markerWidth="7" markerHeight="5" refX="7" refY="2.5" orient="auto"><polygon points="0 0,7 2.5,0 5" fill="#000"/></marker></defs>\n'
    '<text x="375" y="20" class="title">PROMPTLOCK THREE-WAVE DEPLOYMENT</text>\n'
    '<line x1="20" y1="28" x2="730" y2="28" stroke="#000" stroke-width="0.6"/>\n'
    '\n'
    '    <line x1="80" y1="130" x2="680" y2="130" stroke="#000" stroke-width="1"/>\n'
    '    <text x="80" y="145" class="sm">T+0</text>\n'
    '    <text x="280" y="145" class="sm">T+10 min</text>\n'
    '    <text x="500" y="145" class="sm">T+35 min</text>\n'
    '    <text x="680" y="145" class="sm">T+40 min</text>\n'
    '    \n'
    '    <rect x="80" y="55" width="200" height="65" class="box2"/>\n'
    '    <text x="180" y="72" class="lbl">Wave 1: Servers</text>\n'
    '    <text x="180" y="86" class="det">Golden Ticket → remote exec</text>\n'
    '    <text x="180" y="108" class="sm">Mass encryption, CPU spike</text>\n'
    '    \n'
    '    <rect x="280" y="55" width="220" height="65" class="box"/>\n'
    '    <text x="390" y="72" class="lbl">Wave 2: Workstations</text>\n'
    '    <text x="390" y="86" class="det">Malicious GPO → domain-wide</text>\n'
    '    <text x="390" y="108" class="sm">GPO modification (4739)</text>\n'
    '    \n'
    '    <rect x="500" y="55" width="180" height="65" class="box3"/>\n'
    '    <text x="590" y="72" class="lbl">Wave 3: Extortion</text>\n'
    '    <text x="590" y="86" class="det">Personalized ransom note</text>\n'
    '    <text x="590" y="108" class="sm">Ransom note file, C2 beacon</text>\n'
    '    \n'
    '    <line x1="80" y1="127" x2="80" y2="133" stroke="#000" stroke-width="1"/>\n'
    '    <line x1="280" y1="127" x2="280" y2="133" stroke="#000" stroke-width="1"/>\n'
    '    <line x1="500" y1="127" x2="500" y2="133" stroke="#000" stroke-width="1"/>\n'
    '    <line x1="680" y1="127" x2="680" y2="133" stroke="#000" stroke-width="1"/>\n'
    '    <text x="80" y="105" class="det2" style="text-anchor:start;font-weight:bold;">Detection signals :</text>\n'
    '\n'
    '<line x1="20" y1="200" x2="730" y2="200" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="20" y="218" style="font-family:Times New Roman,serif;font-size:10px;"><tspan font-weight="bold">Figure 17.</tspan> PromptLock three-wave deployment sequence (T+0 to T+40 minutes). Each wave produces</text>\n'
    '<text x="20" y="233" style="font-family:Times New Roman,serif;font-size:10px;">specific detection signals (italic), offering decreasing intervention windows.</text>\n'
    '\n'
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
        name = f"Figure17_WAVES_{suffix}.png"
        path = os.path.join(OUTPUT_DIR, name)
        cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=path, dpi=DPI, output_width=WIDTH)
        print(f"  \u2713 {name} ({os.path.getsize(path)//1024} KB)")


if __name__ == "__main__":
    lang = sys.argv[1].lower() if len(sys.argv) > 1 else None
    generate(lang)
