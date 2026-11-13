"""Cabeçalhos de folha, tabela de conversão, lista de materiais, terminal, rodapé e botões."""
from common import *

SECTIONS = ["IDENTITY", "THE TRANSITION", "ENGINEERING MINDSET", "TECHNOLOGY",
            "SELECTED WORKS", "CURRENT FOCUS", "ACTIVITY", "CONNECTION"]
SLUGS = ["identity", "transition", "mindset", "technology", "works", "focus", "activity", "connection"]


# ---------------------------------------------------------------- cabeçalhos
def header(n, title, total=8):
    W, H = 1000, 78
    x0, x1 = 28, 972
    px = x0 + (x1 - x0) * n / total
    # régua: 80 divisões, traço maior a cada 10
    step = (x1 - x0) / 80
    ticks = "".join(f"M{x0 + i*step:.1f} 66v{-9 if i % 10 == 0 else -4}" for i in range(81))
    css = (f"@keyframes prog{{from{{stroke-dashoffset:1}}to{{stroke-dashoffset:0}}}}"
           f"@keyframes mark{{from{{transform:translateX({x0 - px:.1f}px)}}to{{transform:translateX(0)}}}}"
           f".prog{{stroke-dasharray:1;animation:prog 1.4s cubic-bezier(.2,.8,.2,1) both}}"
           f".mark{{animation:mark 1.4s cubic-bezier(.2,.8,.2,1) both}}")
    b = [
        mono(x0, 44, f"{n:02d}", size=30, fill=CYAN, weight=700, ls=0),
        f'<path d="M78 20L68 50" stroke="{SLATE}" stroke-width="1.5"/>',
        text(92, 44, title, size=25, weight=800, ls=3.5),
        mono(x1, 30, f"FOLHA {n:02d} / {total:02d}", size=10.5, fill=MUTED, anchor="end", ls=1.8),
        f'<path d="{ticks}" stroke="{SLATE}" stroke-width="1"/>',
        f'<path d="M{x0} 66H{x1}" stroke="{SLATE}" stroke-width="1"/>',
        f'<path class="prog" pathLength="1" d="M{x0} 66H{px:.1f}" stroke="{CYAN}" stroke-width="2"/>',
        f'<path class="mark" d="M{px:.1f} 66l-5 -9h10z" fill="{LIME}"/>',
    ]
    return svg(W, H, "\n".join(b), css, f"Folha {n:02d} de {total:02d} — {title}", rx=12, border=False)


# ------------------------------------------------------- tabela de conversão
ROWS = [
    ("Tolerância dimensional", "± 0,02 mm: o limite do aceitável",
     "Tipos e validação", "TypeScript · Zod"),
    ("Encaixe na primeira montagem", "interfaces entre peças",
     "Contratos de API", "REST versionado · Swagger / OpenAPI"),
    ("Desenho técnico", "o que o outro precisa para não errar",
     "Decisões documentadas", "PRD · registro de problemas · README"),
    ("“O que pode falhar aqui?”", "análise antes da fabricação",
     "Concorrência e segurança", "SELECT … FOR UPDATE · auditoria RBAC / IDOR / XSS"),
]
FLOW = ("@keyframes flow{to{stroke-dashoffset:-48}}"
        ".flow{stroke-dasharray:10 14;animation:flow 2.4s linear infinite}")
CONV_LABEL = ("Tabela de conversão: tolerância dimensional vira tipos e validação; encaixe na montagem vira "
              "contratos de API; desenho técnico vira decisões documentadas; a pergunta 'o que pode falhar "
              "aqui?' vira concorrência e segurança.")


def conversion():
    W, H = 1000, 366
    b = [f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="16" fill="url(#grid)"/>',
         mono(32, 40, "TABELA DE CONVERSÃO", size=11, fill=CYAN, ls=2.5),
         mono(968, 40, "DE → PARA", size=11, fill=MUTED, anchor="end", ls=2.5),
         mono(32, 74, "NO PROJETO MECÂNICO", size=9.5, fill=MUTED, ls=2),
         mono(540, 74, "NO SOFTWARE", size=9.5, fill=MUTED, ls=2),
         f'<path d="M32 86H968" stroke="{SLATE}"/>']
    for i, (a, a2, c, c2) in enumerate(ROWS):
        y = 86 + i * 66
        b.append(f'<g class="r{i}">')
        b.append(text(32, y + 30, a, size=19, weight=600))
        b.append(mono(32, y + 50, a2, size=11, fill=MUTED, ls=0.3))
        b.append(f'<path d="M352 {y+33}H506" stroke="{SLATE}" stroke-width="1"/>'
                 f'<path class="flow" d="M352 {y+33}H506" stroke="{CYAN}" stroke-width="1.6"/>'
                 f'<path d="M514 {y+33}l-10 -4.5v9z" fill="{CYAN}"/>')
        b.append(text(540, y + 30, c, size=19, weight=600))
        b.append(mono(540, y + 50, c2, size=11, fill=LIME, ls=0.3))
        if i < 3:
            b.append(f'<path d="M32 {y+66}H968" stroke="{LINE}"/>')
        b.append('</g>')
    return svg(W, H, "\n".join(b), FLOW, CONV_LABEL)


