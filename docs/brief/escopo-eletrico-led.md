# Escopo elétrico e LED — Memorial v2

## Referência

- Planta: [`../referencias/eletrica-apto-patio-clube.pdf`](../referencias/eletrica-apto-patio-clube.pdf)
- Empreendimento: Pátio Condomínio Clube
- `layout_espelhado: true`
- Quarto Giulia: **2,54 × 2,54 m**, sem suíte, apto 3 quartos

## Estado atual (dormitório tipo)

| Ponto | Qtd. | Localização típica |
|-------|------|-------------------|
| Luz teto | 1 | Centro do teto |
| Interruptor simples | 1 | Junto à porta (PO no layout espelhado) |
| Tomada 220V | 3 | Paredes laterais + TV |
| Ponto TV | 1 | Parede oposta à porta |

**Atenção:** *Não executar furos na região do quadro de luz* (hall).

## Objetivo do retrofit

Substituir interruptor único por **2 circuitos independentes**, sendo o circuito 2 controlado por **dimmer compatível com LED**.

```
ANTES                          DEPOIS
────────                       ──────
[Interruptor]──► Luz teto      [Tecla 1]──────► Luz teto
                               [Dimmer LED]───► Fita rodapé 10,5m
                                                └──► Arandela PS
```

## Circuitos

| Circuito | Carga | Potência est. | Controle |
|----------|-------|---------------|----------|
| **C1 — Geral** | Luminária teto existente ou plafon LED | 10–30 W | Interruptor simples (tecla 1) |
| **C2 — Ambiente** | Fita LED rodapé 2700K + arandela | 15–40 W total | **Dimmer LED** (tecla 2) |

### Fita LED rodapé

| Parâmetro | Especificação |
|-----------|---------------|
| Comprimento | **10,5 m** (perímetro 9,4 m + reserva) |
| Temperatura | **2700K** (quente) |
| Perfil | Alumínio embutido ou sobreposto tipo rodapé |
| Driver | Compatível com dimmer (verificar carga mínima do dimmer, tip. 5 W) |
| Instalação | Derivação na caixa do interruptor ou quadro do circuito |

### Arandela

| Parâmetro | Especificação |
|-----------|---------------|
| Posição | Parede **PS**, acima da poltrona amamentação |
| Temperatura | 2700–3000K |
| Fluxo | Baixo (indireto / abajur de parede) |
| Circuito | **C2** (mesmo dimmer do LED rodapé) |

## Materiais — lista para eletricista

| Item | Qtd. | Observação |
|------|------|------------|
| Interruptor duplo 4×2 | 1 | Substituir módulo existente |
| Dimmer LED bivolt | 1 | Mín. 5 W; testar com fita escolhida |
| Fita LED 2700K 12V/24V | 10,5 m | Com driver se necessário |
| Perfil alumínio | 10,5 m | Cantos com união |
| Fonte/driver LED | 1 | Dimensionar para 10,5 m |
| Arandela LED | 1 | Baixo fluxo, 2700K |
| Cabo flexível 1,5 mm² | ~15 m | Derivações rodapé + arandela |
| Caixa 4×2 profunda | 1 | Se dimmer + interruptor não couberem na caixa atual |

### Links de referência (compra)

- Interruptor + dimmer: https://lista.mercadolivre.com.br/interruptor-duplo-dimmer-led
- Perfil + fita: https://casaedetalhe.com.br/produto/perfil-aluminio-c-fita-led/
- Arandela: https://lista.mercadolivre.com.br/arandela-led-2700k-dimerizavel

## Sequência de instalação

1. Desligar circuito no disjuntor
2. Substituir interruptor por módulo duplo (tecla + dimmer)
3. Passar cabos do rodapé LED no rodapé/perfil (antes da pintura final se embutido)
4. Instalar perfil + fita no perímetro (exceto vão porta ~80 cm)
5. Derivar cabo para arandela na PS
6. Testar dimmer em brilho mínimo/máximo
7. Ajustar cena: mamada = rodapé 10–20%, arandela ligada; dia = teto C1

## Pendências

- [ ] Foto da caixa de interruptor existente (profundidade, neutro disponível)
- [ ] Confirmar se luz teto atual é LED ou incandescente (define troca do bulbo)
- [ ] Validar parede PS para arandela (sem tubulação/umidade)

## Ordem de obra integrada

1. **Elétrica** (este memorial)
2. Pintura base
3. Boiserie EVA + massa + pintura
4. Papel de parede
5. Acabamento rodapé LED (tampa perfil)
6. Móveis
