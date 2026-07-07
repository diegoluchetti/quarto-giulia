from __future__ import annotations

import html
import json
import subprocess
from dataclasses import dataclass
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "entregaveis"


@dataclass
class Product:
    category: str
    item: str
    tier: str
    qty: int
    price: float
    link: str
    source: str
    description: str
    styling: str


PRODUCTS = [
    Product("Paredes", "Tinta acrílica off-white quente 24 m²", "Essencial", 1, 220.00, "https://www.suvinil.com.br/produtos/tintas-para-paredes", "Suvinil", "Duas demãos em ~24 m².", "Branco quente Baunilha/Cremoso."),
    Product("Paredes", "Kit EVA autocolante boiserie ~12 m", "Essencial", 1, 89.90, "https://lista.mercadolivre.com.br/eva-autocolante-boiserie-moldura-parede", "ML", "Moldura painel PL.", "Massa + pintura na cor da parede."),
    Product("Paredes", "Massa acrílica 1,4 kg", "Essencial", 1, 34.90, "https://www.leroymerlin.com.br/massa-acrilica", "Leroy Merlin", "Emendas EVA.", ""),
    Product("Paredes", "Papel de parede laços neutros", "Essencial", 6, 10.30, "https://lojadaparede.com.br/infantil/359-papel-de-parede-infantil-nuvem-com-laco-tons-neutros-adesivo-autocolante.html", "Loja da Parede", "Painel dentro da boiserie.", "Laços blush/areia sutis."),
    Product("Paredes", "Perfil LED rodapé 10,5 m + fita 2700K", "Essencial", 1, 380.00, "https://casaedetalhe.com.br/produto/perfil-aluminio-c-fita-led/", "Casa & Detalhe", "Perímetro quarto menos porta.", "Wash indireto; dimmer C2."),
    Product("Elétrica", "Interruptor duplo + dimmer LED", "Essencial", 1, 145.00, "https://lista.mercadolivre.com.br/interruptor-duplo-dimmer-led", "ML", "Tecla 1 teto; tecla 2 LED.", "Levar memorial ao eletricista."),
    Product("Elétrica", "Arandela LED 2700K", "Essencial", 1, 129.90, "https://lista.mercadolivre.com.br/arandela-led-2700k-dimerizavel", "ML", "Acima poltrona PS.", "Mamada com luz baixa."),
    Product("Elétrica", "Instalação elétrica (serviço)", "Essencial", 1, 350.00, "https://www.getninjas.com.br/reformas-e-reparos/eletricista", "GetNinjas", "Retrofit 2 circuitos.", ""),
    Product("Mobiliário", "Poltrona amamentação giratória bouclé", "Essencial", 1, 1299.00, "https://produto.mercadolivre.com.br/MLB-4102544042-poltrona-de-amamentacao-clarice-giro-balanco-beb-completo-_JM", "ML", "Bouclé creme; giro ~90 cm.", "Canto PS."),
    Product("Mobiliário", "Mesa lateral redonda 45 cm", "Upgrade", 1, 349.90, "https://www.tokstok.com.br/mesa-lateral-redonda-45-cm-branco-gueridon/p", "Tok&Stok", "Apoio poltrona.", ""),
    Product("Cortinas", "Trilho suíço duplo 2 m", "Essencial", 1, 109.99, "https://www.doceaconchego.com.br/trilho-suico-duplo-para-parede-maxi-49mm-2-metros-aluminio-cor-branco/p/MLB26297408", "Doce Aconchego", "PN janela.", ""),
    Product("Cortinas", "Blackout off-white 2,50 m", "Essencial", 1, 165.99, "https://www.laraconchegante.com.br/cortina-trilho-suico-300x250", "Lar Aconchegante", "Sono diurno.", ""),
    Product("Cortinas", "Voil off-white", "Essencial", 1, 129.90, "https://lista.mercadolivre.com.br/cortina-voil-branca-trilho-suico-3m", "ML", "Camada leve.", ""),
    Product("Enxoval", "Colchão 130×70×12", "Essencial", 1, 456.00, "https://www.angelinababy.com.br/colchoes/colchao-baby-ligth-ortobom-130x70x12", "Angelina Baby", "Berço presenteado.", ""),
    Product("Enxoval", "Lençol berço 3 peças algodão", "Essencial", 3, 56.10, "https://baobababy.com.br/produto/jogo-de-lencol-3-pecas-berco-americano/", "Baobá Baby", "Branco, areia, blush.", ""),
    Product("Enxoval", "Saco dormir TOG 1.0", "Essencial", 2, 177.65, "https://www.casulodeanjo.com.br/collections/saco-de-dormir-bebe-0-a-12-meses/saco-de-dormir-em-algodao-natural-cogumelo", "Casulo de Anjo", "Sono seguro.", ""),
    Product("Climatização", "AC LG 9000 BTU 220V", "Essencial", 1, 2179.00, "https://www.dufrio.com.br/ar-condicionado-split-dual-inverter-lg-compact-ia-s3nq09aaqak-eb2gam1-220v.html", "Dufrio", "PS, jato no teto.", ""),
    Product("Climatização", "Instalação AC", "Essencial", 1, 900.00, "https://www.getninjas.com.br/reformas-e-reparos/ar-condicionado/instalacao", "GetNinjas", "", ""),
    Product("Climatização", "Termo-higrômetro", "Essencial", 1, 86.00, "https://www.laderquimica.com.br/termo-higrometro-digital-incoterm-th80-com-alarme-de-temperatura-e-umidade-medicao-interna-e-externa", "Laderquimica", "", ""),
    Product("Decoração", "Kit quadros blush 30×30", "Essencial", 1, 119.80, "https://lista.mercadolivre.com.br/quadro-minimalista-rosa-bebe-30x30", "ML", "Moldura branca.", ""),
    Product("Decoração", "Tapete lavável bege", "Essencial", 1, 249.00, "https://lista.mercadolivre.com.br/tapete-lavavel-quarto-infantil-bege-200x150", "ML", "160×120 ou similar.", ""),
    Product("Decoração", "Luz noturna USB", "Essencial", 1, 39.90, "https://www.kindakids.com.br/luminaria-led/luz-noturna-led-bebe-usb-controle-remoto-dimerizavel-patinho", "Kinda Kids", "", ""),
    Product("Decoração", "Cesto algodão 28 cm", "Essencial", 2, 92.64, "https://www.graodegente.com.br/produto/cesto-organizador-para-brinquedos-nuvem-de-algodao-28cm/", "Grão de Gente", "", ""),
    Product("Segurança", "Protetor tomadas kit 10", "Essencial", 1, 10.76, "https://safety1st.com.br/collections/seguranca/products/protetor-de-tomadas-10-unidades", "Safety 1st", "", ""),
    Product("Segurança", "Trava gavetas magnética", "Essencial", 1, 64.90, "https://safety1st.com.br/products/trava-magnetica", "Safety 1st", "Cômoda presenteada.", ""),
    Product("Segurança", "Trava janela correr", "Essencial", 1, 49.90, "https://lista.mercadolivre.com.br/trava-janela-correr-infantil", "ML", "", ""),
]


