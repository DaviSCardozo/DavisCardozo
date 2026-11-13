#!/usr/bin/env python3
"""Gera os cards de projeto do README a partir de um template consistente."""
import os

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

ICONS = {
    "ticket": """
      <path d="M14 30 h44 a4 4 0 0 1 4 4 a7 7 0 0 0 0 14 a4 4 0 0 1 -4 4 h-44 a4 4 0 0 1 -4 -4 a7 7 0 0 0 0 -14 a4 4 0 0 1 4 -4 z" fill="none" stroke="currentColor" stroke-width="2.2"/>
      <line x1="36" y1="30" x2="36" y2="52" stroke="currentColor" stroke-width="2.2" stroke-dasharray="3 4"/>
      <rect x="44" y="36" width="12" height="12" rx="1.5" fill="none" stroke="currentColor" stroke-width="2"/>
      <rect x="47" y="39" width="2.4" height="2.4" fill="currentColor"/>
      <rect x="51.6" y="39" width="2.4" height="2.4" fill="currentColor"/>
      <rect x="47" y="43.6" width="2.4" height="2.4" fill="currentColor"/>
    """,
    "finance": """
      <path d="M14 56 V22" stroke="currentColor" stroke-width="2.2" fill="none"/>
      <path d="M14 56 H58" stroke="currentColor" stroke-width="2.2" fill="none"/>
      <rect x="21" y="40" width="7" height="16" fill="currentColor" opacity="0.85"/>
      <rect x="33" y="30" width="7" height="26" fill="currentColor" opacity="0.85"/>
      <rect x="45" y="36" width="7" height="20" fill="currentColor" opacity="0.85"/>
      <path d="M20 34 L32 24 L41 29 L56 16" fill="none" stroke="currentColor" stroke-width="2" opacity="0.9"/>
      <path d="M48 16 H56 V24" fill="none" stroke="currentColor" stroke-width="2"/>
    """,
    "network": """
      <circle cx="36" cy="20" r="5.5" fill="none" stroke="currentColor" stroke-width="2.2"/>
      <circle cx="16" cy="48" r="5.5" fill="none" stroke="currentColor" stroke-width="2.2"/>
      <circle cx="56" cy="48" r="5.5" fill="none" stroke="currentColor" stroke-width="2.2"/>
      <circle cx="36" cy="58" r="4" fill="currentColor"/>
      <path d="M32 24.5 L20 43.5 M40 24.5 L52 43.5 M21 48 H51" stroke="currentColor" stroke-width="1.6" fill="none"/>
    """,
    "journal": """
      <path d="M16 18 H44 a4 4 0 0 1 4 4 V58 H20 a4 4 0 0 1 -4 -4 Z" fill="none" stroke="currentColor" stroke-width="2.2"/>
      <path d="M16 18 V54 a4 4 0 0 0 4 4 h28" fill="none" stroke="currentColor" stroke-width="2.2"/>
      <line x1="24" y1="28" x2="40" y2="28" stroke="currentColor" stroke-width="1.8"/>
      <line x1="24" y1="35" x2="40" y2="35" stroke="currentColor" stroke-width="1.8"/>
      <line x1="24" y1="42" x2="34" y2="42" stroke="currentColor" stroke-width="1.8"/>
    """,
}

PROJECTS = [
    dict(
        file="verzel-pass.svg",
        icon="ticket",
        tag="LIVE", tag_color="#84CC16",
        title="Verzel Pass — Redesign",
        desc="Plataforma de ingressos em tempo real: QR Code, mapa de assentos, concorrência segura e auditoria própria de seguranca.",
        stack=["Next.js 16", "Fastify", "Prisma", "PostgreSQL"],
    ),
    dict(
        file="finance-control.svg",
        icon="finance",
        tag="LIVE", tag_color="#84CC16",
        title="FinanceControl",
        desc="Controle financeiro pessoal com saldo projetado, dashboards e tabela estilo planilha em tempo real.",
        stack=["Spring Boot", "React", "TanStack Table", "Recharts"],
    ),
    dict(
        file="ai-portfolio.svg",
        icon="network",
        tag="ÍNDICE", tag_color="#06B6D4",
        title="AI Portfolio Hub",
        desc="Repositório central dos meus projetos com IA: engenharia de prompts, agentes autônomos e sistemas RAG.",
        stack=["LangChain", "Spring AI", "Gemini", "Agentic Skills"],
    ),
    dict(
        file="daily-dev-studies.svg",
        icon="journal",
        tag="EM EVOLUÇÃO", tag_color="#7b8a9c",
        title="Daily Dev Studies",
        desc="Diário técnico da minha transição de carreira: exercícios, projetos e arquitetura, documentados dia a dia.",
        stack=["TypeScript", "Node.js", "SQL", "Arquitetura"],
    ),
]

