from __future__ import annotations

import html
import json
import shutil
import subprocess
from dataclasses import dataclass
from datetime import date
from pathlib import Path


ROOT = Path(r"C:\Users\Administrator\Documents\quarto_bb")
VAULT = Path(r"C:\Users\Administrator\Projects\segundo-cerebro-ai\2nd-brain\100_quarto_bb")
OUT = ROOT / "entregaveis"
ASSETS = ROOT / "assets" / "editorial"
VAULT_OUT = VAULT / "entregaveis"
VAULT_ASSETS = VAULT / "assets" / "editorial"

GEN_ASSETS = Path(r"C:\Users\Administrator\.cursor\projects\c-Users-Administrator-Documents-quarto-bb\assets")


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
    priority: str = "Essencial"


PRODUCTS = [
    Product("Móveis âncora", "Berço Multifuncional Luna c/ Auxiliar Reller", "Essencial", 1, 2298.60, "https://www.angelinababy.com.br/bercos/berco-multifuncional-luna-moveis-reller?variant_id=3883", "Angelina Baby", "Berço 3 em 1 com cômoda/trocador e cama auxiliar baixa. Medida 194 x 83 x 102 cm, colchão 130 x 70.", "Escolher Branco Fosco/Savana: conversa com o armário existente e entrega a leitura quiet luxury."),
    Product("Móveis âncora", "Colchão Baby Light Ortobom 130 x 70 x 12", "Essencial", 1, 456.00, "https://www.angelinababy.com.br/colchoes/colchao-baby-ligth-ortobom-130x70x12", "Angelina Baby", "Colchão compatível com berço americano 130 x 70 cm.", "Base branca, sem estampas fortes. O luxo aqui é proporção e limpeza visual."),
    Product("Móveis âncora", "Poltrona Clarice Giro + Balanço + Puff", "Essencial", 1, 1999.00, "https://produto.mercadolivre.com.br/MLB-4102544042-poltrona-de-amamentacao-clarice-giro-balanco-beb-completo-_JM", "Mercado Livre", "Poltrona com mecanismo de giro e balanço, puff incluso; referência 72 x 88 x 106 cm.", "Tecido bouclé pérola/creme: referência Chanel sem parecer fantasia."),
    Product("Móveis complementares", "Kit 2 Prateleiras Luna 89,6 cm Savana", "Essencial", 1, 185.00, "https://www.prmoveis.com.br/produto/kit-2-prateleiras-luna-89-6cm-savana-fosco-com-alcas-de-couro-reller-moveis-115553", "PR Móveis", "Duas prateleiras em MDF com alças em couro sintético. Instalar na PS, nunca na PO.", "Prateleiras como vitrine: poucos livros, 1 escultura, 1 cesto. Nada abarrotado."),
    Product("Móveis complementares", "Mesa lateral redonda branca Gueridon 45 cm", "Essencial", 1, 349.90, "https://www.tokstok.com.br/mesa-lateral-redonda-45-cm-branco-gueridon/p", "Tok&Stok", "Mesa de apoio de 45 cm para água, mamadeira, livro e luminária pequena.", "Uma peça redonda quebra as linhas retas do berço e deixa o canto mais francês."),
    Product("Móveis complementares", "Kit higiene porcelana branco + dourado", "Upgrade", 1, 139.80, "https://www.cirandaartecriativa.com.br/kit-higiene-porcelana-bebe-neutro-pote-algodao-cotonete", "Ciranda Arte Criativa", "Potes e bandeja para algodão, cotonete e higiene no trocador.", "Dourado pequeno e controlado: toque joalheria, não ostentação."),
    Product("Móveis complementares", "Lixeira inox pedal Tramontina 12 L", "Essencial", 1, 146.30, "https://www.tramontina.com.br/lixeira-com-pedal-tramontina-brasil-em-aco-inox-com-acabamento-polido-e-balde-interno-12-l/94538112.html", "Tramontina", "Lixeira com pedal e balde interno para fraldas e rotina de troca.", "Inox é prático; se quiser suavizar, posicionar ao lado do Luna, fora do foco visual."),
    Product("Cortina e janela", "Cortina Basic Blackout 3,00 x 2,50 m trilho suíço", "Essencial", 1, 165.99, "https://www.laraconchegante.com.br/cortina-trilho-suico-300x250", "Lar Aconchegante", "Blackout para sono e sonecas. Confirmar estoque e altura final antes da compra.", "Preferir off-white/cinza quente; sem personagem."),
    Product("Cortina e janela", "Cortina blackout com linho 3,00 x 2,50 m", "Upgrade", 1, 299.90, "https://www.ludatex.com.br/produtos/cortina-blackout-com-linho-300x250-para-trilho-suico/", "Ludatex", "Blackout com textura de linho, mais editorial que blackout liso.", "A textura tipo linho é o truque para parecer sob medida."),
    Product("Cortina e janela", "Trilho suíço duplo branco 2 m", "Essencial", 1, 109.99, "https://www.doceaconchego.com.br/trilho-suico-duplo-para-parede-maxi-49mm-2-metros-aluminio-cor-branco/p/MLB26297408", "Doce Aconchego", "Trilho duplo para voil + blackout. Conferir se suporta o tecido escolhido.", "Instalar o mais alto possível abaixo da sanca para alongar o quarto."),
    Product("Cortina e janela", "Voil branco/off-white 3 m", "Essencial", 1, 129.90, "https://lista.mercadolivre.com.br/cortina-voil-branca-trilho-suico-3m", "Mercado Livre", "Camada leve para luz diurna e privacidade.", "Voil é a parte francesa do quarto: movimento, leveza, foto bonita."),
    Product("Parede e acabamento", "Papel de parede Nuvem com Laço tons neutros", "Essencial", 12, 10.30, "https://lojadaparede.com.br/infantil/359-papel-de-parede-infantil-nuvem-com-laco-tons-neutros-adesivo-autocolante.html", "Loja da Parede", "Adesivo vinílico autocolante, lavável, atóxico. Preço por faixa/rolo de referência.", "Aplicar somente no painel PL ou usar poucos módulos; menos é mais."),
    Product("Parede e acabamento", "Papel de parede infantil laços neutros", "Upgrade", 1, 199.90, "https://www.varonidecor.com.br/infantil/papel-de-parede-infantil-lacos-vr132", "Varoni Decor", "Alternativa mais fashionista, com laços em leitura delicada.", "Laços têm perfume Dior/Chloé, mas precisam ficar bem sutis."),
    Product("Parede e acabamento", "Tinta equivalente Cloud Dancer 11-4201", "Essencial", 1, 260.00, "https://www.suvinil.com.br/produtos/tintas-para-paredes", "Suvinil", "Tinta acrílica fosca ou acetinada em branco quente sob medida aproximando Cloud Dancer.", "Pedir amostra: branco precisa ser quente, nunca hospitalar."),
    Product("Iluminação", "Painel LED inteligente NEO Avant 24 W 2700K-6500K", "Essencial", 1, 109.90, "https://neoavant.com.br/products/avant-neo-painel-led-plafon-smart-sobrepor-24w-2700k-a-6500k-30cm-110v-220v-bivolt-quadrado-cod-291990734-neo-avant", "NEO Avant", "Plafon smart dimerizável, bivolt, com luz quente a fria.", "Usar cenas: banho/troca mais claro; mamada noturna bem baixo e quente."),
    Product("Iluminação", "Plafon Taschibra Liora On TW 30 W", "Upgrade", 1, 390.90, "https://www.lumedecoronline.com.br/led/plafon-de-led/plafon-led-taschibra-liora-on-tw-30w-com-controle-remoto-quadrado-dimerizavel-e-multitemperatura", "Lume Decor", "Plafon dimerizável com controle e multitemperatura.", "Upgrade se quiser acabamento mais robusto e controle dedicado."),
    Product("Iluminação", "Luz noturna LED bebê USB dimerizável", "Essencial", 1, 39.90, "https://www.kindakids.com.br/luminaria-led/luz-noturna-led-bebe-usb-controle-remoto-dimerizavel-patinho", "Kinda Kids", "Luz noturna com controle remoto e três níveis de brilho.", "Usar escondida perto da poltrona, não como peça protagonista."),
    Product("Iluminação", "Perfil de alumínio + fita LED 2700K 1 m", "Desejo", 2, 106.90, "https://casaedetalhe.com.br/produto/perfil-aluminio-c-fita-led/", "Casa & Detalhe", "Luz indireta quente para painel ou prateleiras.", "Se o orçamento apertar, cortar primeiro; é lindo, mas não essencial."),
    Product("Climatização", "LG Dual Inverter Compact + IA 9000 BTU 220 V", "Essencial", 1, 2179.00, "https://www.dufrio.com.br/ar-condicionado-split-dual-inverter-lg-compact-ia-s3nq09aaqak-eb2gam1-220v.html", "Dufrio", "Split inverter frio, 9000 BTU, adequado para quarto pequeno.", "Instalar na PS, jato paralelo ao teto, nunca direto no berço."),
    Product("Climatização", "Instalação ar-condicionado + dreno + suporte", "Essencial", 1, 900.00, "https://www.getninjas.com.br/reformas-e-reparos/ar-condicionado/instalacao", "Serviço local", "Valor de referência para instalação profissional.", "Não economizar na instalação; é item técnico e afeta segurança."),
    Product("Climatização", "Termo-higrômetro BBLUV Igrö 2 em 1", "Upgrade", 1, 249.90, "https://www.jhbabystore.com.br/bbluv-igro-termometro-higrometro-digital-2-em-1", "JH Baby Store", "Mede temperatura e umidade com indicador de conforto.", "Objeto bonito e funcional para o trocador."),
    Product("Climatização", "Termo-higrômetro Incoterm TH80", "Essencial", 1, 86.00, "https://www.laderquimica.com.br/termo-higrometro-digital-incoterm-th80-com-alarme-de-temperatura-e-umidade-medicao-interna-e-externa", "Laderquimica", "Alternativa técnica e acessível para temperatura/umidade.", "Menos bonito, mais racional. Pode ficar discreto no armário."),
    Product("Climatização", "Umidificador Fisher-Price HC115 3,4 L", "Upgrade", 1, 199.90, "https://www.farmacianacional.com.br/umidificador-fisher-price-3-4l-mtl-hc115-p557823-p180285", "Farmácia Nacional", "Umidificador ultrassônico silencioso, reservatório 3,4 L.", "Usar só se a umidade ficar abaixo de 40%; sem óleos essenciais para bebê."),
    Product("Tapete e têxteis", "Tapete lavável infantil 200 x 140 cm Lorena Canals Bereber Beige", "Desejo", 1, 2211.79, "https://www.bililababy.com.br/lorena-canals/tapete-bereber-beige", "Bilila Baby", "Tapete premium lavável, 100% algodão, estética europeia.", "Peça desejo: é caro, mas muda o quarto inteiro."),
    Product("Tapete e têxteis", "Tapete infantil lavável bege 200 x 150", "Essencial", 1, 299.00, "https://lista.mercadolivre.com.br/tapete-lavavel-quarto-infantil-bege-200x150", "Mercado Livre", "Alternativa acessível em bege/creme, lavável ou fácil de higienizar.", "Escolher sem desenho grande; textura ganha de estampa."),
    Product("Tapete e têxteis", "Almofada Boppy Chicco amamentação", "Upgrade", 1, 249.00, "https://www.dafiti.com.br/Almofada-Chicco-Boppy-Sem-Capa-Branco-2968095.html", "Dafiti", "Suporte ergonômico para amamentação.", "Capa em branco/creme e uma manta blush fazem o styling."),
    Product("Tapete e têxteis", "Manta tricot canelado blush 80 x 80", "Upgrade", 1, 159.90, "https://www.bebefacil.com.br/manta-para-bebe-em-tricot-canelado-rosa-blush---mini-co/p", "Bebê Fácil", "Manta decorativa e de colo, usar fora do berço durante sono.", "O blush é o toque moda; guardar dobrada na poltrona."),
    Product("Enxoval seguro", "Jogo lençol berço americano 3 peças 100% algodão", "Essencial", 3, 56.10, "https://baobababy.com.br/produto/jogo-de-lencol-3-pecas-berco-americano/", "Baobá Baby", "Lençol com elástico para colchão 130 x 70, superior e fronha.", "Comprar branco, areia e blush muito claro; evitar estampas fortes."),
    Product("Enxoval seguro", "Protetor colchão impermeável 130 x 70", "Essencial", 2, 44.91, "https://www.paraisodobebe.com.br/protetor-de-colch-o-130x70-impermeavel-matelado-premium", "Paraíso de Bebê", "Capa impermeável para proteger o colchão.", "Item invisível, mas obrigatório."),
    Product("Enxoval seguro", "Saco de dormir TOG 1.0 algodão", "Essencial", 2, 177.65, "https://www.casulodeanjo.com.br/collections/saco-de-dormir-bebe-0-a-12-meses/saco-de-dormir-em-algodao-natural-cogumelo", "Casulo de Anjo", "Saquinho de dormir para 20-24°C, substitui mantas soltas.", "Sono seguro > kit berço volumoso."),
    Product("Enxoval seguro", "Saco de dormir TOG 2.0", "Upgrade", 1, 220.00, "https://www.comcarinhobaby.com/produtos/saquinho-de-dormir-tog-2-0-verde-calmaria/", "Com Carinho Baby", "Versão mais quente para noites frias com AC.", "Verde calmaria conversa com paletas Pantone sem infantilizar."),
    Product("Organização", "Cesto organizador nuvem algodão 28 cm", "Essencial", 2, 92.64, "https://www.graodegente.com.br/produto/cesto-organizador-para-brinquedos-nuvem-de-algodao-28cm/", "Grão de Gente", "Cesto para fraldas, mantas e pequenos brinquedos.", "Dois cestos iguais deixam a prateleira com cara de boutique."),
    Product("Organização", "Cesto tricot onda natural", "Upgrade", 1, 265.68, "https://www.quintaldemadame.com.br/decoracao/cestos/cesto-tricot-onda-natural", "Quintal de Madame", "Cesto em tricô natural, peça textural.", "A textura faz o papel de luxo sem precisar de marca."),
    Product("Decoração", "Quadro infantil minimalista leão", "Essencial", 2, 59.90, "https://mundiminfantil.com/produtos/quadro-leao-minimalista-divertida/", "Mundi Infantil", "Quadro minimalista com moldura opcional.", "Usar em par, moldura madeira clara ou branca; instalar alto."),
    Product("Decoração", "Kit quadros minimalistas infantil", "Upgrade", 1, 239.70, "https://www.aluriakids.com.br/quadros/minimalista/", "Aluria Kids", "Kit de quadros infantis em estética minimalista.", "Escolher arte abstrata/animais lineares, não personagem."),
    Product("Decoração", "Mobile decorativo fora do berço", "Desejo", 1, 149.90, "https://lista.mercadolivre.com.br/mobile-montessori-bebe-madeira-feltro-neutro", "Mercado Livre", "Mobile para usar sobre trocador ou prateleira; não sobre grades do berço.", "Serve mais para styling do que para sono."),
    Product("Segurança", "Protetor de tomadas Safety 1st kit 10", "Essencial", 1, 10.76, "https://safety1st.com.br/collections/seguranca/products/protetor-de-tomadas-10-unidades", "Safety 1st", "Kit com 10 protetores de tomada.", "Comprar agora, instalar quando o bebê começar a explorar."),
    Product("Segurança", "Trava magnética Safety 1st kit 4", "Essencial", 1, 64.90, "https://safety1st.com.br/products/trava-magnetica", "Safety 1st", "Travas invisíveis para gavetas/armários.", "Instalar nas gavetas do Luna quando começar a engatinhar."),
    Product("Segurança", "Trava multifuncional Safety 1st", "Essencial", 2, 19.90, "https://safety1st.com.br/collections/travas-seguranca-armario-gaveta", "Safety 1st", "Travas flexíveis para portas ou gavetas.", "Útil para armário existente e portas de correr."),
    Product("Segurança", "Trava infantil para janela de correr", "Essencial", 1, 49.90, "https://lista.mercadolivre.com.br/trava-janela-correr-infantil", "Mercado Livre", "Limitador/trava para esquadria de correr.", "Mesmo com tela externa, a trava é camada extra."),
]


