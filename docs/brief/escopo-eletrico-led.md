# Escopo elétrico e LED

## Referência

- Planta: [`../referencias/eletrica-apto-patio-clube.pdf`](../referencias/eletrica-apto-patio-clube.pdf)
- Empreendimento: Pátio Condomínio Clube
- `layout_espelhado: true`
- Apartamento: 3 quartos (Giulia = quadrado 2,54×2,54 m, sem suíte)

## Estado atual (por dormitório — planta tipo)

| Ponto | Qtd. |
|-------|------|
| Luz teto | 1 |
| Interruptor simples | 1 (junto à porta) |
| Tomada 220V | 3 |
| Ponto TV | 1 |

**Atenção:** *Não executar furos na região do quadro de luz* (hall).

## Retrofit solicitado

Converter **interruptor único → 2 circuitos + dimmer LED**.

| Circuito | Carga | Controle |
|----------|-------|----------|
| **1 — Geral** | Luminária teto | Interruptor / tecla 1 |
| **2 — Ambiente** | Fita LED rodapé + arandela | **Dimmer LED** / tecla 2 |

### Materiais elétricos preliminares

- Interruptor duplo ou 2 módulos em caixa existente
- Dimmer compatível com LED (mín. 5 W, verificar carga total fita)
- Fita LED 2700K ~10,5 m + driver/blindagem
- Perfil alumínio embutido ou sobreposto (rodapé)
- Cabo adequado para derivação arandela
- Arandela LED baixo fluxo (2700–3000K)

## Impacto do espelhamento

Paredes com interruptor e tomadas **invertem** em relação à planta PDF. Usar fotos reais PL/PN/PO/PS para posicionar arandela (zona poltrona) e derivação LED.

## Pendências

- [ ] Foto interruptor real no quarto Giulia
- [ ] Confirmar voltagem (planta indica 220V nas tomadas)
- [ ] Definir se arandela compartilha circuito 2 com LED rodapé

## Memorial para eletricista (rascunho)

```
Entrada: interruptor simples existente (1 módulo)
Saída:   módulo 1 → retorno luz teto (manter ou trocar por plafon LED)
         módulo 2 → dimmer LED → fita rodapé (~10,5 m, 2700K) + arandela
Derivação: alimentação contínua para LED se dimmer exigir neutro permanente
```
