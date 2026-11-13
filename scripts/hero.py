"""Hero: um flange de desenho técnico cujos furos se soltam e viram os nós de um
diagrama de sistema. Mesma mentalidade, novo material."""
import math
from common import *

T = 20  # duração do ciclo (s)
NODES = ["ui", "api", "auth", "types", "db", "deploy"]
EDGES = [(0, 1), (1, 2), (3, 4), (4, 5), (0, 3), (1, 4)]
# furo k (ângulo k*60°) -> índice do nó; escolhido para as trajetórias não se cruzarem demais
HOLE_TO_NODE = {5: 0, 0: 1, 1: 4, 4: 2, 2: 3, 3: 5}


def flange(cx, cy, R, fs):
    """Vista frontal de um flange com cotas. Retorna (svg, posições dos furos)."""
    rb, rbore, rh = R * 0.69, R * 0.33, R * 0.092
    holes = [(cx + rb * math.cos(math.radians(a)), cy + rb * math.sin(math.radians(a)))
             for a in range(0, 360, 60)]
    o = []
    ext = R * 1.2
    # linhas de centro
    o.append(f'<path class="draw d2" pathLength="1" d="M{cx-ext} {cy}H{cx+ext}M{cx} {cy-ext}V{cy+ext}" '
             f'stroke="{CYAN}" stroke-opacity="0.55" stroke-width="0.8" fill="none"/>')
    o.append(f'<circle class="dim" cx="{cx}" cy="{cy}" r="{rb:.1f}" fill="none" stroke="{CYAN}" '
             f'stroke-opacity="0.55" stroke-width="0.8" stroke-dasharray="12 4 2 4"/>')
    # contornos
    for r, w, op in ((R, 2, 1), (R * 0.92, 0.8, 0.45), (rbore, 2, 1)):
        o.append(f'<circle class="draw" pathLength="1" cx="{cx}" cy="{cy}" r="{r:.1f}" fill="none" '
                 f'stroke="{WHITE}" stroke-opacity="{op}" stroke-width="{w}" '
                 f'transform="rotate(-90 {cx} {cy})"/>')
    # rasgo de chaveta no furo central
    k = rbore * 0.28
    o.append(f'<path class="draw d2" pathLength="1" d="M{cx-k:.1f} {cy-rbore+1:.1f}V{cy-rbore-k:.1f}H{cx+k:.1f}V{cy-rbore+1:.1f}" '
             f'fill="{BG}" stroke="{WHITE}" stroke-width="2"/>')
    # furos "fantasma" (o que fica na peça depois que os pontos partem)
    for hx, hy in holes:
        o.append(f'<circle class="dim" cx="{hx:.1f}" cy="{hy:.1f}" r="{rh:.1f}" fill="none" '
                 f'stroke="{WHITE}" stroke-opacity="0.4" stroke-width="1" stroke-dasharray="3 3"/>')
    # cota do diâmetro externo
    yd = cy + R * 1.34
    o.append(f'<g class="dim" stroke="{CYAN}" stroke-width="0.9" fill="none">'
             f'<path d="M{cx-R} {cy+R*0.25:.1f}V{yd+5:.1f}M{cx+R} {cy+R*0.25:.1f}V{yd+5:.1f}" stroke-opacity="0.6"/>'
             f'<path d="M{cx-R} {yd:.1f}H{cx+R}"/>'
             f'<path d="M{cx-R} {yd:.1f}l8 -3v6zM{cx+R} {yd:.1f}l-8 -3v6z" fill="{CYAN}" stroke="none"/></g>')
    o.append(mono(cx, yd - 6, "Ø300", size=fs, fill=CYAN, anchor="middle", cls="dim"))
    # chamadas
    hx, hy = holes[5]
    lx = cx + R * 1.12
    o.append(f'<path class="dim" d="M{hx+rh*0.7:.1f} {hy-rh*0.7:.1f}L{lx:.1f} {cy-R*1.08:.1f}h{fs*5.2:.0f}" '
             f'stroke="{CYAN}" stroke-width="0.9" fill="none"/>')
    o.append(mono(lx + 2, cy - R * 1.08 - 6, "6× Ø26", size=fs, fill=CYAN, cls="dim"))
    bx, by = cx - rbore * 0.707, cy - rbore * 0.707
    lx2 = cx - R * 1.12
    o.append(f'<path class="dim" d="M{bx:.1f} {by:.1f}L{lx2:.1f} {cy-R*1.08:.1f}h-{fs*5.6:.0f}" '
             f'stroke="{CYAN}" stroke-width="0.9" fill="none"/>')
    o.append(mono(lx2 - fs * 5.6, cy - R * 1.08 - 6, "Ø100 H7", size=fs, fill=CYAN, cls="dim"))
    return "\n".join(o), holes, rh


