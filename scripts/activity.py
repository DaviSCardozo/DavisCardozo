"""Painel de atividade — métricas reais, desenhadas na identidade do perfil.

  python scripts/activity.py          -> redesenha o SVG a partir de data/activity.json
  python scripts/activity.py --fetch  -> busca dados atuais na API do GitHub (usa GITHUB_TOKEN)
                                         e só então redesenha. Se a API falhar, o SVG anterior
                                         permanece no repositório: esse é o fallback estático.
"""
import datetime as dt
import json
import os
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(__file__))
from common import *

DATA = ROOT / "data" / "activity.json"
MONTHS = ["JAN", "FEV", "MAR", "ABR", "MAI", "JUN", "JUL", "AGO", "SET", "OUT", "NOV", "DEZ"]
LANG_COLORS = [CYAN, LIME, WHITE, MUTED, SLATE]


def api(url, token, payload=None):
    req = urllib.request.Request(url, data=json.dumps(payload).encode() if payload else None, headers={
        "Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json",
        "User-Agent": "profile-activity"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def fetch(login):
    token = os.environ["GITHUB_TOKEN"]
    q = ("query($l:String!){user(login:$l){contributionsCollection{contributionCalendar{"
         "totalContributions weeks{contributionDays{date contributionCount}}}}}}")
    cal = api("https://api.github.com/graphql", token, {"query": q, "variables": {"l": login}})[
        "data"]["user"]["contributionsCollection"]["contributionCalendar"]
    days = [d for w in cal["weeks"] for d in w["contributionDays"]]
    langs = {}
    for repo in api(f"https://api.github.com/users/{login}/repos?per_page=100&type=owner", token):
        if repo["fork"] or repo["name"].lower() == login.lower():
            continue
        for k, v in api(repo["languages_url"], token).items():
            langs[k] = langs.get(k, 0) + v
    langs.pop("Dockerfile", None)
    return {"login": login, "updated": dt.date.today().isoformat(),
            "start": days[0]["date"], "end": days[-1]["date"], "total": cal["totalContributions"],
            "days": {d["date"]: d["contributionCount"] for d in days if d["contributionCount"]},
            "languages": dict(sorted(langs.items(), key=lambda kv: -kv[1]))}


def render(d):
    W, H = 1000, 336
    start, end = dt.date.fromisoformat(d["start"]), dt.date.fromisoformat(d["end"])
    start -= dt.timedelta(days=(start.weekday() + 1) % 7)  # alinha no domingo
    weeks, cur = [], start
    while cur <= end:
        tot = sum(d["days"].get((cur + dt.timedelta(days=i)).isoformat(), 0) for i in range(7))
        weeks.append((cur, tot))
        cur += dt.timedelta(days=7)
    peak_day = max(d["days"].values(), default=0)
    active = len(d["days"])
    wmax = max((t for _, t in weeks), default=1) or 1

    b = [f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="16" fill="url(#grid)"/>',
         mono(32, 40, "REGISTRO DE ATIVIDADE", size=11, fill=CYAN, ls=2.5),
         mono(968, 40, "ÚLTIMOS 12 MESES · DADOS PÚBLICOS", size=11, fill=MUTED, anchor="end", ls=2.5),
         text(30, 128, f"{d['total']:n}".replace(",", "."), size=76, weight=800, ls=-2),
         text(32, 156, "contribuições", size=17, fill=MUTED)]
    for i, (k, v) in enumerate((("DIAS ATIVOS", active), ("PICO EM UM DIA", peak_day))):
        y = 190 + i * 22
        b.append(mono(32, y, k, size=9.5, fill=MUTED, ls=1.8))
        b.append(mono(250, y, str(v), size=13, fill=WHITE, anchor="end", ls=0.5, weight=700))
        b.append(f'<path d="M{32 + mono_w(k, 9.5, 1.8) + 6:.0f} {y-3}H{250 - mono_w(str(v), 13, .5) - 8:.0f}" stroke="{SLATE}" stroke-dasharray="1 4"/>')

    # gráfico semanal
    gx0, gx1, gy0, gyb = 300, 968, 70, 210
    n = len(weeks)
    step = (gx1 - gx0) / n
    bw = step * 0.62
    for f in (0.5, 1.0):
        y = gyb - (gyb - gy0) * f
        b.append(f'<path d="M{gx0} {y:.1f}H{gx1}" stroke="{LINE}"/>')
        b.append(mono(gx0, y - 4, f"{round(wmax*f)} / SEMANA", size=8, fill=MUTED, ls=1.2))
    last_m = None
    for i, (ws, tot) in enumerate(weeks):
        x = gx0 + i * step + (step - bw) / 2
        if ws.month != last_m and i < n - 2:
            if last_m is not None or ws.day <= 7:
                b.append(mono(x, gyb + 17, MONTHS[ws.month - 1], size=8.5, fill=MUTED, ls=1.2))
                b.append(f'<path d="M{x-2.5:.1f} {gyb}v8" stroke="{SLATE}"/>')
            last_m = ws.month
        if tot:
            h = max(3, (gyb - gy0) * tot / wmax)
            b.append(f'<rect x="{x:.1f}" y="{gyb-h:.1f}" width="{bw:.1f}" height="{h:.1f}" '
                     f'rx="1.5" fill="{LIME if tot == wmax else CYAN}"/>')
        else:
            b.append(f'<rect x="{x:.1f}" y="{gyb-1.5}" width="{bw:.1f}" height="1.5" fill="{SLATE}"/>')
    b.append(f'<path d="M{gx0} {gyb}H{gx1}" stroke="{SLATE}"/>')

    # linguagens (bytes de código nos repositórios públicos próprios)
    langs = list(d["languages"].items())
    total = sum(v for _, v in langs) or 1
    top = langs[:4]
    rest = total - sum(v for _, v in top)
    if rest > 0:
        top.append(("Outras", rest))
    b.append(mono(32, 262, "LINGUAGENS", size=9.5, fill=MUTED, ls=1.8))
    x, bx0, bx1 = 0, 140, 968
    b.append(f'<clipPath id="lc"><rect x="{bx0}" y="254" width="{bx1-bx0}" height="9" rx="4.5"/></clipPath><g clip-path="url(#lc)">')
    segs = []
    for (name, v), col in zip(top, LANG_COLORS):
        w = (bx1 - bx0) * v / total
        b.append(f'<rect x="{bx0 + x:.1f}" y="254" width="{max(w-2, 1):.1f}" height="9" fill="{col}"/>')
        segs.append((name, v, col))
        x += w
    b.append('</g>')
    lx = bx0
    for name, v, col in segs:
        lab = f"{name} {v/total*100:.0f}%"
        b.append(f'<circle cx="{lx+4}" cy="286" r="4" fill="{col}"/>')
        b.append(mono(lx + 14, 290, lab, size=11, fill=WHITE, ls=0.3))
        lx += mono_w(lab, 11, 0.3) + 38
    b.append(mono(968, 316, f"GERADO POR GITHUB ACTIONS · {d['updated']}", size=8, fill=SLATE, anchor="end", ls=1.5))
    css = ""  # dado não se anima: o painel mostra sempre o valor real
    label = (f"Atividade no GitHub nos últimos 12 meses: {d['total']} contribuições, {active} dias ativos, "
             f"pico de {peak_day} em um dia. Linguagens: "
             + ", ".join(f"{n} {v/total*100:.0f}%" for n, v, _ in segs) + ".")
    return svg(W, H, "\n".join(b), css, label)


def build():
    write("graphics/activity.svg", render(json.loads(DATA.read_text())))


if __name__ == "__main__":
    if "--fetch" in sys.argv:
        try:
            login = json.loads(DATA.read_text())["login"]
            DATA.write_text(json.dumps(fetch(login), ensure_ascii=False, indent=1) + "\n")
        except Exception as ex:  # mantém o último SVG válido
            print(f"::warning::não foi possível atualizar os dados ({ex}); mantendo a versão anterior")
            sys.exit(0)
    build()
