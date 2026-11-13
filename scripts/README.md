# Ativos do perfil

Todos os SVGs em `assets/` são gerados por código. Para alterar um texto, uma cor ou um projeto,
edite o script correspondente e rode:

```bash
python scripts/build.py
```

| Script | Gera |
| --- | --- |
| `common.py` | paleta, tipografia e utilitários compartilhados |
| `hero.py` | `assets/banners/hero*.svg` (animado, estático e mobile) |
| `sections.py` | cabeçalhos de folha, tabela de conversão, lista de materiais, terminal, rodapé e botões |
| `projects.py` | `assets/project-covers/*.svg` |
| `activity.py` | `assets/graphics/activity.svg` a partir de `data/activity.json` |
| `render.py` | utilitário opcional: PNGs de conferência (requer Playwright + Chrome) |

O painel de atividade é atualizado diariamente por `.github/workflows/activity.yml`
(`python scripts/activity.py --fetch`). Se a API estiver indisponível, o último SVG válido permanece.