def diagram(cols, rows, nw, nh, fs):
    pos = [(x, y) for y in rows for x in cols]
    o = []
    for a, b in EDGES:
        (x1, y1), (x2, y2) = pos[a], pos[b]
        if y1 == y2:
            d = f"M{x1+nw/2} {y1}H{x2-nw/2}"
        else:
            d = f"M{x1} {y1+nh/2}V{y2-nh/2}"
        o.append(f'<path class="edge" pathLength="1" d="{d}" stroke="{CYAN}" stroke-width="1.4" fill="none"/>')
    for (x, y), name in zip(pos, NODES):
        o.append(f'<g class="node"><rect x="{x-nw/2}" y="{y-nh/2}" width="{nw}" height="{nh}" rx="8" '
                 f'fill="{PANEL}" stroke="{SLATE}" stroke-width="1.2"/>'
                 + mono(x - nw / 2 + nw * 0.36, y + fs * 0.35, name, size=fs, fill=WHITE, ls=0.5) + '</g>')
    return "\n".join(o), pos


def travellers(holes, rh, pos, nw):
    """Os seis furos: partem do flange e pousam como indicador de cada nó."""
    o, css = [], []
    for k, (hx, hy) in enumerate(holes):
        n = HOLE_TO_NODE[k]
        tx, ty = pos[n][0] - nw / 2 + nw * 0.19, pos[n][1]
        dx, dy = hx - tx, hy - ty
        s, a = 30 + k * 1.6, 44 + k * 1.6
        css.append(f"@keyframes h{k}{{0%{{transform:translate({dx:.1f}px,{dy:.1f}px);opacity:0}}"
                   f"9%{{transform:translate({dx:.1f}px,{dy:.1f}px);opacity:0}}"
                   f"13%,{s:.1f}%{{transform:translate({dx:.1f}px,{dy:.1f}px);opacity:1}}"
                   f"{a:.1f}%,100%{{transform:translate(0,0);opacity:1}}}}"
                   f".h{k}{{animation:h{k} {T}s cubic-bezier(.65,0,.35,1) infinite}}")
        o.append(f'<g class="h{k}"><circle class="ring" cx="{tx:.1f}" cy="{ty:.1f}" r="{rh:.1f}" fill="{BG}" '
                 f'stroke="{WHITE}" stroke-width="2" opacity="0"/>'
                 f'<circle class="dot" cx="{tx:.1f}" cy="{ty:.1f}" r="{rh*0.5:.1f}" fill="{LIME}"/></g>')
    return "\n".join(o), "".join(css)


