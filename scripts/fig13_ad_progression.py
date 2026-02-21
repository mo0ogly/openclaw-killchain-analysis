#!/usr/bin/env python3
"""
OpenClaw — Figure 13 : AD_Progression
========================================
Generates Figure13_AD_Progression_FR.png and Figure13_AD_Progression_EN.png

EDIT: Change text directly in SVG_FR / SVG_EN below.

Usage:
    python3 fig13_ad_progression.py              # FR + EN
    python3 fig13_ad_progression.py fr           # FR only
    python3 fig13_ad_progression.py en           # EN only

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
    '<svg xmlns="http://www.w3.org/2000/svg" width="750" height="500" viewBox="0 0 750 500">\n'
    '  <style>\n'
    '    text { font-family: "Times New Roman", Times, serif; }\n'
    '    .title { font-size: 11px; font-weight: bold; text-anchor: middle; }\n'
    '    .tier { stroke: #000; stroke-width: 1; }\n'
    '    .label { font-size: 9px; font-weight: bold; text-anchor: middle; }\n'
    '    .detail { font-size: 8px; text-anchor: middle; fill: #333; }\n'
    '    .mitre { font-size: 7.5px; text-anchor: middle; fill: #555; font-family: "Courier New", monospace; }\n'
    '    .defense { font-size: 8px; text-anchor: start; fill: #333; }\n'
    '    .defense-title { font-size: 8px; font-weight: bold; text-anchor: start; fill: #000; }\n'
    '    .arrow { fill: none; stroke: #000; stroke-width: 0.8; marker-end: url(#arr); }\n'
    '    .caption { font-size: 10px; text-anchor: start; }\n'
    '    .block-label { font-size: 7.5px; text-anchor: middle; fill: #666; font-style: italic; }\n'
    '  </style>\n'
    '  <defs><marker id="arr" markerWidth="7" markerHeight="5" refX="7" refY="2.5" orient="auto"><polygon points="0 0, 7 2.5, 0 5" fill="#000"/></marker></defs>\n'
    '\n'
    '  <text x="375" y="20" class="title">PROGRESSION ACTIVE DIRECTORY — MODÈLE DE TIERING</text>\n'
    '  <line x1="30" y1="28" x2="720" y2="28" stroke="#000" stroke-width="0.6"/>\n'
    '\n'
    '  <!-- Left side: Attack progression (staircase) -->\n'
    '  <!-- Tier 2: User workstations -->\n'
    '  <rect x="60" y="260" width="200" height="55" fill="#eee" class="tier"/>\n'
    '  <text x="160" y="278" class="label">Tier 2 — Postes utilisateurs</text>\n'
    '  <text x="160" y="292" class="detail">Credentials locaux, hash NTLM</text>\n'
    '  <text x="160" y="305" class="mitre">T1003.001 (LSASS Memory)</text>\n'
    '\n'
    '  <!-- Tier 1: Application servers -->\n'
    '  <rect x="200" y="180" width="200" height="55" fill="#ddd" class="tier"/>\n'
    '  <text x="300" y="198" class="label">Tier 1 — Serveurs applicatifs</text>\n'
    '  <text x="300" y="212" class="detail">Comptes de service, accès ERP/NAS</text>\n'
    '  <text x="300" y="225" class="mitre">T1021.002 (SMB/Admin Shares)</text>\n'
    '\n'
    '  <!-- Tier 0: Domain controllers -->\n'
    '  <rect x="340" y="100" width="200" height="55" fill="#ccc" class="tier"/>\n'
    '  <text x="440" y="118" class="label">Tier 0 — Contrôleurs de domaine</text>\n'
    '  <text x="440" y="132" class="detail">DCSync → hash KRBTGT → Golden Ticket</text>\n'
    '  <text x="440" y="145" class="mitre">T1003.006 (DCSync) T1558.001 (Golden Ticket)</text>\n'
    '\n'
    '  <!-- Arrows: progression -->\n'
    '  <line x1="220" y1="260" x2="280" y2="237" class="arrow"/>\n'
    '  <text x="235" y="248" class="block-label">élévation</text>\n'
    '  <line x1="360" y1="180" x2="420" y2="157" class="arrow"/>\n'
    '  <text x="375" y="168" class="block-label">élévation</text>\n'
    '\n'
    '  <!-- Top: Domain Admin -->\n'
    '  <rect x="420" y="50" width="160" height="35" fill="#999" class="tier"/>\n'
    '  <text x="500" y="68" class="label" style="fill:#fff;">Domain Admin</text>\n'
    '  <text x="500" y="80" class="detail" style="fill:#eee;">Contrôle total (conditionnel)</text>\n'
    '  <line x1="440" y1="100" x2="480" y2="87" class="arrow"/>\n'
    '\n'
    '  <!-- Right side: Defensive controls at each tier -->\n'
    '  <line x1="570" y1="50" x2="570" y2="320" stroke="#000" stroke-width="0.5" stroke-dasharray="3,2"/>\n'
    '  <text x="580" y="65" class="defense-title">Contrôles défensifs par tier :</text>\n'
    '\n'
    '  <text x="580" y="85" class="defense-title">Tier 0</text>\n'
    '  <text x="580" y="97" class="defense">• Double rotation KRBTGT (invalide Golden Ticket)</text>\n'
    '  <text x="580" y="109" class="defense">• PAM, tiering d\'administration strict</text>\n'
    '  <text x="580" y="121" class="defense">• Monitoring DCSync (Event ID 4662)</text>\n'
    '\n'
    '  <text x="580" y="145" class="defense-title">Tier 1</text>\n'
    '  <text x="580" y="157" class="defense">• Segmentation réseau IT/serveurs</text>\n'
    '  <text x="580" y="169" class="defense">• Comptes de service gérés (gMSA)</text>\n'
    '  <text x="580" y="181" class="defense">• Détection Pass-the-Hash</text>\n'
    '\n'
    '  <text x="580" y="205" class="defense-title">Tier 2</text>\n'
    '  <text x="580" y="217" class="defense">• Credential Guard / protection LSASS</text>\n'
    '  <text x="580" y="229" class="defense">• EDR comportemental</text>\n'
    '  <text x="580" y="241" class="defense">• Restriction des admin locaux</text>\n'
    '\n'
    '  <text x="580" y="270" class="defense-title">Transversal</text>\n'
    '  <text x="580" y="282" class="defense">• MFA sur tous les accès privilégiés</text>\n'
    '  <text x="580" y="294" class="defense">• Audit des authentifications Kerberos</text>\n'
    '  <text x="580" y="306" class="defense">• Principe du moindre privilège</text>\n'
    '\n'
    '  <!-- Condition note -->\n'
    '  <rect x="60" y="330" width="470" height="30" fill="none" stroke="#000" stroke-width="0.8" stroke-dasharray="4,2"/>\n'
    '  <text x="295" y="348" class="block-label" style="font-size:8px;">Condition : la progression au tier supérieur dépend des permissions effectives, de la qualité du raisonnement</text>\n'
    '  <text x="295" y="358" class="block-label" style="font-size:8px;">de l\'agent IA, et de l\'absence de contrôles de détection à chaque niveau.</text>\n'
    '\n'
    '  <!-- Caption -->\n'
    '  <line x1="30" y1="380" x2="720" y2="380" stroke="#000" stroke-width="0.5"/>\n'
    '  <text x="30" y="398" class="caption"><tspan font-weight="bold">Figure 13.</tspan> Progression Active Directory selon le modèle de tiering (Tier 0/1/2). L\'escalier à gauche représente la</text>\n'
    '  <text x="30" y="413" class="caption">trajectoire offensive : du Tier 2 (postes utilisateurs) vers le Tier 0 (contrôleurs de domaine) puis Domain Admin.</text>\n'
    '  <text x="30" y="428" class="caption">Les contrôles défensifs à droite identifient les mécanismes d\'interruption à chaque niveau. La progression n\'est pas</text>\n'
    '  <text x="30" y="443" class="caption">automatique : elle dépend des permissions effectives, de la capacité de l\'agent IA, et des contrôles en place.</text>\n'
    '</svg>\n'
)

# ────────────────────────────────────────────────────────────
# SVG ANGLAIS (modifiable)
# ────────────────────────────────────────────────────────────
SVG_EN = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<svg xmlns="http://www.w3.org/2000/svg" width="750" height="500" viewBox="0 0 750 500">\n'
    '  <style>\n'
    '    text { font-family: "Times New Roman", Times, serif; }\n'
    '    .title { font-size: 11px; font-weight: bold; text-anchor: middle; }\n'
    '    .tier { stroke: #000; stroke-width: 1; }\n'
    '    .label { font-size: 9px; font-weight: bold; text-anchor: middle; }\n'
    '    .detail { font-size: 8px; text-anchor: middle; fill: #333; }\n'
    '    .mitre { font-size: 7.5px; text-anchor: middle; fill: #555; font-family: "Courier New", monospace; }\n'
    '    .defense { font-size: 8px; text-anchor: start; fill: #333; }\n'
    '    .defense-title { font-size: 8px; font-weight: bold; text-anchor: start; fill: #000; }\n'
    '    .arrow { fill: none; stroke: #000; stroke-width: 0.8; marker-end: url(#arr); }\n'
    '    .caption { font-size: 10px; text-anchor: start; }\n'
    '    .block-label { font-size: 7.5px; text-anchor: middle; fill: #666; font-style: italic; }\n'
    '  </style>\n'
    '  <defs><marker id="arr" markerWidth="7" markerHeight="5" refX="7" refY="2.5" orient="auto"><polygon points="0 0, 7 2.5, 0 5" fill="#000"/></marker></defs>\n'
    '\n'
    '  <text x="375" y="20" class="title">ACTIVE DIRECTORY PROGRESSION — TIERING MODEL</text>\n'
    '  <line x1="30" y1="28" x2="720" y2="28" stroke="#000" stroke-width="0.6"/>\n'
    '\n'
    '  <rect x="60" y="260" width="200" height="55" fill="#eee" class="tier"/>\n'
    '  <text x="160" y="278" class="label">Tier 2 — User Workstations</text>\n'
    '  <text x="160" y="292" class="detail">Local credentials, NTLM hashes</text>\n'
    '  <text x="160" y="305" class="mitre">T1003.001 (LSASS Memory)</text>\n'
    '\n'
    '  <rect x="200" y="180" width="200" height="55" fill="#ddd" class="tier"/>\n'
    '  <text x="300" y="198" class="label">Tier 1 — Application Servers</text>\n'
    '  <text x="300" y="212" class="detail">Service accounts, ERP/NAS access</text>\n'
    '  <text x="300" y="225" class="mitre">T1021.002 (SMB/Admin Shares)</text>\n'
    '\n'
    '  <rect x="340" y="100" width="200" height="55" fill="#ccc" class="tier"/>\n'
    '  <text x="440" y="118" class="label">Tier 0 — Domain Controllers</text>\n'
    '  <text x="440" y="132" class="detail">DCSync → KRBTGT hash → Golden Ticket</text>\n'
    '  <text x="440" y="145" class="mitre">T1003.006 (DCSync) T1558.001 (Golden Ticket)</text>\n'
    '\n'
    '  <line x1="220" y1="260" x2="280" y2="237" class="arrow"/>\n'
    '  <text x="235" y="248" class="block-label">escalation</text>\n'
    '  <line x1="360" y1="180" x2="420" y2="157" class="arrow"/>\n'
    '  <text x="375" y="168" class="block-label">escalation</text>\n'
    '\n'
    '  <rect x="420" y="50" width="160" height="35" fill="#999" class="tier"/>\n'
    '  <text x="500" y="68" class="label" style="fill:#fff;">Domain Admin</text>\n'
    '  <text x="500" y="80" class="detail" style="fill:#eee;">Full control (conditional)</text>\n'
    '  <line x1="440" y1="100" x2="480" y2="87" class="arrow"/>\n'
    '\n'
    '  <line x1="570" y1="50" x2="570" y2="320" stroke="#000" stroke-width="0.5" stroke-dasharray="3,2"/>\n'
    '  <text x="580" y="65" class="defense-title">Defensive controls per tier:</text>\n'
    '\n'
    '  <text x="580" y="85" class="defense-title">Tier 0</text>\n'
    '  <text x="580" y="97" class="defense">• Double KRBTGT rotation (invalidates Golden Ticket)</text>\n'
    '  <text x="580" y="109" class="defense">• PAM, strict admin tiering</text>\n'
    '  <text x="580" y="121" class="defense">• DCSync monitoring (Event ID 4662)</text>\n'
    '\n'
    '  <text x="580" y="145" class="defense-title">Tier 1</text>\n'
    '  <text x="580" y="157" class="defense">• Network segmentation IT/servers</text>\n'
    '  <text x="580" y="169" class="defense">• Group Managed Service Accounts (gMSA)</text>\n'
    '  <text x="580" y="181" class="defense">• Pass-the-Hash detection</text>\n'
    '\n'
    '  <text x="580" y="205" class="defense-title">Tier 2</text>\n'
    '  <text x="580" y="217" class="defense">• Credential Guard / LSASS protection</text>\n'
    '  <text x="580" y="229" class="defense">• Behavioral EDR</text>\n'
    '  <text x="580" y="241" class="defense">• Local admin restriction</text>\n'
    '\n'
    '  <text x="580" y="270" class="defense-title">Cross-tier</text>\n'
    '  <text x="580" y="282" class="defense">• MFA on all privileged access</text>\n'
    '  <text x="580" y="294" class="defense">• Kerberos authentication auditing</text>\n'
    '  <text x="580" y="306" class="defense">• Least privilege principle</text>\n'
    '\n'
    '  <rect x="60" y="330" width="470" height="30" fill="none" stroke="#000" stroke-width="0.8" stroke-dasharray="4,2"/>\n'
    '  <text x="295" y="348" class="block-label" style="font-size:8px;">Condition: progression to the next tier depends on effective permissions, AI agent reasoning quality,</text>\n'
    '  <text x="295" y="358" class="block-label" style="font-size:8px;">and the absence of detection controls at each level.</text>\n'
    '\n'
    '  <line x1="30" y1="380" x2="720" y2="380" stroke="#000" stroke-width="0.5"/>\n'
    '  <text x="30" y="398" class="caption"><tspan font-weight="bold">Figure 13.</tspan> Active Directory progression following the tiering model (Tier 0/1/2). The staircase on the left represents</text>\n'
    '  <text x="30" y="413" class="caption">the offensive trajectory: from Tier 2 (user workstations) to Tier 0 (domain controllers) then Domain Admin.</text>\n'
    '  <text x="30" y="428" class="caption">Defensive controls on the right identify disruption mechanisms at each level. Progression is not automatic:</text>\n'
    '  <text x="30" y="443" class="caption">it depends on effective permissions, AI agent capability, and controls in place.</text>\n'
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
        name = f"Figure13_AD_Progression_{suffix}.png"
        path = os.path.join(OUTPUT_DIR, name)
        cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=path, dpi=DPI, output_width=WIDTH)
        print(f"  \u2713 {name} ({os.path.getsize(path)//1024} KB)")


if __name__ == "__main__":
    lang = sys.argv[1].lower() if len(sys.argv) > 1 else None
    generate(lang)
