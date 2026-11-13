"""Capas dos projetos: mesma grade editorial, uma ilustração técnica própria para cada um."""
import random
from common import *

W, H = 1000, 320


def art_verzel():
    """Mapa de assentos + ingresso com QR sendo validado."""
    rnd = random.Random(7)
    o = []
    x0, y0, s, g = 632, 58, 22, 9
    sel = (2, 5)
    for r in range(5):
        for c in range(10):
            x, y = x0 + c * (s + g), y0 + r * (s + g)
            if (r, c) == sel:
                o.append(f'<rect class="seat" x="{x}" y="{y}" width="{s}" height="{s}" rx="5" fill="{LIME}"/>')
            elif rnd.random() < 0.38:
                o.append(f'<rect x="{x}" y="{y}" width="{s}" height="{s}" rx="5" fill="{SLATE}" fill-opacity="0.7"/>')
            else:
                o.append(f'<rect x="{x}" y="{y}" width="{s}" height="{s}" rx="5" fill="none" stroke="{SLATE}"/>')
    o.append(mono(x0, y0 - 14, "MAPA DE ASSENTOS · 1 SELECIONADO", size=8.5, fill=MUTED, ls=1.6))
    # ingresso
    tx, ty, tw, th = 716, 202, 236, 92
    o.append(f'<path d="M{tx+8} {ty}H{tx+tw-8}a8 8 0 0 1 8 8V{ty+th-8}a8 8 0 0 1 -8 8H{tx+8}a8 8 0 0 1 -8 -8'
             f'V{ty+th/2+9}a9 9 0 0 0 0 -18V{ty+8}a8 8 0 0 1 8 -8Z" fill="{PANEL}" stroke="{WHITE}" stroke-width="1.6"/>')
    o.append(f'<path d="M{tx+tw-92} {ty+6}V{ty+th-6}" stroke="{WHITE}" stroke-opacity="0.5" stroke-dasharray="3 5"/>')
    o.append(mono(tx + 22, ty + 28, "INGRESSO", size=9, fill=MUTED, ls=2))
    o.append(f'<path d="M{tx+22} {ty+44}h96M{tx+22} {ty+58}h64" stroke="{WHITE}" stroke-opacity="0.7" stroke-width="3" stroke-linecap="round"/>')
    o.append(f'<circle cx="{tx+26}" cy="{ty+74}" r="3.5" fill="{LIME}"/>')
    o.append(mono(tx + 36, ty + 77.5, "VÁLIDO", size=9, fill=LIME, ls=2))
    # QR
    qx, qy, m = tx + tw - 76, ty + 16, 6
    cells = set()
    for r in range(10):
        for c in range(10):
            finder = (r < 3 and c < 3) or (r < 3 and c > 6) or (r > 6 and c < 3)
            if finder:
                if r in (0, 2, 7, 9) or c in (0, 2, 7, 9):
                    cells.add((r, c))
            elif rnd.random() < 0.48:
                cells.add((r, c))
    o.append("".join(f'<rect x="{qx+c*m}" y="{qy+r*m}" width="{m}" height="{m}" fill="{WHITE}"/>' for r, c in sorted(cells)))
    o.append(f'<rect class="scan" x="{qx-5}" y="{qy-1}" width="70" height="2.5" fill="{CYAN}"/>')
    css = ("@keyframes scan{0%,100%{transform:translateY(0)}50%{transform:translateY(60px)}}"
           ".scan{animation:scan 3.2s ease-in-out infinite}"
           "@keyframes seat{0%,100%{fill-opacity:1}50%{fill-opacity:.45}}.seat{animation:seat 2.4s ease-in-out infinite}")
    return "\n".join(o), css