def conversion_mobile():
    W, H = 600, 600
    b = [f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="16" fill="url(#grid)"/>',
         mono(30, 46, "TABELA DE CONVERSÃO", size=14, fill=CYAN, ls=2.5),
         f'<path d="M30 64H570" stroke="{SLATE}"/>']
    for i, (a, a2, c, c2) in enumerate(ROWS):
        y = 64 + i * 132
        b.append(f'<g class="r{i}">')
        b.append(text(30, y + 40, a, size=25, weight=600, fill=MUTED))
        b.append(f'<path d="M40 {y+52}V{y+76}H62" stroke="{CYAN}" stroke-width="1.6" fill="none"/>'
                 f'<path d="M70 {y+76}l-10 -4.5v9z" fill="{CYAN}"/>')
        b.append(text(82, y + 85, c, size=25, weight=700))
        b.append(mono(82, y + 112, c2, size=13.5 if len(c2) < 40 else 11.8, fill=LIME, ls=0))
        if i < 3:
            b.append(f'<path d="M30 {y+132}H570" stroke="{LINE}"/>')
        b.append('</g>')
    return svg(W, H, "\n".join(b), FLOW, CONV_LABEL)


# ------------------------------------------------------- lista de materiais
BOM = [
    ("Linguagens", ["TypeScript", "Java", "JavaScript", "SQL"], "verzel-pass · finance-control"),
    ("Frontend", ["React", "Next.js (App Router)", "Tailwind CSS", "Vite"], "verzel-pass · finance-control"),
    ("Backend", ["Node.js", "Fastify", "Spring Boot", "Spring Security (JWT)"], "verzel-pass · finance-control"),
    ("Dados", ["PostgreSQL", "Prisma", "Flyway", "Spring Data JPA"], "verzel-pass · finance-control"),
    ("Infra", ["Docker", "Git", "Vercel", "Render"], "deploys ativos"),
    ("Em estudo", ["Python", "RAG", "IA aplicada", "Ciência de Dados"], "bootcamp · pós-graduação"),
]
BOM_LABEL = "Lista de materiais (stack): " + "; ".join(
    f"{c}: {', '.join(v)}" for c, v, _ in BOM) + ". A última linha são tecnologias em estudo."


def bom():
    W, H = 1000, 412
    b = [f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="16" fill="url(#grid)"/>',
         mono(32, 40, "LISTA DE MATERIAIS", size=11, fill=CYAN, ls=2.5),
         mono(968, 40, "SOMENTE O QUE ESTÁ NO CÓDIGO", size=11, fill=MUTED, anchor="end", ls=2.5)]
    for x, h in ((32, "ITEM"), (96, "CATEGORIA"), (250, "COMPONENTES"), (748, "COMPROVADO EM")):
        b.append(mono(x, 74, h, size=9.5, fill=MUTED, ls=2))
    b.append(f'<path d="M32 86H968" stroke="{SLATE}"/>')
    for i, (cat, comps, ev) in enumerate(BOM):
        y = 86 + i * 52
        study = i == len(BOM) - 1
        b.append(f'<g class="r{i}">')
        if study:
            b.append(f'<rect x="20" y="{y+6}" width="960" height="40" rx="8" fill="{LIME}" fill-opacity="0.05" '
                     f'stroke="{LIME}" stroke-opacity="0.5" stroke-dasharray="4 4"/>')
        b.append(mono(32, y + 32, f"{i+1:02d}", size=14, fill=LIME if study else CYAN, ls=0))
        b.append(text(96, y + 32, cat, size=17, weight=700, fill=LIME if study else WHITE))
        cx = 250
        t = f'<text x="{cx}" y="{y+32}" font-family="{SANS}" font-size="17" fill="{WHITE}">'
        t += f'<tspan fill="{MUTED}"> · </tspan>'.join(f"<tspan>{e(c)}</tspan>" for c in comps)
        b.append(t + "</text>")
        b.append(mono(748, y + 31, ev, size=11, fill=MUTED, ls=0.2))
        if i < len(BOM) - 2:
            b.append(f'<path d="M32 {y+52}H968" stroke="{LINE}"/>')
        b.append('</g>')
    return svg(W, H, "\n".join(b), "", BOM_LABEL)