def base_css(extra):
    return (
        f"@keyframes scene{{0%{{opacity:0}}3%,95%{{opacity:1}}100%{{opacity:0}}}}"
        f"@keyframes draw{{0%{{stroke-dashoffset:1}}12%,100%{{stroke-dashoffset:0}}}}"
        f"@keyframes draw2{{0%,8%{{stroke-dashoffset:1}}16%,100%{{stroke-dashoffset:0}}}}"
        f"@keyframes dim{{0%,13%{{opacity:0}}20%,100%{{opacity:1}}}}"
        f"@keyframes node{{0%,52%{{opacity:0}}60%,100%{{opacity:1}}}}"
        f"@keyframes edge{{0%,58%{{stroke-dashoffset:1}}68%,100%{{stroke-dashoffset:0}}}}"
        f"@keyframes code{{0%,68%{{opacity:0}}74%,100%{{opacity:1}}}}"
        f"@keyframes ring{{0%,54%{{opacity:1}}59%,100%{{opacity:0}}}}"
        f"@keyframes dot{{0%,54%{{opacity:0}}59%,100%{{opacity:1}}}}"
        f"@keyframes blink{{0%,100%{{opacity:1}}50%{{opacity:.25}}}}"
        f".scene{{animation:scene {T}s linear infinite}}"
        f".draw{{stroke-dasharray:1;animation:draw {T}s ease-out infinite}}"
        f".d2{{animation-name:draw2}}"
        f".dim{{animation:dim {T}s linear infinite}}"
        f".node{{animation:node {T}s linear infinite}}"
        f".edge{{stroke-dasharray:1;animation:edge {T}s ease-in-out infinite}}"
        f".code{{animation:code {T}s linear infinite}}"
        f".ring{{animation:ring {T}s linear infinite}}"
        f".dot{{animation:dot {T}s linear infinite}}"
        f".blink{{animation:blink 2.4s ease-in-out infinite}}" + extra)


LABEL = ("Davi Cardozo — do projeto mecânico ao software. Um flange de desenho técnico "
         "cujos furos se tornam os nós de um diagrama de sistema.")
CODE = "tolerancia: z.number().min(-0.02).max(+0.02)"


def frame(w, h, inset, zones=True):
    o = [f'<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="16" fill="url(#grid)"/>',
         f'<rect x="{inset}" y="{inset}" width="{w-2*inset}" height="{h-2*inset}" fill="none" stroke="{SLATE}" stroke-opacity="0.8"/>']
    if zones:
        n = 8
        zw = (w - 2 * inset) / n
        for i in range(n):
            x = inset + zw * i
            if i:
                o.append(f'<path d="M{x:.1f} {inset-5}v5M{x:.1f} {h-inset}v5" stroke="{SLATE}"/>')
            o.append(mono(x + zw / 2, inset - 5, str(i + 1), size=7.5, fill=SLATE, anchor="middle", ls=0))
        for j, ch in enumerate("ABCD"):
            zh = (h - 2 * inset) / 4
            y = inset + zh * j
            if j:
                o.append(f'<path d="M{inset-5} {y:.1f}h5M{w-inset} {y:.1f}h5" stroke="{SLATE}"/>')
            o.append(mono(inset - 9, y + zh / 2 + 3, ch, size=7.5, fill=SLATE, anchor="middle", ls=0))
    return "\n".join(o)