def art_finance():
    """Barras de entradas/saídas e a linha de saldo que continua tracejada: o saldo projetado."""
    o = []
    x0, y0, x1, yb = 640, 52, 952, 250
    for i in range(4):
        y = yb - i * 50
        o.append(f'<path d="M{x0} {y}H{x1}" stroke="{LINE if i else SLATE}"/>')
    ins = [70, 96, 82, 118, 104, 126]
    outs = [58, 74, 90, 80, 96, 88]
    pts = []
    bal = 40
    for i, (a, b) in enumerate(zip(ins, outs)):
        x = x0 + 14 + i * 40
        o.append(f'<rect class="bar" style="animation-delay:{i*0.08:.2f}s" x="{x}" y="{yb-a}" width="12" height="{a}" rx="2" fill="{CYAN}" fill-opacity="0.85"/>')
        o.append(f'<rect class="bar" style="animation-delay:{i*0.08+0.04:.2f}s" x="{x+14}" y="{yb-b}" width="12" height="{b}" rx="2" fill="{SLATE}"/>')
        bal += (a - b) * 0.9
        pts.append((x + 13, yb - 60 - bal))
    d = "M" + "L".join(f"{x:.0f} {y:.0f}" for x, y in pts)
    o.append(f'<path d="{d}" stroke="{WHITE}" stroke-width="2.2" fill="none" stroke-linejoin="round"/>')
    lx, ly = pts[-1]
    ex, ey = x1 - 8, ly - 26
    o.append(f'<path d="M{lx:.0f} {yb+10}V{ly+8:.0f}" stroke="{SLATE}" stroke-dasharray="2 4"/>')
    o.append(mono(lx, yb + 24.5, "HOJE", size=8.5, fill=MUTED, anchor="middle", ls=1.6))
    o.append(f'<path class="proj" pathLength="1" d="M{lx:.0f} {ly:.0f}L{ex} {ey:.0f}" stroke="{LIME}" stroke-width="2.2" fill="none"/>')
    o.append(f'<path d="M{lx:.0f} {ly:.0f}L{ex} {ey:.0f}" stroke="{BG}" stroke-width="3" stroke-dasharray="4 5" fill="none"/>')
    o.append(f'<circle class="pdot" cx="{ex}" cy="{ey:.0f}" r="5" fill="{LIME}"/>')
    o.append(f'<circle cx="{lx:.0f}" cy="{ly:.0f}" r="4" fill="{BG}" stroke="{WHITE}" stroke-width="2"/>')
    o.append(mono(ex + 2, ey - 14, "SALDO PROJETADO", size=8.5, fill=LIME, anchor="end", ls=1.6))
    o.append(f'<rect x="{x0}" y="{yb+16}" width="9" height="9" rx="2" fill="{CYAN}"/>' + mono(x0 + 15, yb + 24.5, "ENTRADAS", size=8.5, ls=1.4))
    o.append(f'<rect x="{x0+96}" y="{yb+16}" width="9" height="9" rx="2" fill="{SLATE}"/>' + mono(x0 + 111, yb + 24.5, "SAÍDAS", size=8.5, ls=1.4))
    css = ("@keyframes proj{0%,20%{stroke-dashoffset:1}70%,100%{stroke-dashoffset:0}}"
           ".proj{stroke-dasharray:1;animation:proj 4.5s ease-in-out infinite}"
           "@keyframes pdot{0%,60%{opacity:0}72%,100%{opacity:1}}.pdot{animation:pdot 4.5s linear infinite}"
           "@keyframes bar{from{transform:scaleY(0)}to{transform:scaleY(1)}}"
           f".bar{{transform-origin:0 {yb}px;animation:bar .8s cubic-bezier(.2,.8,.2,1) both}}")
    return "\n".join(o), css


def art_elite():
    """Três papéis (RBAC) em torno de um núcleo de autenticação."""
    o = []
    cx, cy = 796, 150
    roles = [("ORGANIZER", 796, 58), ("CUSTOMER", 676, 236), ("DOORMAN", 916, 236)]
    o.append(f'<circle cx="{cx}" cy="{cy+18}" r="118" fill="none" stroke="{SLATE}" stroke-opacity="0.6" stroke-dasharray="2 7"/>')
    for i, (name, x, y) in enumerate(roles):
        o.append(f'<path d="M{cx} {cy+18}L{x} {y}" stroke="{SLATE}" stroke-width="1.2"/>')
        o.append(f'<path class="flow" style="animation-delay:{-i*0.8}s" d="M{cx} {cy+18}L{x} {y}" stroke="{CYAN}" stroke-width="1.6"/>')
    for name, x, y in roles:
        w = mono_w(name, 10.5, 1.6) + 26
        o.append(f'<rect x="{x-w/2:.1f}" y="{y-15}" width="{w:.1f}" height="30" rx="15" fill="{PANEL}" stroke="{WHITE}" stroke-width="1.4"/>')
        o.append(mono(x, y + 4, name, size=10.5, fill=WHITE, anchor="middle", ls=1.6))
    # núcleo: cadeado
    o.append(f'<circle cx="{cx}" cy="{cy+18}" r="30" fill="{PANEL}" stroke="{CYAN}" stroke-width="1.6"/>')
    o.append(f'<rect x="{cx-10}" y="{cy+15}" width="20" height="15" rx="3" fill="none" stroke="{LIME}" stroke-width="2"/>'
             f'<path d="M{cx-6} {cy+15}v-5a6 6 0 0 1 12 0v5" fill="none" stroke="{LIME}" stroke-width="2"/>')
    o.append(mono(cx, cy + 66, "RBAC · JWT", size=8.5, fill=MUTED, anchor="middle", ls=1.6))
    css = ("@keyframes flow{to{stroke-dashoffset:-48}}"
           ".flow{stroke-dasharray:6 42;animation:flow 2.4s linear infinite}")
    return "\n".join(o), css


