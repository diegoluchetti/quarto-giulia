# Quarto Giulia — workspace arquitetônico

Design de interiores e material arquitetônico para **quarto de bebê** (conceito *Budget Couture / Cloud Dancer*).

## Mapa do projeto (Graphify)

O repositório foi mapeado com [Graphify](https://github.com/safishamsi/graphify) em um grafo de conhecimento navegável:

| Artefato | Descrição |
|----------|-----------|
| [`graphify-out/graph.html`](graphify-out/graph.html) | Grafo interativo — abra no navegador |
| [`graphify-out/GRAPH_REPORT.md`](graphify-out/GRAPH_REPORT.md) | Relatório: comunidades, conexões, lacunas |
| [`graphify-out/graph.json`](graphify-out/graph.json) | Grafo em JSON para consultas (`graphify query`) |

**Comunidades principais:** Budget Couture PDF Generation · Budget Couture Visual Assets · File Management System · Furniture Layout Design · Bedroom Floor Plan · Bedroom Project Overview

**Nós centrais:** `build_html()`, `main()`, `Budget Couture PDF Implementation Plan`, `Budget Couture HTML Dossier`

```bash
# Regenerar o mapa (requer API key ou Ollama)
graphify . --backend ollama
graphify cluster-only .
```

## Estrutura do repositório

```
quarto-giulia/
├── 100_quarto_bb/          ← junction Obsidian (não versionado)
├── assets/
│   ├── editorial/          ← capa e moodboard do dossiê
│   ├── fotos/              ← fotos do ambiente real
│   ├── referencias/        ← referências visuais
│   └── renders/            ← plantas e vistas 3D
├── docs/
│   └── plans/              ← planos de implementação
├── entregaveis/            ← HTML, PDF e listas finais
├── graphify-out/           ← mapa Graphify (versionado)
├── modelos/                ← modelos 3D (futuro)
├── plantas/                ← espelhos das notas Obsidian
└── scripts/                ← automação de build
```

## Sincronização com Obsidian (2nd_brain)

| Conteúdo | Onde fica |
|----------|-----------|
| Ideias, medidas, parâmetros, brief | `100_quarto_bb/` (junction → vault) |
| Plantas, 3D, renders, entregáveis | Este repositório |

**Vault:** `C:\Users\Administrator\Projects\segundo-cerebro-ai\2nd-brain`  
**Notas canônicas:** `100_quarto_bb/Index.md`, `06-projeto-interiores.md`, `07-layout-mobiliario.md`

## Projeto atual

- **Interiores:** `100_quarto_bb/06-projeto-interiores.md`
- **Layout:** `100_quarto_bb/07-layout-mobiliario.md` · espelho em [`plantas/`](plantas/)
- **Lista de compras:** [`entregaveis/quarto-bb-lista-compras-budget-couture.md`](entregaveis/quarto-bb-lista-compras-budget-couture.md)
- **Dossiê editorial:** [`entregaveis/quarto-bb-budget-couture.html`](entregaveis/quarto-bb-budget-couture.html)

## Seções

| Pasta | README |
|-------|--------|
| [`assets/`](assets/) | Visuais, renders e referências |
| [`docs/`](docs/) | Planos e documentação de processo |
| [`entregaveis/`](entregaveis/) | Artefatos finais para compartilhar |
| [`plantas/`](plantas/) | Espelhos de planta e layout |
| [`scripts/`](scripts/) | Scripts de build e automação |
