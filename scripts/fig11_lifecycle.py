#!/usr/bin/env python3
"""
OpenClaw — Figure 11 : LIFECYCLE
========================================
Generates Figure11_LIFECYCLE_FR.png and Figure11_LIFECYCLE_EN.png

EDIT: Change text directly in SVG_FR / SVG_EN below.

Usage:
    python3 fig11_lifecycle.py              # FR + EN
    python3 fig11_lifecycle.py fr           # FR only
    python3 fig11_lifecycle.py en           # EN only

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
    '<svg xmlns="http://www.w3.org/2000/svg" width="780" height="360" viewBox="0 0 780 360">\n'
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
    '<text x="390" y="20" class="title">CYCLE DE VIE DE L\'IDENTITÉ AGENTIQUE VOLÉE</text>\n'
    '<line x1="20" y1="28" x2="760" y2="28" stroke="#000" stroke-width="0.6"/>\n'
    '<circle cx="130" cy="130" r="55" fill="#eee" stroke="#000" stroke-width="1"/>\n'
    '<text x="130" y="120" class="lbl">Vol</text>\n'
    '<text x="130" y="135" class="det2">Gateway token, clés API,</text>\n'
    '<text x="130" y="147" class="det2">soul.md</text>\n'
    '<line x1="187" y1="130" x2="243" y2="130" class="arr"/>\n'
    '<circle cx="300" cy="130" r="55" fill="#eee" stroke="#000" stroke-width="1"/>\n'
    '<text x="300" y="120" class="lbl">Clonage</text>\n'
    '<text x="300" y="135" class="det2">Réplication contexte</text>\n'
    '<text x="300" y="147" class="det2">agent complet</text>\n'
    '<line x1="357" y1="130" x2="413" y2="130" class="arr"/>\n'
    '<circle cx="470" cy="130" r="55" fill="#eee" stroke="#000" stroke-width="1"/>\n'
    '<text x="470" y="120" class="lbl">Usurpation</text>\n'
    '<text x="470" y="135" class="det2">Exécution sous identité</text>\n'
    '<text x="470" y="147" class="det2">légitime</text>\n'
    '<line x1="527" y1="130" x2="583" y2="130" class="arr"/>\n'
    '<circle cx="640" cy="130" r="55" fill="#ddd" stroke="#000" stroke-width="1"/>\n'
    '<text x="640" y="120" class="lbl">Persistance</text>\n'
    '<text x="640" y="135" class="det2">HEARTBEAT.md, rotation</text>\n'
    '<text x="640" y="147" class="det2">automatique tokens</text>\n'
    '\n'
    '    <line x1="640" y1="187" x2="640" y2="220" class="arr" style="stroke:#000;stroke-dasharray:3,2;"/>\n'
    '    <rect x="520" y="222" width="240" height="30" class="boxd"/>\n'
    '    <text x="640" y="241" class="lbl">Détection / Révocation</text>\n'
    '    <line x1="520" y1="237" x2="130" y2="188" style="fill:none;stroke:#000;stroke-width:0.8;stroke-dasharray:3,2;marker-end:url(#a);"/>\n'
    '    \n'
    '<line x1="20" y1="295" x2="760" y2="295" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="20" y="313" style="font-family:Times New Roman,serif;font-size:10px;"><tspan font-weight="bold">Figure 11.</tspan> Cycle de vie de l\'identité agentique volée. Du vol initial (tokens, clés, configuration) au clonage</text>\n'
    '<text x="20" y="328" style="font-family:Times New Roman,serif;font-size:10px;">du contexte agent, puis à l\'usurpation d\'identité et à la persistance via HEARTBEAT.md. La boucle de</text>\n'
    '<text x="20" y="343" style="font-family:Times New Roman,serif;font-size:10px;">détection/révocation (pointillés) représente le mécanisme défensif de rupture du cycle.</text>\n'
    '\n'
    '</svg>\n'
)

# ────────────────────────────────────────────────────────────
# SVG ANGLAIS (modifiable)
# ────────────────────────────────────────────────────────────
SVG_EN = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<svg xmlns="http://www.w3.org/2000/svg" width="780" height="360" viewBox="0 0 780 360">\n'
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
    '<text x="390" y="20" class="title">STOLEN AGENTIC IDENTITY LIFECYCLE</text>\n'
    '<line x1="20" y1="28" x2="760" y2="28" stroke="#000" stroke-width="0.6"/>\n'
    '<circle cx="130" cy="130" r="55" fill="#eee" stroke="#000" stroke-width="1"/>\n'
    '<text x="130" y="120" class="lbl">Theft</text>\n'
    '<text x="130" y="135" class="det2">Gateway token, API keys,</text>\n'
    '<text x="130" y="147" class="det2">soul.md</text>\n'
    '<line x1="187" y1="130" x2="243" y2="130" class="arr"/>\n'
    '<circle cx="300" cy="130" r="55" fill="#eee" stroke="#000" stroke-width="1"/>\n'
    '<text x="300" y="120" class="lbl">Cloning</text>\n'
    '<text x="300" y="135" class="det2">Full agent context</text>\n'
    '<text x="300" y="147" class="det2">replication</text>\n'
    '<line x1="357" y1="130" x2="413" y2="130" class="arr"/>\n'
    '<circle cx="470" cy="130" r="55" fill="#eee" stroke="#000" stroke-width="1"/>\n'
    '<text x="470" y="120" class="lbl">Impersonation</text>\n'
    '<text x="470" y="135" class="det2">Execution under</text>\n'
    '<text x="470" y="147" class="det2">legitimate identity</text>\n'
    '<line x1="527" y1="130" x2="583" y2="130" class="arr"/>\n'
    '<circle cx="640" cy="130" r="55" fill="#ddd" stroke="#000" stroke-width="1"/>\n'
    '<text x="640" y="120" class="lbl">Persistence</text>\n'
    '<text x="640" y="135" class="det2">HEARTBEAT.md, automatic</text>\n'
    '<text x="640" y="147" class="det2">token rotation</text>\n'
    '\n'
    '    <line x1="640" y1="187" x2="640" y2="220" class="arr" style="stroke:#000;stroke-dasharray:3,2;"/>\n'
    '    <rect x="520" y="222" width="240" height="30" class="boxd"/>\n'
    '    <text x="640" y="241" class="lbl">Detection / Revocation</text>\n'
    '    <line x1="520" y1="237" x2="130" y2="188" style="fill:none;stroke:#000;stroke-width:0.8;stroke-dasharray:3,2;marker-end:url(#a);"/>\n'
    '    \n'
    '<line x1="20" y1="295" x2="760" y2="295" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="20" y="313" style="font-family:Times New Roman,serif;font-size:10px;"><tspan font-weight="bold">Figure 11.</tspan> Stolen agentic identity lifecycle. From initial theft (tokens, keys, configuration) to agent context</text>\n'
    '<text x="20" y="328" style="font-family:Times New Roman,serif;font-size:10px;">cloning, then identity impersonation and persistence via HEARTBEAT.md. The detection/revocation loop</text>\n'
    '<text x="20" y="343" style="font-family:Times New Roman,serif;font-size:10px;">(dashed) represents the defensive mechanism for breaking the cycle.</text>\n'
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
        name = f"Figure11_LIFECYCLE_{suffix}.png"
        path = os.path.join(OUTPUT_DIR, name)
        cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=path, dpi=DPI, output_width=WIDTH)
        print(f"  \u2713 {name} ({os.path.getsize(path)//1024} KB)")


if __name__ == "__main__":
    lang = sys.argv[1].lower() if len(sys.argv) > 1 else None
    generate(lang)
