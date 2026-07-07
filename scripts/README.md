# Scripts — automação de build

Scripts que geram entregáveis a partir dos dados do projeto.

## Arquivos

```
scripts/
└── build_budget_couture_pdf.py    ← gera HTML, PDF e lista de compras
```

## Mapa Graphify

**Comunidade:** Budget Couture PDF Generation

| Nó no grafo | Função |
|-------------|--------|
| `main()` | Orquestra cópia de assets e geração |
| `build_html()` | Monta o dossiê editorial HTML (7 conexões — nó central) |
| `category_sections()` | Seções por categoria de produto |
| `money()` | Formatação de valores em R$ |
| `esc()` | Escape HTML |
| `layout_svg()` | SVG do layout no dossiê |
| `copy_assets()` | Copia renders e imagens editoriais |
| `markdown_list()` | Gera lista de compras em Markdown |
| `Product` | Dataclass de produto (categoria, preço, link) |

**Comunidade relacionada:** File Management System (`Path`, `main()`, `copy_assets()`)

```bash
python scripts/build_budget_couture_pdf.py
```

Consulte o grafo: [`../graphify-out/graph.html`](../graphify-out/graph.html)
