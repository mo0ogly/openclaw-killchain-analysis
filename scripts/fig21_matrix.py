#!/usr/bin/env python3
"""
OpenClaw — Figure 21 : MATRIX
========================================
Generates Figure21_MATRIX_FR.png and Figure21_MATRIX_EN.png

EDIT: Change text directly in SVG_FR / SVG_EN below.

Usage:
    python3 fig21_matrix.py              # FR + EN
    python3 fig21_matrix.py fr           # FR only
    python3 fig21_matrix.py en           # EN only

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
    '<svg xmlns="http://www.w3.org/2000/svg" width="780" height="370" viewBox="0 0 780 370">\n'
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
    '<text x="390" y="20" class="title">CONTRÔLES SPÉCIFIQUES IA VS CONTRÔLES CLASSIQUES</text>\n'
    '<line x1="20" y1="28" x2="760" y2="28" stroke="#000" stroke-width="0.6"/>\n'
    '\n'
    '    <text x="450" y="65" class="lbl">Menace classique</text>\n'
    '    <text x="650" y="65" class="lbl">Menace agentique</text>\n'
    '    <text x="230" y="120" class="lbl">Contrôle classique</text>\n'
    '    <text x="230" y="210" class="lbl">Contrôle IA-spécifique</text>\n'
    '    <rect x="350" y="80" width="190" height="80" fill="#e0e0e0" stroke="#000" stroke-width="1"/>\n'
    '<text x="445" y="115" class="det">Patch, MFA, segmentation,</text>\n'
    '<text x="445" y="129" class="det">EDR, sauvegardes</text>\n'
    '<rect x="550" y="80" width="190" height="80" fill="#f5f5f5" stroke="#000" stroke-width="1"/>\n'
    '<text x="645" y="115" class="det">Insuffisant seul :</text>\n'
    '<text x="645" y="129" class="det">agent contourne par LotL</text>\n'
    '<rect x="350" y="170" width="190" height="80" fill="#f5f5f5" stroke="#000" stroke-width="1"/>\n'
    '<text x="445" y="205" class="det">Non applicable</text>\n'
    '<text x="445" y="219" class="det">(pas de composant IA)</text>\n'
    '<rect x="550" y="170" width="190" height="80" fill="#d0d0d0" stroke="#000" stroke-width="1"/>\n'
    '<text x="645" y="205" class="det">Sandboxing agent, allowlist</text>\n'
    '<text x="645" y="219" class="det">outils, monitoring tool calls</text>\n'
    '<line x1="340" y1="70" x2="340" y2="260" stroke="#000" stroke-width="0.8"/>\n'
    '<line x1="300" y1="80" x2="750" y2="80" stroke="#000" stroke-width="0.8"/>\n'
    '<line x1="300" y1="160" x2="750" y2="160" stroke="#000" stroke-width="0.5" stroke-dasharray="2,2"/>\n'
    '\n'
    '<line x1="20" y1="305" x2="760" y2="305" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="20" y="323" style="font-family:Times New Roman,serif;font-size:10px;"><tspan font-weight="bold">Figure 21.</tspan> Matrice contrôles classiques / IA-spécifiques × menaces classiques / agentiques. Le quadrant</text>\n'
    '<text x="20" y="338" style="font-family:Times New Roman,serif;font-size:10px;">inférieur droit (fond foncé) représente les contrôles spécifiques aux risques agentiques. Le quadrant supérieur</text>\n'
    '<text x="20" y="353" style="font-family:Times New Roman,serif;font-size:10px;">droit montre que les contrôles classiques sont nécessaires mais insuffisants face aux menaces agentiques.</text>\n'
    '\n'
    '</svg>\n'
)

# ────────────────────────────────────────────────────────────
# SVG ANGLAIS (modifiable)
# ────────────────────────────────────────────────────────────
SVG_EN = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<svg xmlns="http://www.w3.org/2000/svg" width="780" height="370" viewBox="0 0 780 370">\n'
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
    '<text x="390" y="20" class="title">AI-SPECIFIC VS CLASSIC CONTROLS</text>\n'
    '<line x1="20" y1="28" x2="760" y2="28" stroke="#000" stroke-width="0.6"/>\n'
    '\n'
    '    <text x="450" y="65" class="lbl">Classic threat</text>\n'
    '    <text x="650" y="65" class="lbl">Agentic threat</text>\n'
    '    <text x="230" y="120" class="lbl">Classic control</text>\n'
    '    <text x="230" y="210" class="lbl">AI-specific control</text>\n'
    '    <rect x="350" y="80" width="190" height="80" fill="#e0e0e0" stroke="#000" stroke-width="1"/>\n'
    '<text x="445" y="115" class="det">Patch, MFA, segmentation,</text>\n'
    '<text x="445" y="129" class="det">EDR, backups</text>\n'
    '<rect x="550" y="80" width="190" height="80" fill="#f5f5f5" stroke="#000" stroke-width="1"/>\n'
    '<text x="645" y="115" class="det">Insufficient alone:</text>\n'
    '<text x="645" y="129" class="det">agent bypasses via LotL</text>\n'
    '<rect x="350" y="170" width="190" height="80" fill="#f5f5f5" stroke="#000" stroke-width="1"/>\n'
    '<text x="445" y="205" class="det">Not applicable</text>\n'
    '<text x="445" y="219" class="det">(no AI component)</text>\n'
    '<rect x="550" y="170" width="190" height="80" fill="#d0d0d0" stroke="#000" stroke-width="1"/>\n'
    '<text x="645" y="205" class="det">Agent sandboxing, tool</text>\n'
    '<text x="645" y="219" class="det">allowlist, tool call monitoring</text>\n'
    '<line x1="340" y1="70" x2="340" y2="260" stroke="#000" stroke-width="0.8"/>\n'
    '<line x1="300" y1="80" x2="750" y2="80" stroke="#000" stroke-width="0.8"/>\n'
    '<line x1="300" y1="160" x2="750" y2="160" stroke="#000" stroke-width="0.5" stroke-dasharray="2,2"/>\n'
    '\n'
    '<line x1="20" y1="305" x2="760" y2="305" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="20" y="323" style="font-family:Times New Roman,serif;font-size:10px;"><tspan font-weight="bold">Figure 21.</tspan> Classic/AI-specific controls × classic/agentic threats matrix. The lower-right quadrant (darker)</text>\n'
    '<text x="20" y="338" style="font-family:Times New Roman,serif;font-size:10px;">represents controls specific to agentic risks. The upper-right quadrant shows that classic controls are</text>\n'
    '<text x="20" y="353" style="font-family:Times New Roman,serif;font-size:10px;">necessary but insufficient against agentic threats.</text>\n'
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
        name = f"Figure21_MATRIX_{suffix}.png"
        path = os.path.join(OUTPUT_DIR, name)
        cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=path, dpi=DPI, output_width=WIDTH)
        print(f"  \u2713 {name} ({os.path.getsize(path)//1024} KB)")


if __name__ == "__main__":
    lang = sys.argv[1].lower() if len(sys.argv) > 1 else None
    generate(lang)