def money(value: float) -> str:
    return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def copy_assets() -> dict[str, Path]:
    ASSETS.mkdir(parents=True, exist_ok=True)
    VAULT_ASSETS.mkdir(parents=True, exist_ok=True)
    files = {
        "cover": "budget-couture-cover-cloud-dancer.png",
        "moodboard": "budget-couture-moodboard-cloud-dancer.png",
    }
    out: dict[str, Path] = {}
    for key, name in files.items():
        src = GEN_ASSETS / name
        dst = ASSETS / name
        if src.exists():
            shutil.copy2(src, dst)
            shutil.copy2(src, VAULT_ASSETS / name)
            out[key] = dst
    return out


def layout_svg() -> str:
    return """
<svg viewBox="0 0 620 620" role="img" aria-label="Planta baixa do quarto" class="plan">
  <rect x="60" y="60" width="500" height="500" fill="#fbfaf7" stroke="#2d2622" stroke-width="2"/>
  <text x="310" y="42" text-anchor="middle">PN • janela</text>
  <text x="310" y="590" text-anchor="middle">PS • prateleiras</text>
  <text x="24" y="315" transform="rotate(-90 24 315)" text-anchor="middle">PO • armário + porta</text>
  <text x="598" y="315" transform="rotate(90 598 315)" text-anchor="middle">PL • Luna</text>
  <rect x="60" y="60" width="110" height="305" fill="#d7bea5" stroke="#8a6d58"/>
  <text x="115" y="215" text-anchor="middle" transform="rotate(-90 115 215)">ARM-01</text>
  <path d="M60 395 L60 560 L205 560" fill="none" stroke="#9e9e9e" stroke-width="9"/>
  <path d="M60 500 Q150 500 150 410" fill="none" stroke="#b89a8d" stroke-width="2" stroke-dasharray="5 5"/>
  <text x="110" y="522" text-anchor="middle">POR-01</text>
  <rect x="398" y="178" width="162" height="382" rx="8" fill="#eee1d4" stroke="#8a6d58"/>
  <rect x="416" y="198" width="108" height="215" rx="6" fill="#f7f0e9" stroke="#c6a98f"/>
  <rect x="416" y="423" width="108" height="110" rx="6" fill="#ead7c8" stroke="#c6a98f"/>
  <rect x="524" y="198" width="24" height="335" rx="4" fill="#d8c0a8" opacity=".65"/>
  <text x="479" y="376" text-anchor="middle">LUNA 194cm</text>
  <text x="480" y="554" text-anchor="middle" class="small">60cm livres</text>
  <circle cx="270" cy="326" r="54" fill="#f1ebe4" stroke="#bfaea1"/>
  <circle cx="345" cy="345" r="28" fill="#f9f7f2" stroke="#c9bbb1"/>
  <text x="270" y="326" text-anchor="middle">Clarice</text>
  <rect x="225" y="536" width="170" height="14" fill="#d8c0a8"/>
  <rect x="245" y="510" width="130" height="14" fill="#d8c0a8"/>
  <text x="310" y="500" text-anchor="middle">Prateleiras PS</text>
  <rect x="195" y="60" width="255" height="14" fill="#d9e2e4" stroke="#9caeb2"/>
  <text x="323" y="94" text-anchor="middle">JAN-01</text>
</svg>"""