def money(value: float) -> str:
    return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def layout_svg() -> str:
    return """
<svg viewBox="0 0 320 320" role="img" aria-label="Planta 2,54x2,54m" class="plan">
  <rect x="20" y="20" width="280" height="280" fill="#faf8f5" stroke="#3d3530" stroke-width="1.5"/>
  <text x="160" y="14" text-anchor="middle" font-size="9">PN janela</text>
  <text x="160" y="312" text-anchor="middle" font-size="9">PS poltrona+AC</text>
  <text x="8" y="165" text-anchor="middle" transform="rotate(-90 8 165)" font-size="9">PO porta</text>
  <text x="312" y="165" text-anchor="middle" transform="rotate(90 312 165)" font-size="9">PL berço</text>
  <rect x="20" y="20" width="70" height="180" fill="#d4c4b0" stroke="#8a7358"/>
  <text x="55" y="115" text-anchor="middle" font-size="8" transform="rotate(-90 55 115)">armário</text>
  <path d="M20 220 L20 300 L95 300" fill="none" stroke="#999" stroke-width="5"/>
  <rect x="30" y="230" width="50" height="35" fill="#fff" stroke="#bbb"/>
  <text x="55" y="252" text-anchor="middle" font-size="7">cômoda</text>
  <rect x="215" y="80" width="75" height="40" fill="#fff" stroke="#c9b8a8"/>
  <text x="252" y="105" text-anchor="middle" font-size="8">berço 130</text>
  <rect x="210" y="55" width="80" height="20" fill="none" stroke="#d4a5b0" stroke-dasharray="3 2"/>
  <text x="250" y="68" text-anchor="middle" font-size="6">boiserie+papel</text>
  <circle cx="80" cy="260" r="22" fill="#f0ebe3" stroke="#c9b8a8"/>
  <text x="80" y="263" text-anchor="middle" font-size="7">poltrona</text>
  <text x="250" y="280" font-size="7" fill="#888">2,54 m</text>
</svg>"""


