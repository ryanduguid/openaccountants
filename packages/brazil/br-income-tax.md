---
name: br-irpf-declaracao
description: >
  Skill para IRPF 2026 (ano-base 2025). Use quando o usuário mencionar "IRPF", "Imposto de Renda",
  "declaração de IR", "malha fina", "DARF", "REVAR", "Cashback IRPF", "pré-preenchida",
  "Núcleo Familiar", "restituição IR", "bets imposto", "ComprovaBet", "e-Social IR", "DIRF",
  "ganhos bolsa imposto", "day trade", "GCAP", "ganho de capital", "vender imóvel",
  "isenção 180 dias", "MEI declaração", "lucro distribuído", "espólio inventário herança",
  "saída definitiva exterior", "residência fiscal", "IRPFM", "imposto mínimo", "Lei 15.270",
  "Lei 14.754", "antidiferimento offshore", "trust", "tributação dividendos", "PCD doença grave",
  "atividade rural DITR", "Carnê-Leão aluguel", "PGBL VGBL", "doação ITCMD", "Simples Nacional",
  "how much tax do I pay in Brazil", "income tax return Brazil", "deductible expenses Brazil",
  "self-employed tax Brazil". Cobre obrigatoriedade, modelos completo/simplificado, pré-preenchida,
  REVAR/B3, renda fixa, bets, ganho de capital, malha fina/e-Social, restituição/cashback, e casos
  especiais (espólio, MEI, saída definitiva, PCD, atividade rural, cônjuges).
version: 3.0
---

# IRPF Brasil — Declaração de Ajuste Anual 2026 (Ano-Base 2025)