def art_smart():
    """O mesmo produto em três redes: a barra mais curta é o menor preço."""
    o = []
    x0, y0 = 640, 50
    # produto + código de barras (EAN)
    o.append(f'<rect x="{x0}" y="{y0}" width="312" height="62" rx="10" fill="{PANEL}" stroke="{SLATE}"/>')
    o.append(mono(x0 + 16, y0 + 24, "MESMO PRODUTO", size=8.5, fill=MUTED, ls=1.6))
    o.append(f'<path d="M{x0+16} {y0+40}h120" stroke="{WHITE}" stroke-opacity="0.75" stroke-width="3" stroke-linecap="round"/>')
    bars = [2, 1, 3, 1, 2, 1, 1, 3, 2, 1, 3, 1, 1, 2, 1, 3, 1, 2, 2, 1, 3, 1]
    bx = x0 + 206
    for i, wd in enumerate(bars):
        if i % 2 == 0:
            o.append(f'<rect x="{bx}" y="{y0+13}" width="{wd*1.6:.1f}" height="28" fill="{WHITE}"/>')
        bx += wd * 1.6 + 1.2
    o.append(mono(x0 + 206, y0 + 53, "EAN-13", size=7.5, fill=MUTED, ls=2))
    o.append(f'<rect class="scan" x="{x0+202}" y="{y0+12}" width="2" height="30" fill="{CYAN}"/>')
    # três redes
    rows = [("REDE A", 226, False), ("REDE B", 168, True), ("REDE C", 262, False)]
    for i, (name, w, best) in enumerate(rows):
        y = y0 + 96 + i * 50
        o.append(mono(x0, y + 4, name, size=9, fill=LIME if best else MUTED, ls=1.6))
        o.append(f'<rect x="{x0+62}" y="{y-9}" width="250" height="18" rx="4" fill="none" stroke="{LINE}"/>')
        o.append(f'<rect class="pb" style="animation-delay:{i*0.12:.2f}s" x="{x0+62}" y="{y-9}" width="{w*250/262:.0f}" height="18" rx="4" '
                 f'fill="{LIME if best else SLATE}"/>')
        if best:
            o.append(mono(x0 + 62 + w * 250 / 262 + 10, y + 4, "MENOR PREÇO", size=8.5, fill=LIME, ls=1.6))
    o.append(mono(x0, y0 + 240, "8 REDES DO RS · CASAMENTO POR EAN", size=8.5, fill=MUTED, ls=1.6))
    css = ("@keyframes scan{0%,100%{transform:translateX(0)}50%{transform:translateX(88px)}}"
           ".scan{animation:scan 3.2s ease-in-out infinite}"
           "@keyframes pb{from{transform:scaleX(.55)}to{transform:scaleX(1)}}"
           f".pb{{transform-origin:{x0+62}px 0;animation:pb .9s cubic-bezier(.2,.8,.2,1) both}}")
    return "\n".join(o), css


PROJECTS = [
    dict(slug="smartmarket", n=1, rev="EM EQUIPE", name="SmartMarket", art=art_smart,
         lines=["Comparador de preços entre supermercados do Rio Grande",
                "do Sul: a mesma lista de compras, no mercado mais barato."],
         stack=["React 19", "Spring Boot 4", "Python", "PostgreSQL"]),
    dict(slug="verzel-pass", n=2, rev="REV. B", name="Verzel Pass", art=art_verzel,
         lines=["Venda, gestão e validação de ingressos em tempo real:",
                "mapa de assentos, QR Code e controle de concorrência."],
         stack=["Next.js 16", "Fastify 5", "Prisma", "PostgreSQL"]),
    dict(slug="finance-control", n=3, rev="MVP", name="FinanceControl", art=art_finance,
         lines=["Controle financeiro pessoal em formato de planilha,",
                "com o saldo projetado até o fim do mês."],
         stack=["Java 17", "Spring Boot 3", "React 18", "PostgreSQL"]),
    dict(slug="elite-events", n=4, rev="REV. A", name="Elite Events Platform", art=art_elite,
         lines=["O desafio técnico original: eventos e ingressos com",
                "autenticação, RBAC, QR Code e API externa (TMDb)."],
         stack=["Next.js", "Fastify", "Prisma", "PostgreSQL"]),
]


def cover(p):
    art, css = p["art"]()
    size = 46 if len(p["name"]) < 16 else 38
    b = [f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="16" fill="url(#grid)"/>',
         f'<path d="M596 28V292" stroke="{LINE}"/>',
         '<g>',
         mono(40, 58, f"PROJETO {p['n']:02d}", size=11, fill=CYAN, ls=2.5),
         mono(40 + mono_w(f"PROJETO {p['n']:02d}", 11, 2.5) + 10, 58, f"· {p['rev']}", size=11, fill=MUTED, ls=2.5),
         text(38, 122, p["name"], size=size, weight=800, ls=-0.6),
         text(40, 164, p["lines"][0], size=17.5, fill=MUTED),
         text(40, 190, p["lines"][1], size=17.5, fill=MUTED),
         pills(40, 242, p["stack"], size=12.5),
         '</g>',
         art]
    return svg(W, H, "\n".join(b), css, f"{p['name']} — {' '.join(p['lines'])} Stack: {', '.join(p['stack'])}.")


def build():
    for p in PROJECTS:
        write(f"project-covers/{p['slug']}.svg", cover(p))
