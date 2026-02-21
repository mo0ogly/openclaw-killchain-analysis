#!/usr/bin/env python3
"""
OpenClaw — Figure 04 : I2D
========================================
Generates Figure04_I2D_FR.png and Figure04_I2D_EN.png

EDIT: Change text directly in SVG_FR / SVG_EN below.

Usage:
    python3 fig04_i2d.py              # FR + EN
    python3 fig04_i2d.py fr           # FR only
    python3 fig04_i2d.py en           # EN only

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
    '<svg xmlns="http://www.w3.org/2000/svg" width="800" height="420" viewBox="0 0 800 420">\n'
    '<style>\n'
    'text { font-family: "Times New Roman", Times, serif; }\n'
    '.title { font-size: 11px; font-weight: bold; text-anchor: middle; }\n'
    '.box { fill: #f5f5f5; stroke: #000; stroke-width: 1; }\n'
    '.box2 { fill: #eee; stroke: #000; stroke-width: 1; }\n'
    '.box3 { fill: #ddd; stroke: #000; stroke-width: 1; }\n'
    '.boxd { fill: none; stroke: #000; stroke-width: 1; stroke-dasharray: 4,2; }\n'
    '.lbl { font-size: 9px; font-weight: bold; text-anchor: middle; }\n'
    '.det { font-size: 8px; text-anchor: middle; fill: #333; }\n'
    '.det2 { font-size: 7.5px; text-anchor: middle; fill: #555; }\n'
    '.sm { font-size: 7px; text-anchor: middle; fill: #666; font-style: italic; }\n'
    '.arr { fill: none; stroke: #000; stroke-width: 0.8; marker-end: url(#a); }\n'
    '.arrd { fill: none; stroke: #000; stroke-width: 0.8; marker-end: url(#a); stroke-dasharray: 3,2; }\n'
    '</style>\n'
    '<defs><marker id="a" markerWidth="7" markerHeight="5" refX="7" refY="2.5" orient="auto"><polygon points="0 0,7 2.5,0 5" fill="#000"/></marker></defs>\n'
    '<text x="400" y="20" class="title">DIAGRAMME D\'INFÉRENCE D\'INFORMATION (I2D) — PHASE DE RECONNAISSANCE</text>\n'
    '<line x1="20" y1="28" x2="780" y2="28" stroke="#000" stroke-width="0.6"/>\n'
    '\n'
    '    <!-- Sources row -->\n'
    '    <rect x="40" y="50" width="130" height="40" class="box"/>\n'
    '    <text x="105" y="68" class="lbl">Sources publiques</text>\n'
    '    <text x="105" y="80" class="det">LinkedIn, Shodan, Censys</text>\n'
    '    \n'
    '    <rect x="200" y="50" width="130" height="40" class="box"/>\n'
    '    <text x="265" y="68" class="lbl">Publications</text>\n'
    '    <text x="265" y="80" class="det">Brevets, conférences, GitHub</text>\n'
    '    \n'
    '    <rect x="360" y="50" width="130" height="40" class="box"/>\n'
    '    <text x="425" y="68" class="lbl">Certificats TLS</text>\n'
    '    <text x="425" y="80" class="det">SNI, SANs, ETags</text>\n'
    '    \n'
    '    <rect x="520" y="50" width="130" height="40" class="box"/>\n'
    '    <text x="585" y="68" class="lbl">Bannières HTTP</text>\n'
    '    <text x="585" y="80" class="det">Server, X-Powered-By</text>\n'
    '    \n'
    '    <!-- Items row -->\n'
    '    <line x1="105" y1="90" x2="105" y2="130" class="arr"/>\n'
    '    <line x1="265" y1="90" x2="265" y2="130" class="arr"/>\n'
    '    <line x1="425" y1="90" x2="425" y2="130" class="arr"/>\n'
    '    <line x1="585" y1="90" x2="585" y2="130" class="arr"/>\n'
    '    \n'
    '    <rect x="40" y="132" width="130" height="40" class="box2"/>\n'
    '    <text x="105" y="150" class="lbl">Items d\'information</text>\n'
    '    <text x="105" y="162" class="det">Rôles, liens, compétences</text>\n'
    '    \n'
    '    <rect x="200" y="132" width="130" height="40" class="box2"/>\n'
    '    <text x="265" y="150" class="lbl">Items techniques</text>\n'
    '    <text x="265" y="162" class="det">Stack, outils, frameworks</text>\n'
    '    \n'
    '    <rect x="360" y="132" width="130" height="40" class="box2"/>\n'
    '    <text x="425" y="150" class="lbl">Items réseau</text>\n'
    '    <text x="425" y="162" class="det">IP, ports, services</text>\n'
    '    \n'
    '    <rect x="520" y="132" width="130" height="40" class="box2"/>\n'
    '    <text x="585" y="150" class="lbl">Items vulnérabilité</text>\n'
    '    <text x="585" y="162" class="det">CVE, versions, expositions</text>\n'
    '    \n'
    '    <!-- Inference engine -->\n'
    '    <line x1="105" y1="172" x2="345" y2="210" class="arr"/>\n'
    '    <line x1="265" y1="172" x2="345" y2="210" class="arr"/>\n'
    '    <line x1="425" y1="172" x2="400" y2="210" class="arr"/>\n'
    '    <line x1="585" y1="172" x2="420" y2="210" class="arr"/>\n'
    '    \n'
    '    <rect x="280" y="212" width="220" height="45" class="box3"/>\n'
    '    <text x="390" y="230" class="lbl">Moteur de corrélation</text>\n'
    '    <text x="390" y="242" class="det">Scoring de confiance, propagation</text>\n'
    '    <text x="390" y="252" class="det">dans le graphe d\'inférence</text>\n'
    '    \n'
    '    <!-- Outputs -->\n'
    '    <line x1="340" y1="257" x2="170" y2="290" class="arr"/>\n'
    '    <line x1="390" y1="257" x2="390" y2="290" class="arr"/>\n'
    '    <line x1="440" y1="257" x2="600" y2="290" class="arr"/>\n'
    '    \n'
    '    <rect x="80" y="292" width="180" height="40" class="boxd"/>\n'
    '    <text x="170" y="308" class="lbl">Vecteurs d\'accès</text>\n'
    '    <text x="170" y="320" class="det2">Classés par score de confiance</text>\n'
    '    \n'
    '    <rect x="300" y="292" width="180" height="40" class="boxd"/>\n'
    '    <text x="390" y="308" class="lbl">Cibles prioritaires</text>\n'
    '    <text x="390" y="320" class="det2">Nœuds à forte centralité</text>\n'
    '    \n'
    '    <rect x="520" y="292" width="180" height="40" class="boxd"/>\n'
    '    <text x="610" y="308" class="lbl">Surface d\'attaque</text>\n'
    '    <text x="610" y="320" class="det2">Vulnérabilités exploitables</text>\n'
    '    \n'
    '<line x1="20" y1="355" x2="780" y2="355" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="20" y="373" style="font-family:Times New Roman,serif;font-size:10px;"><tspan font-weight="bold">Figure 4.</tspan> Diagramme d\'inférence d\'information (I2D) appliqué à la phase de reconnaissance. Les sources publiques</text>\n'
    '<text x="20" y="388" style="font-family:Times New Roman,serif;font-size:10px;">alimentent des items d\'information typés, corrélés par un moteur de scoring pour produire l\'intelligence actionnable :</text>\n'
    '<text x="20" y="403" style="font-family:Times New Roman,serif;font-size:10px;">vecteurs d\'accès, cibles prioritaires et surface d\'attaque. Extension du modèle DFD pour la modélisation OSINT [163].</text>\n'
    '\n'
    '</svg>\n'
)

# ────────────────────────────────────────────────────────────
# SVG ANGLAIS (modifiable)
# ────────────────────────────────────────────────────────────
SVG_EN = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<svg xmlns="http://www.w3.org/2000/svg" width="800" height="420" viewBox="0 0 800 420">\n'
    '<style>\n'
    'text { font-family: "Times New Roman", Times, serif; }\n'
    '.title { font-size: 11px; font-weight: bold; text-anchor: middle; }\n'
    '.box { fill: #f5f5f5; stroke: #000; stroke-width: 1; }\n'
    '.box2 { fill: #eee; stroke: #000; stroke-width: 1; }\n'
    '.box3 { fill: #ddd; stroke: #000; stroke-width: 1; }\n'
    '.boxd { fill: none; stroke: #000; stroke-width: 1; stroke-dasharray: 4,2; }\n'
    '.lbl { font-size: 9px; font-weight: bold; text-anchor: middle; }\n'
    '.det { font-size: 8px; text-anchor: middle; fill: #333; }\n'
    '.det2 { font-size: 7.5px; text-anchor: middle; fill: #555; }\n'
    '.sm { font-size: 7px; text-anchor: middle; fill: #666; font-style: italic; }\n'
    '.arr { fill: none; stroke: #000; stroke-width: 0.8; marker-end: url(#a); }\n'
    '.arrd { fill: none; stroke: #000; stroke-width: 0.8; marker-end: url(#a); stroke-dasharray: 3,2; }\n'
    '</style>\n'
    '<defs><marker id="a" markerWidth="7" markerHeight="5" refX="7" refY="2.5" orient="auto"><polygon points="0 0,7 2.5,0 5" fill="#000"/></marker></defs>\n'
    '<text x="400" y="20" class="title">INFORMATION INFERENCE DIAGRAM (I2D) — RECONNAISSANCE PHASE</text>\n'
    '<line x1="20" y1="28" x2="780" y2="28" stroke="#000" stroke-width="0.6"/>\n'
    '\n'
    '    <rect x="40" y="50" width="130" height="40" class="box"/>\n'
    '    <text x="105" y="68" class="lbl">Public sources</text>\n'
    '    <text x="105" y="80" class="det">LinkedIn, Shodan, Censys</text>\n'
    '    \n'
    '    <rect x="200" y="50" width="130" height="40" class="box"/>\n'
    '    <text x="265" y="68" class="lbl">Publications</text>\n'
    '    <text x="265" y="80" class="det">Patents, conferences, GitHub</text>\n'
    '    \n'
    '    <rect x="360" y="50" width="130" height="40" class="box"/>\n'
    '    <text x="425" y="68" class="lbl">TLS Certificates</text>\n'
    '    <text x="425" y="80" class="det">SNI, SANs, ETags</text>\n'
    '    \n'
    '    <rect x="520" y="50" width="130" height="40" class="box"/>\n'
    '    <text x="585" y="68" class="lbl">HTTP Banners</text>\n'
    '    <text x="585" y="80" class="det">Server, X-Powered-By</text>\n'
    '    \n'
    '    <line x1="105" y1="90" x2="105" y2="130" class="arr"/>\n'
    '    <line x1="265" y1="90" x2="265" y2="130" class="arr"/>\n'
    '    <line x1="425" y1="90" x2="425" y2="130" class="arr"/>\n'
    '    <line x1="585" y1="90" x2="585" y2="130" class="arr"/>\n'
    '    \n'
    '    <rect x="40" y="132" width="130" height="40" class="box2"/>\n'
    '    <text x="105" y="150" class="lbl">Information items</text>\n'
    '    <text x="105" y="162" class="det">Roles, links, skills</text>\n'
    '    \n'
    '    <rect x="200" y="132" width="130" height="40" class="box2"/>\n'
    '    <text x="265" y="150" class="lbl">Technical items</text>\n'
    '    <text x="265" y="162" class="det">Stack, tools, frameworks</text>\n'
    '    \n'
    '    <rect x="360" y="132" width="130" height="40" class="box2"/>\n'
    '    <text x="425" y="150" class="lbl">Network items</text>\n'
    '    <text x="425" y="162" class="det">IPs, ports, services</text>\n'
    '    \n'
    '    <rect x="520" y="132" width="130" height="40" class="box2"/>\n'
    '    <text x="585" y="150" class="lbl">Vulnerability items</text>\n'
    '    <text x="585" y="162" class="det">CVEs, versions, exposures</text>\n'
    '    \n'
    '    <line x1="105" y1="172" x2="345" y2="210" class="arr"/>\n'
    '    <line x1="265" y1="172" x2="345" y2="210" class="arr"/>\n'
    '    <line x1="425" y1="172" x2="400" y2="210" class="arr"/>\n'
    '    <line x1="585" y1="172" x2="420" y2="210" class="arr"/>\n'
    '    \n'
    '    <rect x="280" y="212" width="220" height="45" class="box3"/>\n'
    '    <text x="390" y="230" class="lbl">Correlation engine</text>\n'
    '    <text x="390" y="242" class="det">Confidence scoring, propagation</text>\n'
    '    <text x="390" y="252" class="det">through inference graph</text>\n'
    '    \n'
    '    <line x1="340" y1="257" x2="170" y2="290" class="arr"/>\n'
    '    <line x1="390" y1="257" x2="390" y2="290" class="arr"/>\n'
    '    <line x1="440" y1="257" x2="600" y2="290" class="arr"/>\n'
    '    \n'
    '    <rect x="80" y="292" width="180" height="40" class="boxd"/>\n'
    '    <text x="170" y="308" class="lbl">Access vectors</text>\n'
    '    <text x="170" y="320" class="det2">Ranked by confidence score</text>\n'
    '    \n'
    '    <rect x="300" y="292" width="180" height="40" class="boxd"/>\n'
    '    <text x="390" y="308" class="lbl">Priority targets</text>\n'
    '    <text x="390" y="320" class="det2">High-centrality nodes</text>\n'
    '    \n'
    '    <rect x="520" y="292" width="180" height="40" class="boxd"/>\n'
    '    <text x="610" y="308" class="lbl">Attack surface</text>\n'
    '    <text x="610" y="320" class="det2">Exploitable vulnerabilities</text>\n'
    '    \n'
    '<line x1="20" y1="355" x2="780" y2="355" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="20" y="373" style="font-family:Times New Roman,serif;font-size:10px;"><tspan font-weight="bold">Figure 4.</tspan> Information Inference Diagram (I2D) applied to the reconnaissance phase. Public sources feed typed</text>\n'
    '<text x="20" y="388" style="font-family:Times New Roman,serif;font-size:10px;">information items, correlated by a scoring engine to produce actionable intelligence: access vectors, priority targets,</text>\n'
    '<text x="20" y="403" style="font-family:Times New Roman,serif;font-size:10px;">and attack surface. Extension of the DFD model for OSINT modeling [163].</text>\n'
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
        name = f"Figure04_I2D_{suffix}.png"
        path = os.path.join(OUTPUT_DIR, name)
        cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=path, dpi=DPI, output_width=WIDTH)
        print(f"  \u2713 {name} ({os.path.getsize(path)//1024} KB)")


if __name__ == "__main__":
    lang = sys.argv[1].lower() if len(sys.argv) > 1 else None
    generate(lang)