def category_sections() -> str:
    parts: list[str] = []
    cats: list[str] = []
    for p in PRODUCTS:
        if p.category not in cats:
            cats.append(p.category)
    for cat in cats:
        items = [p for p in PRODUCTS if p.category == cat]
        rows = []
        sub = 0.0
        for p in items:
            line = p.price * p.qty
            sub += line
            tier = p.tier.lower()
            rows.append(
                f"<tr><td><span class=\"tier {tier}\">{esc(p.tier)}</span><br><strong>{esc(p.item)}</strong>"
                f"<br><span class=\"muted\">{esc(p.source)}</span></td>"
                f"<td>{esc(p.description)}<p class=\"styling\">{esc(p.styling)}</p></td>"
                f"<td class=\"num\">{p.qty}</td><td class=\"num\">{money(p.price)}</td>"
                f"<td class=\"num\"><strong>{money(line)}</strong></td>"
                f"<td><a href=\"{esc(p.link)}\">Ver</a></td></tr>"
            )
        parts.append(
            f"<section class=\"page\"><h2>{esc(cat)}</h2><table><thead><tr>"
            f"<th>Item</th><th>Descrição</th><th>Qtd</th><th>Unit.</th><th>Total</th><th>Link</th>"
            f"</tr></thead><tbody>{''.join(rows)}</tbody></table>"
            f"<p class=\"subtotal\">Subtotal {esc(cat)}: <strong>{money(sub)}</strong></p></section>"
        )
    return "\n".join(parts)


