#!/usr/bin/env python3
"""
OpenClaw — Figure 10 : CONVERGENCE
========================================
Generates Figure10_CONVERGENCE_FR.png and Figure10_CONVERGENCE_EN.png

EDIT: Change text directly in SVG_FR / SVG_EN below.

Usage:
    python3 fig10_convergence.py              # FR + EN
    python3 fig10_convergence.py fr           # FR only
    python3 fig10_convergence.py en           # EN only

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
    '<svg xmlns="http://www.w3.org/2000/svg" width="650" height="370" viewBox="0 0 650 370">\n'
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
    '<text x="325" y="20" class="title">CONVERGENCE DES VECTEURS D\'ACCÈS INITIAL</text>\n'
    '<line x1="20" y1="28" x2="630" y2="28" stroke="#000" stroke-width="0.6"/>\n'
    '\n'
    '    <rect x="40" y="60" width="180" height="45" class="box"/>\n'
    '    <text x="130" y="78" class="lbl">Supply chain skill</text>\n'
    '    <text x="130" y="92" class="det">T1195.002</text>\n'
    '    \n'
    '    <rect x="40" y="130" width="180" height="45" class="box2"/>\n'
    '    <text x="130" y="148" class="lbl">Infostealer</text>\n'
    '    <text x="130" y="162" class="det">T1078 (credentials)</text>\n'
    '    \n'
    '    <rect x="40" y="200" width="180" height="45" class="box3"/>\n'
    '    <text x="130" y="218" class="lbl">CVE-2024-55591</text>\n'
    '    <text x="130" y="232" class="det">T1190 (VPN exploit)</text>\n'
    '    \n'
    '    <line x1="220" y1="82" x2="380" y2="150" class="arr"/>\n'
    '    <line x1="220" y1="152" x2="380" y2="152" class="arr"/>\n'
    '    <line x1="220" y1="222" x2="380" y2="155" class="arr"/>\n'
    '    \n'
    '    <rect x="380" y="120" width="200" height="65" class="box3"/>\n'
    '    <text x="480" y="145" class="lbl">MediFrance SI</text>\n'
    '    <text x="480" y="160" class="det">Accès initial obtenu</text>\n'
    '    <text x="480" y="175" class="det2">(agent contexte compromis)</text>\n'
    '    \n'
    '    <rect x="40" y="270" width="540" height="22" class="boxd"/>\n'
    '    <text x="310" y="285" class="sm" style="font-size:8px;">Redondance : un seul vecteur suffit</text>\n'
    '    \n'
    '<line x1="20" y1="305" x2="630" y2="305" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="20" y="323" style="font-family:Times New Roman,serif;font-size:10px;"><tspan font-weight="bold">Figure 10.</tspan> Convergence des trois vecteurs d\'accès initial vers le SI de MediFrance. Chaque vecteur opère</text>\n'
    '<text x="20" y="338" style="font-family:Times New Roman,serif;font-size:10px;">indépendamment (supply chain de skills, infostealer, exploitation VPN). Cette redondance stratégique</text>\n'
    '<text x="20" y="353" style="font-family:Times New Roman,serif;font-size:10px;">augmente la probabilité de succès de l\'accès initial, même si un vecteur est bloqué par les défenses.</text>\n'
    '\n'
    '</svg>\n'
)

# ────────────────────────────────────────────────────────────
# SVG ANGLAIS (modifiable)
# ────────────────────────────────────────────────────────────
SVG_EN = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<svg xmlns="http://www.w3.org/2000/svg" width="650" height="370" viewBox="0 0 650 370">\n'
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
    '<text x="325" y="20" class="title">INITIAL ACCESS VECTOR CONVERGENCE</text>\n'
    '<line x1="20" y1="28" x2="630" y2="28" stroke="#000" stroke-width="0.6"/>\n'
    '\n'
    '    <rect x="40" y="60" width="180" height="45" class="box"/>\n'
    '    <text x="130" y="78" class="lbl">Supply chain skill</text>\n'
    '    <text x="130" y="92" class="det">T1195.002</text>\n'
    '    \n'
    '    <rect x="40" y="130" width="180" height="45" class="box2"/>\n'
    '    <text x="130" y="148" class="lbl">Infostealer</text>\n'
    '    <text x="130" y="162" class="det">T1078 (credentials)</text>\n'
    '    \n'
    '    <rect x="40" y="200" width="180" height="45" class="box3"/>\n'
    '    <text x="130" y="218" class="lbl">CVE-2024-55591</text>\n'
    '    <text x="130" y="232" class="det">T1190 (VPN exploit)</text>\n'
    '    \n'
    '    <line x1="220" y1="82" x2="380" y2="150" class="arr"/>\n'
    '    <line x1="220" y1="152" x2="380" y2="152" class="arr"/>\n'
    '    <line x1="220" y1="222" x2="380" y2="155" class="arr"/>\n'
    '    \n'
    '    <rect x="380" y="120" width="200" height="65" class="box3"/>\n'
    '    <text x="480" y="145" class="lbl">MediFrance IS</text>\n'
    '    <text x="480" y="160" class="det">Accès initial obtenu</text>\n'
    '    <text x="480" y="175" class="det2">(agent contexte compromis)</text>\n'
    '    \n'
    '    <rect x="40" y="270" width="540" height="22" class="boxd"/>\n'
    '    <text x="310" y="285" class="sm" style="font-size:8px;">Redundancy: any single vector is sufficient</text>\n'
    '    \n'
    '<line x1="20" y1="305" x2="630" y2="305" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="20" y="323" style="font-family:Times New Roman,serif;font-size:10px;"><tspan font-weight="bold">Figure 10.</tspan> Convergence of the three initial access vectors toward the MediFrance IS. Each vector operates</text>\n'
    '<text x="20" y="338" style="font-family:Times New Roman,serif;font-size:10px;">independently (skill supply chain, infostealer, VPN exploitation). This strategic redundancy increases</text>\n'
    '<text x="20" y="353" style="font-family:Times New Roman,serif;font-size:10px;">the probability of successful initial access, even if one vector is blocked by defenses.</text>\n'
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
        name = f"Figure10_CONVERGENCE_{suffix}.png"
        path = os.path.join(OUTPUT_DIR, name)
        cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=path, dpi=DPI, output_width=WIDTH)
        print(f"  \u2713 {name} ({os.path.getsize(path)//1024} KB)")


if __name__ == "__main__":
    lang = sys.argv[1].lower() if len(sys.argv) > 1 else None
    generate(lang)