def bom_mobile():
    W, H = 600, 690
    b = [f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="16" fill="url(#grid)"/>',
         mono(30, 46, "LISTA DE MATERIAIS", size=14, fill=CYAN, ls=2.5),
         f'<path d="M30 64H570" stroke="{SLATE}"/>']
    for i, (cat, comps, ev) in enumerate(BOM):
        y = 64 + i * 102
        study = i == len(BOM) - 1
        b.append(f'<g class="r{i}">')
        if study:
            b.append(f'<rect x="16" y="{y+8}" width="568" height="88" rx="10" fill="{LIME}" fill-opacity="0.05" '
                     f'stroke="{LIME}" stroke-opacity="0.5" stroke-dasharray="4 4"/>')
        b.append(mono(30, y + 40, f"{i+1:02d}", size=17, fill=LIME if study else CYAN, ls=0))
        b.append(text(70, y + 41, cat, size=24, weight=700, fill=LIME if study else WHITE))
        t = f'<text x="30" y="{y+76}" font-family="{SANS}" font-size="20" fill="{WHITE}">'
        t += f'<tspan fill="{MUTED}"> · </tspan>'.join(f"<tspan>{e(c)}</tspan>" for c in comps)
        b.append(t + "</text>")
        if i < len(BOM) - 2:
            b.append(f'<path d="M30 {y+102}H570" stroke="{LINE}"/>')
        b.append('</g>')
    return svg(W, H, "\n".join(b), "", BOM_LABEL)


# ----------------------------------------------------------------- terminal
FOCUS = [
    ("cursando", "Bootcamp Full Stack +praTi · módulo de Java"),
    ("pós", "Ciência de Dados e Big Data Analytics"),
    ("estudando", "RAG e IA aplicada à engenharia de software"),
    ("buscando", "Estágio / Júnior · Desenvolvedor Full Stack"),
]
CMD = "davi status --agora"
TERM_LABEL = "Terminal — foco atual: " + "; ".join(f"{k}: {v}" for k, v in FOCUS) + "."


def term_css(n_chars, char_w):
    # o conteúdo nunca fica oculto: as linhas começam esmaecidas e "acendem" em sequência
    return ("@keyframes row{from{opacity:.28}to{opacity:1}}"
            + "".join(f".r{i}{{animation:row .3s {1.0 + i*0.5:.2f}s both}}" for i in range(6))
            + "@keyframes blink{0%,49%{opacity:1}50%,100%{opacity:0}}.cur{animation:blink 1.1s step-end infinite}")


def chrome(W, H, title, fs):
    return (f'<path d="M0.5 46H{W-0.5}" stroke="{LINE}"/>'
            + "".join(f'<circle cx="{28 + i*20}" cy="23" r="5.5" fill="none" stroke="{SLATE}" stroke-width="1.4"/>' for i in range(3))
            + mono(W / 2, 28, title, size=fs, fill=MUTED, anchor="middle", ls=0.5))


def terminal():
    W, H = 1000, 262
    fs, cw = 16, 16 * 0.602
    b = [chrome(W, H, "davi@github: ~/agora", 12),
         mono(32, 82, "$", size=fs, fill=LIME, ls=0),
         mono(56, 82, CMD, size=fs, fill=WHITE, ls=0)]
    for i, (k, v) in enumerate(FOCUS):
        y = 118 + i * 30
        b.append(f'<g class="r{i}">' + mono(56, y, k, size=fs, fill=CYAN, ls=0)
                 + mono(196, y, v, size=fs, fill=WHITE, ls=0) + '</g>')
    y = 118 + 4 * 30 + 6
    b.append(f'<g class="r4">' + mono(32, y, "$", size=fs, fill=LIME, ls=0)
             + f'<rect class="cur" x="56" y="{y-15}" width="10" height="19" fill="{WHITE}"/></g>')
    return svg(W, H, "\n".join(b), term_css(len(CMD), cw), TERM_LABEL)


def terminal_mobile():
    W, H = 600, 440
    fs, cw = 20, 20 * 0.602
    b = [chrome(W, H, "davi@github: ~/agora", 14),
         mono(28, 88, "$", size=fs, fill=LIME, ls=0),
         mono(54, 88, CMD, size=fs, fill=WHITE, ls=0)]
    for i, (k, v) in enumerate(FOCUS):
        y = 132 + i * 68
        b.append(f'<g class="r{i}">' + mono(28, y, k, size=15, fill=CYAN, ls=1.5)
                 + mono(28, y + 27, v, size=18 if len(v) < 42 else 16.5, fill=WHITE, ls=0) + '</g>')
    y = 132 + 4 * 68 + 8
    b.append(f'<g class="r4">' + mono(28, y, "$", size=fs, fill=LIME, ls=0)
             + f'<rect class="cur" x="54" y="{y-18}" width="12" height="23" fill="{WHITE}"/></g>')
    return svg(W, H, "\n".join(b), term_css(len(CMD), cw), TERM_LABEL)


