# Quarto Giulia v2 — Plano de implementação (Fase 2)

> Brief canônico: [`../brief/2026-07-07-quarto-giulia-v2.md`](../brief/2026-07-07-quarto-giulia-v2.md)

**Goal:** Produzir layout, lista de compras, memorial elétrico e dossiê HTML/PDF para o quarto 2,54×2,54 m da Giulia.

**Fase 1 concluída:** brief, JSONs, arquivar v1, reorganizar assets.

---

## Gate

| Item | Status |
|------|--------|
| Medidas quarto | OK — 2,54×2,54 m |
| Móveis brancos (sem azul) | OK — berço + cômoda trocador |
| Medidas móveis | Pendente |
| Foto interruptor | Pendente |

---

### Task 1: Layout v2

**Files:** `plantas/layout-v2.md`, `docs/quarto.json`

- [ ] Planta 2,54×2,54 com berço, cômoda branca, poltrona, armário PO/PN
- [ ] Circulação 60–70 cm
- [ ] Marcar parede PL (boiserie + papel)

### Task 2: Lista de compras v2

**Files:** `entregaveis/quarto-giulia-lista-compras-v2.md`

- [ ] Paredes: tinta, EVA, massa, papel, perfil LED 10,5 m, dimmer
- [ ] Poltrona bouclé giratória
- [ ] Elétrica: interruptor duplo, dimmer LED, arandela
- [ ] Decoração, enxoval 130×70
- [ ] Tiers: Essencial / Upgrade / Desejo
- [ ] **Excluir** berço e cômoda (presenteados)

### Task 3: Memorial elétrico

**Files:** `docs/brief/escopo-eletrico-led.md` (expandir)

- [ ] Diagrama 2 circuitos para eletricista
- [ ] Lista de materiais com links BR

### Task 4: Dossiê HTML/PDF v2

**Files:** `scripts/build_quarto_giulia_v2.py`, `entregaveis/quarto-giulia-v2.html`

- [ ] Moodboard Soft Feminine
- [ ] Seção móveis brancos presenteados
- [ ] Sistema de paredes em camadas

### Task 5: Graphify + publicação

- [ ] Regenerar `graphify-out/`
- [ ] Commit e push
