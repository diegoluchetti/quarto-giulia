# Graph Report - .  (2026-07-07)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 22 nodes · 29 edges · 6 communities (3 shown, 3 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 213 input · 64 output

## Community Hubs (Navigation)
- Budget Couture PDF Generation
- Budget Couture Visual Assets
- File Management System
- Furniture Layout Design
- Bedroom Floor Plan
- Bedroom Project Overview

## God Nodes (most connected - your core abstractions)
1. `build_html()` - 7 edges
2. `main()` - 5 edges
3. `money()` - 4 edges
4. `category_sections()` - 4 edges
5. `Budget Couture PDF Implementation Plan` - 4 edges
6. `esc()` - 3 edges
7. `copy_assets()` - 3 edges
8. `markdown_list()` - 3 edges
9. `Budget Couture HTML Dossier` - 3 edges
10. `layout_svg()` - 2 edges

## Surprising Connections (you probably didn't know these)
- `Budget Couture PDF Implementation Plan` --references--> `Layout 3D Render Cloud Dancer`  [EXTRACTED]
  docs/plans/2026-05-17-budget-couture-pdf.md → assets/renders/layout-quarto-bb-cloud-dancer-v2-3d.png
- `Budget Couture PDF Implementation Plan` --references--> `Layout Planta Render Cloud Dancer`  [EXTRACTED]
  docs/plans/2026-05-17-budget-couture-pdf.md → assets/renders/layout-quarto-bb-cloud-dancer-v2-planta.png
- `Budget Couture HTML Dossier` --references--> `Budget Couture Cover Image`  [EXTRACTED]
  entregaveis/quarto-bb-budget-couture.html → assets/editorial/budget-couture-cover-cloud-dancer.png
- `Budget Couture HTML Dossier` --references--> `Budget Couture Moodboard Image`  [EXTRACTED]
  entregaveis/quarto-bb-budget-couture.html → assets/editorial/budget-couture-moodboard-cloud-dancer.png
- `Budget Couture PDF Implementation Plan` --references--> `Budget Couture HTML Dossier`  [EXTRACTED]
  docs/plans/2026-05-17-budget-couture-pdf.md → entregaveis/quarto-bb-budget-couture.html

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Budget Couture Delivery Package** — docs_plans_budget_couture_plan, entregaveis_budget_couture_html, entregaveis_lista_compras_markdown [EXTRACTED 1.00]
- **Editorial Visual Assets** — assets_editorial_budget_couture_cover, assets_editorial_budget_couture_moodboard, assets_renders_layout_3d, assets_renders_layout_planta [EXTRACTED 1.00]
- **Layout Documentation Set** — plantas_layout_v1, plantas_planta_baixa, 100_quarto_bb_07_layout_mobiliario, 100_quarto_bb_04_planta_baixa [INFERRED 0.85]

## Communities (6 total, 3 thin omitted)

### Community 0 - "Budget Couture PDF Generation"
Cohesion: 0.46
Nodes (6): build_html(), category_sections(), esc(), layout_svg(), money(), Product

### Community 1 - "Budget Couture Visual Assets"
Cohesion: 0.29
Nodes (7): Budget Couture Cover Image, Budget Couture Moodboard Image, Layout 3D Render Cloud Dancer, Layout Planta Render Cloud Dancer, Budget Couture PDF Implementation Plan, Budget Couture HTML Dossier, Lista de Compras Budget Couture

### Community 2 - "File Management System"
Cohesion: 0.67
Nodes (4): Path, copy_assets(), main(), markdown_list()

## Knowledge Gaps
- **9 isolated node(s):** `Product`, `Quarto BB Project Overview`, `Lista de Compras Budget Couture`, `Layout Mobiliário V1`, `Planta Baixa Quarto BB` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **3 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `build_html()` connect `Budget Couture PDF Generation` to `File Management System`?**
  _High betweenness centrality (0.041) - this node is a cross-community bridge._
- **What connects `Product`, `Quarto BB Project Overview`, `Lista de Compras Budget Couture` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._