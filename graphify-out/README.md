# Graphify — mapa de conhecimento

Grafo gerado automaticamente pelo [Graphify](https://github.com/safishamsi/graphify) em 2026-07-07.

## Artefatos

```
graphify-out/
├── graph.html           ← abrir no navegador (interativo)
├── GRAPH_REPORT.md      ← relatório legível
├── graph.json           ← grafo completo para queries
└── manifest.json        ← índice de arquivos processados
```

## Como usar

```bash
# Consultar o grafo
graphify query "o que conecta o plano ao HTML?"
graphify path "Budget Couture PDF Implementation Plan" "build_html()"
graphify explain "Product"

# Regenerar (após mudanças nos arquivos)
graphify . --backend ollama
graphify cluster-only .
```

## Resumo (22 nós · 29 arestas · 6 comunidades)

| Comunidade | Foco |
|------------|------|
| Budget Couture PDF Generation | Script Python (`build_html`, `Product`, etc.) |
| Budget Couture Visual Assets | Imagens, HTML, lista, plano |
| File Management System | `main()`, `copy_assets()`, `Path` |
| Furniture Layout Design | Layout e mobiliário |
| Bedroom Floor Plan | Planta baixa |
| Bedroom Project Overview | Visão geral do projeto |

Ver relatório completo: [`GRAPH_REPORT.md`](GRAPH_REPORT.md)