> **Baseado no trabalho de [Daniel Luz (@Danielbluz)](https://github.com/Danielbluz/skill-irpf-brasil)**, licenciado sob MIT. Adaptado para o formato OpenAccountants.

> **Aviso:** Esta skill orienta e audita. Não substitui o programa oficial da Receita Federal nem orientação contábil profissional. Todos os outputs devem ser revisados por um contador habilitado (CRC) antes de protocolar/transmitir.

---

## Premissas Operacionais

- **Período de entrega**: 23/03/2026 a 29/05/2026 (IN RFB nº 2.312).
- **Multa por atraso**: R$ 165,74 (mínima) até 20% do imposto devido.
- **Nova isenção de R$ 5.000/mês NÃO vale para IRPF 2026.** Só se aplica ao ciclo 2027 (ano-base 2026). Para 2026, o limite continua R$ 35.584,00.

---

## Fluxo de Trabalho

Executar nesta ordem:

1. **Triagem de obrigatoriedade** — Verificar TODOS os critérios antes de prosseguir.
2. **Escolha do modelo** — Completo vs simplificado (teste A/B).
3. **Pré-preenchida** — Importar primeiro, auditar depois.
4. **Renda variável** — Se houver operações em bolsa/FII.
5. **Renda fixa** — Se houver CDB, Tesouro, LCI/LCA, fundos.
6. **Bets** — Se houver apostas esportivas/cassino online.
7. **Ganho de capital** — Se houve venda de imóvel, veículo ou ações fora de bolsa.
8. **Auditoria malha fina** — Cruzar informe vs pré-preenchida.
9. **Restituição/Cashback** — Orientar sobre lotes e PIX-CPF.

### Princípios de Comunicação

- Responder em português brasileiro.
- Valores em formato BR: R$ 35.584,00 (não R$ 35,584.00).
- Datas em DD/MM/AAAA.
- Nunca inventar valores ou alíquotas.
- Nunca recomendar sonegação ou planejamento fiscal agressivo.

### Sinalizadores de Risco

| Sinal | Risco | Ação |
|---|---|---|
| "Vou declarar só o que tem no informe" | Omissão de bens/renda variável | Verificar obrigatoriedade |
| "Vou apagar o que veio na pré-preenchida" | Malha fina garantida | Ver seção Malha Fina |
| "Recebi prêmio de aposta lá fora" | Tributação inversa | Ver seção Bets |
| "Meu filho de 22 anos trabalhou em 2025" | Núcleo Familiar pode importar renda | Ver seção Pré-preenchida |
| "Não preciso declarar, recebi pouco" | Pode ter direito ao Cashback | Ver seção Restituição |

---

## Obrigatoriedade de Declaração

Base legal: IN RFB nº 2.312/2026. Basta **qualquer um** dos critérios abaixo:

| # | Critério | Limite |
|---|---|---|
| 1 | Rendimentos tributáveis (salário, aposentadoria, pensão, aluguel) | > R$ 35.584,00 |
| 2 | Rendimentos isentos, não tributáveis ou tributados exclusivamente na fonte | > R$ 200.000,00 |
| 3 | Posse ou propriedade de bens e direitos em 31/12/2025 | > R$ 800.000,00 |
| 4 | Receita bruta em atividade rural | > R$ 177.920,00 |
| 5 | Operações em bolsa — soma das vendas no ano | > R$ 40.000,00 |
| 6 | Ganho líquido mensal em ações (operações comuns) | Qualquer mês > R$ 20.000,00 |
| 7 | Day trade | Qualquer ganho líquido |
| 8 | Compensação de prejuízos rurais | Qualquer valor |
| 9 | Ganho de capital em alienação de bens sujeito a IR | Qualquer ganho tributável |
| 10 | Venda de imóvel residencial com isenção (180 dias) | Qualquer operação |
| 11 | Passou à condição de residente no Brasil em 2025 | Qualquer caso |
| 12 | Optou por declarar bens no exterior como entidade controlada | Qualquer caso |

### MEI — Duas Obrigações Distintas

1. **DASN-SIMEI** — Sempre obrigatória, prazo até 31/05.
2. **IRPF (DAA)** — Só se a pessoa física se enquadrar nos critérios acima.

Lucro distribuível isento do MEI:
- Comércio/Indústria: 8% da receita bruta
- Transporte de cargas: 8%
- Transporte de passageiros: 16%
- Serviços em geral: 32%

O excedente é rendimento tributável.

---

## Tabela Progressiva Anual IRPF 2026 (Ano-Base 2025)

| Base de cálculo anual | Alíquota | Parcela a deduzir |
|---|---|---|
| Até R$ 29.145,60 | 0% | — |
| R$ 29.145,61 a R$ 33.919,80 | 7,5% | R$ 2.185,92 |
| R$ 33.919,81 a R$ 45.012,60 | 15% | R$ 4.729,91 |
| R$ 45.012,61 a R$ 55.976,16 | 22,5% | R$ 8.105,85 |
| Acima de R$ 55.976,16 | 27,5% | R$ 10.904,66 |

**Fórmula:** Imposto = (base de cálculo × alíquota) − parcela a deduzir

### Isenção Adicional — Aposentados 65+

Limite mensal: R$ 1.903,98 sobre rendimentos de aposentadoria/pensão. Limite anual: ~R$ 24.751,74.

---

## Modelos de Declaração e Deduções

### Simplificado
- Desconto de 20% sobre rendimentos tributáveis, máximo R$ 16.754,34.
- Sem comprovação de despesas.

### Completo — Deduções Discriminadas

| Dedução | Limite |
|---|---|---|
| Dependentes | R$ 2.275,08 por dependente/ano |
| Educação | R$ 3.561,50 por pessoa/ano |
| Despesas médicas | Sem teto |
| Previdência privada PGBL | 12% da renda tributável |
| Pensão alimentícia judicial | Sem teto |
| INSS / Previdência oficial | Sem teto |
| Livro Caixa (autônomo) | Despesas necessárias |
| Doações (FIA, esporte, idoso) | 6% do imposto devido |

### Algoritmo de Decisão

1. Somar todas as deduções discriminadas válidas.
2. Calcular limite simplificado: min(rendimento × 0,20; R$ 16.754,34).
3. Se deduções > simplificado → completa. Caso contrário → simplificada.

### Educação — O que ENTRA

Educação infantil, ensino fundamental/médio, técnico, superior, pós stricto sensu (mestrado, doutorado).

### Educação — O que NÃO ENTRA

Idiomas, informática, música/arte/esportes, material escolar, transporte escolar, cursos pré-vestibular, cursos livres, pós lato sensu (MBA, especialização).

### Despesas Médicas — Validação Obrigatória

- Toda despesa > R$ 1.500 deve ter comprovante (NF com CPF/CNPJ do prestador).
- Reembolsos do plano de saúde devem ser subtraídos. Top 3 motivos de malha fina.
- NÃO entram: medicamentos de farmácia (exceto em nota de internação), vacinas em geral, acompanhante.

### Dependentes — Regras

| Dependente | Condição |
|---|---|
| Cônjuge/companheiro(a) | Convivência > 5 anos ou filho em comum |
| Filho/enteado | Até 21. Até 24 se ensino superior. Sem limite se incapacitado. |
| Pais, avós | Renda própria até R$ 28.467,20 em 2025 |

---

## Pré-Preenchida e Núcleo Familiar

### Por que usar

- Prioridade na restituição (com PIX-CPF).
- Menor risco de malha fina.
- Requer Gov.br nível Prata ou Ouro.

### O que vem pré-preenchido

Dados do e-Social, EFD-Reinf, REVAR (B3), DMED (saúde), e-Financeira (bancos), cartórios, DIMOB (aluguéis), declarações anteriores.

### Núcleo Familiar — A Armadilha

Ao incluir dependente, o sistema importa automaticamente TODA a renda associada ao CPF do dependente. Se o dependente teve renda significativa, ela é somada à base do titular.

**Sempre simular 3 cenários:**
- A: Titular sozinho + dependente separado
- B: Titular com dependente (Núcleo Familiar)
- C: Quem tem renda maior declara o outro

Escolher o cenário com menor imposto total combinado.

---

## Renda Variável e REVAR

### Alíquotas

| Operação | Alíquota |
|---|---|
| Swing trade em ações | 15% |
| Day trade | 20% |
| FIIs | 20% |
| ETFs de ações | 15% |
| Opções, futuros, termo | 15% comum / 20% day trade |

### Isenção Mensal

Operações comuns em ações: vendas no mês ≤ R$ 20.000 → lucro isento. Não vale para FIIs, day trade, opções.

### Apuração Mensal

Renda variável é apurada mês a mês, não anualmente. DARF código 6015 até último dia útil do mês seguinte.

### Compensação de Prejuízos

- Prejuízo de operação comum só compensa lucro de operação comum.
- Prejuízo de day trade só compensa lucro de day trade.
- Sem compensação cruzada. Sem prazo de prescrição.

### Criptomoedas

- Isenção: vendas mensais até R$ 35.000.
- Acima: 15% sobre ganho de capital via GCAP.
- Bens e Direitos código 08, grupo 99.

### Erros Frequentes

- Declarar ações pelo valor de mercado (correto: custo médio de aquisição).
- Esquecer JCP recebido (tributação exclusiva).
- Compensar prejuízo de day trade com lucro de swing trade.
- Operações em bolsa internacional NÃO entram no REVAR.

---

## Apostas Esportivas e Cassino Online (Bets)

Base legal: Lei nº 14.790/2023.

### Declaração Patrimonial

Saldo na carteira da bet em 31/12/2025 superior a R$ 140 → obrigatório declarar em Bens e Direitos (Grupo 06, Código 02).

### Tributação — POR EVENTO

**A apuração é por evento, não consolidada anualmente** (IN RFB nº 2.191/2024).

- NÃO existe compensação de perdas entre eventos.
- Cada evento/sessão é um fato gerador isolado.
- Faixa isenta: primeira faixa da tabela progressiva (~R$ 28.467,20/ano).
- Alíquota: 15% sobre o excedente.

### Plataforma Nacional vs Offshore

**Nacional (autorizada pelo Min. Fazenda):**
- Empresa retém 15% automaticamente.
- Declarar em Rendimentos Sujeitos à Tributação Exclusiva/Definitiva.
- Exigir ComprovaBet.

**Offshore (não autorizada):**
- Responsabilidade de recolhimento inverte para o apostador.
- Carnê-Leão mensal, DARF código 0190.
- Tabela progressiva mensal (não faixa fixa de 15%).
- Se não recolheu durante 2025: DARFs retroativos com multa + juros SELIC.

---

## Ganho de Capital (GCAP)

Apurado em programa separado (GCAP), não no programa IRPF. DARF código 4600.

### Alíquotas Progressivas

| Faixa de ganho | Alíquota |
|---|---|
| Até R$ 5.000.000 | 15% |
| R$ 5M a R$ 10M | 17,5% |
| R$ 10M a R$ 30M | 20% |
| Acima de R$ 30M | 22,5% |

### Isenções — Imóvel Residencial

**Imóvel único até R$ 440.000:** isento se não houve outra alienação isenta nos últimos 5 anos.

**Reinvestimento 180 dias:** isento se todo o produto da venda for aplicado em outro imóvel residencial no Brasil em até 180 dias. Não usada nos últimos 5 anos. Aplicação parcial → tributação proporcional.

### Custo de Aquisição Inclui

Valor do contrato, ITBI, corretagem na compra, reformas/benfeitorias com NF, juros de financiamento.

---

## Malha Fina e e-Social

### Contexto 2026

DIRF foi extinta. Substituída por e-Social + EFD-Reinf. A migração gerou erros massivos de parametrização pelos RHs.

### Regra de Ouro

**NUNCA alterar manualmente a pré-preenchida para igualar ao informe.** A pré-preenchida vem da base oficial do governo.

### Erros Mais Comuns

1. **13º como rendimento comum** — Deve ser tributação exclusiva. Diferença de ~1/13 do total.
2. **Regime caixa vs competência** — Salário de dezembro/2025 pago em janeiro/2026 não tributa em 2025.
3. **Plano de saúde duplicado** — e-Social + DMED.
4. **PLR como rendimento comum** — Deve ser tributação exclusiva.

### Protocolo de Defesa

1. **Congelar** — Não transmitir, não apagar valores.
2. **Analisar** — Identificar qual rubrica diverge.
3. **Acionar RH por escrito** — Solicitar retificação do e-Social (evento S-5002).
4. **Aguardar reprocessamento** — 7 dias úteis após retificação.
5. **Transmitir** — Após confirmação de que os dados batem.

Se empresa não retifica: transmitir com valores da pré-preenchida e enviar retificadora quando corrigido.

---

## Restituição e Cashback IRPF

### Cronograma 2026 — 4 Lotes

| Lote | Data |
|---|---|
| 1º | 29/05/2026 |
| 2º | 30/06/2026 |
| 3º | 31/07/2026 |
| 4º | 28/08/2026 |

### Ordem de Prioridade

1. Idosos 80+
2. Idosos 60+
3. Portadores de doença grave
4. PCD
5. Professores
6. Pré-preenchida + PIX-CPF
7. Demais, por ordem cronológica

### PIX-CPF

Chave PIX deve ser exclusivamente o CPF do declarante. Dá prioridade adicional na restituição.

### Cashback IRPF — Novidade 2026

Para quem NÃO é obrigado a declarar mas teve IR retido na fonte em 2025. Devolução automática via PIX em 15/07/2026. Critérios: renda < R$ 35.584, IRRF retido, CPF regularizado com PIX-CPF ativo.

### Imposto a Pagar

- Quota única até 30/05/2026, ou até 8 parcelas (mínimo R$ 50/quota).
- DARF código 0211.
- Débito automático disponível se transmitir até 10/05/2026.

---

## Casos Especiais

### Espólio

Três tipos de declaração: Inicial (ano do falecimento), Intermediária (anos entre falecimento e partilha), Final (ano da partilha). Inventariante declara usando CPF do falecido. Não há ganho de capital se bens transferidos pelo valor declarado.

### Saída Definitiva

Comunicação até último dia de fevereiro do ano seguinte. Após saída: CPF fica como não-residente, rendimentos no Brasil tributados na fonte (25% trabalho, 15% aluguéis). Saída temporária (< 12 meses) não requer DSDP.

### Cônjuges — Conjunta vs Separada

**Conjunta vence:** apenas um tem renda significativa. **Separada vence:** ambos com renda alta. Sempre simular ambos cenários.

### PCD / Doença Grave

Aposentadoria/pensão isenta de IR para portadores de doença grave (Lei 7.713/88). Dependente sem limite de idade se incapacitado. Isenção permanente após reconhecimento.

### Atividade Rural

Obriga DAA se receita bruta > R$ 177.920. Pode optar por lucro presumido (20%) ou real (receita − despesas). Prejuízos compensáveis sem limite de tempo.

### Carnê-Leão

Para rendimentos sem retenção na fonte (aluguéis de PF, serviços a PF, rendimentos do exterior). DARF código 0190, mensal.

---

## Checklist Pré-Transmissão

- [ ] Verificar TODOS os critérios de obrigatoriedade
- [ ] Comparar informes de rendimento vs pré-preenchida
- [ ] 13º em Tributação Exclusiva (não em Tributáveis)
- [ ] Plano de saúde não duplicado
- [ ] Reembolsos de saúde subtraídos das despesas
- [ ] Despesas médicas com NF e CPF do prestador
- [ ] Educação dentro do teto (R$ 3.561,50/pessoa)
- [ ] Simulação completa vs simplificada feita
- [ ] Bens novos lançados com valor de escritura/NF
- [ ] Saldos em 31/12/2025 batem com extratos bancários
- [ ] DARFs mensais pagos durante 2025 (renda variável, Carnê-Leão)
- [ ] PIX-CPF ativo para restituição
- [ ] Recibo da declaração salvo (guardar 5 anos)

---

## Fontes Oficiais

- **IN RFB nº 2.312/2026** — Regras IRPF 2026
- **Lei nº 14.790/2023** — Apostas esportivas
- **Lei nº 14.754/2023** — Investimentos no exterior
- **Lei nº 14.973/2024** — Atualização de imóveis
- **Portal Meu Imposto de Renda**: https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda
- **Perguntas e Respostas IRPF 2026**: https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/perguntas-e-respostas

---

*Última atualização: abril/2026 — IRPF 2026 (ano-base 2025), conforme IN RFB 2.312/2026.*
*Conteúdo original: [Daniel Luz (@Danielbluz)](https://github.com/Danielbluz/skill-irpf-brasil) — MIT License.*
*OpenAccountants — open-source tax computation skills — info@openaaccountants.com*
