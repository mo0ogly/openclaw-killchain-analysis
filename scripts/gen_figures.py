#!/usr/bin/env python3
"""
OpenClaw v8 — Figures académiques (FR + EN)
Numérotation dynamique : modifier FIG_START pour décaler toute la série.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Wedge
from matplotlib.collections import PatchCollection
import numpy as np
import os

# ============================================================
# CONFIG — Modifier ici pour décaler la numérotation
# ============================================================
FIG_START = 21  # Premier numéro de figure de cette série
# Les figures seront numérotées FIG_START, FIG_START+1, etc.

OUT = "/home/claude/figures"
os.makedirs(OUT, exist_ok=True)

# Academic style
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif', 'Times New Roman', 'Bitstream Vera Serif'],
    'font.size': 10,
    'axes.titlesize': 11,
    'axes.labelsize': 10,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 8,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.15,
    'axes.linewidth': 0.6,
    'lines.linewidth': 0.8,
})

# Color palette — muted academic
C_PHASE = ['#2166AC', '#4393C3', '#92C5DE', '#D1E5F0', '#F4A582']
C_DARK = '#1a1a2e'
C_ACCENT = '#c0392b'
C_GRAY = '#7f8c8d'
C_BG = '#fafafa'

# ============================================================
# FIGURE 1 — TIMELINE (Gantt)
# ============================================================
def fig_timeline(lang='fr'):
    n = FIG_START
    fig, ax = plt.subplots(figsize=(12, 4.5))
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    
    if lang == 'fr':
        phases = [
            ("Phase 1 — Reconnaissance", -30, -15, C_PHASE[0]),
            ("Phase 2 — Armement", -15, -7, C_PHASE[1]),
            ("Phase 3 — Livraison / Exploitation", -7, 0, C_PHASE[2]),
            ("Phase 4 — Mouvement latéral", 0, 5, C_PHASE[3]),
            ("Phase 5 — Actions sur l'objectif", 5, 6, C_PHASE[4]),
        ]
        milestones = [
            (-30, "Début OSINT\n(LinkedIn, Shodan)", 0),
            (-15, "Arsenal prêt\n(skill, ransomware,\nprompt payloads)", 1),
            (-7, "Skill publiée\nsur ClawHub", 2),
            (-2, "Infostealer\n(vol tokens)", 2),
            (0, "Jour J\nCVE-2024-55591\nexploité", 2),
            (1, "Usurpation\nagent IA", 3),
            (3, "Domain\nAdmin", 3),
            (4, "Sauvegardes\nneutralisées", 3),
            (5, "Exfiltration\ncomplète", 4),
            (6, "PromptLock\ndéployé", 4),
        ]
        title = f"Figure {n} — Chronologie de l'Opération OpenClaw (J−30 à J+6)"
        xlabel = "Jours relatifs au déclenchement (J = exploitation VPN)"
    else:
        phases = [
            ("Phase 1 — Reconnaissance", -30, -15, C_PHASE[0]),
            ("Phase 2 — Weaponization", -15, -7, C_PHASE[1]),
            ("Phase 3 — Delivery / Exploitation", -7, 0, C_PHASE[2]),
            ("Phase 4 — Lateral Movement", 0, 5, C_PHASE[3]),
            ("Phase 5 — Actions on Objectives", 5, 6, C_PHASE[4]),
        ]
        milestones = [
            (-30, "OSINT begins\n(LinkedIn, Shodan)", 0),
            (-15, "Arsenal ready\n(skill, ransomware,\nprompt payloads)", 1),
            (-7, "Malicious skill\npublished on ClawHub", 2),
            (-2, "Infostealer\n(token theft)", 2),
            (0, "D-Day\nCVE-2024-55591\nexploited", 2),
            (1, "Agent\nimpersonation", 3),
            (3, "Domain\nAdmin", 3),
            (4, "Backups\ndestroyed", 3),
            (5, "Full\nexfiltration", 4),
            (6, "PromptLock\ndeployed", 4),
        ]
        title = f"Figure {n} — Operation OpenClaw Timeline (D−30 to D+6)"
        xlabel = "Days relative to trigger (D = VPN exploitation)"
    
    # Draw phases as horizontal bars
    for i, (label, start, end, color) in enumerate(phases):
        y = len(phases) - 1 - i
        ax.barh(y, end - start, left=start, height=0.6, color=color, alpha=0.85,
                edgecolor='white', linewidth=0.5)
        # Label inside bar
        mid = (start + end) / 2
        ax.text(mid, y, label, ha='center', va='center', fontsize=7.5,
                fontweight='bold', color='white' if i < 3 else C_DARK)
    
    # Milestones
    for day, label, phase_idx in milestones:
        y_base = len(phases) - 1 - phase_idx
        ax.plot(day, y_base + 0.35, 'v', color=C_ACCENT, markersize=6, zorder=5)
        ax.text(day, y_base + 0.55, label, ha='center', va='bottom', fontsize=5.5,
                color=C_DARK, linespacing=0.9)
    
    # D-Day line
    ax.axvline(x=0, color=C_ACCENT, linestyle='--', linewidth=0.8, alpha=0.6, zorder=1)
    
    ax.set_xlim(-33, 9)
    ax.set_ylim(-0.5, len(phases) + 0.8)
    ax.set_yticks([])
    ax.set_xlabel(xlabel, fontsize=9)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    
    fig.suptitle(title, fontsize=10.5, fontweight='bold', y=0.98)
    
    fname = f"{OUT}/fig{n}_timeline_{lang}.png"
    fig.savefig(fname)
    plt.close(fig)
    print(f"  ✓ {fname}")


# ============================================================
# FIGURE 2 — KILL CHAIN FLOW
# ============================================================
def fig_killchain_flow(lang='fr'):
    n = FIG_START + 1
    fig, ax = plt.subplots(figsize=(14, 7))
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    
    if lang == 'fr':
        phases_data = [
            ("Phase 1\nReconnaissance", "J−30 → J−15",
             ["OSINT LinkedIn", "Shodan/Censys", "Graphe social", "Fingerprinting"],
             "Intelligence\nactionnable"),
            ("Phase 2\nArmement", "J−15 → J−7",
             ["Skill piégée", "PromptLock (Go)", "Payloads injection", "Deepfake audio"],
             "Arsenal\nopérationnel"),
            ("Phase 3\nLivraison", "J−7 → J",
             ["ClawHub supply chain", "Infostealer (tokens)", "CVE-2024-55591"],
             "3 accès\ninitaux"),
            ("Phase 4\nMouv. latéral", "J → J+5",
             ["Agent fantôme", "Prompt injection Slack", "DCSync → Golden Ticket", "PoisonGPT chatbot"],
             "Contrôle\ncomplet SI"),
            ("Phase 5\nImpact", "J+5 → J+6",
             ["Exfiltration R&D", "PromptLock déployé", "Double extorsion"],
             "Impact\nmaximum"),
        ]
        title = f"Figure {n} — Flux de la kill chain agentique — Opération OpenClaw"
        output_label = "Extrant →"
    else:
        phases_data = [
            ("Phase 1\nReconnaissance", "D−30 → D−15",
             ["LinkedIn OSINT", "Shodan/Censys", "Social graph", "Fingerprinting"],
             "Actionable\nintelligence"),
            ("Phase 2\nWeaponization", "D−15 → D−7",
             ["Malicious skill", "PromptLock (Go)", "Injection payloads", "Audio deepfake"],
             "Operational\narsenal"),
            ("Phase 3\nDelivery", "D−7 → D",
             ["ClawHub supply chain", "Infostealer (tokens)", "CVE-2024-55591"],
             "3 initial\naccess vectors"),
            ("Phase 4\nLateral Mov.", "D → D+5",
             ["Shadow agent", "Slack prompt injection", "DCSync → Golden Ticket", "PoisonGPT chatbot"],
             "Full SI\ncontrol"),
            ("Phase 5\nImpact", "D+5 → D+6",
             ["R&D exfiltration", "PromptLock deployed", "Double extortion"],
             "Maximum\nimpact"),
        ]
        title = f"Figure {n} — Agentic Kill Chain Flow — Operation OpenClaw"
        output_label = "Output →"
    
    box_w, box_h = 2.0, 3.8
    gap = 0.7
    y_base = 1.0
    
    for i, (name, timing, actions, output) in enumerate(phases_data):
        x = i * (box_w + gap)
        
        # Phase box
        rect = FancyBboxPatch((x, y_base), box_w, box_h, boxstyle="round,pad=0.1",
                              facecolor=C_PHASE[i], edgecolor='white', linewidth=1.5, alpha=0.9)
        ax.add_patch(rect)
        
        # Phase name
        ax.text(x + box_w/2, y_base + box_h - 0.35, name, ha='center', va='top',
                fontsize=8, fontweight='bold', color='white', linespacing=0.95)
        
        # Timing
        ax.text(x + box_w/2, y_base + box_h - 1.05, timing, ha='center', va='top',
                fontsize=6.5, color='white', alpha=0.85, style='italic')
        
        # Actions
        for j, action in enumerate(actions):
            y_act = y_base + box_h - 1.5 - j * 0.55
            ax.text(x + 0.15, y_act, f"• {action}", ha='left', va='top',
                    fontsize=6.5, color='white', alpha=0.95)
        
        # Output arrow + label
        if i < len(phases_data) - 1:
            ax.annotate('', xy=(x + box_w + gap - 0.05, y_base + box_h/2),
                       xytext=(x + box_w + 0.05, y_base + box_h/2),
                       arrowprops=dict(arrowstyle='->', color=C_DARK, lw=1.2))
            ax.text(x + box_w + gap/2, y_base + box_h/2 + 0.35, output,
                   ha='center', va='bottom', fontsize=6, color=C_DARK,
                   fontweight='bold', linespacing=0.9,
                   bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                           edgecolor=C_GRAY, alpha=0.9, linewidth=0.5))
    
    ax.set_xlim(-0.3, len(phases_data) * (box_w + gap))
    ax.set_ylim(0.3, y_base + box_h + 0.6)
    ax.set_aspect('equal')
    ax.axis('off')
    
    fig.suptitle(title, fontsize=10.5, fontweight='bold', y=0.97)
    
    fname = f"{OUT}/fig{n}_killchain_flow_{lang}.png"
    fig.savefig(fname)
    plt.close(fig)
    print(f"  ✓ {fname}")


# ============================================================
# FIGURE 3 — LETHAL TRIFECTA (Venn)
# ============================================================
def fig_trifecta(lang='fr'):
    n = FIG_START + 2
    fig, ax = plt.subplots(figsize=(8, 7))
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    
    # Three overlapping circles
    r = 1.8
    centers = [
        (0, 1.1),      # top
        (-1.2, -0.7),  # bottom-left
        (1.2, -0.7),   # bottom-right
    ]
    colors_v = ['#2166AC', '#B2182B', '#1B7837']
    alphas = [0.25, 0.25, 0.25]
    
    if lang == 'fr':
        labels = [
            "Accès aux\ndonnées privées",
            "Exposition au\ncontenu non fiable",
            "Capacité de\ncommunication externe",
        ]
        center_text = "ZONE\nCRITIQUE\n\nOpenClaw\n+ Connecteurs"
        examples = [
            "Fichiers R&D, emails,\ncanaux Slack internes",
            "Pages web, documents\npartagés, messages\nSlack publics",
            "API LLM, requêtes HTTP,\nconnecteurs email/Slack",
        ]
        title = f"Figure {n} — Trifecta létale de Willison appliquée à OpenClaw"
        subtitle = "La co-présence des trois propriétés crée la condition nécessaire à l'exfiltration par prompt injection"
        ref_text = "Source : S. Willison (2026), adapté au scénario MediFrance"
    else:
        labels = [
            "Access to\nprivate data",
            "Exposure to\nuntrusted content",
            "External\ncommunication capability",
        ]
        center_text = "CRITICAL\nZONE\n\nOpenClaw\n+ Connectors"
        examples = [
            "R&D files, emails,\ninternal Slack channels",
            "Web pages, shared\ndocuments, public\nSlack messages",
            "LLM API, HTTP requests,\nemail/Slack connectors",
        ]
        title = f"Figure {n} — Willison's Lethal Trifecta Applied to OpenClaw"
        subtitle = "The co-presence of all three properties creates the necessary condition for prompt injection exfiltration"
        ref_text = "Source: S. Willison (2026), adapted to MediFrance scenario"
    
    for i, ((cx, cy), color, alpha, label) in enumerate(zip(centers, colors_v, alphas, labels)):
        circle = plt.Circle((cx, cy), r, facecolor=color, alpha=alpha,
                           edgecolor=color, linewidth=1.5)
        ax.add_patch(circle)
        
        # Label outside
        if i == 0:
            lx, ly = cx, cy + r + 0.3
        elif i == 1:
            lx, ly = cx - 0.8, cy - r - 0.2
        else:
            lx, ly = cx + 0.8, cy - r - 0.2
        
        ax.text(lx, ly, label, ha='center', va='center' if i == 0 else 'top',
                fontsize=10, fontweight='bold', color=color)
        
        # Examples
        if i == 0:
            ex, ey = cx, cy + r + 0.95
        elif i == 1:
            ex, ey = cx - 0.8, cy - r - 0.85
        else:
            ex, ey = cx + 0.8, cy - r - 0.85
        
        ax.text(ex, ey, examples[i], ha='center', va='center' if i == 0 else 'top',
                fontsize=7, color=C_GRAY, style='italic', linespacing=1.1)
    
    # Center label
    ax.text(0, 0, center_text, ha='center', va='center', fontsize=9,
            fontweight='bold', color=C_ACCENT, linespacing=1.1,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                     edgecolor=C_ACCENT, alpha=0.85, linewidth=1.2))
    
    ax.set_xlim(-4, 4)
    ax.set_ylim(-3.8, 3.8)
    ax.set_aspect('equal')
    ax.axis('off')
    
    fig.suptitle(title, fontsize=10.5, fontweight='bold', y=0.97)
    ax.text(0, -3.3, subtitle, ha='center', va='top', fontsize=8, style='italic', color=C_GRAY)
    ax.text(0, -3.65, ref_text, ha='center', va='top', fontsize=7, color=C_GRAY)
    
    fname = f"{OUT}/fig{n}_trifecta_{lang}.png"
    fig.savefig(fname)
    plt.close(fig)
    print(f"  ✓ {fname}")


# ============================================================
# FIGURE 4 — MITRE ATT&CK HEATMAP
# ============================================================
def fig_mitre_heatmap(lang='fr'):
    n = FIG_START + 3
    
    if lang == 'fr':
        tactics = ["Recon.", "Dév.\nressources", "Accès\ninitial", "Exécution", "Persistance",
                   "Escalade\nprivilèges", "Évasion\ndéfenses", "Accès\ncredentials",
                   "Découverte", "Mouv.\nlatéral", "Collecte", "C2", "Exfiltration", "Impact"]
        phases_labels = ["Phase 1\nRecon.", "Phase 2\nArmement", "Phase 3\nLivraison",
                        "Phase 4\nMouv. lat.", "Phase 5\nImpact"]
        title = f"Figure {n} — Matrice de densité MITRE ATT&CK par phase — Opération OpenClaw"
        cbar_label = "Nombre de techniques identifiées"
    else:
        tactics = ["Recon.", "Resource\nDev.", "Initial\nAccess", "Execution", "Persistence",
                   "Privilege\nEscal.", "Defense\nEvasion", "Credential\nAccess",
                   "Discovery", "Lateral\nMov.", "Collection", "C2", "Exfiltration", "Impact"]
        phases_labels = ["Phase 1\nRecon.", "Phase 2\nWeapon.", "Phase 3\nDelivery",
                        "Phase 4\nLat. Mov.", "Phase 5\nImpact"]
        title = f"Figure {n} — MITRE ATT&CK Density Matrix by Phase — Operation OpenClaw"
        cbar_label = "Number of techniques identified"
    
    # Data: techniques per tactic per phase (estimated from document)
    data = np.array([
        # Recon RD  IA  Exec Pers PEsc DEv  Cred Disc LatM Coll C2   Exf  Imp
        [  4,   1,  0,  0,   0,   0,   0,   0,   2,   0,   1,   0,   0,   0],  # P1
        [  1,   3,  0,  1,   0,   0,   1,   0,   0,   0,   0,   1,   0,   0],  # P2
        [  0,   1,  3,  2,   2,   1,   1,   2,   0,   0,   1,   1,   1,   0],  # P3
        [  0,   0,  1,  3,   2,   3,   2,   3,   2,   2,   3,   2,   3,   1],  # P4
        [  0,   0,  0,  2,   0,   1,   1,   0,   0,   0,   1,   1,   2,   4],  # P5
    ])
    
    fig, ax = plt.subplots(figsize=(13, 4.5))
    fig.patch.set_facecolor('white')
    
    cmap = plt.cm.YlOrRd
    cmap.set_under('white')
    
    im = ax.imshow(data, cmap=cmap, aspect='auto', vmin=0.5, vmax=4,
                   interpolation='nearest')
    
    # Annotations
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            val = data[i, j]
            if val > 0:
                color = 'white' if val >= 3 else C_DARK
                ax.text(j, i, str(val), ha='center', va='center',
                       fontsize=9, fontweight='bold', color=color)
    
    ax.set_xticks(range(len(tactics)))
    ax.set_xticklabels(tactics, fontsize=7, ha='center')
    ax.set_yticks(range(len(phases_labels)))
    ax.set_yticklabels(phases_labels, fontsize=8)
    
    ax.set_xticks(np.arange(-0.5, len(tactics), 1), minor=True)
    ax.set_yticks(np.arange(-0.5, len(phases_labels), 1), minor=True)
    ax.grid(which='minor', color='white', linewidth=1.5)
    ax.tick_params(which='minor', size=0)
    
    cbar = fig.colorbar(im, ax=ax, shrink=0.8, pad=0.02)
    cbar.set_label(cbar_label, fontsize=8)
    
    fig.suptitle(title, fontsize=10, fontweight='bold', y=0.98)
    
    fname = f"{OUT}/fig{n}_mitre_heatmap_{lang}.png"
    fig.savefig(fname)
    plt.close(fig)
    print(f"  ✓ {fname}")


# ============================================================
# FIGURE 5 — EXFILTRATION CHANNELS
# ============================================================
def fig_exfiltration(lang='fr'):
    n = FIG_START + 4
    fig, ax = plt.subplots(figsize=(12, 7))
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    
    if lang == 'fr':
        title = f"Figure {n} — Canaux d'exfiltration : trafic légitime vs. malveillant"
        legend_legit = "Flux légitime"
        legend_mal = "Flux malveillant (camouflé)"
        nodes = {
            'medifrance': ("MediFrance\nSI interne", 1, 4),
            'openclaw': ("Agent\nOpenClaw", 4, 4),
            'gateway': ("Gateway\nOpenClaw", 7, 6),
            'llm': ("API LLM\n(Claude/GPT)", 10, 7),
            'slack': ("Slack\nWorkspace", 7, 4),
            'c2': ("Serveur C2\nAttaquant", 10, 4),
            'email': ("Email\n(Outlook)", 7, 2),
            'exfil_email': ("Boîte mail\nextérieure", 10, 1),
            'fichiers': ("Fichiers R&D\n(NAS/SharePoint)", 1, 2),
            'ad': ("Active\nDirectory", 1, 6),
        }
        note = "Les flux malveillants empruntent les mêmes protocoles (HTTPS/WSS) que les flux légitimes,\nrendant la détection par signature ou destination insuffisante."
    else:
        title = f"Figure {n} — Exfiltration Channels: Legitimate vs. Malicious Traffic"
        legend_legit = "Legitimate flow"
        legend_mal = "Malicious flow (camouflaged)"
        nodes = {
            'medifrance': ("MediFrance\nInternal SI", 1, 4),
            'openclaw': ("OpenClaw\nAgent", 4, 4),
            'gateway': ("OpenClaw\nGateway", 7, 6),
            'llm': ("LLM API\n(Claude/GPT)", 10, 7),
            'slack': ("Slack\nWorkspace", 7, 4),
            'c2': ("C2 Server\nAttacker", 10, 4),
            'email': ("Email\n(Outlook)", 7, 2),
            'exfil_email': ("External\nmailbox", 10, 1),
            'fichiers': ("R&D Files\n(NAS/SharePoint)", 1, 2),
            'ad': ("Active\nDirectory", 1, 6),
        }
        note = "Malicious flows use the same protocols (HTTPS/WSS) as legitimate flows,\nmaking signature or destination-based detection insufficient."
    
    # Draw nodes
    node_colors = {
        'medifrance': '#D6E4F0', 'openclaw': '#2166AC', 'gateway': '#92C5DE',
        'llm': '#D1E5F0', 'slack': '#D1E5F0', 'c2': '#B2182B',
        'email': '#D1E5F0', 'exfil_email': '#F4A582', 'fichiers': '#D6E4F0', 'ad': '#D6E4F0',
    }
    
    for key, (label, x, y) in nodes.items():
        color = node_colors[key]
        text_color = 'white' if key in ('openclaw', 'c2') else C_DARK
        box = FancyBboxPatch((x - 0.65, y - 0.5), 1.3, 1.0, boxstyle="round,pad=0.1",
                            facecolor=color, edgecolor=C_DARK if key != 'c2' else C_ACCENT,
                            linewidth=1.2 if key in ('c2', 'openclaw') else 0.7)
        ax.add_patch(box)
        ax.text(x, y, label, ha='center', va='center', fontsize=7,
               fontweight='bold' if key in ('openclaw', 'c2') else 'normal',
               color=text_color, linespacing=0.95)
    
    # Legitimate flows (blue)
    legit_flows = [
        ('ad', 'openclaw'), ('fichiers', 'openclaw'),
        ('openclaw', 'gateway'), ('gateway', 'llm'),
        ('openclaw', 'slack'), ('openclaw', 'email'),
    ]
    for src, dst in legit_flows:
        sx, sy = nodes[src][1], nodes[src][2]
        dx, dy = nodes[dst][1], nodes[dst][2]
        ax.annotate('', xy=(dx - 0.65 if dx > sx else dx + 0.65, dy),
                   xytext=(sx + 0.65 if dx > sx else sx - 0.65, sy),
                   arrowprops=dict(arrowstyle='->', color='#2166AC', lw=1.5, alpha=0.7))
    
    # Malicious flows (red dashed)
    mal_flows = [
        ('openclaw', 'c2', 'HTTPS\n(skill)'),
        ('slack', 'c2', 'Webhook\n(camouflé)'),
        ('email', 'exfil_email', 'SMTP\n(pièces jointes)'),
    ]
    for src, dst, label in mal_flows:
        sx, sy = nodes[src][1], nodes[src][2]
        dx, dy = nodes[dst][1], nodes[dst][2]
        ax.annotate('', xy=(dx - 0.65, dy),
                   xytext=(sx + 0.65, sy),
                   arrowprops=dict(arrowstyle='->', color=C_ACCENT, lw=2.0,
                                 linestyle='dashed', alpha=0.85))
        mx, my = (sx + dx) / 2, (sy + dy) / 2
        ax.text(mx + 0.1, my + 0.25, label, ha='center', va='bottom', fontsize=6,
               color=C_ACCENT, style='italic', fontweight='bold',
               bbox=dict(boxstyle='round,pad=0.15', facecolor='white', edgecolor=C_ACCENT,
                        alpha=0.85, linewidth=0.5))
    
    # Legend
    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], color='#2166AC', lw=1.5, label=legend_legit),
        Line2D([0], [0], color=C_ACCENT, lw=2, linestyle='dashed', label=legend_mal),
    ]
    ax.legend(handles=legend_elements, loc='lower left', fontsize=8, framealpha=0.9)
    
    ax.text(5.5, 0.3, note, ha='center', va='bottom', fontsize=7, style='italic', color=C_GRAY)
    
    ax.set_xlim(-0.2, 11.5)
    ax.set_ylim(0, 8)
    ax.set_aspect('equal')
    ax.axis('off')
    
    fig.suptitle(title, fontsize=10.5, fontweight='bold', y=0.97)
    
    fname = f"{OUT}/fig{n}_exfiltration_{lang}.png"
    fig.savefig(fname)
    plt.close(fig)
    print(f"  ✓ {fname}")


# ============================================================
# FIGURE 6 — DEFENSE MATURITY RADAR
# ============================================================
def fig_radar(lang='fr'):
    n = FIG_START + 5
    
    if lang == 'fr':
        categories = [
            'C1 — Gouvernance\nde l\'agent',
            'C2 — Contrôle\ndes entrées',
            'C3 — Contrôle\ndes sorties',
            'C4 — Réduction\nde l\'impact',
            'C5 — Hygiène\nfondamentale',
        ]
        title = f"Figure {n} — Radar de maturité défensive — MediFrance SA"
        label_before = "Posture avant l'attaque (estimée)"
        label_after = "Posture recommandée"
    else:
        categories = [
            'C1 — Agent\nGovernance',
            'C2 — Input\nControl',
            'C3 — Output\nControl',
            'C4 — Impact\nReduction',
            'C5 — Basic\nHygiene',
        ]
        title = f"Figure {n} — Defensive Maturity Radar — MediFrance SA"
        label_before = "Pre-attack posture (estimated)"
        label_after = "Recommended posture"
    
    # Scores (0-5)
    before = [0.5, 0.5, 1.0, 1.5, 2.0]  # MediFrance was weak
    after =  [4.0, 3.5, 4.0, 4.5, 4.5]  # Recommended
    
    N = len(categories)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    angles += angles[:1]
    before += before[:1]
    after += after[:1]
    
    fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))
    fig.patch.set_facecolor('white')
    
    # Grid
    ax.set_ylim(0, 5)
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(['1', '2', '3', '4', '5'], fontsize=7, color=C_GRAY)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=8, fontweight='bold')
    
    # Before
    ax.fill(angles, before, alpha=0.15, color=C_ACCENT)
    ax.plot(angles, before, 'o-', color=C_ACCENT, linewidth=1.5, markersize=5, label=label_before)
    
    # After
    ax.fill(angles, after, alpha=0.1, color='#2166AC')
    ax.plot(angles, after, 's--', color='#2166AC', linewidth=1.5, markersize=5, label=label_after)
    
    ax.legend(loc='lower right', bbox_to_anchor=(1.3, -0.05), fontsize=8)
    
    fig.suptitle(title, fontsize=10.5, fontweight='bold', y=0.98)
    
    fname = f"{OUT}/fig{n}_radar_{lang}.png"
    fig.savefig(fname)
    plt.close(fig)
    print(f"  ✓ {fname}")


# ============================================================
# FIGURE 7 — FINANCIAL WATERFALL
# ============================================================
def fig_waterfall(lang='fr'):
    n = FIG_START + 6
    
    if lang == 'fr':
        categories = [
            "Rançon\ndemandée",
            "Arrêt\nproduction\n(5 jours)",
            "Restauration\nSI",
            "Investigation\nforensique",
            "Notification\nRGPD /\namendes",
            "Atteinte\nréputation",
            "TOTAL\nESTIMÉ",
        ]
        title = f"Figure {n} — Impact financier estimé — Opération OpenClaw vs. MediFrance SA"
        ylabel = "Coût estimé (M€)"
        note = "Estimations basées sur : Verizon DBIR 2025, Securin Ransomware Report 2025,\nVikingCloud Statistics 2026, Sophos State of Ransomware 2025"
    else:
        categories = [
            "Ransom\ndemanded",
            "Production\ndowntime\n(5 days)",
            "SI\nrestoration",
            "Forensic\ninvestigation",
            "GDPR\nnotification\n/ fines",
            "Reputation\ndamage",
            "ESTIMATED\nTOTAL",
        ]
        title = f"Figure {n} — Estimated Financial Impact — Operation OpenClaw vs. MediFrance SA"
        ylabel = "Estimated cost (M€)"
        note = "Estimates based on: Verizon DBIR 2025, Securin Ransomware Report 2025,\nVikingCloud Statistics 2026, Sophos State of Ransomware 2025"
    
    values = [2.5, 1.8, 0.8, 0.4, 1.2, 0.8, 7.5]
    is_total = [False, False, False, False, False, False, True]
    
    # Compute waterfall positions
    cumulative = 0
    bottoms = []
    for i, v in enumerate(values):
        if is_total[i]:
            bottoms.append(0)
        else:
            bottoms.append(cumulative)
            cumulative += v
    
    fig, ax = plt.subplots(figsize=(10, 5.5))
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    
    colors = [C_ACCENT if is_total[i] else C_PHASE[i % len(C_PHASE)] for i in range(len(values))]
    
    bars = ax.bar(range(len(values)), values, bottom=bottoms, color=colors,
                  edgecolor='white', linewidth=1, width=0.65, alpha=0.9)
    
    # Value labels
    for i, (v, b) in enumerate(zip(values, bottoms)):
        ax.text(i, b + v + 0.1, f"{v:.1f} M€", ha='center', va='bottom',
               fontsize=9, fontweight='bold', color=C_DARK)
    
    # Connector lines
    for i in range(len(values) - 2):
        top = bottoms[i] + values[i]
        ax.plot([i + 0.35, i + 0.65], [top, top], color=C_GRAY, linewidth=0.5, linestyle=':')
    
    ax.set_xticks(range(len(categories)))
    ax.set_xticklabels(categories, fontsize=7.5)
    ax.set_ylabel(ylabel, fontsize=9)
    ax.set_ylim(0, 9)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    ax.text(len(categories)/2, -1.8, note, ha='center', va='top', fontsize=7,
           style='italic', color=C_GRAY)
    
    fig.suptitle(title, fontsize=10, fontweight='bold', y=0.98)
    
    fname = f"{OUT}/fig{n}_waterfall_{lang}.png"
    fig.savefig(fname)
    plt.close(fig)
    print(f"  ✓ {fname}")


# ============================================================
# GENERATE ALL
# ============================================================
print(f"\nGénération des figures (numérotation à partir de Figure {FIG_START})...\n")

for lang in ['fr', 'en']:
    print(f"\n--- {lang.upper()} ---")
    fig_timeline(lang)
    fig_killchain_flow(lang)
    fig_trifecta(lang)
    fig_mitre_heatmap(lang)
    fig_exfiltration(lang)
    fig_radar(lang)
    fig_waterfall(lang)

print(f"\n✅ 14 figures générées dans {OUT}/")
print(f"   Numérotation : Figure {FIG_START} → Figure {FIG_START + 6}")
print(f"   Pour décaler : modifier FIG_START en haut du script")
