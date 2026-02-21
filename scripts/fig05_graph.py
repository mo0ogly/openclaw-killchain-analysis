#!/usr/bin/env python3
"""
OpenClaw — Figure 05 : GRAPH
========================================
Generates Figure05_GRAPH_FR.png and Figure05_GRAPH_EN.png

EDIT: Change text directly in SVG_FR / SVG_EN below.

Usage:
    python3 fig05_graph.py              # FR + EN
    python3 fig05_graph.py fr           # FR only
    python3 fig05_graph.py en           # EN only

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
    '<svg xmlns="http://www.w3.org/2000/svg" width="700" height="500" viewBox="0 0 700 500">\n'
    '<style>\n'
    'text { font-family: "Times New Roman", Times, serif; }\n'
    '.title { font-size: 11px; font-weight: bold; text-anchor: middle; }\n'
    '.lbl { font-size: 9px; font-weight: bold; text-anchor: middle; }\n'
    '.det { font-size: 8px; text-anchor: middle; fill: #333; }\n'
    '.det2 { font-size: 7.5px; text-anchor: middle; fill: #555; }\n'
    '.sm { font-size: 7px; text-anchor: start; fill: #666; }\n'
    '.caption { font-size: 10px; text-anchor: start; }\n'
    '</style>\n'
    '\n'
    '<text x="350" y="20" class="title">GRAPHE SOCIAL RECONSTITUÉ — MEDIFRANCE SA</text>\n'
    '<line x1="20" y1="28" x2="680" y2="28" stroke="#000" stroke-width="0.6"/>\n'
    '\n'
    '<!-- Central node -->\n'
    '<circle cx="350" cy="180" r="28" fill="#ccc" stroke="#000" stroke-width="1.5"/>\n'
    '<text x="350" y="177" class="lbl">DSI</text>\n'
    '<text x="350" y="190" class="det2">(forte centralité)</text>\n'
    '\n'
    '<!-- Top left: R&D Lead -->\n'
    '<circle cx="160" cy="90" r="22" fill="#eee" stroke="#000" stroke-width="1"/>\n'
    '<text x="160" y="87" class="det">R&amp;D Lead</text>\n'
    '<text x="160" y="99" class="det2">OpenClaw user</text>\n'
    '\n'
    '<!-- Top right: DevOps -->\n'
    '<circle cx="540" cy="90" r="22" fill="#eee" stroke="#000" stroke-width="1"/>\n'
    '<text x="540" y="87" class="det">DevOps</text>\n'
    '<text x="540" y="99" class="det2">ClawHub contrib.</text>\n'
    '\n'
    '<!-- Mid left: Researcher 1 -->\n'
    '<circle cx="130" cy="265" r="22" fill="#eee" stroke="#000" stroke-width="1"/>\n'
    '<text x="130" y="262" class="det">Chercheur 1</text>\n'
    '<text x="130" y="274" class="det2">Publications</text>\n'
    '\n'
    '<!-- Mid right: Admin -->\n'
    '<circle cx="570" cy="265" r="22" fill="#eee" stroke="#000" stroke-width="1"/>\n'
    '<text x="570" y="262" class="det">Admin sys.</text>\n'
    '<text x="570" y="274" class="det2">Tier 1 access</text>\n'
    '\n'
    '<!-- Bottom left: Researcher 2 -->\n'
    '<circle cx="230" cy="330" r="22" fill="#eee" stroke="#000" stroke-width="1"/>\n'
    '<text x="230" y="327" class="det">Chercheur 2</text>\n'
    '<text x="230" y="339" class="det2">Brevet récent</text>\n'
    '\n'
    '<!-- Bottom right: HR -->\n'
    '<circle cx="470" cy="330" r="22" fill="#eee" stroke="#000" stroke-width="1"/>\n'
    '<text x="470" y="327" class="det">RH</text>\n'
    '<text x="470" y="339" class="det2">Organigramme</text>\n'
    '\n'
    '<!-- Strong edges (solid) -->\n'
    '<line x1="180" y1="105" x2="325" y2="165" stroke="#000" stroke-width="0.8"/>\n'
    '<line x1="520" y1="105" x2="375" y2="165" stroke="#000" stroke-width="0.8"/>\n'
    '<line x1="148" y1="250" x2="326" y2="192" stroke="#000" stroke-width="0.8"/>\n'
    '<line x1="552" y1="250" x2="374" y2="192" stroke="#000" stroke-width="0.8"/>\n'
    '<line x1="247" y1="318" x2="330" y2="200" stroke="#000" stroke-width="0.8"/>\n'
    '<line x1="453" y1="318" x2="370" y2="200" stroke="#000" stroke-width="0.8"/>\n'
    '\n'
    '<!-- Weak ties (dashed) -->\n'
    '<line x1="172" y1="106" x2="138" y2="246" stroke="#999" stroke-width="0.5" stroke-dasharray="3,2"/>\n'
    '<line x1="528" y1="106" x2="558" y2="246" stroke="#999" stroke-width="0.5" stroke-dasharray="3,2"/>\n'
    '<line x1="250" y1="325" x2="450" y2="325" stroke="#999" stroke-width="0.5" stroke-dasharray="3,2"/>\n'
    '\n'
    '<!-- Legend — bien espacée en bas -->\n'
    '<line x1="20" y1="380" x2="680" y2="380" stroke="#000" stroke-width="0.3"/>\n'
    '\n'
    '<circle cx="40" cy="400" r="8" fill="#ccc" stroke="#000" stroke-width="1"/>\n'
    '<text x="55" y="403" class="sm">Nœud à forte centralité d\'intermédiarité (betweenness) [161]</text>\n'
    '\n'
    '<line x1="30" y1="425" x2="50" y2="425" stroke="#999" stroke-width="0.6" stroke-dasharray="3,2"/>\n'
    '<text x="55" y="428" class="sm">Lien faible (weak tie) — vecteur de compromission supply chain</text>\n'
    '\n'
    '<!-- Caption -->\n'
    '<line x1="20" y1="445" x2="680" y2="445" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="20" y="462" class="caption"><tspan font-weight="bold">Figure 5.</tspan> Graphe social reconstitué de MediFrance SA par fouille OSINT (LinkedIn, publications, ClawHub).</text>\n'
    '<text x="20" y="477" class="caption">Le nœud DSI présente la plus forte centralité d\'intermédiarité [161], le désignant comme cible prioritaire.</text>\n'
    '<text x="20" y="492" class="caption">Les liens en pointillés représentent les weak ties exploités pour la compromission de la supply chain (Phase 2).</text>\n'
    '</svg>\n'
)

# ────────────────────────────────────────────────────────────
# SVG ANGLAIS (modifiable)
# ────────────────────────────────────────────────────────────
SVG_EN = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<svg xmlns="http://www.w3.org/2000/svg" width="700" height="500" viewBox="0 0 700 500">\n'
    '<style>\n'
    'text { font-family: "Times New Roman", Times, serif; }\n'
    '.title { font-size: 11px; font-weight: bold; text-anchor: middle; }\n'
    '.lbl { font-size: 9px; font-weight: bold; text-anchor: middle; }\n'
    '.det { font-size: 8px; text-anchor: middle; fill: #333; }\n'
    '.det2 { font-size: 7.5px; text-anchor: middle; fill: #555; }\n'
    '.sm { font-size: 7px; text-anchor: start; fill: #666; }\n'
    '.caption { font-size: 10px; text-anchor: start; }\n'
    '</style>\n'
    '\n'
    '<text x="350" y="20" class="title">RECONSTRUCTED SOCIAL GRAPH — MEDIFRANCE SA</text>\n'
    '<line x1="20" y1="28" x2="680" y2="28" stroke="#000" stroke-width="0.6"/>\n'
    '\n'
    '<!-- Central node -->\n'
    '<circle cx="350" cy="180" r="28" fill="#ccc" stroke="#000" stroke-width="1.5"/>\n'
    '<text x="350" y="177" class="lbl">CIO</text>\n'
    '<text x="350" y="190" class="det2">(high centrality)</text>\n'
    '\n'
    '<!-- Top left: R&D Lead -->\n'
    '<circle cx="160" cy="90" r="22" fill="#eee" stroke="#000" stroke-width="1"/>\n'
    '<text x="160" y="87" class="det">R&amp;D Lead</text>\n'
    '<text x="160" y="99" class="det2">OpenClaw user</text>\n'
    '\n'
    '<!-- Top right: DevOps -->\n'
    '<circle cx="540" cy="90" r="22" fill="#eee" stroke="#000" stroke-width="1"/>\n'
    '<text x="540" y="87" class="det">DevOps</text>\n'
    '<text x="540" y="99" class="det2">ClawHub contrib.</text>\n'
    '\n'
    '<!-- Mid left: Researcher 1 -->\n'
    '<circle cx="130" cy="265" r="22" fill="#eee" stroke="#000" stroke-width="1"/>\n'
    '<text x="130" y="262" class="det">Researcher 1</text>\n'
    '<text x="130" y="274" class="det2">Publications</text>\n'
    '\n'
    '<!-- Mid right: Admin -->\n'
    '<circle cx="570" cy="265" r="22" fill="#eee" stroke="#000" stroke-width="1"/>\n'
    '<text x="570" y="262" class="det">Sys. Admin</text>\n'
    '<text x="570" y="274" class="det2">Tier 1 access</text>\n'
    '\n'
    '<!-- Bottom left: Researcher 2 -->\n'
    '<circle cx="230" cy="330" r="22" fill="#eee" stroke="#000" stroke-width="1"/>\n'
    '<text x="230" y="327" class="det">Researcher 2</text>\n'
    '<text x="230" y="339" class="det2">Recent patent</text>\n'
    '\n'
    '<!-- Bottom right: HR -->\n'
    '<circle cx="470" cy="330" r="22" fill="#eee" stroke="#000" stroke-width="1"/>\n'
    '<text x="470" y="327" class="det">HR</text>\n'
    '<text x="470" y="339" class="det2">Org. chart</text>\n'
    '\n'
    '<!-- Strong edges (solid) -->\n'
    '<line x1="180" y1="105" x2="325" y2="165" stroke="#000" stroke-width="0.8"/>\n'
    '<line x1="520" y1="105" x2="375" y2="165" stroke="#000" stroke-width="0.8"/>\n'
    '<line x1="148" y1="250" x2="326" y2="192" stroke="#000" stroke-width="0.8"/>\n'
    '<line x1="552" y1="250" x2="374" y2="192" stroke="#000" stroke-width="0.8"/>\n'
    '<line x1="247" y1="318" x2="330" y2="200" stroke="#000" stroke-width="0.8"/>\n'
    '<line x1="453" y1="318" x2="370" y2="200" stroke="#000" stroke-width="0.8"/>\n'
    '\n'
    '<!-- Weak ties (dashed) -->\n'
    '<line x1="172" y1="106" x2="138" y2="246" stroke="#999" stroke-width="0.5" stroke-dasharray="3,2"/>\n'
    '<line x1="528" y1="106" x2="558" y2="246" stroke="#999" stroke-width="0.5" stroke-dasharray="3,2"/>\n'
    '<line x1="250" y1="325" x2="450" y2="325" stroke="#999" stroke-width="0.5" stroke-dasharray="3,2"/>\n'
    '\n'
    '<!-- Legend — bien espacée en bas -->\n'
    '<line x1="20" y1="380" x2="680" y2="380" stroke="#000" stroke-width="0.3"/>\n'
    '\n'
    '<circle cx="40" cy="400" r="8" fill="#ccc" stroke="#000" stroke-width="1"/>\n'
    '<text x="55" y="403" class="sm">High betweenness centrality node [161]</text>\n'
    '\n'
    '<line x1="30" y1="425" x2="50" y2="425" stroke="#999" stroke-width="0.6" stroke-dasharray="3,2"/>\n'
    '<text x="55" y="428" class="sm">Weak tie — supply chain compromise vector</text>\n'
    '\n'
    '<!-- Caption -->\n'
    '<line x1="20" y1="445" x2="680" y2="445" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="20" y="462" class="caption"><tspan font-weight="bold">Figure 5.</tspan> Reconstructed social graph of MediFrance SA via OSINT (LinkedIn, publications, ClawHub).</text>\n'
    '<text x="20" y="477" class="caption">The CIO node exhibits the highest betweenness centrality [161], designating it as a priority target.</text>\n'
    '<text x="20" y="492" class="caption">Dashed links represent weak ties exploited for supply chain compromise (Phase 2).</text>\n'
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
        name = f"Figure05_GRAPH_{suffix}.png"
        path = os.path.join(OUTPUT_DIR, name)
        cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=path, dpi=DPI, output_width=WIDTH)
        print(f"  \u2713 {name} ({os.path.getsize(path)//1024} KB)")


if __name__ == "__main__":
    lang = sys.argv[1].lower() if len(sys.argv) > 1 else None
    generate(lang)
