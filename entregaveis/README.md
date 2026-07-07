# Entregáveis — artefatos finais

Documentos prontos para compartilhar: dossiê editorial, lista de compras e PDF.

## Arquivos

```
entregaveis/
├── quarto-bb-budget-couture.html          ← dossiê editorial interativo
├── quarto-bb-budget-couture.pdf           ← versão PDF para impressão
└── quarto-bb-lista-compras-budget-couture.md  ← lista com links BR e preços
```

## Mapa Graphify

**Comunidade:** Budget Couture Visual Assets

| Nó no grafo | Arquivo |
|-------------|---------|
| Budget Couture HTML Dossier | `quarto-bb-budget-couture.html` |
| Lista de Compras Budget Couture | `quarto-bb-lista-compras-budget-couture.md` |

**Hyperedge:** *Budget Couture Delivery Package* — agrupa plano, HTML e lista de compras como pacote de entrega.

**Conexões:**
- HTML referencia imagens em [`../assets/editorial/`](../assets/editorial/)
- Lista e HTML são gerados por [`../scripts/build_budget_couture_pdf.py`](../scripts/build_budget_couture_pdf.py)
- Plano de implementação em [`../docs/plans/`](../docs/plans/)

Consulte o grafo: [`../graphify-out/graph.html`](../graphify-out/graph.html)
