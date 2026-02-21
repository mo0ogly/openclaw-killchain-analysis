#!/usr/bin/env python3
"""
OpenClaw — Figure 19 : WATERFALL
========================================
Generates Figure19_WATERFALL_FR.png and Figure19_WATERFALL_EN.png

EDIT: Change text directly in SVG_FR / SVG_EN below.

Usage:
    python3 fig19_waterfall.py              # FR + EN
    python3 fig19_waterfall.py fr           # FR only
    python3 fig19_waterfall.py en           # EN only

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
    '<svg xmlns="http://www.w3.org/2000/svg" width="750" height="340" viewBox="0 0 750 340">\n'
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
    '<text x="375" y="20" class="title">IMPACT FINANCIER — DÉCOMPOSITION EN CASCADE</text>\n'
    '<line x1="20" y1="28" x2="730" y2="28" stroke="#000" stroke-width="0.6"/>\n'
    '<rect x="60" y="160" width="90" height="60" fill="#ddd" stroke="#000" stroke-width="0.8"/>\n'
    '<text x="105" y="152" class="det">Rançon</text>\n'
    '<text x="105" y="164" class="det">(si payée)</text>\n'
    '<rect x="170" y="120" width="90" height="40" fill="#ddd" stroke="#000" stroke-width="0.8"/>\n'
    '<text x="215" y="112" class="det">Réponse</text>\n'
    '<text x="215" y="124" class="det">incident</text>\n'
    '<rect x="280" y="65" width="90" height="55" fill="#ddd" stroke="#000" stroke-width="0.8"/>\n'
    '<text x="325" y="57" class="det">Arrêt</text>\n'
    '<text x="325" y="69" class="det">activité</text>\n'
    '<rect x="390" y="20" width="90" height="45" fill="#bbb" stroke="#000" stroke-width="0.8"/>\n'
    '<text x="435" y="12" class="det">PI</text>\n'
    '<text x="435" y="24" class="det">exfiltrée</text>\n'
    '<rect x="500" y="-15" width="90" height="35" fill="#bbb" stroke="#000" stroke-width="0.8"/>\n'
    '<text x="545" y="-23" class="det">RGPD</text>\n'
    '<text x="545" y="-11" class="det">sanctions</text>\n'
    '<rect x="610" y="-65" width="90" height="50" fill="#bbb" stroke="#000" stroke-width="0.8"/>\n'
    '<text x="655" y="-73" class="det">Réputation</text>\n'
    '<line x1="50" y1="220" x2="740" y2="220" stroke="#000" stroke-width="0.8"/>\n'
    '<text x="170" y="235" class="sm">Pertes directes</text>\n'
    '<text x="500" y="235" class="sm">Pertes indirectes</text>\n'
    '<line x1="330" y1="215" x2="330" y2="225" stroke="#000" stroke-width="0.5" stroke-dasharray="2,2"/>\n'
    '\n'
    '<line x1="20" y1="275" x2="730" y2="275" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="20" y="293" style="font-family:Times New Roman,serif;font-size:10px;"><tspan font-weight="bold">Figure 19.</tspan> Décomposition en cascade de l\'impact financier. Les pertes directes (rançon, réponse incident,</text>\n'
    '<text x="20" y="308" style="font-family:Times New Roman,serif;font-size:10px;">arrêt d\'activité) et indirectes (PI, RGPD, réputation) sont représentées par des barres cumulatives.</text>\n'
    '<text x="20" y="323" style="font-family:Times New Roman,serif;font-size:10px;">Les montants sont illustratifs — l\'impact réel dépend de la taille de l\'organisation et du secteur (cf. §5.2).</text>\n'
    '\n'
    '</svg>\n'
)

# ────────────────────────────────────────────────────────────
# SVG ANGLAIS (modifiable)
# ────────────────────────────────────────────────────────────
SVG_EN = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<svg xmlns="http://www.w3.org/2000/svg" width="750" height="340" viewBox="0 0 750 340">\n'
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
    '<text x="375" y="20" class="title">FINANCIAL IMPACT — WATERFALL DECOMPOSITION</text>\n'
    '<line x1="20" y1="28" x2="730" y2="28" stroke="#000" stroke-width="0.6"/>\n'
    '<rect x="60" y="160" width="90" height="60" fill="#ddd" stroke="#000" stroke-width="0.8"/>\n'
    '<text x="105" y="152" class="det">Ransom</text>\n'
    '<text x="105" y="164" class="det">(if paid)</text>\n'
    '<rect x="170" y="120" width="90" height="40" fill="#ddd" stroke="#000" stroke-width="0.8"/>\n'
    '<text x="215" y="112" class="det">Incident</text>\n'
    '<text x="215" y="124" class="det">response</text>\n'
    '<rect x="280" y="65" width="90" height="55" fill="#ddd" stroke="#000" stroke-width="0.8"/>\n'
    '<text x="325" y="57" class="det">Business</text>\n'
    '<text x="325" y="69" class="det">downtime</text>\n'
    '<rect x="390" y="20" width="90" height="45" fill="#bbb" stroke="#000" stroke-width="0.8"/>\n'
    '<text x="435" y="12" class="det">IP</text>\n'
    '<text x="435" y="24" class="det">exfiltrated</text>\n'
    '<rect x="500" y="-15" width="90" height="35" fill="#bbb" stroke="#000" stroke-width="0.8"/>\n'
    '<text x="545" y="-23" class="det">GDPR</text>\n'
    '<text x="545" y="-11" class="det">sanctions</text>\n'
    '<rect x="610" y="-65" width="90" height="50" fill="#bbb" stroke="#000" stroke-width="0.8"/>\n'
    '<text x="655" y="-73" class="det">Reputation</text>\n'
    '<line x1="50" y1="220" x2="740" y2="220" stroke="#000" stroke-width="0.8"/>\n'
    '<text x="170" y="235" class="sm">Direct losses</text>\n'
    '<text x="500" y="235" class="sm">Indirect losses</text>\n'
    '<line x1="330" y1="215" x2="330" y2="225" stroke="#000" stroke-width="0.5" stroke-dasharray="2,2"/>\n'
    '\n'
    '<line x1="20" y1="275" x2="730" y2="275" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="20" y="293" style="font-family:Times New Roman,serif;font-size:10px;"><tspan font-weight="bold">Figure 19.</tspan> Waterfall decomposition of financial impact. Direct losses (ransom, incident response,</text>\n'
    '<text x="20" y="308" style="font-family:Times New Roman,serif;font-size:10px;">downtime) and indirect losses (IP, GDPR, reputation) are shown as cumulative bars.</text>\n'
    '<text x="20" y="323" style="font-family:Times New Roman,serif;font-size:10px;">Amounts are illustrative — actual impact depends on organization size and sector (cf. §5.2).</text>\n'
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
        name = f"Figure19_WATERFALL_{suffix}.png"
        path = os.path.join(OUTPUT_DIR, name)
        cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=path, dpi=DPI, output_width=WIDTH)
        print(f"  \u2713 {name} ({os.path.getsize(path)//1024} KB)")


if __name__ == "__main__":
    lang = sys.argv[1].lower() if len(sys.argv) > 1 else None
    generate(lang)
