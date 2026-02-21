#!/usr/bin/env python3
"""
OpenClaw — Figure 06 : DECISION
========================================
Generates Figure06_DECISION_FR.png and Figure06_DECISION_EN.png

EDIT: Change text directly in SVG_FR / SVG_EN below.

Usage:
    python3 fig06_decision.py              # FR + EN
    python3 fig06_decision.py fr           # FR only
    python3 fig06_decision.py en           # EN only

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
    '<svg xmlns="http://www.w3.org/2000/svg" width="750" height="400" viewBox="0 0 750 400">\n'
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
    '<text x="375" y="20" class="title">ARBRE DE DÉCISION — RECONNAISSANCE AUTOMATISÉE</text>\n'
    '<line x1="20" y1="28" x2="730" y2="28" stroke="#000" stroke-width="0.6"/>\n'
    '\n'
    '    <rect x="300" y="45" width="150" height="30" class="box3"/>\n'
    '    <text x="375" y="64" class="lbl">Cible identifiée</text>\n'
    '    \n'
    '    <line x1="375" y1="75" x2="375" y2="95" class="arr"/>\n'
    '    \n'
    '    <rect x="280" y="97" width="190" height="30" class="box"/>\n'
    '    <text x="375" y="116" class="det">Empreinte OpenClaw détectée ?</text>\n'
    '    \n'
    '    <line x1="280" y1="112" x2="140" y2="152" class="arr"/>\n'
    '    <text x="195" y="128" class="sm">non</text>\n'
    '    <line x1="470" y1="112" x2="570" y2="152" class="arr"/>\n'
    '    <text x="530" y="128" class="sm">oui</text>\n'
    '    \n'
    '    <rect x="50" y="154" width="180" height="30" class="box"/>\n'
    '    <text x="140" y="173" class="det">VPN Fortinet exposé (CVE) ?</text>\n'
    '    \n'
    '    <rect x="480" y="154" width="180" height="30" class="box"/>\n'
    '    <text x="570" y="173" class="det">Utilisateurs ClawHub identifiés ?</text>\n'
    '    \n'
    '    <line x1="50" y1="169" x2="30" y2="209" class="arr"/>\n'
    '    <text x="28" y="195" class="sm">non</text>\n'
    '    <line x1="230" y1="169" x2="250" y2="209" class="arr"/>\n'
    '    <text x="252" y="195" class="sm">oui</text>\n'
    '    \n'
    '    <line x1="480" y1="169" x2="460" y2="209" class="arr"/>\n'
    '    <text x="458" y="195" class="sm">non</text>\n'
    '    <line x1="660" y1="169" x2="680" y2="209" class="arr"/>\n'
    '    <text x="682" y="195" class="sm">oui</text>\n'
    '    \n'
    '    <rect x="10" y="211" width="80" height="25" class="boxd"/>\n'
    '    <text x="50" y="228" class="det2">Score faible</text>\n'
    '    \n'
    '    <rect x="190" y="211" width="120" height="25" class="box2"/>\n'
    '    <text x="250" y="228" class="det">Vecteur VPN</text>\n'
    '    \n'
    '    <rect x="400" y="211" width="120" height="25" class="boxd"/>\n'
    '    <text x="460" y="228" class="det2">Pivot OSINT</text>\n'
    '    \n'
    '    <rect x="620" y="211" width="110" height="25" class="box2"/>\n'
    '    <text x="675" y="228" class="det">Vecteur supply ch.</text>\n'
    '    \n'
    '    <!-- Convergence -->\n'
    '    <line x1="250" y1="236" x2="350" y2="270" class="arr"/>\n'
    '    <line x1="675" y1="236" x2="450" y2="270" class="arr"/>\n'
    '    \n'
    '    <rect x="300" y="272" width="200" height="35" class="box3"/>\n'
    '    <text x="400" y="288" class="lbl">Intelligence actionnable</text>\n'
    '    <text x="400" y="300" class="det2">Score de confiance → décision go/no-go</text>\n'
    '    \n'
    '<line x1="20" y1="335" x2="730" y2="335" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="20" y="353" style="font-family:Times New Roman,serif;font-size:10px;"><tspan font-weight="bold">Figure 6.</tspan> Arbre de décision de la reconnaissance automatisée. L\'agent évalue séquentiellement la présence</text>\n'
    '<text x="20" y="368" style="font-family:Times New Roman,serif;font-size:10px;">d\'empreintes OpenClaw, de vulnérabilités VPN et d\'utilisateurs ClawHub pour déterminer les vecteurs d\'accès</text>\n'
    '<text x="20" y="383" style="font-family:Times New Roman,serif;font-size:10px;">et produire un score de confiance agrégé orientant la décision d\'engagement (go/no-go).</text>\n'
    '\n'
    '</svg>\n'
)

# ────────────────────────────────────────────────────────────
# SVG ANGLAIS (modifiable)
# ────────────────────────────────────────────────────────────
SVG_EN = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<svg xmlns="http://www.w3.org/2000/svg" width="750" height="400" viewBox="0 0 750 400">\n'
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
    '<text x="375" y="20" class="title">DECISION TREE — AUTOMATED RECONNAISSANCE</text>\n'
    '<line x1="20" y1="28" x2="730" y2="28" stroke="#000" stroke-width="0.6"/>\n'
    '\n'
    '    <rect x="300" y="45" width="150" height="30" class="box3"/>\n'
    '    <text x="375" y="64" class="lbl">Target identified</text>\n'
    '    \n'
    '    <line x1="375" y1="75" x2="375" y2="95" class="arr"/>\n'
    '    \n'
    '    <rect x="280" y="97" width="190" height="30" class="box"/>\n'
    '    <text x="375" y="116" class="det">OpenClaw footprint detected?</text>\n'
    '    \n'
    '    <line x1="280" y1="112" x2="140" y2="152" class="arr"/>\n'
    '    <text x="195" y="128" class="sm">no</text>\n'
    '    <line x1="470" y1="112" x2="570" y2="152" class="arr"/>\n'
    '    <text x="530" y="128" class="sm">yes</text>\n'
    '    \n'
    '    <rect x="50" y="154" width="180" height="30" class="box"/>\n'
    '    <text x="140" y="173" class="det">Fortinet VPN exposed (CVE)?</text>\n'
    '    \n'
    '    <rect x="480" y="154" width="180" height="30" class="box"/>\n'
    '    <text x="570" y="173" class="det">ClawHub users identified?</text>\n'
    '    \n'
    '    <line x1="50" y1="169" x2="30" y2="209" class="arr"/>\n'
    '    <text x="28" y="195" class="sm">no</text>\n'
    '    <line x1="230" y1="169" x2="250" y2="209" class="arr"/>\n'
    '    <text x="252" y="195" class="sm">yes</text>\n'
    '    \n'
    '    <line x1="480" y1="169" x2="460" y2="209" class="arr"/>\n'
    '    <text x="458" y="195" class="sm">no</text>\n'
    '    <line x1="660" y1="169" x2="680" y2="209" class="arr"/>\n'
    '    <text x="682" y="195" class="sm">yes</text>\n'
    '    \n'
    '    <rect x="10" y="211" width="80" height="25" class="boxd"/>\n'
    '    <text x="50" y="228" class="det2">Low score</text>\n'
    '    \n'
    '    <rect x="190" y="211" width="120" height="25" class="box2"/>\n'
    '    <text x="250" y="228" class="det">VPN vector</text>\n'
    '    \n'
    '    <rect x="400" y="211" width="120" height="25" class="boxd"/>\n'
    '    <text x="460" y="228" class="det2">OSINT pivot</text>\n'
    '    \n'
    '    <rect x="620" y="211" width="110" height="25" class="box2"/>\n'
    '    <text x="675" y="228" class="det">Supply ch. vector</text>\n'
    '    \n'
    '    <line x1="250" y1="236" x2="350" y2="270" class="arr"/>\n'
    '    <line x1="675" y1="236" x2="450" y2="270" class="arr"/>\n'
    '    \n'
    '    <rect x="300" y="272" width="200" height="35" class="box3"/>\n'
    '    <text x="400" y="288" class="lbl">Actionable intelligence</text>\n'
    '    <text x="400" y="300" class="det2">Confidence score → go/no-go decision</text>\n'
    '    \n'
    '<line x1="20" y1="335" x2="730" y2="335" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="20" y="353" style="font-family:Times New Roman,serif;font-size:10px;"><tspan font-weight="bold">Figure 6.</tspan> Automated reconnaissance decision tree. The agent sequentially evaluates OpenClaw footprints,</text>\n'
    '<text x="20" y="368" style="font-family:Times New Roman,serif;font-size:10px;">VPN vulnerabilities, and ClawHub users to determine access vectors and produce an aggregated confidence</text>\n'
    '<text x="20" y="383" style="font-family:Times New Roman,serif;font-size:10px;">score driving the engagement decision (go/no-go).</text>\n'
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
        name = f"Figure06_DECISION_{suffix}.png"
        path = os.path.join(OUTPUT_DIR, name)
        cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=path, dpi=DPI, output_width=WIDTH)
        print(f"  \u2713 {name} ({os.path.getsize(path)//1024} KB)")


if __name__ == "__main__":
    lang = sys.argv[1].lower() if len(sys.argv) > 1 else None
    generate(lang)