def totals_by_priority() -> dict[str, float]:
    totals: dict[str, float] = {}
    for p in PRODUCTS:
        totals[p.priority] = totals.get(p.priority, 0.0) + p.price * p.qty
    return totals


def category_sections() -> str:
    cats = []
    for cat in dict.fromkeys(p.category for p in PRODUCTS):
        rows = []
        subtotal = 0.0
        for p in [x for x in PRODUCTS if x.category == cat]:
            total = p.qty * p.price
            subtotal += total
            rows.append(f"""
<tr>
  <td><span class="tier {esc(p.tier).lower()}">{esc(p.tier)}</span><br><strong>{esc(p.item)}</strong><br><span class="muted">{esc(p.source)}</span></td>
  <td>{esc(p.description)}<p class="styling">{esc(p.styling)}</p></td>
  <td class="num">{p.qty}</td>
  <td class="num">{money(p.price)}</td>
  <td class="num">{money(total)}</td>
  <td><a href="{esc(p.link)}">Comprar / ver</a></td>
</tr>""")
        cats.append(f"""
<section class="page">
  <div class="kicker">Curadoria de compra</div>
  <h2>{esc(cat)}</h2>
  <table>
    <thead><tr><th>Item</th><th>Descrição + styling</th><th>Qtd.</th><th>Preço ref.</th><th>Total</th><th>Link</th></tr></thead>
    <tbody>{''.join(rows)}</tbody>
  </table>
  <p class="subtotal">Subtotal {esc(cat)}: <strong>{money(subtotal)}</strong></p>
</section>""")
    return "\n".join(cats)