def build_html() -> str:
    total = sum(p.price * p.qty for p in PRODUCTS)
    essential = sum(p.price * p.qty for p in PRODUCTS if p.tier == "Essencial")
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Quarto Giulia v2 — Dossiê</title>
<style>
@page {{ size: A4; margin: 14mm; }}
body {{ margin:0; font-family: Arial, sans-serif; color:#3d3530; background:#faf8f5; line-height:1.45; }}
a {{ color:#9a6b7a; }}
h1,h2 {{ font-family: Georgia, serif; font-weight:400; }}
.page {{ page-break-after: always; padding: 8mm 0; }}
.kicker {{ text-transform:uppercase; letter-spacing:.15em; font-size:9px; color:#a08090; }}
.cover {{ min-height:250mm; display:flex; flex-direction:column; justify-content:center; }}
.cover h1 {{ font-size:48px; color:#5c4a52; }}
.meta {{ border:1px solid #e8dce0; padding:16px; border-radius:12px; background:#fff; margin-top:24px; }}
.swatches {{ display:grid; grid-template-columns:repeat(5,1fr); gap:8px; margin:20px 0; }}
.swatch {{ height:56px; border-radius:10px; font-size:9px; padding:6px; display:flex; align-items:end; }}
.s1{{background:#f5f0eb}} .s2{{background:#e8d4d8}} .s3{{background:#f0e8e4}} .s4{{background:#d9c0a6}} .s5{{background:#fff}}
.grid2 {{ display:grid; grid-template-columns:1fr 1fr; gap:20px; }}
.plan {{ width:100%; }}
table {{ width:100%; border-collapse:collapse; font-size:9px; background:#fff; }}
th,td {{ border-bottom:1px solid #eee; padding:6px; vertical-align:top; }}
.tier {{ font-size:7px; padding:2px 6px; border-radius:99px; background:#f0e8e4; }}
.essencial {{ background:#efe8e4; }}
.upgrade {{ background:#e8d4d8; }}
.subtotal {{ text-align:right; }}
.cards {{ display:grid; grid-template-columns:1fr 1fr; gap:16px; }}
.card {{ background:#fff; border:1px solid #e8dce0; padding:16px; border-radius:12px; }}
.big {{ font-size:28px; font-family:Georgia,serif; }}
ul li {{ margin:6px 0; }}
</style>
</head>
<body>
<section class="page cover">
  <div class="kicker">Quarto Giulia · Julho 2026</div>
  <h1>Soft Feminine<br>Calm</h1>
  <p>Quarto 2,54 × 2,54 m · Berço e cômoda brancos presenteados · Paredes em camadas · LED dimmerizável</p>
  <div class="meta">
    <strong>Área:</strong> 6,45 m² · <strong>Prazo:</strong> out/2026<br>
  <strong>Presenteados:</strong> berço + cômoda trocador brancos (sem azul)<br>
    <strong>Obra:</strong> boiserie EVA + papel + rodapé LED + retrofit elétrico
  </div>
</section>

<section class="page">
  <div class="kicker">Conceito</div>
  <h2>Paleta e móveis</h2>
  <p>Móveis brancos são a base neutra. O feminino suave entra via <strong>rosa pó</strong>, <strong>pêssego</strong> e <strong>lavanda</strong> em paredes, têxteis e decoração — sem repintar móveis.</p>
  <div class="swatches">
    <div class="swatch s1">Off-white</div>
    <div class="swatch s2">Rosa pó</div>
    <div class="swatch s3">Pêssego</div>
    <div class="swatch s4">Madeira</div>
    <div class="swatch s5">Branco móveis</div>
  </div>
  <h3>Sistema de paredes</h3>
  <ol>
    <li>Pintura base</li>
    <li>Boiserie EVA autocolante pintada</li>
    <li>Papel de parede no painel PL</li>
    <li>Rodapé LED 10,5 m (2700K, dimmer)</li>
  </ol>
</section>

<section class="page">
  <div class="kicker">Layout</div>
  <h2>Planta 2,54 × 2,54 m</h2>
  <div class="grid2">
    <div>{layout_svg()}</div>
    <div>
      <ul>
        <li><strong>PL:</strong> berço + boiserie + papel</li>
        <li><strong>PN:</strong> janela + cortina + armário</li>
        <li><strong>PO:</strong> porta + cômoda trocador</li>
        <li><strong>PS:</strong> poltrona bouclé + AC + arandela</li>
      </ul>
      <p><em>Dimensões dos móveis estimadas até medição.</em></p>
    </div>
  </div>
</section>

<section class="page">
  <div class="kicker">Orçamento</div>
  <h2>Resumo</h2>
  <div class="cards">
    <div class="card"><div class="kicker">Essencial</div><div class="big">{money(essential)}</div><p>Sem berço/cômoda (presenteados)</p></div>
    <div class="card"><div class="kicker">Lista completa</div><div class="big">{money(total)}</div><p>Inclui upgrades</p></div>
  </div>
</section>

{category_sections()}

<section class="page">
  <h2>Ordem de execução</h2>
  <ol>
    <li>Elétrica (2 circuitos + dimmer)</li>
    <li>Pintura base</li>
    <li>Boiserie EVA + massa + pintura</li>
    <li>Papel de parede PL</li>
    <li>Rodapé LED</li>
    <li>AC + cortinas</li>
    <li>Móveis presenteados + poltrona</li>
    <li>Decoração e enxoval</li>
  </ol>
  <p><small>Preços referência jul/2026. Conferir antes de comprar.</small></p>
</section>
</body>
</html>"""


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    html_path = OUT / "quarto-giulia-v2.html"
    html_path.write_text(build_html(), encoding="utf-8")

    md_src = ROOT / "entregaveis" / "quarto-giulia-lista-compras-v2.md"
    if not md_src.exists():
        raise SystemExit("Missing shopping list markdown")

    pdf_path = OUT / "quarto-giulia-v2.pdf"
    browsers = [
        Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
        Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
        Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
    ]
    browser = next((p for p in browsers if p.exists()), None)
    if browser:
        subprocess.run(
            [str(browser), "--headless=new", "--disable-gpu",
             f"--print-to-pdf={pdf_path}", "--print-to-pdf-no-header", html_path.as_uri()],
            check=True,
        )
    print(json.dumps({"html": str(html_path), "pdf": str(pdf_path) if pdf_path.exists() else None}, indent=2))


if __name__ == "__main__":
    main()