# ------------------------------------------------------------------- rodapé
def footer():
    W, H = 1000, 210
    css = ("@keyframes blink{0%,100%{opacity:1}50%{opacity:.25}}.blink{animation:blink 2.4s ease-in-out infinite}"
           "@keyframes spin{to{transform:rotate(360deg)}}.spin{transform-origin:900px 105px;animation:spin 90s linear infinite}")
    b = [f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="16" fill="url(#grid)"/>',
         f'<clipPath id="fc"><rect x="1" y="1" width="{W-2}" height="{H-2}" rx="16"/></clipPath>']
    # fragmento do flange do hero, cortado na borda direita
    cx, cy, R = 900, 105, 150
    import math
    g = [f'<circle cx="{cx}" cy="{cy}" r="{R}" stroke="{WHITE}" stroke-opacity="0.5" stroke-width="1.6"/>',
         f'<circle cx="{cx}" cy="{cy}" r="{R*0.69:.0f}" stroke="{CYAN}" stroke-opacity="0.5" stroke-width="0.8" stroke-dasharray="12 4 2 4"/>',
         f'<circle cx="{cx}" cy="{cy}" r="{R*0.33:.0f}" stroke="{WHITE}" stroke-opacity="0.5" stroke-width="1.6"/>']
    for a in range(0, 360, 60):
        hx, hy = cx + R * 0.69 * math.cos(math.radians(a)), cy + R * 0.69 * math.sin(math.radians(a))
        g.append(f'<circle cx="{hx:.1f}" cy="{hy:.1f}" r="13" stroke="{WHITE}" stroke-opacity="0.5" stroke-width="1.6"/>')
        g.append(f'<circle cx="{hx:.1f}" cy="{hy:.1f}" r="4" fill="{LIME}" fill-opacity="0.8"/>')
    b.append(f'<g clip-path="url(#fc)"><g class="spin" fill="none">{"".join(g)}</g>'
             f'<path d="M{cx-190} {cy}H{W}M{cx} 0V{H}" stroke="{CYAN}" stroke-opacity="0.35" stroke-width="0.8"/></g>')
    b.append(monogram(36, 34, 0.9))
    b.append(text(150, 82, "Toda peça boa começa", size=30, weight=800, ls=-0.3))
    b.append(text(150, 118, "com uma boa conversa.", size=30, weight=800, ls=-0.3))
    b.append(mono(150, 150, "PERSISTÊNCIA · VISÃO · DETERMINAÇÃO", size=11, fill=MUTED, ls=2.5))
    b.append(f'<path d="M36 172H700" stroke="{SLATE}"/>')
    b.append(mono(36, 191, "FOLHA 08 / 08", size=10, fill=MUTED, ls=1.8))
    b.append(f'<circle class="blink" cx="174" cy="187.5" r="3.5" fill="{LIME}"/>')
    b.append(mono(186, 191, "PRÓXIMA REVISÃO: EM ANDAMENTO", size=10, fill=LIME, ls=1.8))
    return svg(W, H, "\n".join(b), css, "Davi Cardozo — Toda peça boa começa com uma boa conversa. "
               "Persistência, visão, determinação. Próxima revisão: em andamento.")


def button(label):
    W, H = 232, 52
    b = [f'<path d="M22 26h16m-6 -5l6 5l-6 5" stroke="{CYAN}" stroke-width="1.8" fill="none"/>',
         mono(52, 31, label, size=13.5, fill=WHITE, ls=2.2)]
    s = svg(W, H, "\n".join(b), "", label.title(), rx=12, border=False)
    return s.replace(f'fill="{BG}"/>', f'fill="{BG}" stroke="{SLATE}"/>', 1)


def build():
    for i, (t, slug) in enumerate(zip(SECTIONS, SLUGS), 1):
        write(f"sections/{i:02d}-{slug}.svg", header(i, t))
    write("graphics/conversion.svg", conversion())
    write("graphics/conversion-mobile.svg", conversion_mobile())
    write("graphics/bom.svg", bom())
    write("graphics/bom-mobile.svg", bom_mobile())
    write("graphics/terminal.svg", terminal())
    write("graphics/terminal-mobile.svg", terminal_mobile())
    write("banners/footer.svg", footer())
    for slug, lab in (("email", "E-MAIL"), ("linkedin", "LINKEDIN"), ("portfolio", "PORTFÓLIO")):
        write(f"icons/btn-{slug}.svg", button(lab))