def markdown_list() -> str:
    lines = [
        "---",
        "type: shopping_list",
        "project: quarto_bb",
        f"date: {date.today().isoformat()}",
        "concept: Budget Couture / Cloud Dancer",
        "---",
        "",
        "# Lista de Compras — Budget Couture",
        "",
        "Preços de referência coletados online em maio/2026. Conferir frete, voltagem, estoque, prazo e medidas antes de comprar.",
        "",
    ]
    for cat in dict.fromkeys(p.category for p in PRODUCTS):
        lines += [f"## {cat}", ""]
        for p in [x for x in PRODUCTS if x.category == cat]:
            lines += [
                f"### {p.item}",
                f"- **Tier:** {p.tier}",
                f"- **Qtd.:** {p.qty}",
                f"- **Preço ref.:** {money(p.price)}",
                f"- **Total:** {money(p.price * p.qty)}",
                f"- **Fonte:** {p.source}",
                f"- **Link:** {p.link}",
                f"- **Descrição:** {p.description}",
                f"- **Styling:** {p.styling}",
                "",
            ]
    total = sum(p.price * p.qty for p in PRODUCTS)
    lines += [f"## Total Geral Estimado", "", f"**{money(total)}**", ""]
    return "\n".join(lines)


def build_html(asset_paths: dict[str, Path]) -> str:
    cover_url = asset_paths.get("cover", "")
    mood_url = asset_paths.get("moodboard", "")
    total = sum(p.price * p.qty for p in PRODUCTS)
    essential = sum(p.price * p.qty for p in PRODUCTS if p.priority == "Essencial")
    upgrades = sum(p.price * p.qty for p in PRODUCTS if p.tier in {"Upgrade", "Desejo"})
    data_json = json.dumps(
        [{"category": p.category, "item": p.item, "tier": p.tier, "qty": p.qty, "price": p.price, "link": p.link} for p in PRODUCTS],
        ensure_ascii=False,
        indent=2,
    )
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Quarto BB — Budget Couture Shopping Dossier</title>
<style>
@page {{ size: A4; margin: 14mm; }}
* {{ box-sizing: border-box; }}
body {{ margin:0; color:#2d2622; background:#fbfaf7; font-family: Arial, Helvetica, sans-serif; line-height:1.42; }}
a {{ color:#7d5044; text-decoration:none; border-bottom:1px solid #d8b9ae; }}
h1,h2,h3 {{ font-family: Georgia, 'Times New Roman', serif; font-weight:400; margin:0 0 12px; }}
h1 {{ font-size:52px; line-height:.95; letter-spacing:-.04em; }}
h2 {{ font-size:34px; letter-spacing:-.03em; }}
h3 {{ font-size:20px; }}
p {{ margin:0 0 12px; }}
.page {{ page-break-after: always; padding: 6mm 0; }}
.cover {{ min-height: 265mm; display:grid; grid-template-rows: 1fr auto; gap:18px; }}
.hero {{ height:150mm; border-radius: 26px; overflow:hidden; border:1px solid #e1d7cf; }}
.hero img, .image img {{ width:100%; height:100%; object-fit:cover; display:block; }}
.titlebar {{ display:grid; grid-template-columns: 1.3fr .7fr; gap:20px; align-items:end; }}
.kicker {{ text-transform:uppercase; letter-spacing:.18em; color:#9a7569; font-size:10px; font-weight:700; margin-bottom:8px; }}
.subtitle {{ font-size:16px; color:#725e56; max-width:620px; }}
.meta {{ border:1px solid #d9ccc2; padding:16px; border-radius:18px; background:#fffdf9; font-size:12px; }}
.quote {{ font-family:Georgia,serif; font-size:25px; color:#5f4a42; padding:22px; border-left:2px solid #b99081; background:#fff; }}
.grid2 {{ display:grid; grid-template-columns:1fr 1fr; gap:20px; align-items:start; }}
.grid3 {{ display:grid; grid-template-columns: repeat(3,1fr); gap:12px; }}
.image {{ height:135mm; border-radius:22px; overflow:hidden; border:1px solid #e4d9d0; background:white; }}
.swatches {{ display:grid; grid-template-columns:repeat(6,1fr); gap:8px; margin:18px 0; }}
.swatch {{ min-height:70px; border-radius:14px; padding:9px; border:1px solid rgba(45,38,34,.08); display:flex; align-items:end; font-size:10px; color:#3b312c; }}
.s1 {{ background:#f4f1eb; }} .s2 {{ background:#e8d8ce; }} .s3 {{ background:#c99f91; }} .s4 {{ background:#d9c0a6; }} .s5 {{ background:#f2ede4; }} .s6 {{ background:#c3ad93; }}
.plan {{ width:100%; background:#fff; border-radius:20px; border:1px solid #dfd2c8; padding:12px; }}
svg text {{ font-family: Arial, sans-serif; font-size:15px; fill:#4b3c35; }} svg .small {{ font-size:12px; fill:#7b6a60; }}
.cards {{ display:grid; grid-template-columns:repeat(3,1fr); gap:14px; }}
.card {{ background:white; border:1px solid #e3d8d0; border-radius:18px; padding:16px; min-height:118px; }}
.big {{ font-family:Georgia,serif; font-size:30px; color:#6e5147; }}
table {{ width:100%; border-collapse:collapse; font-size:10px; background:#fff; border:1px solid #e2d8d0; }}
th {{ text-align:left; text-transform:uppercase; letter-spacing:.1em; font-size:8px; color:#8a6e64; background:#f3ede6; }}
th, td {{ padding:8px; vertical-align:top; border-bottom:1px solid #eee6df; }}
td.num {{ text-align:right; white-space:nowrap; }}
.muted {{ color:#88746b; font-size:9px; }}
.styling {{ margin-top:5px; font-style:italic; color:#7f6258; font-size:9px; }}
.tier {{ display:inline-block; padding:3px 7px; border-radius:999px; font-size:8px; text-transform:uppercase; letter-spacing:.08em; margin-bottom:4px; background:#eee; }}
.essencial {{ background:#efe5dc; }} .upgrade {{ background:#ead2cd; }} .desejo {{ background:#d5b69f; color:#fff; }}
.subtotal {{ text-align:right; margin-top:10px; color:#5e4a42; }}
.budget {{ font-size:22px; font-family:Georgia,serif; }}
.checklist li {{ margin:7px 0; }}
.footer-note {{ font-size:10px; color:#806d64; }}
pre {{ white-space:pre-wrap; font-size:8px; background:#fff; border:1px solid #eee; padding:10px; max-height:120mm; overflow:hidden; }}
</style>
</head>
<body>
<section class="page cover">
  <div class="hero"><img src="{Path(cover_url).as_uri() if cover_url else ''}" alt="Mood editorial Cloud Dancer"></div>
  <div class="titlebar">
    <div>
      <div class="kicker">Quarto BB · Shopping dossier</div>
      <h1>Budget<br>Couture</h1>
      <p class="subtitle">Curadoria completa para um quarto de bebê fashionista, inspirado em PANTONE 11-4201 Cloud Dancer, com compras reais no Brasil e inteligência de orçamento.</p>
    </div>
    <div class="meta">
      <strong>Cliente:</strong> Mãe do bebê<br>
      <strong>Área:</strong> 2,54 m × 2,54 m<br>
      <strong>Direção:</strong> Low budget, high taste<br>
      <strong>Data:</strong> Maio/2026<br>
      <strong>Entrega:</strong> PDF clicável + lista canônica
    </div>
  </div>
</section>

<section class="page">
  <div class="kicker">Manifesto</div>
  <h2>Moda italiana/francesa, orçamento brasileiro</h2>
  <div class="grid2">
    <div>
      <p class="quote">A proposta não é comprar luxo. É editar como quem entende luxo: pouca coisa, boa proporção, textura certa e paleta impecável.</p>
      <p>O quarto parte do <strong>Cloud Dancer</strong>, branco etéreo da Pantone 2026, e substitui o excesso infantil por uma atmosfera de boutique: madeira savana, bouclé, algodão, voil, blush em pequenas doses e metal champagne.</p>
      <p>Para uma mãe que ama Vogue, Itália e França, a régua é: <strong>silhueta limpa, materiais táteis, nada óbvio, nada temático demais</strong>. O bebê ganha conforto; a mãe ganha um quarto com identidade.</p>
    </div>
    <div class="image"><img src="{Path(mood_url).as_uri() if mood_url else ''}" alt="Moodboard Cloud Dancer"></div>
  </div>
  <div class="swatches">
    <div class="swatch s1">Cloud Dancer</div><div class="swatch s2">Powder blush</div><div class="swatch s3">Tea rose</div><div class="swatch s4">Savana wood</div><div class="swatch s5">Bouclé cream</div><div class="swatch s6">Champagne</div>
  </div>
</section>

<section class="page">
  <div class="kicker">Layout fiel</div>
  <h2>Planta de implantação</h2>
  <div class="grid2">
    <div>{layout_svg()}</div>
    <div>
      <h3>Regras executivas</h3>
      <ul>
        <li><strong>PO:</strong> armário existente no trecho norte e porta no sudoeste. Sem prateleiras.</li>
        <li><strong>PL:</strong> Luna encostado na parede leste, ocupando 194 cm de uma parede de 254 cm.</li>
        <li><strong>PS:</strong> parede vazia para duas prateleiras, fora da zona de abertura da porta.</li>
        <li><strong>PN:</strong> janela com voil + blackout; manter berço fora do eixo direto da janela.</li>
      </ul>
      <div class="card">
        <div class="kicker">Proporção</div>
        <div class="big">194 / 254 = 76%</div>
        <p class="footer-note">O berço multifuncional é grande, mas não ocupa a parede inteira: restam cerca de 60 cm no canto PS-PL.</p>
      </div>
    </div>
  </div>
</section>

<section class="page">
  <div class="kicker">Resumo financeiro</div>
  <h2>Quanto comprar agora</h2>
  <div class="cards">
    <div class="card"><div class="kicker">Essencial executável</div><div class="budget">{money(essential)}</div><p>Itens para o quarto funcionar com segurança, sono, troca, amamentação e clima.</p></div>
    <div class="card"><div class="kicker">Upgrades + desejos</div><div class="budget">{money(upgrades)}</div><p>Camadas editoriais: textura, tapete premium, luz indireta, peças com acabamento mais fashion.</p></div>
    <div class="card"><div class="kicker">Lista completa</div><div class="budget">{money(total)}</div><p>Inclui todos os itens e alternativas, sem descontar escolhas mutuamente excludentes.</p></div>
  </div>
  <p class="footer-note">Observação: a lista completa soma opções alternativas. Para compra real, escolher uma opção por categoria quando houver Essencial/Upgrade/Desejo.</p>
</section>

{category_sections()}

<section class="page">
  <div class="kicker">Ordem de compra</div>
  <h2>Sequência para não errar</h2>
  <ol class="checklist">
    <li><strong>Medir antes de comprar:</strong> altura útil da cortina na PN e voltagem do ar-condicionado.</li>
    <li><strong>Comprar âncoras:</strong> Luna, colchão e Clarice. Eles definem tudo.</li>
    <li><strong>Resolver obra leve:</strong> pintura Cloud Dancer, AC, ponto de luz/dimmer.</li>
    <li><strong>Instalar cortina e papel:</strong> antes da montagem final, para evitar sujeira nos móveis.</li>
    <li><strong>Montar o styling:</strong> prateleiras PS, mesa, luz noturna, cestos, quadros.</li>
    <li><strong>Finalizar segurança:</strong> protetor de tomadas, travas, janela, checagem de fios e cortina.</li>
  </ol>
  <div class="quote">Comprar menos, mas editar melhor. A estética Vogue nasce da seleção, não da quantidade.</div>
</section>

<section class="page">
  <div class="kicker">Checklist final</div>
  <h2>Lista rápida para WhatsApp</h2>
  <ul class="checklist">
    <li>Luna Branco/Savana + colchão 130x70x12</li>
    <li>Clarice bouclé pérola/creme + puff</li>
    <li>Prateleiras Luna na PS + mesa Gueridon branca</li>
    <li>Blackout + voil + trilho suíço duplo na PN</li>
    <li>Pintura Cloud Dancer + painel discreto PL</li>
    <li>Plafon dimerizável + luz noturna + termo-higrômetro</li>
    <li>AC 9.000 BTU inverter na PS, sem jato no berço</li>
    <li>Tapete lavável bege/creme</li>
    <li>Lençóis 100% algodão, protetores impermeáveis e sacos de dormir</li>
    <li>Cestos, quadros minimalistas, kit higiene branco/dourado</li>
    <li>Travas, protetores de tomada e trava de janela</li>
  </ul>
  <p class="footer-note">Preços e disponibilidade mudam. Conferir estoque, frete, prazo, voltagem, medidas e política de troca antes de finalizar a compra.</p>
</section>

<section class="page">
  <div class="kicker">Dados estruturados</div>
  <h2>Apêndice técnico</h2>
  <p class="footer-note">Resumo JSON para futuras automações ou atualização de preços.</p>
  <pre>{esc(data_json)}</pre>
</section>
</body>
</html>"""


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    VAULT_OUT.mkdir(parents=True, exist_ok=True)
    asset_paths = copy_assets()

    md = markdown_list()
    md_path = VAULT / "09-lista-compras-budget-couture.md"
    md_path.write_text(md, encoding="utf-8")
    (OUT / "quarto-bb-lista-compras-budget-couture.md").write_text(md, encoding="utf-8")

    html_text = build_html(asset_paths)
    html_path = OUT / "quarto-bb-budget-couture.html"
    html_path.write_text(html_text, encoding="utf-8")
    (VAULT_OUT / "quarto-bb-budget-couture.html").write_text(html_text, encoding="utf-8")

    pdf_path = OUT / "quarto-bb-budget-couture.pdf"
    edge_candidates = [
        Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
        Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
        Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
    ]
    browser = next((p for p in edge_candidates if p.exists()), None)
    if not browser:
        raise SystemExit("No Edge/Chrome executable found for PDF generation")

    subprocess.run(
        [
            str(browser),
            "--headless=new",
            "--disable-gpu",
            f"--print-to-pdf={pdf_path}",
            "--print-to-pdf-no-header",
            html_path.as_uri(),
        ],
        check=True,
    )
    if not pdf_path.exists() or pdf_path.stat().st_size < 1000:
        raise SystemExit("PDF was not generated correctly")

    shutil.copy2(pdf_path, VAULT_OUT / pdf_path.name)
    shutil.copy2(html_path, VAULT_OUT / html_path.name)
    print(json.dumps({
        "html": str(html_path),
        "pdf": str(pdf_path),
        "markdown": str(md_path),
        "pdf_size": pdf_path.stat().st_size,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
