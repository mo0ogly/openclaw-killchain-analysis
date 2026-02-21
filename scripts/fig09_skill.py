#!/usr/bin/env python3
"""
OpenClaw — Figure 09 : SKILL
========================================
Generates Figure09_SKILL_FR.png and Figure09_SKILL_EN.png

EDIT: Change text directly in SVG_FR / SVG_EN below.

Usage:
    python3 fig09_skill.py              # FR + EN
    python3 fig09_skill.py fr           # FR only
    python3 fig09_skill.py en           # EN only

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
    '<svg xmlns="http://www.w3.org/2000/svg" width="750" height="380" viewBox="0 0 750 380">\n'
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
    '<text x="375" y="20" class="title">ANATOMIE D\'UNE SKILL PIÉGÉE — COMPARAISON</text>\n'
    '<line x1="20" y1="28" x2="730" y2="28" stroke="#000" stroke-width="0.6"/>\n'
    '\n'
    '    <text x="200" y="55" class="lbl">Skill légitime</text>\n'
    '    <text x="550" y="55" class="lbl">Skill piégée (PharmaResearch)</text>\n'
    '    <line x1="375" y1="42" x2="375" y2="265" stroke="#000" stroke-width="0.8"/>\n'
    '    <rect x="40" y="70" width="280" height="20" class="box2"/>\n'
    '<text x="180" y="84" class="det">skill.json (métadonnées)</text>\n'
    '<rect x="400" y="70" width="280" height="20" class="box2"/>\n'
    '<text x="540" y="84" class="det">skill.json (métadonnées)</text>\n'
    '<text x="180" y="104" class="det2" style="fill:#060;">Instructions légitimes</text>\n'
    '<text x="540" y="104" class="det2" style="fill:#600;">Instructions malveillantes cachées</text>\n'
    '<rect x="40" y="118" width="280" height="20" class="box2"/>\n'
    '<text x="180" y="132" class="det">README.md</text>\n'
    '<rect x="400" y="118" width="280" height="20" class="box2"/>\n'
    '<text x="540" y="132" class="det">README.md</text>\n'
    '<text x="180" y="152" class="det2" style="fill:#060;">Requêtes API normales</text>\n'
    '<text x="540" y="152" class="det2" style="fill:#600;">Vol credentials + clés API</text>\n'
    '<rect x="40" y="166" width="280" height="20" class="box2"/>\n'
    '<text x="180" y="180" class="det">Permissions déclarées</text>\n'
    '<rect x="400" y="166" width="280" height="20" class="box2"/>\n'
    '<text x="540" y="180" class="det">Permissions déclarées</text>\n'
    '<text x="180" y="200" class="det2" style="fill:#060;">Accès lecture seule</text>\n'
    '<text x="540" y="200" class="det2" style="fill:#600;">Écriture HEARTBEAT.md</text>\n'
    '<rect x="40" y="214" width="280" height="20" class="box2"/>\n'
    '<text x="180" y="228" class="det">Code source (visible)</text>\n'
    '<rect x="400" y="214" width="280" height="20" class="box2"/>\n'
    '<text x="540" y="228" class="det">Code source (visible)</text>\n'
    '<text x="180" y="248" class="det2" style="fill:#060;">Pas de connectivité externe</text>\n'
    '<text x="540" y="248" class="det2" style="fill:#600;">Exfiltration HTTPS vers C2</text>\n'
    '\n'
    '<line x1="20" y1="315" x2="730" y2="315" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="20" y="333" style="font-family:Times New Roman,serif;font-size:10px;"><tspan font-weight="bold">Figure 9.</tspan> Comparaison côte à côte d\'une skill légitime et de la skill piégée PharmaResearch Assistant.</text>\n'
    '<text x="20" y="348" style="font-family:Times New Roman,serif;font-size:10px;">Les fichiers de surface (skill.json, README, permissions) sont identiques ; la différence réside dans les instructions</text>\n'
    '<text x="20" y="363" style="font-family:Times New Roman,serif;font-size:10px;">du prompt système, invisibles à l\'utilisateur sans inspection du code source.</text>\n'
    '\n'
    '</svg>\n'
)

# ────────────────────────────────────────────────────────────
# SVG ANGLAIS (modifiable)
# ────────────────────────────────────────────────────────────
SVG_EN = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<svg xmlns="http://www.w3.org/2000/svg" width="750" height="380" viewBox="0 0 750 380">\n'
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
    '<text x="375" y="20" class="title">TROJANIZED SKILL ANATOMY — COMPARISON</text>\n'
    '<line x1="20" y1="28" x2="730" y2="28" stroke="#000" stroke-width="0.6"/>\n'
    '\n'
    '    <text x="200" y="55" class="lbl">Skill légitime</text>\n'
    '    <text x="550" y="55" class="lbl">Skill piégée (PharmaResearch)</text>\n'
    '    <line x1="375" y1="42" x2="375" y2="265" stroke="#000" stroke-width="0.8"/>\n'
    '    <rect x="40" y="70" width="280" height="20" class="box2"/>\n'
    '<text x="180" y="84" class="det">skill.json (metadata)</text>\n'
    '<rect x="400" y="70" width="280" height="20" class="box2"/>\n'
    '<text x="540" y="84" class="det">skill.json (metadata)</text>\n'
    '<text x="180" y="104" class="det2" style="fill:#060;">Legitimate instructions</text>\n'
    '<text x="540" y="104" class="det2" style="fill:#600;">Hidden malicious instructions</text>\n'
    '<rect x="40" y="118" width="280" height="20" class="box2"/>\n'
    '<text x="180" y="132" class="det">README.md</text>\n'
    '<rect x="400" y="118" width="280" height="20" class="box2"/>\n'
    '<text x="540" y="132" class="det">README.md</text>\n'
    '<text x="180" y="152" class="det2" style="fill:#060;">Normal API requests</text>\n'
    '<text x="540" y="152" class="det2" style="fill:#600;">Credential + API key theft</text>\n'
    '<rect x="40" y="166" width="280" height="20" class="box2"/>\n'
    '<text x="180" y="180" class="det">Declared permissions</text>\n'
    '<rect x="400" y="166" width="280" height="20" class="box2"/>\n'
    '<text x="540" y="180" class="det">Declared permissions</text>\n'
    '<text x="180" y="200" class="det2" style="fill:#060;">Read-only access</text>\n'
    '<text x="540" y="200" class="det2" style="fill:#600;">HEARTBEAT.md writing</text>\n'
    '<rect x="40" y="214" width="280" height="20" class="box2"/>\n'
    '<text x="180" y="228" class="det">Source code (visible)</text>\n'
    '<rect x="400" y="214" width="280" height="20" class="box2"/>\n'
    '<text x="540" y="228" class="det">Source code (visible)</text>\n'
    '<text x="180" y="248" class="det2" style="fill:#060;">No external connectivity</text>\n'
    '<text x="540" y="248" class="det2" style="fill:#600;">HTTPS exfiltration to C2</text>\n'
    '\n'
    '<line x1="20" y1="315" x2="730" y2="315" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="20" y="333" style="font-family:Times New Roman,serif;font-size:10px;"><tspan font-weight="bold">Figure 9.</tspan> Side-by-side comparison of a legitimate skill and the trojanized PharmaResearch Assistant skill.</text>\n'
    '<text x="20" y="348" style="font-family:Times New Roman,serif;font-size:10px;">Surface files (skill.json, README, permissions) are identical; the difference lies in the system prompt</text>\n'
    '<text x="20" y="363" style="font-family:Times New Roman,serif;font-size:10px;">instructions, invisible to the user without source code inspection.</text>\n'
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
        name = f"Figure09_SKILL_{suffix}.png"
        path = os.path.join(OUTPUT_DIR, name)
        cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=path, dpi=DPI, output_width=WIDTH)
        print(f"  \u2713 {name} ({os.path.getsize(path)//1024} KB)")


if __name__ == "__main__":
    lang = sys.argv[1].lower() if len(sys.argv) > 1 else None
    generate(lang)
