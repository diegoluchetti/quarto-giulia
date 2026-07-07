# Graph Report - .  (2026-07-07)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 49 nodes · 80 edges · 8 communities (6 shown, 2 thin omitted)
- Extraction: 89% EXTRACTED · 11% INFERRED · 0% AMBIGUOUS · INFERRED: 9 edges (avg confidence: 0.79)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `2ce5c181`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- build_budget_couture_pdf.py
- docs/quarto.json
- Budget Couture PDF Implementation Plan
- docs/brief/2026-07-07-quarto-giulia-v2.md
- plantas/planta-baixa-quarto-bb.md
- docs/berco.json
- entregaveis/archive/v1-budget-couture/quarto-bb-budget-couture.html
- docs/plans/2026-07-07-quarto-giulia-v2.md

## God Nodes (most connected - your core abstractions)
1. `docs/brief/2026-07-07-quarto-giulia-v2.md` - 11 edges
2. `docs/README.md` - 10 edges
3. `docs/quarto.json` - 9 edges
4. `build_html()` - 7 edges
5. `assets/README.md` - 6 edges
6. `main()` - 5 edges
7. `docs/plans/2026-07-07-quarto-giulia-v2.md` - 5 edges
8. `docs/berco.json` - 5 edges
9. `docs/comoda.json` - 5 edges
10. `money()` - 4 edges

## Surprising Connections (you probably didn't know these)
- `plantas/planta-baixa-quarto-bb.md` --references--> `docs/quarto.json`  [EXTRACTED]
  plantas/planta-baixa-quarto-bb.md → docs/quarto.json
- `Budget Couture HTML Dossier` --references--> `Budget Couture Cover Image`  [EXTRACTED]
  entregaveis/quarto-bb-budget-couture.html → assets/editorial/budget-couture-cover-cloud-dancer.png
- `Budget Couture HTML Dossier` --references--> `Budget Couture Moodboard Image`  [EXTRACTED]
  entregaveis/quarto-bb-budget-couture.html → assets/editorial/budget-couture-moodboard-cloud-dancer.png
- `Budget Couture PDF Implementation Plan` --references--> `Layout 3D Render Cloud Dancer`  [EXTRACTED]
  docs/plans/2026-05-17-budget-couture-pdf.md → assets/renders/layout-quarto-bb-cloud-dancer-v2-3d.png
- `Budget Couture PDF Implementation Plan` --references--> `Layout Planta Render Cloud Dancer`  [EXTRACTED]
  docs/plans/2026-05-17-budget-couture-pdf.md → assets/renders/layout-quarto-bb-cloud-dancer-v2-planta.png

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Budget Couture Delivery Package** — docs_plans_budget_couture_plan, entregaveis_budget_couture_html, entregaveis_lista_compras_markdown [EXTRACTED 1.00]
- **Editorial Visual Assets** — assets_editorial_budget_couture_cover, assets_editorial_budget_couture_moodboard, assets_renders_layout_3d, assets_renders_layout_planta [EXTRACTED 1.00]
- **Quarto Giulia v2 Brief Set** — docs_brief_2026_07_07_quarto_giulia_v2, docs_brief_sistema_paredes, docs_brief_escopo_eletrico_led, docs_brief_mobiliario_presenteado, docs_brief_paleta_soft_feminine [EXTRACTED 1.00]
- **Quarto Giulia v2 JSON Data Files** — docs_quarto_json, docs_berco_json, docs_comoda_json [EXTRACTED 1.00]
- **Layout Documentation Set** — plantas_planta_baixa_quarto_bb, plantas_layout_v1, docs_quarto_json [INFERRED 0.80]

## Communities (8 total, 2 thin omitted)

### Community 0 - "build_budget_couture_pdf.py"
Cohesion: 0.35
Nodes (10): Path, build_html(), category_sections(), copy_assets(), esc(), layout_svg(), main(), markdown_list() (+2 more)

### Community 2 - "Budget Couture PDF Implementation Plan"
Cohesion: 0.29
Nodes (7): Budget Couture Cover Image, Budget Couture Moodboard Image, Layout 3D Render Cloud Dancer, Layout Planta Render Cloud Dancer, Budget Couture PDF Implementation Plan, Budget Couture HTML Dossier, Lista de Compras Budget Couture

### Community 3 - "docs/brief/2026-07-07-quarto-giulia-v2.md"
Cohesion: 0.52
Nodes (6): docs/brief/2026-07-07-quarto-giulia-v2.md, docs/brief/escopo-eletrico-led.md, docs/brief/paleta-soft-feminine.md, docs/brief/sistema-paredes.md, docs/README.md, docs/referencias/eletrica-apto-patio-clube.pdf

### Community 4 - "plantas/planta-baixa-quarto-bb.md"
Cohesion: 0.40
Nodes (3): plantas/layout-v1.md, plantas/planta-baixa-quarto-bb.md, plantas/README.md

### Community 5 - "docs/berco.json"
Cohesion: 0.67
Nodes (3): docs/berco.json, docs/brief/mobiliario-presenteado.md, docs/comoda.json

### Community 6 - "entregaveis/archive/v1-budget-couture/quarto-bb-budget-couture.html"
Cohesion: 0.67
Nodes (4): entregaveis/archive/v1-budget-couture/quarto-bb-budget-couture.html, entregaveis/archive/v1-budget-couture/quarto-bb-lista-compras-budget-couture.md, entregaveis/archive/v1-budget-couture/README.md, scripts/README.md

## Knowledge Gaps
- **7 isolated node(s):** `Product`, `Lista de Compras Budget Couture`, `Budget Couture Cover Image`, `Budget Couture Moodboard Image`, `Layout 3D Render Cloud Dancer` (+2 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `docs/quarto.json` connect `docs/quarto.json` to `docs/brief/2026-07-07-quarto-giulia-v2.md`, `plantas/planta-baixa-quarto-bb.md`, `docs/berco.json`, `docs/plans/2026-07-07-quarto-giulia-v2.md`?**
  _High betweenness centrality (0.142) - this node is a cross-community bridge._
- **Why does `plantas/planta-baixa-quarto-bb.md` connect `plantas/planta-baixa-quarto-bb.md` to `docs/quarto.json`?**
  _High betweenness centrality (0.077) - this node is a cross-community bridge._
- **Why does `docs/brief/2026-07-07-quarto-giulia-v2.md` connect `docs/brief/2026-07-07-quarto-giulia-v2.md` to `docs/quarto.json`, `docs/berco.json`, `docs/plans/2026-07-07-quarto-giulia-v2.md`?**
  _High betweenness centrality (0.063) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `docs/quarto.json` (e.g. with `PL-01-parede-leste.png` and `PN-01-janela-armario.png`) actually correct?**
  _`docs/quarto.json` has 4 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Product`, `Lista de Compras Budget Couture`, `Budget Couture Cover Image` to the rest of the system?**
  _7 weakly-connected nodes found - possible documentation gaps or missing edges._