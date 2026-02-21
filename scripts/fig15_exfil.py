#!/usr/bin/env python3
"""
OpenClaw — Figure 15 : EXFIL
========================================
Generates Figure15_EXFIL_FR.png and Figure15_EXFIL_EN.png

EDIT: Change text directly in SVG_FR / SVG_EN below.

Usage:
    python3 fig15_exfil.py              # FR + EN
    python3 fig15_exfil.py fr           # FR only
    python3 fig15_exfil.py en           # EN only

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
    '<svg xmlns="http://www.w3.org/2000/svg" width="700" height="340" viewBox="0 0 700 340">\n'
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
    '<text x="350" y="20" class="title">CANAUX D\'EXFILTRATION — COMPARAISON</text>\n'
    '<line x1="20" y1="28" x2="680" y2="28" stroke="#000" stroke-width="0.6"/>\n'
    '<rect x="40" y="50" width="160" height="25" class="box3"/>\n'
    '<text x="120" y="67" class="lbl">Critère</text>\n'
    '<rect x="200" y="50" width="200" height="25" class="box3"/>\n'
    '<text x="300" y="67" class="lbl">Skill (T1041)</text>\n'
    '<rect x="440" y="50" width="200" height="25" class="box3"/>\n'
    '<text x="540" y="67" class="lbl">Chatbot empoisonné</text>\n'
    '<rect x="40" y="78" width="160" height="26" fill="#f5f5f5" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="120" y="95" class="det">Mécanisme</text>\n'
    '<rect x="200" y="78" width="200" height="26" fill="#f5f5f5" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="300" y="95" class="det">HTTPS direct vers C2</text>\n'
    '<rect x="440" y="78" width="200" height="26" fill="#f5f5f5" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="540" y="95" class="det">Via connecteurs SaaS</text>\n'
    '<rect x="40" y="106" width="160" height="26" fill="#eee" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="120" y="123" class="det">Volume</text>\n'
    '<rect x="200" y="106" width="200" height="26" fill="#eee" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="300" y="123" class="det">Élevé (fichiers complets)</text>\n'
    '<rect x="440" y="106" width="200" height="26" fill="#eee" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="540" y="123" class="det">Faible (fragments)</text>\n'
    '<rect x="40" y="134" width="160" height="26" fill="#f5f5f5" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="120" y="151" class="det">Pré-requis</text>\n'
    '<rect x="200" y="134" width="200" height="26" fill="#f5f5f5" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="300" y="151" class="det">Skill installée + exécutée</text>\n'
    '<rect x="440" y="134" width="200" height="26" fill="#f5f5f5" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="540" y="151" class="det">Accès chatbot + injection</text>\n'
    '<rect x="40" y="162" width="160" height="26" fill="#eee" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="120" y="179" class="det">Détectabilité</text>\n'
    '<rect x="200" y="162" width="200" height="26" fill="#eee" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="300" y="179" class="det">Inspection TLS, DLP</text>\n'
    '<rect x="440" y="162" width="200" height="26" fill="#eee" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="540" y="179" class="det">Monitoring tool calls</text>\n'
    '<rect x="40" y="190" width="160" height="26" fill="#f5f5f5" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="120" y="207" class="det">Contrôle</text>\n'
    '<rect x="200" y="190" width="200" height="26" fill="#f5f5f5" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="300" y="207" class="det">Allowlist egress</text>\n'
    '<rect x="440" y="190" width="200" height="26" fill="#f5f5f5" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="540" y="207" class="det">Confirmation humaine</text>\n'
    '\n'
    '<line x1="20" y1="290" x2="680" y2="290" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="20" y="308" style="font-family:Times New Roman,serif;font-size:10px;"><tspan font-weight="bold">Figure 15.</tspan> Comparaison des deux canaux d\'exfiltration du scénario OpenClaw. Le canal skill offre un</text>\n'
    '<text x="20" y="323" style="font-family:Times New Roman,serif;font-size:10px;">débit élevé mais une détectabilité par DLP ; le chatbot empoisonné est discret mais à faible volume.</text>\n'
    '\n'
    '</svg>\n'
)

# ────────────────────────────────────────────────────────────
# SVG ANGLAIS (modifiable)
# ────────────────────────────────────────────────────────────
SVG_EN = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<svg xmlns="http://www.w3.org/2000/svg" width="700" height="340" viewBox="0 0 700 340">\n'
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
    '<text x="350" y="20" class="title">EXFILTRATION CHANNELS — COMPARISON</text>\n'
    '<line x1="20" y1="28" x2="680" y2="28" stroke="#000" stroke-width="0.6"/>\n'
    '<rect x="40" y="50" width="160" height="25" class="box3"/>\n'
    '<text x="120" y="67" class="lbl">Criterion</text>\n'
    '<rect x="200" y="50" width="200" height="25" class="box3"/>\n'
    '<text x="300" y="67" class="lbl">Skill (T1041)</text>\n'
    '<rect x="440" y="50" width="200" height="25" class="box3"/>\n'
    '<text x="540" y="67" class="lbl">Poisoned chatbot</text>\n'
    '<rect x="40" y="78" width="160" height="26" fill="#f5f5f5" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="120" y="95" class="det">Mechanism</text>\n'
    '<rect x="200" y="78" width="200" height="26" fill="#f5f5f5" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="300" y="95" class="det">Direct HTTPS to C2</text>\n'
    '<rect x="440" y="78" width="200" height="26" fill="#f5f5f5" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="540" y="95" class="det">Via SaaS connectors</text>\n'
    '<rect x="40" y="106" width="160" height="26" fill="#eee" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="120" y="123" class="det">Volume</text>\n'
    '<rect x="200" y="106" width="200" height="26" fill="#eee" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="300" y="123" class="det">High (full files)</text>\n'
    '<rect x="440" y="106" width="200" height="26" fill="#eee" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="540" y="123" class="det">Low (fragments)</text>\n'
    '<rect x="40" y="134" width="160" height="26" fill="#f5f5f5" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="120" y="151" class="det">Prerequisite</text>\n'
    '<rect x="200" y="134" width="200" height="26" fill="#f5f5f5" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="300" y="151" class="det">Skill installed + executed</text>\n'
    '<rect x="440" y="134" width="200" height="26" fill="#f5f5f5" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="540" y="151" class="det">Chatbot access + injection</text>\n'
    '<rect x="40" y="162" width="160" height="26" fill="#eee" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="120" y="179" class="det">Detectability</text>\n'
    '<rect x="200" y="162" width="200" height="26" fill="#eee" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="300" y="179" class="det">TLS inspection, DLP</text>\n'
    '<rect x="440" y="162" width="200" height="26" fill="#eee" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="540" y="179" class="det">Tool call monitoring</text>\n'
    '<rect x="40" y="190" width="160" height="26" fill="#f5f5f5" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="120" y="207" class="det">Control</text>\n'
    '<rect x="200" y="190" width="200" height="26" fill="#f5f5f5" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="300" y="207" class="det">Egress allowlist</text>\n'
    '<rect x="440" y="190" width="200" height="26" fill="#f5f5f5" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="540" y="207" class="det">Human confirmation</text>\n'
    '\n'
    '<line x1="20" y1="290" x2="680" y2="290" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="20" y="308" style="font-family:Times New Roman,serif;font-size:10px;"><tspan font-weight="bold">Figure 15.</tspan> Comparison of the two exfiltration channels in the OpenClaw scenario. The skill channel offers</text>\n'
    '<text x="20" y="323" style="font-family:Times New Roman,serif;font-size:10px;">high throughput but DLP detectability; the poisoned chatbot is stealthy but low-volume.</text>\n'
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
        name = f"Figure15_EXFIL_{suffix}.png"
        path = os.path.join(OUTPUT_DIR, name)
        cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=path, dpi=DPI, output_width=WIDTH)
        print(f"  \u2713 {name} ({os.path.getsize(path)//1024} KB)")


if __name__ == "__main__":
    lang = sys.argv[1].lower() if len(sys.argv) > 1 else None
    generate(lang)
