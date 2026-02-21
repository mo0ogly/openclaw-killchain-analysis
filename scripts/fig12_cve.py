#!/usr/bin/env python3
"""
OpenClaw — Figure 12 : CVE
========================================
Generates Figure12_CVE_FR.png and Figure12_CVE_EN.png

EDIT: Change text directly in SVG_FR / SVG_EN below.

Usage:
    python3 fig12_cve.py              # FR + EN
    python3 fig12_cve.py fr           # FR only
    python3 fig12_cve.py en           # EN only

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
    '<svg xmlns="http://www.w3.org/2000/svg" width="780" height="260" viewBox="0 0 780 260">\n'
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
    '<text x="390" y="20" class="title">CHAÎNE D\'EXPLOITATION — CVE-2024-55591</text>\n'
    '<line x1="20" y1="28" x2="760" y2="28" stroke="#000" stroke-width="0.6"/>\n'
    '<rect x="50" y="60" width="150" height="55" class="box"/>\n'
    '<text x="125" y="80" class="lbl">Requête HTTP</text>\n'
    '<text x="125" y="94" class="lbl">Node.js forgée</text>\n'
    '<text x="125" y="105" class="sm">T1190</text>\n'
    '<line x1="202" y1="87" x2="223" y2="87" class="arr"/>\n'
    '<rect x="225" y="60" width="150" height="55" class="box"/>\n'
    '<text x="300" y="80" class="lbl">Contournement</text>\n'
    '<text x="300" y="94" class="lbl">authentification</text>\n'
    '<line x1="377" y1="87" x2="398" y2="87" class="arr"/>\n'
    '<rect x="400" y="60" width="150" height="55" class="box"/>\n'
    '<text x="475" y="80" class="lbl">Création compte</text>\n'
    '<text x="475" y="94" class="lbl">super_admin</text>\n'
    '<text x="475" y="105" class="sm">T1136</text>\n'
    '<line x1="552" y1="87" x2="573" y2="87" class="arr"/>\n'
    '<rect x="575" y="60" width="150" height="55" class="box"/>\n'
    '<text x="650" y="80" class="lbl">Accès réseau</text>\n'
    '<text x="650" y="94" class="lbl">interne</text>\n'
    '<text x="650" y="105" class="sm">T1078</text>\n'
    '<rect x="50" y="140" width="680" height="22" class="boxd"/>\n'
    '<text x="390" y="155" class="sm" style="font-size:8px;">Condition : FortiOS non patché, interface admin exposée</text>\n'
    '\n'
    '<line x1="20" y1="210" x2="760" y2="210" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="20" y="228" style="font-family:Times New Roman,serif;font-size:10px;"><tspan font-weight="bold">Figure 12.</tspan> Chaîne d\'exploitation CVE-2024-55591. Séquence en quatre étapes menant de la requête HTTP</text>\n'
    '<text x="20" y="243" style="font-family:Times New Roman,serif;font-size:10px;">forgée à l\'accès réseau interne. L\'exploitation est conditionnelle au non-patching de FortiOS.</text>\n'
    '\n'
    '</svg>\n'
)

# ────────────────────────────────────────────────────────────
# SVG ANGLAIS (modifiable)
# ────────────────────────────────────────────────────────────
SVG_EN = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<svg xmlns="http://www.w3.org/2000/svg" width="780" height="260" viewBox="0 0 780 260">\n'
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
    '<text x="390" y="20" class="title">EXPLOITATION CHAIN — CVE-2024-55591</text>\n'
    '<line x1="20" y1="28" x2="760" y2="28" stroke="#000" stroke-width="0.6"/>\n'
    '<rect x="50" y="60" width="150" height="55" class="box"/>\n'
    '<text x="125" y="80" class="lbl">Crafted Node.js</text>\n'
    '<text x="125" y="94" class="lbl">HTTP request</text>\n'
    '<text x="125" y="105" class="sm">T1190</text>\n'
    '<line x1="202" y1="87" x2="223" y2="87" class="arr"/>\n'
    '<rect x="225" y="60" width="150" height="55" class="box"/>\n'
    '<text x="300" y="80" class="lbl">Authentication</text>\n'
    '<text x="300" y="94" class="lbl">bypass</text>\n'
    '<line x1="377" y1="87" x2="398" y2="87" class="arr"/>\n'
    '<rect x="400" y="60" width="150" height="55" class="box"/>\n'
    '<text x="475" y="80" class="lbl">super_admin</text>\n'
    '<text x="475" y="94" class="lbl">account creation</text>\n'
    '<text x="475" y="105" class="sm">T1136</text>\n'
    '<line x1="552" y1="87" x2="573" y2="87" class="arr"/>\n'
    '<rect x="575" y="60" width="150" height="55" class="box"/>\n'
    '<text x="650" y="80" class="lbl">Internal network</text>\n'
    '<text x="650" y="94" class="lbl">access</text>\n'
    '<text x="650" y="105" class="sm">T1078</text>\n'
    '<rect x="50" y="140" width="680" height="22" class="boxd"/>\n'
    '<text x="390" y="155" class="sm" style="font-size:8px;">Condition: unpatched FortiOS, exposed admin interface</text>\n'
    '\n'
    '<line x1="20" y1="210" x2="760" y2="210" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="20" y="228" style="font-family:Times New Roman,serif;font-size:10px;"><tspan font-weight="bold">Figure 12.</tspan> CVE-2024-55591 exploitation chain. Four-step sequence from crafted HTTP request to internal</text>\n'
    '<text x="20" y="243" style="font-family:Times New Roman,serif;font-size:10px;">network access. Exploitation is conditional on unpatched FortiOS.</text>\n'
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
        name = f"Figure12_CVE_{suffix}.png"
        path = os.path.join(OUTPUT_DIR, name)
        cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=path, dpi=DPI, output_width=WIDTH)
        print(f"  \u2713 {name} ({os.path.getsize(path)//1024} KB)")


if __name__ == "__main__":
    lang = sys.argv[1].lower() if len(sys.argv) > 1 else None
    generate(lang)
