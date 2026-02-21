#!/usr/bin/env python3
"""
OpenClaw — Figure 18 : EXTORTION
========================================
Generates Figure18_EXTORTION_FR.png and Figure18_EXTORTION_EN.png

EDIT: Change text directly in SVG_FR / SVG_EN below.

Usage:
    python3 fig18_extortion.py              # FR + EN
    python3 fig18_extortion.py fr           # FR only
    python3 fig18_extortion.py en           # EN only

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
    '<svg xmlns="http://www.w3.org/2000/svg" width="720" height="410" viewBox="0 0 720 410">\n'
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
    '<text x="360" y="20" class="title">MÉCANISME DE DOUBLE EXTORSION</text>\n'
    '<line x1="20" y1="28" x2="700" y2="28" stroke="#000" stroke-width="0.6"/>\n'
    '\n'
    '    <rect x="280" y="45" width="160" height="35" class="box3"/>\n'
    '    <text x="360" y="67" class="lbl">PromptLock</text>\n'
    '    \n'
    '    <line x1="320" y1="80" x2="180" y2="110" class="arr"/>\n'
    '    <line x1="400" y1="80" x2="540" y2="110" class="arr"/>\n'
    '    \n'
    '    <rect x="80" y="112" width="200" height="40" class="box"/>\n'
    '    <text x="180" y="130" class="lbl">Chiffrement (T1486)</text>\n'
    '    <text x="180" y="142" class="det">Données inaccessibles</text>\n'
    '    \n'
    '    <rect x="440" y="112" width="200" height="40" class="box2"/>\n'
    '    <text x="540" y="130" class="lbl">Exfiltration (T1041)</text>\n'
    '    <text x="540" y="142" class="det">Données copiées par attaquant</text>\n'
    '    \n'
    '    <line x1="180" y1="152" x2="180" y2="180" class="arr"/>\n'
    '    <line x1="540" y1="152" x2="540" y2="180" class="arr"/>\n'
    '    \n'
    '    <rect x="100" y="182" width="160" height="35" class="box"/>\n'
    '    <text x="180" y="203" class="det">Rançon → clé</text>\n'
    '    \n'
    '    <rect x="460" y="182" width="160" height="45" class="box"/><text x="540" y="200" class="det">Menace publication</text>\n'
    '<text x="540" y="214" class="det">→ leak site</text>\n'
    '\n'
    '    <line x1="180" y1="217" x2="320" y2="260" class="arr"/>\n'
    '    <line x1="540" y1="227" x2="400" y2="260" class="arr"/>\n'
    '    \n'
    '    <rect x="260" y="262" width="200" height="35" class="box3"/>\n'
    '    <text x="360" y="283" class="lbl">Décision victime</text>\n'
    '    \n'
    '    <text x="200" y="320" class="det">Payer</text>\n'
    '    <text x="360" y="320" class="det">Ne pas payer</text>\n'
    '    <text x="520" y="320" class="det">Restaurer</text>\n'
    '    <line x1="310" y1="297" x2="200" y2="310" class="arr"/>\n'
    '    <line x1="360" y1="297" x2="360" y2="310" class="arr"/>\n'
    '    <line x1="410" y1="297" x2="520" y2="310" class="arr"/>\n'
    '    \n'
    '<line x1="20" y1="345" x2="700" y2="345" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="20" y="363" style="font-family:Times New Roman,serif;font-size:10px;"><tspan font-weight="bold">Figure 18.</tspan> Mécanisme de double extorsion. Deux leviers de pression parallèles (chiffrement + menace de</text>\n'
    '<text x="20" y="378" style="font-family:Times New Roman,serif;font-size:10px;">publication) convergent vers la décision de la victime. Le non-paiement est recommandé par l\'ANSSI,</text>\n'
    '<text x="20" y="393" style="font-family:Times New Roman,serif;font-size:10px;">le CISA et Europol, la restauration par sauvegardes immuables constituant la réponse privilégiée.</text>\n'
    '\n'
    '</svg>\n'
)

# ────────────────────────────────────────────────────────────
# SVG ANGLAIS (modifiable)
# ────────────────────────────────────────────────────────────
SVG_EN = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<svg xmlns="http://www.w3.org/2000/svg" width="720" height="410" viewBox="0 0 720 410">\n'
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
    '<text x="360" y="20" class="title">DOUBLE EXTORTION MECHANISM</text>\n'
    '<line x1="20" y1="28" x2="700" y2="28" stroke="#000" stroke-width="0.6"/>\n'
    '\n'
    '    <rect x="280" y="45" width="160" height="35" class="box3"/>\n'
    '    <text x="360" y="67" class="lbl">PromptLock</text>\n'
    '    \n'
    '    <line x1="320" y1="80" x2="180" y2="110" class="arr"/>\n'
    '    <line x1="400" y1="80" x2="540" y2="110" class="arr"/>\n'
    '    \n'
    '    <rect x="80" y="112" width="200" height="40" class="box"/>\n'
    '    <text x="180" y="130" class="lbl">Encryption (T1486)</text>\n'
    '    <text x="180" y="142" class="det">Données inaccessibles</text>\n'
    '    \n'
    '    <rect x="440" y="112" width="200" height="40" class="box2"/>\n'
    '    <text x="540" y="130" class="lbl">Exfiltration (T1041)</text>\n'
    '    <text x="540" y="142" class="det">Données copiées par attaquant</text>\n'
    '    \n'
    '    <line x1="180" y1="152" x2="180" y2="180" class="arr"/>\n'
    '    <line x1="540" y1="152" x2="540" y2="180" class="arr"/>\n'
    '    \n'
    '    <rect x="100" y="182" width="160" height="35" class="box"/>\n'
    '    <text x="180" y="203" class="det">Ransom → key</text>\n'
    '    \n'
    '    <rect x="460" y="182" width="160" height="45" class="box"/><text x="540" y="200" class="det">Publication threat</text>\n'
    '<text x="540" y="214" class="det">→ leak site</text>\n'
    '\n'
    '    <line x1="180" y1="217" x2="320" y2="260" class="arr"/>\n'
    '    <line x1="540" y1="227" x2="400" y2="260" class="arr"/>\n'
    '    \n'
    '    <rect x="260" y="262" width="200" height="35" class="box3"/>\n'
    '    <text x="360" y="283" class="lbl">Victim decision</text>\n'
    '    \n'
    '    <text x="200" y="320" class="det">Pay</text>\n'
    '    <text x="360" y="320" class="det">Do not pay</text>\n'
    '    <text x="520" y="320" class="det">Restore</text>\n'
    '    <line x1="310" y1="297" x2="200" y2="310" class="arr"/>\n'
    '    <line x1="360" y1="297" x2="360" y2="310" class="arr"/>\n'
    '    <line x1="410" y1="297" x2="520" y2="310" class="arr"/>\n'
    '    \n'
    '<line x1="20" y1="345" x2="700" y2="345" stroke="#000" stroke-width="0.5"/>\n'
    '<text x="20" y="363" style="font-family:Times New Roman,serif;font-size:10px;"><tspan font-weight="bold">Figure 18.</tspan> Double extortion mechanism. Two parallel pressure levers (encryption + publication threat)</text>\n'
    '<text x="20" y="378" style="font-family:Times New Roman,serif;font-size:10px;">converge on the victim\'s decision. Non-payment is recommended by ANSSI, CISA, and Europol,</text>\n'
    '<text x="20" y="393" style="font-family:Times New Roman,serif;font-size:10px;">with restoration from immutable backups as the preferred response.</text>\n'
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
        name = f"Figure18_EXTORTION_{suffix}.png"
        path = os.path.join(OUTPUT_DIR, name)
        cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=path, dpi=DPI, output_width=WIDTH)
        print(f"  \u2713 {name} ({os.path.getsize(path)//1024} KB)")


if __name__ == "__main__":
    lang = sys.argv[1].lower() if len(sys.argv) > 1 else None
    generate(lang)
