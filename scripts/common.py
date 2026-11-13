"""Tokens e utilitários compartilhados por todos os ativos SVG do perfil.

Tudo aqui é propositalmente simples: SVG puro + CSS interno, sem fontes
externas, sem JavaScript — o que o renderizador do GitHub aceita em <img>.
"""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"

# Paleta (brief)
BG = "#0D1117"      # Graphite
SLATE = "#3B4252"   # Slate
CYAN = "#06B6D4"    # Electric Cyan
LIME = "#84CC16"    # Signal Lime
WHITE = "#F4F4F5"   # Soft White
# Neutros derivados (entre Graphite e Soft White)
LINE = "#1F2733"    # linhas de grade / bordas discretas
MUTED = "#8B95A5"   # texto secundário
PANEL = "#111722"   # superfície levemente elevada

SANS = "'Segoe UI','Helvetica Neue',Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace"

REDUCED = "@media (prefers-reduced-motion:reduce){*{animation:none!important}}"


def e(s):
    return escape(str(s), quote=True)


def text(x, y, s, size=14, fill=WHITE, font=SANS, weight=400, anchor="start",
         ls=0, cls="", extra=""):
    a = f' text-anchor="{anchor}"' if anchor != "start" else ""
    l = f' letter-spacing="{ls}"' if ls else ""
    c = f' class="{cls}"' if cls else ""
    w = f' font-weight="{weight}"' if weight != 400 else ""
    return (f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}"{w}'
            f' fill="{fill}"{a}{l}{c}{extra}>{e(s)}</text>')


def mono(x, y, s, size=11, fill=MUTED, **kw):
    kw.setdefault("ls", 1)
    return text(x, y, s, size=size, fill=fill, font=MONO, **kw)


def mono_w(s, size, ls=1):
    """Largura aproximada de texto monoespaçado."""
    return len(s) * (size * 0.602 + ls)


def pills(x, y, labels, size=13, h=28, gap=8, stroke=SLATE, fill=WHITE):
    out, cx = [], x
    for lab in labels:
        w = mono_w(lab, size, 0.5) + 24
        out.append(f'<rect x="{cx:.1f}" y="{y}" width="{w:.1f}" height="{h}" rx="{h/2}" '
                   f'fill="none" stroke="{stroke}"/>')
        out.append(mono(cx + w / 2, y + h / 2 + size * 0.36, lab, size=size, fill=fill,
                        anchor="middle", ls=0.5))
        cx += w + gap
    return "\n".join(out)


def monogram(x, y, s=1.0, cls=""):
    """Monograma DC: D em branco, C em ciano, com marcas de centro de desenho técnico."""
    c = f' class="{cls}"' if cls else ""
    return f'''<g transform="translate({x},{y}) scale({s})"{c} fill="none">
  <path d="M-6 40H102M48 -6V86" stroke="{SLATE}" stroke-width="0.8" stroke-dasharray="10 3 2 3"/>
  <path d="M18 18V62H30A22 22 0 0 0 30 18Z" stroke="{WHITE}" stroke-width="5" stroke-linejoin="miter"/>
  <path d="M77.6 24.4A22 22 0 1 0 77.6 55.6" stroke="{CYAN}" stroke-width="5"/>
  <circle cx="48" cy="40" r="2.2" fill="{LIME}"/>
</g>'''


def svg(w, h, body, style="", label="", rx=16, border=True, defs=""):
    st = f"<style>{style}{REDUCED if 'animation' in style else ''}</style>" if style else ""
    b = f' stroke="{LINE}"' if border else ""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{e(label)}">
<title>{e(label)}</title>
{st}
<defs>
<pattern id="grid" width="25" height="25" patternUnits="userSpaceOnUse"><path d="M25 0H0V25" fill="none" stroke="{WHITE}" stroke-opacity="0.04"/></pattern>
{defs}
</defs>
<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="{rx}" fill="{BG}"{b}/>
{body}
</svg>
'''


def write(rel, content):
    p = ASSETS / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    return p
