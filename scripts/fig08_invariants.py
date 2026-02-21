#!/usr/bin/env python3
"""
OpenClaw — Figure 08 : INVARIANTS
========================================
Generates Figure08_INVARIANTS_FR.png and Figure08_INVARIANTS_EN.png

EDIT: Change text directly in SVG_FR / SVG_EN below.

Usage:
    python3 fig08_invariants.py              # FR + EN
    python3 fig08_invariants.py fr           # FR only
    python3 fig08_invariants.py en           # EN only

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
    '<svg xmlns="http://www.w3.org/2000/svg" width="700" height="370" viewBox="0 0 700 370">\n'
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
    '<text x="350" y="20" class="title">INVARIANTS COMPORTEMENTAUX VS VARIABLES SYNTAXIQUES — PROMPTLOCK</text>\n'
    '<line x1="20" y1="28" x2="680" y2="28" stroke="#000" stroke-width="0.6"/>\n'
    '\n'
    '    <rect x="40" y="45" width="280" height="30" class="box3"/>\n'
    '    <text x="180" y="64" class="lbl">Invariants (détectables)</text>\n'
    '    <rect x="380" y="45" width="280" height="30" class="box"/>\n'
    '    <text x="520" y="64" class="lbl">Variables (polymorphes)</text>\n'
    '    <rect x="40" y="85" width="280" height="26" fill="#e8e8e8" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="180" y="102" class="det">Chiffrement AES en masse (T1486)</text>\n'
    '<rect x="40" y="113" width="280" height="26" fill="#e8e8e8" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="180" y="130" class="det">Suppression Volume Shadow Copies (T1490)</text>\n'
    '<rect x="40" y="141" width="280" height="26" fill="#e8e8e8" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="180" y="158" class="det">Appels API au serveur LLM local</text>\n'
    '<rect x="40" y="169" width="280" height="26" fill="#e8e8e8" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="180" y="186" class="det">Création de note de rançon par cible</text>\n'
    '<rect x="40" y="197" width="280" height="26" fill="#e8e8e8" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="180" y="214" class="det">Exfiltration préalable via HTTPS (T1041)</text>\n'
    '<rect x="40" y="225" width="280" height="26" fill="#e8e8e8" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="180" y="242" class="det">Énumération séquentielle des disques</text>\n'
    '<rect x="380" y="85" width="280" height="26" fill="#f8f8f8" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="520" y="102" class="det">Noms de fichiers du script</text>\n'
    '<rect x="380" y="113" width="280" height="26" fill="#f8f8f8" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="520" y="130" class="det">Structure syntaxique du code</text>\n'
    '<rect x="380" y="141" width="280" height="26" fill="#f8f8f8" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="520" y="158" class="det">Chaînes de caractères, variables</text>\n'
    '<rect x="380" y="169" width="280" height="26" fill="#f8f8f8" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="520" y="186" class="det">Ordre d\'exécution des fonctions</text>\n'
    '<rect x="380" y="197" width="280" height="26" fill="#f8f8f8" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="520" y="214" class="det">Chemins et extensions ciblés</text>\n'
    '<rect x="380" y="225" width="280" height="26" fill="#f8f8f8" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="520" y="242" class="det">User-Agent des requêtes HTTP</text>\n'
    '<rect x="40" y="260" width="620" height="25" class="boxd"/>\n'
    '    <text x="350" y="277" class="sm" style="font-size:8px;">La variabilité syntaxique complexifie la détection par signature mais ne supprime pas les invariants comportementaux.</text>\n'
    '<line x1="20" y1="305" x2="680" y2="305" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="20" y="323" style="font-family:Times New Roman,serif;font-size:10px;"><tspan font-weight="bold">Figure 8.</tspan> Comparaison des invariants comportementaux et des variables syntaxiques de PromptLock.</text>\n'
    '<text x="20" y="338" style="font-family:Times New Roman,serif;font-size:10px;">Les invariants (colonne gauche) restent constants quel que soit le variant généré par le LLM et constituent</text>\n'
    '<text x="20" y="353" style="font-family:Times New Roman,serif;font-size:10px;">les signaux de détection prioritaires pour les solutions EDR comportementales.</text>\n'
    '\n'
    '</svg>\n'
)

# ────────────────────────────────────────────────────────────
# SVG ANGLAIS (modifiable)
# ────────────────────────────────────────────────────────────
SVG_EN = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<svg xmlns="http://www.w3.org/2000/svg" width="700" height="370" viewBox="0 0 700 370">\n'
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
    '<text x="350" y="20" class="title">BEHAVIORAL INVARIANTS VS SYNTACTIC VARIABLES — PROMPTLOCK</text>\n'
    '<line x1="20" y1="28" x2="680" y2="28" stroke="#000" stroke-width="0.6"/>\n'
    '\n'
    '    <rect x="40" y="45" width="280" height="30" class="box3"/>\n'
    '    <text x="180" y="64" class="lbl">Invariants (detectable)</text>\n'
    '    <rect x="380" y="45" width="280" height="30" class="box"/>\n'
    '    <text x="520" y="64" class="lbl">Variables (polymorphic)</text>\n'
    '    <rect x="40" y="85" width="280" height="26" fill="#e8e8e8" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="180" y="102" class="det">Mass AES encryption (T1486)</text>\n'
    '<rect x="40" y="113" width="280" height="26" fill="#e8e8e8" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="180" y="130" class="det">Volume Shadow Copy deletion (T1490)</text>\n'
    '<rect x="40" y="141" width="280" height="26" fill="#e8e8e8" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="180" y="158" class="det">API calls to local LLM server</text>\n'
    '<rect x="40" y="169" width="280" height="26" fill="#e8e8e8" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="180" y="186" class="det">Per-target ransom note creation</text>\n'
    '<rect x="40" y="197" width="280" height="26" fill="#e8e8e8" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="180" y="214" class="det">Prior exfiltration via HTTPS (T1041)</text>\n'
    '<rect x="40" y="225" width="280" height="26" fill="#e8e8e8" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="180" y="242" class="det">Sequential disk enumeration</text>\n'
    '<rect x="380" y="85" width="280" height="26" fill="#f8f8f8" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="520" y="102" class="det">Script file names</text>\n'
    '<rect x="380" y="113" width="280" height="26" fill="#f8f8f8" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="520" y="130" class="det">Code syntactic structure</text>\n'
    '<rect x="380" y="141" width="280" height="26" fill="#f8f8f8" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="520" y="158" class="det">String literals, variables</text>\n'
    '<rect x="380" y="169" width="280" height="26" fill="#f8f8f8" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="520" y="186" class="det">Function execution order</text>\n'
    '<rect x="380" y="197" width="280" height="26" fill="#f8f8f8" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="520" y="214" class="det">Targeted paths and extensions</text>\n'
    '<rect x="380" y="225" width="280" height="26" fill="#f8f8f8" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="520" y="242" class="det">HTTP User-Agent strings</text>\n'
    '<rect x="40" y="260" width="620" height="25" class="boxd"/>\n'
    '    <text x="350" y="277" class="sm" style="font-size:8px;">Syntactic variability complicates signature-based detection but does not eliminate behavioral invariants.</text>\n'
    '<line x1="20" y1="305" x2="680" y2="305" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="20" y="323" style="font-family:Times New Roman,serif;font-size:10px;"><tspan font-weight="bold">Figure 8.</tspan> Comparison of PromptLock behavioral invariants and syntactic variables.</text>\n'
    '<text x="20" y="338" style="font-family:Times New Roman,serif;font-size:10px;">Invariants (left column) remain constant regardless of the LLM-generated variant and constitute</text>\n'
    '<text x="20" y="353" style="font-family:Times New Roman,serif;font-size:10px;">priority detection signals for behavioral EDR solutions.</text>\n'
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
        name = f"Figure08_INVARIANTS_{suffix}.png"
        path = os.path.join(OUTPUT_DIR, name)
        cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=path, dpi=DPI, output_width=WIDTH)
        print(f"  \u2713 {name} ({os.path.getsize(path)//1024} KB)")


if __name__ == "__main__":
    lang = sys.argv[1].lower() if len(sys.argv) > 1 else None
    generate(lang)