TEMPLATE = """<svg viewBox="0 0 1000 220" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{title}">
  <defs>
    <linearGradient id="bar-{key}" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#06B6D4"/>
      <stop offset="100%" stop-color="#84CC16"/>
    </linearGradient>
  </defs>
  <g opacity="0">
    <animate attributeName="opacity" from="0" to="1" dur="0.5s" fill="freeze"/>
    <rect x="1" y="1" width="998" height="218" rx="14" fill="#0d121c" stroke="#1b2432" stroke-width="1"/>
    <rect x="1" y="1" width="8" height="218" rx="4" fill="url(#bar-{key})"/>

    <g transform="translate(40,30)" color="#84CC16">
      {icon}
    </g>

    <rect x="{tag_x}" y="28" width="{tag_w}" height="26" rx="13" fill="none" stroke="{tag_color}" stroke-width="1.3"/>
    <text x="{tag_tx}" y="45.5" font-family="'SFMono-Regular',Consolas,Menlo,monospace" font-size="11.5" letter-spacing="1.2" fill="{tag_color}" text-anchor="middle">{tag}</text>

    <text x="40" y="128" font-family="'Segoe UI',Helvetica,Arial,sans-serif" font-size="28" font-weight="700" fill="#F4F4F5">{title}</text>
    <text x="40" y="160" font-family="'Segoe UI',Helvetica,Arial,sans-serif" font-size="15" fill="#9aa5b4">
      <tspan x="40" dy="0">{desc_l1}</tspan>
      <tspan x="40" dy="21">{desc_l2}</tspan>
    </text>

    <g font-family="'SFMono-Regular',Consolas,Menlo,monospace" font-size="11.5" fill="#aeb9c7">
      {stack_chips}
    </g>
  </g>
</svg>
"""

def wrap_desc(desc, width=72):
    words = desc.split()
    l1, l2 = [], []
    cur = l1
    length = 0
    for w in words:
        if cur is l1 and length + len(w) + 1 > width:
            cur = l2
            length = 0
        cur.append(w)
        length += len(w) + 1
    return " ".join(l1), " ".join(l2)

def chips(stack, y=198):
    x = 40
    out = []
    for s in stack:
        w = 14 + len(s) * 7.2
        out.append(
            f'<rect x="{x:.1f}" y="{y-18}" width="{w:.1f}" height="24" rx="12" fill="none" stroke="#1f2a38"/>'
            f'<text x="{x+w/2:.1f}" y="{y-2}" text-anchor="middle">{s}</text>'
        )
        x += w + 10
    return "\n      ".join(out)

for p in PROJECTS:
    desc_l1, desc_l2 = wrap_desc(p["desc"])
    tag_w = 24 + len(p["tag"]) * 8.2
    tag_x = 950 - tag_w
    svg = TEMPLATE.format(
        key=p["file"].split(".")[0],
        icon=ICONS[p["icon"]],
        title=p["title"],
        desc_l1=desc_l1,
        desc_l2=desc_l2,
        tag=p["tag"],
        tag_color=p["tag_color"],
        tag_w=f"{tag_w:.1f}",
        tag_x=f"{tag_x:.1f}",
        tag_tx=f"{tag_x + tag_w/2:.1f}",
        stack_chips=chips(p["stack"]),
    )
    out_path = os.path.join(OUT_DIR, p["file"])
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print("wrote", out_path)