def desktop(static=False):
    W, H = 1000, 440
    fl, holes, rh = flange(190, 158, 96, 10.5)
    dg, pos = diagram([700, 812, 924], [112, 212], 96, 46, 14)
    tr, tcss = travellers(holes, rh, pos, 96)
    b = [frame(W, H, 20)]
    b.append('<g class="scene">')
    b.append(mono(40, 300, "PEÇA · REV. A", size=9.5, fill=MUTED, ls=2, cls="dim"))
    b.append(fl)
    # eixo de transformação
    b.append(f'<g class="dim"><path d="M330 158H612" stroke="{SLATE}" stroke-dasharray="2 6" fill="none"/>'
             f'<path d="M612 158l-9 -4v8z" fill="{SLATE}"/>'
             + mono(471, 146, "MESMA MENTALIDADE · NOVO MATERIAL", size=9.5, fill=MUTED, anchor="middle", ls=2.2) + '</g>')
    b.append(mono(652, 62, "SISTEMA · REV. B", size=9.5, fill=MUTED, ls=2, cls="node"))
    b.append(dg)
    b.append(mono(652, 270, CODE, size=11, fill=CYAN, ls=0, cls="code"))
    b.append(tr)
    b.append('</g>')
    # faixa de identidade (estática: a identidade não pisca)
    b.append(f'<path d="M20 318H980" stroke="{SLATE}" stroke-opacity="0.8"/>')
    b.append(text(42, 380, "DAVI CARDOZO", size=58, weight=800, ls=-1,
                  extra=' textLength="452" lengthAdjust="spacingAndGlyphs"'))
    b.append(text(44, 405, "Precisão de engenharia, aplicada a software.", size=16.5, fill=MUTED))
    # carimbo (title block)
    x0, x1, x2, x3 = 590, 664, 852, 980
    b.append(f'<path d="M{x0} 318V420M{x1} 318V386M{x2} 318V386M{x1} 352H{x3}M{x0} 386H{x3}" stroke="{SLATE}" stroke-opacity="0.8" fill="none"/>')
    b.append(monogram(x0 + 11, 320, 0.55))
    cells = [(x1, 318, "DESENHADO POR", "D. S. CARDOZO"), (x2, 318, "LOCAL", "RS · BRASIL"),
             (x1, 352, "FUNÇÃO", "DESENVOLVEDOR FULL STACK"), (x2, 352, "FOLHA", "00 / 08")]
    for cx, cy, k, v in cells:
        b.append(mono(cx + 8, cy + 13, k, size=7.5, fill=MUTED, ls=1.2))
        b.append(mono(cx + 8, cy + 27, v, size=10.5, fill=WHITE, ls=0.4))
    b.append(mono(x0 + 10, 399, "STATUS", size=7.5, fill=MUTED, ls=1.2))
    b.append(f'<circle class="blink" cx="{x0+15}" cy="409.5" r="3.5" fill="{LIME}"/>')
    b.append(mono(x0 + 26, 413.5, "ABERTO A OPORTUNIDADES · ESTÁGIO / JÚNIOR", size=10.5, fill=LIME, ls=0.6))
    return svg(W, H, "\n".join(b), "" if static else base_css(tcss), LABEL)


def mobile():
    W, H = 600, 800
    fl, holes, rh = flange(300, 190, 112, 13)
    dg, pos = diagram([140, 300, 460], [452, 540], 132, 56, 18)
    tr, tcss = travellers(holes, rh, pos, 132)
    b = [frame(W, H, 16, zones=False)]
    b.append('<g class="scene">')
    b.append(fl)
    b.append(mono(300, 388, "MESMA MENTALIDADE · NOVO MATERIAL", size=11.5, fill=MUTED, anchor="middle", ls=2.2, cls="dim"))
    b.append(dg)
    b.append(mono(300, 604, CODE, size=13.5, fill=CYAN, ls=0, anchor="middle", cls="code"))
    b.append(tr)
    b.append('</g>')
    b.append(f'<path d="M16 632H584" stroke="{SLATE}" stroke-opacity="0.8"/>')
    b.append(text(38, 706, "DAVI CARDOZO", size=66, weight=800, ls=-1,
                  extra=' textLength="524" lengthAdjust="spacingAndGlyphs"'))
    b.append(text(40, 738, "Precisão de engenharia, aplicada a software.", size=21, fill=MUTED))
    b.append(f'<circle class="blink" cx="45" cy="765" r="4.5" fill="{LIME}"/>')
    b.append(mono(58, 770, "ABERTO A OPORTUNIDADES · ESTÁGIO / JÚNIOR", size=13, fill=LIME, ls=0.6))
    return svg(W, H, "\n".join(b), base_css(tcss), LABEL)


def build():
    write("banners/hero.svg", desktop())
    write("banners/hero-static.svg", desktop(static=True))
    write("banners/hero-mobile.svg", mobile())
