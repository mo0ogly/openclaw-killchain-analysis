#!/usr/bin/env python3
"""
OpenClaw — Figure 16 : SCHNEIER
========================================
Generates Figure16_SCHNEIER_FR.png and Figure16_SCHNEIER_EN.png

EDIT: Change text directly in SVG_FR / SVG_EN below.

Usage:
    python3 fig16_schneier.py              # FR + EN
    python3 fig16_schneier.py fr           # FR only
    python3 fig16_schneier.py en           # EN only

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
    '<svg xmlns="http://www.w3.org/2000/svg" width="750" height="230" viewBox="0 0 750 230">\n'
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
    '<text x="375" y="20" class="title">PROMPTWARE KILL CHAIN (SCHNEIER ET AL.)</text>\n'
    '<line x1="20" y1="28" x2="730" y2="28" stroke="#000" stroke-width="0.6"/>\n'
    '<rect x="40" y="60" width="120" height="50" fill="#ccc" stroke="#000" stroke-width="1"/>\n'
    '<text x="100" y="80" class="lbl">Injection</text>\n'
    '<text x="100" y="94" class="lbl">indirecte</text>\n'
    '<text x="100" y="100" class="sm">Étape 1</text>\n'
    '<line x1="162" y1="85" x2="178" y2="85" class="arr"/>\n'
    '<rect x="180" y="60" width="120" height="50" fill="#e0e0e0" stroke="#000" stroke-width="1"/>\n'
    '<text x="240" y="80" class="lbl">Compromission</text>\n'
    '<text x="240" y="94" class="lbl">du raisonnement</text>\n'
    '<text x="240" y="100" class="sm">Étape 2</text>\n'
    '<line x1="302" y1="85" x2="318" y2="85" class="arr"/>\n'
    '<rect x="320" y="60" width="120" height="50" fill="#e0e0e0" stroke="#000" stroke-width="1"/>\n'
    '<text x="380" y="80" class="lbl">Action</text>\n'
    '<text x="380" y="94" class="lbl">malveillante</text>\n'
    '<text x="380" y="100" class="sm">Étape 3</text>\n'
    '<line x1="442" y1="85" x2="458" y2="85" class="arr"/>\n'
    '<rect x="460" y="60" width="120" height="50" fill="#e0e0e0" stroke="#000" stroke-width="1"/>\n'
    '<text x="520" y="80" class="lbl">Exfiltration</text>\n'
    '<text x="520" y="94" class="lbl">données</text>\n'
    '<text x="520" y="100" class="sm">Étape 4</text>\n'
    '<line x1="582" y1="85" x2="598" y2="85" class="arr"/>\n'
    '<rect x="600" y="60" width="120" height="50" fill="#ccc" stroke="#000" stroke-width="1"/>\n'
    '<text x="660" y="80" class="lbl">Persistance</text>\n'
    '<text x="660" y="94" class="lbl">agent</text>\n'
    '<text x="660" y="100" class="sm">Étape 5</text>\n'
    '\n'
    '<line x1="20" y1="180" x2="730" y2="180" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="20" y="198" style="font-family:Times New Roman,serif;font-size:10px;"><tspan font-weight="bold">Figure 16.</tspan> Promptware Kill Chain adaptée de Schneier et al. Les cinq étapes décrivent la progression</text>\n'
    '<text x="20" y="213" style="font-family:Times New Roman,serif;font-size:10px;">d\'une attaque par injection indirecte de prompt, de l\'injection initiale à la persistance de l\'agent compromis.</text>\n'
    '\n'
    '</svg>\n'
)

# ────────────────────────────────────────────────────────────
# SVG ANGLAIS (modifiable)
# ────────────────────────────────────────────────────────────
SVG_EN = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<svg xmlns="http://www.w3.org/2000/svg" width="750" height="230" viewBox="0 0 750 230">\n'
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
    '<text x="375" y="20" class="title">PROMPTWARE KILL CHAIN (SCHNEIER ET AL.)</text>\n'
    '<line x1="20" y1="28" x2="730" y2="28" stroke="#000" stroke-width="0.6"/>\n'
    '<rect x="40" y="60" width="120" height="50" fill="#ccc" stroke="#000" stroke-width="1"/>\n'
    '<text x="100" y="80" class="lbl">Indirect</text>\n'
    '<text x="100" y="94" class="lbl">injection</text>\n'
    '<text x="100" y="100" class="sm">Étape 1</text>\n'
    '<line x1="162" y1="85" x2="178" y2="85" class="arr"/>\n'
    '<rect x="180" y="60" width="120" height="50" fill="#e0e0e0" stroke="#000" stroke-width="1"/>\n'
    '<text x="240" y="80" class="lbl">Reasoning</text>\n'
    '<text x="240" y="94" class="lbl">compromise</text>\n'
    '<text x="240" y="100" class="sm">Étape 2</text>\n'
    '<line x1="302" y1="85" x2="318" y2="85" class="arr"/>\n'
    '<rect x="320" y="60" width="120" height="50" fill="#e0e0e0" stroke="#000" stroke-width="1"/>\n'
    '<text x="380" y="80" class="lbl">Malicious</text>\n'
    '<text x="380" y="94" class="lbl">action</text>\n'
    '<text x="380" y="100" class="sm">Étape 3</text>\n'
    '<line x1="442" y1="85" x2="458" y2="85" class="arr"/>\n'
    '<rect x="460" y="60" width="120" height="50" fill="#e0e0e0" stroke="#000" stroke-width="1"/>\n'
    '<text x="520" y="80" class="lbl">Data</text>\n'
    '<text x="520" y="94" class="lbl">exfiltration</text>\n'
    '<text x="520" y="100" class="sm">Étape 4</text>\n'
    '<line x1="582" y1="85" x2="598" y2="85" class="arr"/>\n'
    '<rect x="600" y="60" width="120" height="50" fill="#ccc" stroke="#000" stroke-width="1"/>\n'
    '<text x="660" y="80" class="lbl">Agent</text>\n'
    '<text x="660" y="94" class="lbl">persistence</text>\n'
    '<text x="660" y="100" class="sm">Étape 5</text>\n'
    '\n'
    '<line x1="20" y1="180" x2="730" y2="180" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="20" y="198" style="font-family:Times New Roman,serif;font-size:10px;"><tspan font-weight="bold">Figure 16.</tspan> Promptware Kill Chain adapted from Schneier et al. The five stages describe the progression</text>\n'
    '<text x="20" y="213" style="font-family:Times New Roman,serif;font-size:10px;">of an indirect prompt injection attack, from initial injection to persistence of the compromised agent.</text>\n'
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
        name = f"Figure16_SCHNEIER_{suffix}.png"
        path = os.path.join(OUTPUT_DIR, name)
        cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=path, dpi=DPI, output_width=WIDTH)
        print(f"  \u2713 {name} ({os.path.getsize(path)//1024} KB)")


if __name__ == "__main__":
    lang = sys.argv[1].lower() if len(sys.argv) > 1 else None
    generate(lang)
