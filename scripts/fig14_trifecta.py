#!/usr/bin/env python3
"""
OpenClaw — Figure 14 : Trifecta
========================================
Generates Figure14_Trifecta_FR.png and Figure14_Trifecta_EN.png

EDIT: Change text directly in SVG_FR / SVG_EN below.

Usage:
    python3 fig14_trifecta.py              # FR + EN
    python3 fig14_trifecta.py fr           # FR only
    python3 fig14_trifecta.py en           # EN only

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
    '<svg xmlns="http://www.w3.org/2000/svg" width="650" height="520" viewBox="0 0 650 520">\n'
    '  <style>\n'
    '    text { font-family: "Times New Roman", Times, serif; }\n'
    '    .title { font-size: 11px; font-weight: bold; text-anchor: middle; }\n'
    '    .circle-label { font-size: 9px; font-weight: bold; text-anchor: middle; }\n'
    '    .circle-detail { font-size: 7.5px; text-anchor: middle; fill: #444; }\n'
    '    .center-label { font-size: 9px; font-weight: bold; text-anchor: middle; fill: #000; }\n'
    '    .center-detail { font-size: 7.5px; text-anchor: middle; fill: #333; }\n'
    '    .caption { font-size: 10px; text-anchor: start; }\n'
    '    .note { font-size: 8px; text-anchor: start; fill: #555; font-style: italic; }\n'
    '  </style>\n'
    '\n'
    '  <text x="325" y="20" class="title">« TRIFECTA LÉTALE » DES AGENTS IA (WILLISON, 2025)</text>\n'
    '  <line x1="30" y1="28" x2="620" y2="28" stroke="#000" stroke-width="0.6"/>\n'
    '\n'
    '  <!-- Three circles - Venn diagram -->\n'
    '  <!-- Circle 1: Private data (top) -->\n'
    '  <circle cx="325" cy="145" r="100" fill="none" stroke="#000" stroke-width="1.2"/>\n'
    '  <text x="325" y="95" class="circle-label">Accès aux données</text>\n'
    '  <text x="325" y="107" class="circle-label">privées</text>\n'
    '  <text x="325" y="125" class="circle-detail">Fichiers R&amp;D, credentials,</text>\n'
    '  <text x="325" y="136" class="circle-detail">bases de données, emails</text>\n'
    '\n'
    '  <!-- Circle 2: Untrusted content (bottom-left) -->\n'
    '  <circle cx="245" cy="275" r="100" fill="none" stroke="#000" stroke-width="1.2"/>\n'
    '  <text x="190" y="295" class="circle-label">Ingestion de</text>\n'
    '  <text x="190" y="307" class="circle-label">contenu non fiable</text>\n'
    '  <text x="190" y="325" class="circle-detail">Messages Slack,</text>\n'
    '  <text x="190" y="336" class="circle-detail">emails, pages web,</text>\n'
    '  <text x="190" y="347" class="circle-detail">documents partagés</text>\n'
    '\n'
    '  <!-- Circle 3: External communications (bottom-right) -->\n'
    '  <circle cx="405" cy="275" r="100" fill="none" stroke="#000" stroke-width="1.2"/>\n'
    '  <text x="460" y="295" class="circle-label">Capacités de</text>\n'
    '  <text x="460" y="307" class="circle-label">communication externe</text>\n'
    '  <text x="460" y="325" class="circle-detail">Requêtes HTTP/HTTPS,</text>\n'
    '  <text x="460" y="336" class="circle-detail">webhooks, API tierces,</text>\n'
    '  <text x="460" y="347" class="circle-detail">connecteurs SaaS</text>\n'
    '\n'
    '  <!-- Center intersection -->\n'
    '  <text x="325" y="230" class="center-label">ZONE DE</text>\n'
    '  <text x="325" y="244" class="center-label">VULNÉRABILITÉ</text>\n'
    '  <text x="325" y="262" class="center-detail">Injection indirecte →</text>\n'
    '  <text x="325" y="274" class="center-detail">exfiltration possible</text>\n'
    '\n'
    '  <!-- OpenClaw annotation -->\n'
    '  <rect x="170" y="385" width="310" height="40" fill="#f0f0f0" stroke="#000" stroke-width="0.8"/>\n'
    '  <text x="325" y="401" class="circle-label">OpenClaw dans le scénario</text>\n'
    '  <text x="325" y="415" class="circle-detail">Réunit les trois conditions : accès fichiers R&amp;D + ingestion Slack + trafic HTTPS sortant</text>\n'
    '\n'
    '  <!-- Arrow from center to annotation -->\n'
    '  <line x1="325" y1="285" x2="325" y2="383" stroke="#000" stroke-width="0.8" marker-end="url(#arr)" stroke-dasharray="3,2"/>\n'
    '\n'
    '  <defs><marker id="arr" markerWidth="7" markerHeight="5" refX="7" refY="2.5" orient="auto"><polygon points="0 0, 7 2.5, 0 5" fill="#000"/></marker></defs>\n'
    '\n'
    '  <!-- Caption -->\n'
    '  <line x1="30" y1="440" x2="620" y2="440" stroke="#000" stroke-width="0.5"/>\n'
    '  <text x="30" y="458" class="caption"><tspan font-weight="bold">Figure 14.</tspan> La « trifecta létale » des agents IA selon Willison [127]. L\'intersection des trois cercles — accès aux</text>\n'
    '  <text x="30" y="473" class="caption">données privées, ingestion de contenu non fiable, et capacités de communication externe — constitue la zone de</text>\n'
    '  <text x="30" y="488" class="caption">vulnérabilité exploitable par injection indirecte de prompt. Dans le scénario OpenClaw, l\'agent réunit les trois</text>\n'
    '  <text x="30" y="503" class="caption">conditions, rendant l\'exfiltration structurellement possible si aucun contrôle dédié n\'est en place.</text>\n'
    '</svg>\n'
)

# ────────────────────────────────────────────────────────────
# SVG ANGLAIS (modifiable)
# ────────────────────────────────────────────────────────────
SVG_EN = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<svg xmlns="http://www.w3.org/2000/svg" width="650" height="520" viewBox="0 0 650 520">\n'
    '  <style>\n'
    '    text { font-family: "Times New Roman", Times, serif; }\n'
    '    .title { font-size: 11px; font-weight: bold; text-anchor: middle; }\n'
    '    .circle-label { font-size: 9px; font-weight: bold; text-anchor: middle; }\n'
    '    .circle-detail { font-size: 7.5px; text-anchor: middle; fill: #444; }\n'
    '    .center-label { font-size: 9px; font-weight: bold; text-anchor: middle; fill: #000; }\n'
    '    .center-detail { font-size: 7.5px; text-anchor: middle; fill: #333; }\n'
    '    .caption { font-size: 10px; text-anchor: start; }\n'
    '  </style>\n'
    '  <defs><marker id="arr" markerWidth="7" markerHeight="5" refX="7" refY="2.5" orient="auto"><polygon points="0 0, 7 2.5, 0 5" fill="#000"/></marker></defs>\n'
    '\n'
    '  <text x="325" y="20" class="title">AI AGENT "LETHAL TRIFECTA" (WILLISON, 2025)</text>\n'
    '  <line x1="30" y1="28" x2="620" y2="28" stroke="#000" stroke-width="0.6"/>\n'
    '\n'
    '  <circle cx="325" cy="145" r="100" fill="none" stroke="#000" stroke-width="1.2"/>\n'
    '  <text x="325" y="95" class="circle-label">Access to</text>\n'
    '  <text x="325" y="107" class="circle-label">private data</text>\n'
    '  <text x="325" y="125" class="circle-detail">R&amp;D files, credentials,</text>\n'
    '  <text x="325" y="136" class="circle-detail">databases, emails</text>\n'
    '\n'
    '  <circle cx="245" cy="275" r="100" fill="none" stroke="#000" stroke-width="1.2"/>\n'
    '  <text x="190" y="295" class="circle-label">Ingestion of</text>\n'
    '  <text x="190" y="307" class="circle-label">untrusted content</text>\n'
    '  <text x="190" y="325" class="circle-detail">Slack messages,</text>\n'
    '  <text x="190" y="336" class="circle-detail">emails, web pages,</text>\n'
    '  <text x="190" y="347" class="circle-detail">shared documents</text>\n'
    '\n'
    '  <circle cx="405" cy="275" r="100" fill="none" stroke="#000" stroke-width="1.2"/>\n'
    '  <text x="460" y="295" class="circle-label">External</text>\n'
    '  <text x="460" y="307" class="circle-label">communication capability</text>\n'
    '  <text x="460" y="325" class="circle-detail">HTTP/HTTPS requests,</text>\n'
    '  <text x="460" y="336" class="circle-detail">webhooks, third-party APIs,</text>\n'
    '  <text x="460" y="347" class="circle-detail">SaaS connectors</text>\n'
    '\n'
    '  <text x="325" y="230" class="center-label">VULNERABILITY</text>\n'
    '  <text x="325" y="244" class="center-label">ZONE</text>\n'
    '  <text x="325" y="262" class="center-detail">Indirect injection →</text>\n'
    '  <text x="325" y="274" class="center-detail">exfiltration possible</text>\n'
    '\n'
    '  <rect x="170" y="385" width="310" height="40" fill="#f0f0f0" stroke="#000" stroke-width="0.8"/>\n'
    '  <text x="325" y="401" class="circle-label">OpenClaw in the scenario</text>\n'
    '  <text x="325" y="415" class="circle-detail">Meets all three conditions: R&amp;D file access + Slack ingestion + outbound HTTPS traffic</text>\n'
    '\n'
    '  <line x1="325" y1="285" x2="325" y2="383" stroke="#000" stroke-width="0.8" marker-end="url(#arr)" stroke-dasharray="3,2"/>\n'
    '\n'
    '  <line x1="30" y1="440" x2="620" y2="440" stroke="#000" stroke-width="0.5"/>\n'
    '  <text x="30" y="458" class="caption"><tspan font-weight="bold">Figure 14.</tspan> The AI agent "lethal trifecta" per Willison [127]. The intersection of the three circles — access to private</text>\n'
    '  <text x="30" y="473" class="caption">data, ingestion of untrusted content, and external communication capabilities — constitutes the vulnerability zone</text>\n'
    '  <text x="30" y="488" class="caption">exploitable via indirect prompt injection. In the OpenClaw scenario, the agent meets all three conditions, making</text>\n'
    '  <text x="30" y="503" class="caption">exfiltration structurally possible absent dedicated controls.</text>\n'
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
        name = f"Figure14_Trifecta_{suffix}.png"
        path = os.path.join(OUTPUT_DIR, name)
        cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=path, dpi=DPI, output_width=WIDTH)
        print(f"  \u2713 {name} ({os.path.getsize(path)//1024} KB)")


if __name__ == "__main__":
    lang = sys.argv[1].lower() if len(sys.argv) > 1 else None
    generate(lang)
