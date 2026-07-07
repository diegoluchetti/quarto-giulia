# Graph Report - .  (2026-07-07)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 64 nodes · 97 edges · 9 communities (7 shown, 2 thin omitted)
- Extraction: 91% EXTRACTED · 9% INFERRED · 0% AMBIGUOUS · INFERRED: 9 edges (avg confidence: 0.79)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `3870e1e1`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- build_budget_couture_pdf.py
- Escopo elétrico e LED
- docs/quarto.json
- docs/brief/2026-07-07-quarto-giulia-v2.md
- build_quarto_giulia_v2.py
- Budget Couture PDF Implementation Plan
- entregaveis/archive/v1-budget-couture/README.md
- layout-quarto-bb-calma-savana-3d.png
- Scripts README

## God Nodes (most connected - your core abstractions)
1. `docs/README.md` - 10 edges
2. `docs/brief/2026-07-07-quarto-giulia-v2.md` - 10 edges
3. `docs/quarto.json` - 8 edges
4. `build_html()` - 7 edges
5. `assets/README.md` - 6 edges
6. `Escopo elétrico e LED` - 6 edges
7. `main()` - 5 edges
8. `build_html()` - 5 edges
9. `money()` - 4 edges
10. `category_sections()` - 4 edges

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
- **Quarto Giulia v2 Brief Set** — docs_brief_2026_07_07_quarto_giulia_v2, docs_brief_sistema_paredes, docs_brief_escopo_eletrico_led, docs_brief_mobiliario_presenteado, docs_brief_paleta_soft_feminine [EXTRACTED 1.00]
- **Quarto Giulia v2 Design System** — quarto_giulia_v2_concept, quarto_giulia_v2_dimensions, quarto_giulia_v2_led_lighting_system [EXTRACTED]
- **Quarto Giulia v2 Deliverables** — entregaveis_quarto_giulia_lista_compras_v2, entregaveis_quarto_giulia_v2_html, plantas_layout_v2 [EXTRACTED]
- **Quarto Giulia v2 Electrical System** — docs_brief_escopo_eletrico_led, quarto_giulia_v2_led_lighting_system, plantas_layout_v2 [EXTRACTED]
- **Budget Couture Delivery Package** — docs_plans_budget_couture_plan, entregaveis_budget_couture_html, entregaveis_lista_compras_markdown [EXTRACTED 1.00]
- **Editorial Visual Assets** — assets_editorial_budget_couture_cover, assets_editorial_budget_couture_moodboard, assets_renders_layout_3d, assets_renders_layout_planta [EXTRACTED 1.00]

## Communities (9 total, 2 thin omitted)

### Community 0 - "build_budget_couture_pdf.py"
Cohesion: 0.35
Nodes (10): Path, build_html(), category_sections(), copy_assets(), esc(), layout_svg(), main(), markdown_list() (+2 more)

### Community 1 - "Escopo elétrico e LED"
Cohesion: 0.25
Nodes (10): Escopo elétrico e LED, Planta elétrica referência, Lista de Compras v2, Dossiê HTML v2, Entregáveis README, Layout v2, Plantas README, Soft Feminine Calm Concept (+2 more)

### Community 2 - "docs/quarto.json"
Cohesion: 0.27
Nodes (3): assets/README.md, docs/quarto.json, plantas/planta-baixa-quarto-bb.md

### Community 3 - "docs/brief/2026-07-07-quarto-giulia-v2.md"
Cohesion: 0.40
Nodes (9): docs/berco.json, docs/brief/2026-07-07-quarto-giulia-v2.md, docs/brief/mobiliario-presenteado.md, docs/brief/paleta-soft-feminine.md, docs/brief/sistema-paredes.md, docs/comoda.json, docs/plans/2026-07-07-quarto-giulia-v2.md, docs/README.md (+1 more)

### Community 4 - "build_quarto_giulia_v2.py"
Cohesion: 0.46
Nodes (7): build_html(), category_sections(), esc(), layout_svg(), main(), money(), Product

### Community 5 - "Budget Couture PDF Implementation Plan"
Cohesion: 0.29
Nodes (7): Budget Couture Cover Image, Budget Couture Moodboard Image, Layout 3D Render Cloud Dancer, Layout Planta Render Cloud Dancer, Budget Couture PDF Implementation Plan, Budget Couture HTML Dossier, Lista de Compras Budget Couture

### Community 6 - "entregaveis/archive/v1-budget-couture/README.md"
Cohesion: 0.67
Nodes (3): entregaveis/archive/v1-budget-couture/quarto-bb-budget-couture.html, entregaveis/archive/v1-budget-couture/quarto-bb-lista-compras-budget-couture.md, entregaveis/archive/v1-budget-couture/README.md

## Knowledge Gaps
- **15 isolated node(s):** `Product`, `Lista de Compras Budget Couture`, `Budget Couture Cover Image`, `Budget Couture Moodboard Image`, `Layout 3D Render Cloud Dancer` (+10 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Escopo elétrico e LED` connect `Escopo elétrico e LED` to `docs/brief/2026-07-07-quarto-giulia-v2.md`?**
  _High betweenness centrality (0.201) - this node is a cross-community bridge._
- **Why does `Entregáveis README` connect `Escopo elétrico e LED` to `build_quarto_giulia_v2.py`?**
  _High betweenness centrality (0.123) - this node is a cross-community bridge._
- **Why does `docs/README.md` connect `docs/brief/2026-07-07-quarto-giulia-v2.md` to `Escopo elétrico e LED`, `docs/quarto.json`?**
  _High betweenness centrality (0.110) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `docs/quarto.json` (e.g. with `PL-01-parede-leste.png` and `PN-01-janela-armario.png`) actually correct?**
  _`docs/quarto.json` has 4 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Product`, `Lista de Compras Budget Couture`, `Budget Couture Cover Image` to the rest of the system?**
  _15 weakly-connected nodes found - possible documentation gaps or missing edges._