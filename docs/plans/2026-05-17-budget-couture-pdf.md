# Budget Couture PDF Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a polished PDF shopping dossier for the baby's room, with real Brazilian links, reference prices, descriptions, images, budget tiers, and a fashion/editorial narrative.

**Architecture:** Create a self-contained HTML/CSS editorial document from curated product data, local renders, moodboard blocks, and tables. Generate PDF via a headless browser so typography, links, colors, and layout remain polished.

**Tech Stack:** Markdown/HTML/CSS, PowerShell/Python helper scripts if useful, Microsoft Edge/Chromium print-to-PDF, existing Obsidian and workspace folders.

---

### Task 1: Product Research

**Files:**
- Read: `100_quarto_bb/06-projeto-interiores.md`
- Create/Modify: `100_quarto_bb/09-lista-compras-budget-couture.md`

- [ ] Collect product names, real links, reference prices, and descriptions for: crib, mattress, nursing chair, side table, shelves, curtains, wallpaper/paint, lighting, rug, bedding, organization, safety, AC, hygrometer, humidifier, decor.
- [ ] Prefer Brazilian online stores and search/product pages that are easy to buy from.
- [ ] Mark prices as reference values and record the date.
- [ ] Group items into tiers: Essencial, Upgrade, Desejo.

### Task 2: Editorial Asset Prep

**Files:**
- Read: `assets/renders/layout-quarto-bb-cloud-dancer-v2-3d.png`
- Read: `assets/renders/layout-quarto-bb-cloud-dancer-v2-planta.png`
- Create: `assets/editorial/`

- [ ] Use existing renders as hero images if present.
- [ ] Add CSS moodboard blocks for Cloud Dancer, blush, tea, savana wood, cream bouclé, and champagne metal.
- [ ] Use product cards with category icons and visual color/material blocks when product images are not reliably downloadable.

### Task 3: HTML Dossier

**Files:**
- Create: `entregaveis/quarto-bb-budget-couture.html`

- [ ] Build cover, intro, moodboard, layout page, shopping list by category, budget table, phase plan, and final checklist.
- [ ] Include clickable links and price references in every product row.
- [ ] Make the document print-friendly with page breaks and luxury editorial typography.

### Task 4: PDF Generation

**Files:**
- Create: `entregaveis/quarto-bb-budget-couture.pdf`
- Copy: `100_quarto_bb/entregaveis/quarto-bb-budget-couture.pdf`

- [ ] Print the HTML to PDF using Edge/Chromium headless.
- [ ] Verify the PDF exists and is non-empty.
- [ ] Save source HTML and a markdown shopping list beside the PDF.

### Task 5: Final Review

**Files:**
- Modify: `100_quarto_bb/Index.md`

- [ ] Link the final PDF and shopping list from the Obsidian project index.
- [ ] Summarize output paths and note that prices are references subject to store changes.
