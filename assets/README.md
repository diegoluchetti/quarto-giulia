# Assets — visuais do projeto

Imagens de referência, renders 3D, fotos do ambiente e blocos editoriais do dossiê *Budget Couture*.

## Arquivos

```
assets/
├── editorial/
│   ├── budget-couture-cover-cloud-dancer.png
│   └── budget-couture-moodboard-cloud-dancer.png
├── fotos/
│   ├── PL-01-parede-leste.png
│   ├── PN-01-janela-armario.png
│   ├── PO-01-armario-porta.png
│   └── PS-01-porta-PO-aberta.png
├── referencias/          ← (reservado)
└── renders/
    ├── layout-quarto-bb-calma-savana-3d.png
    ├── layout-quarto-bb-cloud-dancer-v2-3d.png
    ├── layout-quarto-bb-cloud-dancer-v2-planta.png
    └── layout-quarto-bb-planta-3d-topo.png
```

## Mapa Graphify

**Comunidade:** Budget Couture Visual Assets

| Nó no grafo | Arquivo |
|-------------|---------|
| Budget Couture Cover Image | `editorial/budget-couture-cover-cloud-dancer.png` |
| Budget Couture Moodboard Image | `editorial/budget-couture-moodboard-cloud-dancer.png` |
| Layout 3D Render Cloud Dancer | `renders/layout-quarto-bb-cloud-dancer-v2-3d.png` |
| Layout Planta Render Cloud Dancer | `renders/layout-quarto-bb-cloud-dancer-v2-planta.png` |

**Hyperedge:** *Editorial Visual Assets* — agrupa capa, moodboard e renders de layout.

**Conexões surpreendentes:**
- `Budget Couture PDF Implementation Plan` → renders (plano referencia os renders como hero images)
- `Budget Couture HTML Dossier` → imagens editoriais (capa e moodboard embutidos no HTML)

Consulte o grafo completo: [`../graphify-out/graph.html`](../graphify-out/graph.html)
