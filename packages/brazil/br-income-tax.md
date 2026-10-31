---
name: br-income-tax
description: "Use esta skill sempre que for solicitado sobre o imposto de renda brasileiro para pessoas físicas autônomas (autônomos / profissionais liberais). Ative com frases como \"quanto de imposto eu pago no Brasil\", \"DIRPF\", \"IRPF\", \"Carnê-Leão\", \"livro caixa\", \"imposto de renda\", \"CPF\", \"declaração de imposto de renda Brasil\", \"despesas dedutíveis Brasil\", \"imposto autônomo Brasil\", \"desconto simplificado\", \"INSS autônomo\", \"pró-labore\", \"DAS MEI\", ou qualquer pergunta sobre apuração ou cálculo de imposto de renda para um cliente autônomo ou freelancer no Brasil. Esta skill cobre a DIRPF anual, os pagamentos mensais estimados via Carnê-Leão, as faixas progressivas do IRPF, livro caixa, deduções permitidas, desconto simplificado (20%), limites obrigatórios de entrega da declaração, contribuições ao INSS e penalidades. SEMPRE leia esta skill antes de tratar qualquer trabalho de imposto de renda brasileiro. Trigger also on: \"how much tax do I pay in Brazil\", \"DIRPF\", \"IRPF\", \"Carnê-Leão\", \"livro caixa\", \"income tax return Brazil\", \"deductible expenses Brazil\", \"self-employed tax Brazil\", \"INSS autônomo\"."
version: 2.0
jurisdiction: BR
category: international
tax_year: 2025
last_updated: 2026-10-31
reviewed_by: Ariane Marrocos
review_status: pending_review
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# BR Income Tax

## Brasil — Imposto de Renda (IRPF e IRPJ) — Skill v2.1

> **Accountant-reviewed.** Rates and thresholds reviewed against the cited authorities by **Ariane Marrocos** on 2026-06-03; the sign-off is recorded in the frontmatter (`reviewed_by`) and on the roster in `PARTNERS.md`. The verified figures are stated in the sections below with their sources (the separate "Verified rates & thresholds" list that carried them was folded into the body on 2026-09-29). Items the review flagged for clarification are excluded from that sign-off and remain marked in the text.

## Seção 1 — Referência rápida

### Reforma tributária 2026 — impacto no IR

A Reforma Tributária de 2026 (EC 132/2023, LC 214/2025, LC 227/2026) substitui apenas os tributos sobre o consumo (PIS, Cofins, ICMS, ISS, IPI) por CBS+IBS. **O IRPF e o IRPJ permanecem inalterados** estruturalmente — alíquotas, faixas, deduções, prazos, regimes (Lucro Real/Presumido/Arbitrado) seguem como hoje. Cuidado apenas com a interação contábil: créditos de CBS/IBS aparecem no resultado e podem alterar lucro contábil → lucro tributável.

### Faixas do IRPF 2025 (ano-calendário janeiro–dezembro 2025)

**Faixas do IRPF 2025 (tabela anual do ano-calendário 2025, DIRPF 2026 — Lei nº 11.482/2007, art. 1º, na redação da Lei nº 14.848/2024 para janeiro a abril e da Lei nº 15.191/2025 para maio a dezembro; Receita Federal, tabelas de 2025)**

| Faixa de renda anual tributável (BRL) | Alíquota | Dedução (Anual) |
| --- | --- | --- |
| Até 28.467,20 | Isento | 0 |
| 28.467,21 – 33.919,80 | 7,5% | 2.135,04 |
| 33.919,81 – 45.012,60 | 15% | 4.679,03 |
| 45.012,61 – 55.976,16 | 22,5% | 8.054,97 |
| Acima de 55.976,16 | 27,5% | 10.853,78 |

- **Fórmula (anual)** — Imposto = (renda tributável × alíquota) − dedução
- **Ano-calendário 2026 (DIRPF 2027)** — A tabela progressiva mantém-se, mas a Lei nº 15.270/2025 (art. 11-A da Lei nº 9.250/1995) reduz o imposto anual de modo a zerá-lo para rendimentos tributáveis até R$ 60.000,00 e, entre R$ 60.000,01 e R$ 88.200,00, em R$ 8.429,73 − (0,095575 × rendimentos tributáveis sujeitos ao ajuste anual), decrescente até zero; institui ainda a tributação mínima das altas rendas (ver 'Lucros e dividendos a partir de janeiro de 2026'). Não aplicar estas reduções ao ano-calendário 2025.

**Faixas mensais do Carnê-Leão** (dividir os limites anuais por 12; tabela mensal específica é publicada pela Receita Federal a cada ano — sempre confirmar a tabela mensal vigente do Carnê-Leão).

### Lucros e dividendos a partir de janeiro de 2026

Seção acrescentada em 2026-10-31, com base no texto da lei, na Receita Federal e no STF; ainda não coberta pela revisão registrada no cabeçalho desta skill.

- **Retenção, pessoa física residente:** desde janeiro de 2026, lucros e dividendos pagos, creditados, empregados ou entregues por uma mesma PJ a uma mesma PF residente em montante superior a R$ 50.000,00 no mês sofrem IRRF de 10% sobre o total do valor, não apenas sobre o excedente, sem deduções. Havendo mais de um pagamento no mês, a retenção é recalculada sobre o total do mês. Até R$ 50.000,00 no mês não há retenção.  _(Lei 9.250/1995, art. 6º-A, caput e §§ 1º e 2º, incluído pela Lei 15.270/2025)_
- **Recolhimento, residente:** DARF código 1841-01, até o último dia útil do 2º decêndio do mês subsequente ao fato gerador.  _(Lei 11.196/2005, art. 70, I, "e"; Receita Federal, orientação sobre o recolhimento do IRRF)_
- **Capitalização e Simples Nacional:** para a Receita, a capitalização de lucros é "emprego" e está sujeita à regra (P&R 12), e a retenção alcança as empresas do Simples Nacional (P&R 10). A cautelar pedida na ADI 7.917 foi indeferida por ora. O mérito das ações segue pendente.  _(Receita Federal, Perguntas e Respostas, versão de 19/12/2025; STF, ADI 7.912 MC)_
- **Ajuste anual:** a isenção do art. 10 da Lei 9.249/1995 continua aplicável no cálculo do imposto do art. 12 da Lei 9.250/1995. Quem não se sujeita à tributação mínima pode ter o IRRF restituído na declaração.  _(Receita Federal, P&R 4 e 12)_
- **Tributação mínima (ano-calendário 2026, exercício 2027):** aplica-se à PF cuja soma de todos os rendimentos do ano supere R$ 600.000,00. Os dividendos entram na base, ainda que sem retenção, salvo os da transição abaixo. Alíquota de 10% para rendimentos a partir de R$ 1.200.000,00; entre os dois valores, alíquota % = (REND/60.000) - 10. O IRRF do art. 6º-A é deduzido, e o art. 16-B prevê um redutor.  _(Lei 9.250/1995, arts. 16-A e 16-B; Receita Federal, P&R 3 e 12)_
- **Transição:** ficam fora da retenção os lucros (I) de resultados apurados até o ano-calendário de 2025; (II) com distribuição aprovada até 31/12/2025; e (III) exigíveis nos termos da legislação civil ou empresarial, pagos nos termos originalmente previstos no ato de aprovação. Para excluí-los da tributação mínima, a lei exige ainda pagamento, crédito, emprego ou entrega em 2026, 2027 e 2028. Os arts. 6º-A, § 3º, e 10, § 5º, I, não fixam esse ano-limite no próprio texto, mas a Receita o aplica também à retenção (P&R 7 e 19). A proposta da administração não supre a aprovação pelo órgão competente (P&R 8).  _(Lei 9.250/1995, arts. 6º-A, § 3º, e 16-A, § 1º, XII; Lei 9.249/1995, art. 10, § 5º, I)_
- **AUDIT FLASH POINT** **Prazo de aprovação da transição:** em 26/12/2025, medida cautelar nas ADIs 7.912 e 7.914, ad referendum do Plenário, prorrogou até 31/01/2026 o prazo do item II acima (arts. 6º-A, § 3º, II, e 16-A, § 1º, XII, "b", da Lei 9.250/1995; art. 10, § 5º, I, "a", da Lei 9.249/1995). Na sessão virtual de 13 a 24/02/2026, houve 2 votos pelo referendo e destaque do Min. Edson Fachin. O andamento da ADI 7.912 consultado em 31/10/2026 não registra decisão do Plenário nem de mérito. O P&R da Receita, anterior à cautelar, ainda indica 31/12/2025. Distribuição aprovada entre 01/01/2026 e 31/01/2026 depende dessa cautelar: sinalizar para revisão e confirmar o andamento antes de concluir. Não confirmado na fonte: efeito de eventual não referendo sobre aprovações já feitas nesse período.  _(STF, ADI 7.912 MC, decisão de 26/12/2025; STF, andamento da ADI 7.912)_
- **Não residentes:** desde janeiro de 2026, lucros e dividendos pagos, creditados, entregues, empregados ou remetidos ao exterior sofrem IRRF de 10%, em qualquer valor, sem o limite de R$ 50.000,00, inclusive para país que não tribute a renda ou a tribute a menos de 17%. DARF código 1841-02, com vencimento no dia do fato gerador. Não há incidência para (a) governos estrangeiros, com reciprocidade; (b) fundos soberanos do art. 3º, § 5º, da Lei 11.312/2006; e (c) entidades no exterior cuja principal atividade seja administrar benefícios previdenciários, conforme regulamento; nesses casos, qualquer que seja o ano de apuração do lucro. A transição acima também se aplica. O art. 10-A prevê crédito, por opção do beneficiário, quando a carga conjunta superar as alíquotas nominais.  _(Lei 9.249/1995, arts. 10, §§ 4º e 5º, e 10-A; Lei 11.196/2005, art. 70, I, "a"; Receita Federal, P&R 16, 17, 18, 19, 21 e 22)_

Fontes abertas em 2026-10-31: Lei 15.270/2025, publicação original (Senado): https://legis.senado.leg.br/norma/41758136/publicacao/41762089 ; Receita Federal: https://www.gov.br/receitafederal/pt-br/assuntos/noticias/2025/dezembro/receita-federal-orienta-sobre-os-procedimentos-para-o-recolhimento-do-imposto-de-renda-retido-na-fonte-sobre-lucros-e-dividendos ; Perguntas e Respostas: https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirf/manual_padrao_rfb_per_tributacao_cotin_v-19-12-2025.pdf ; STF: https://noticias.stf.jus.br/postsnoticias/stf-prorroga-prazo-para-aprovacao-de-lucros-e-dividendos-ate-janeiro-de-2026/ ; andamento: https://portal.stf.jus.br/processos/detalhe.asp?incidente=7466925

### IRPJ — alíquotas e regimes

- **IRPJ** — 15% sobre o lucro tributável, mais adicional de 10% sobre a parcela do lucro que ultrapassar R$ 240.000 anuais (R$ 20.000/mês)  _(Lei 9.249/1995, Lei 9.430/1996, IN RFB 1.700/2017)_
- **Lucro Real** — apuração pelo lucro contábil ajustado por adições/exclusões; obrigatório para receita > R$ 78 milhões/ano e para determinadas atividades  _(Lei 9.249/1995, Lei 9.430/1996, IN RFB 1.700/2017)_
- **Lucro Presumido** — base presumida sobre receita bruta (percentuais de 1,6% a 32% conforme atividade); opcional para receita ≤ R$ 78 milhões/ano  _(Lei 9.249/1995, Lei 9.430/1996, IN RFB 1.700/2017)_
- **Lucro Arbitrado** — aplicado quando a escrituração é imprestável ou ausente; bases majoradas  _(Lei 9.249/1995, Lei 9.430/1996, IN RFB 1.700/2017)_

Referência: Lei 9.249/1995, Lei 9.430/1996, IN RFB 1.700/2017.

### Desconto Simplificado

- **Desconto simplificado** — O contribuinte pode optar pelo desconto simplificado em vez das deduções via livro caixa: Dedução: 20% da renda bruta, limitada a BRL 16.754,34 por ano; Não exige comprovantes; Não pode ser combinado com as deduções do livro caixa; Vantajoso quando as despesas reais < 20% do bruto

### Livro Caixa (dedução das despesas reais)

- **Livro caixa** — No livro caixa, as despesas profissionais reais e documentadas são deduzidas da renda bruta do Carnê-Leão. Exige registros contemporâneos. Substitui o desconto simplificado de 20% (é necessário escolher um).

### Contribuições ao INSS para autônomos

**Contribuições ao INSS para autônomos**

| Tipo de contribuinte | Alíquota | Teto (2025) |
| --- | --- | --- |
| Autônomo (contribuinte individual) | 20% | BRL 908,46/mês (teto INSS: BRL 7.786,02 × 11,67%) |
| Empregador retendo do autônomo | 20% (empregador) | Sobre cada pagamento |
| Microempreendedor Individual (MEI) | DAS fixo ~BRL 75/mês | Regime separado |

- **Dedutibilidade INSS** — As contribuições pagas ao INSS são integralmente dedutíveis da base tributável do IRPF (via livro caixa ou como dedução separada na DIRPF).

### Carnê-Leão (pagamentos mensais estimados)

- **Obrigação Carnê-Leão** — Os autônomos que recebem rendimentos de pessoas físicas (PF) brasileiras ou de fontes no exterior devem recolher o Carnê-Leão mensalmente, até o último dia útil do mês seguinte.
- **Rendimentos de PJ - IRRF** — Rendimentos de pessoas jurídicas (PJ) → a PJ retém 1,5% ou 11% de IRRF (conforme o tipo de serviço) — crédito a compensar na DIRPF anual.

**Carnê-Leão (pagamentos mensais estimados)**

| Fonte | Obrigação mensal |
| --- | --- |
| Renda de PF (pessoas físicas) ou exterior | Carnê-Leão obrigatório |
| Renda de PJ (empresas) | IRRF retido na fonte (1,5% + INSS 11%) |

### Padrões conservadores

**Padrões conservadores**

| Situação | Premissa padrão |
| --- | --- |
| Desconto simplificado vs. livro caixa — indefinido | Comparar ambos: se despesas reais < 20% do bruto, simplificado é melhor; apresentar os dois |
| INSS retido pela PJ vs. pago pelo autônomo indefinido | Sinalizar — depende de o cliente ser PJ ou PF |
| Pagamento de PJ: alíquota de IRRF indefinida | Aplicar 1,5% (serviços profissionais) como padrão; sinalizar |
| Renda do exterior | Tratar como Carnê-Leão obrigatório; sinalizar para análise de tratado |
| Status MEI vs. autônomo indefinido | NÃO prosseguir — o status determina todo o regime |
| Receita em espécie sem Recibo / NF | Tributável — sinalizar; a Receita Federal fiscaliza declarações com muito caixa |

### Limites de alerta (red flags)

**Limites de alerta (red flags)**

| Alerta | Limite |
| --- | --- |
| Receita bruta > BRL 81.000/ano | Era MEI? — limite MEI BRL 81.000; ultrapassar gera desenquadramento |
| Nenhum pagamento de Carnê-Leão feito | Verificar se toda a renda veio de PJs (retido na fonte) |
| Receita total > BRL 33.888 | DIRPF obrigatória |
| Contribuições ao INSS aparecem zeradas | Verificar — autônomos têm obrigação de INSS |
| Uma única fonte PJ > 90% da renda | Pode indicar vínculo empregatício |

## Seção 2 — Inputs obrigatórios + catálogo de recusas

### Inputs obrigatórios

- **Lista de inputs obrigatórios** — Antes de calcular o IRPF brasileiro, colete: 1. Receita bruta total — separadamente por fontes PF e PJ (detalhamento mensal); 2. Comprovantes de Rendimentos (IRRF) — de cada cliente PJ; 3. Pagamentos de Carnê-Leão realizados — recibos mensais (DARF códigos 0190/5936); 4. Contribuições ao INSS pagas — resumo anual do INSS ou recibos GPS; 5. Livro caixa ou registros de despesas — se for utilizar despesas reais; 6. Extratos bancários — 12 meses (janeiro–dezembro); 7. Deduções por dependentes — BRL 2.275,08 por dependente por ano; 8. Despesas com saúde/educação — para deduções pessoais (deduções de saúde/educação); 9. Juros de financiamento imobiliário — se for deduzir (apenas residência principal); 10. Outras rendas — Categoria I (trabalho), salário (se houver vínculo), rendimentos isentos

### Catálogo de recusas

**Catálogo de recusas**

| Código | Situação | Ação |
| --- | --- | --- |
| R-BR-1 | Cliente é MEI (Microempreendedor Individual) — não autônomo | Parar — MEI paga DAS (INSS + ICMS/ISS), não IRPF sobre receita do negócio; IRPF apenas sobre o pró-labore retirado; redirecionar para a skill específica de MEI |
| R-BR-2 | Sem Comprovantes de Rendimentos de clientes PJ | Parar — não é possível calcular o crédito de IRRF sem os comprovantes de retenção |
| R-BR-3 | Renda do exterior sem conversão cambial | Parar — todos os valores devem estar em BRL na data do recebimento (taxa PTAX do Banco Central) |
| R-BR-4 | Renda mista Simples Nacional / autônomo | Sinalizar — a renda da empresa do Simples Nacional flui de forma diferente; não misturar |
| R-BR-5 | Cliente alega que não precisa de Carnê-Leão apesar de ter renda PF ou do exterior | Sinalizar — se houver qualquer fonte PF ou estrangeira, o Carnê-Leão é obrigatório; o não pagamento gera multa |

## Seção 3 — Biblioteca de padrões de transações

### Padrões de receita

**Padrões de receita**

| # | Padrão de histórico | Linha tributária | Observações |
| --- | --- | --- | --- |
| I-01 | `TED DE [nome do cliente]` / `PIX DE [cliente]` | Receita bruta — IRPF | Crédito padrão TED/PIX do cliente |
| I-02 | `PIX RECEBIDO [cliente]` | Receita bruta — IRPF | PIX (pagamento instantâneo) do cliente |
| I-03 | `DOC DE [cliente]` | Receita bruta — IRPF | DOC (transferência interbancária legada) |
| I-04 | `STRIPE PAYOUT` / `STRIPE PAGAMENTOS` | Receita bruta — fonte estrangeira | Stripe Brasil ou repasse externo; Carnê-Leão se vier de entidade estrangeira; conversão para BRL via PTAX |
| I-05 | `PAYPAL SAQUE` / `PAYPAL TRANSFERÊNCIA` | Receita bruta — fonte estrangeira | PayPal; Carnê-Leão aplicável; conversão para BRL via PTAX |
| I-06 | `PAGAMENTO MERCADO PAGO` / `MERCADOPAGO` | Receita bruta — IRPF | Liquidação Mercado Pago; valor líquido — efetuar gross-up se houve dedução de taxas |
| I-07 | `PAGAMENTO HOTMART` / `HOTMART SAQUE` | Receita bruta — IRPF | Repasse Hotmart (plataforma de produtos digitais); gross-up |
| I-08 | `KIWIFY SAQUE` / `EDUZZ PAGAMENTO` | Receita bruta — IRPF | Plataformas brasileiras de produtos digitais; gross-up |
| I-09 | `NOTA FISCAL [número]` / `NF SERVIÇOS` | Receita bruta — retenção de PJ | Se de PJ, IRRF e INSS podem ter sido retidos; conferir com o Comprovante |
| I-10 | `RESTITUIÇÃO IRPF RECEITA` | NÃO é receita — restituição de IRPF | Restituição não é renda tributável |
| I-11 | `RENDIMENTO POUPANÇA` / `JUROS CDB` | Rendimentos isentos (até certos limites) ou tributados | Juros bancários: LCA/LCI podem ser isentos; CDB sujeito a IOF/IR — sinalizar |
| I-12 | `DIVIDENDOS` (de empresa) | Isentos no cálculo do art. 12; desde janeiro de 2026, IRRF de 10% sobre o total se a mesma PJ pagar à mesma PF mais de R$ 50.000,00 no mês | Lei 9.250/1995, art. 6º-A. Confirmar transição e tributação mínima (Seção 1, 'Lucros e dividendos a partir de janeiro de 2026') |

### Padrões de despesa

**Padrões de despesa**

| # | Padrão de histórico | Linha tributária | Observações |
| --- | --- | --- | --- |
| E-01 | `ALUGUEL ESCRITÓRIO` / `ALUGUEL SALA COMERCIAL` | Aluguel — dedutível via livro caixa | Home office: proporcional — exige cálculo documentado |
| E-02 | `ENERGIA ELÉTRICA` / `CONTA DE LUZ` / `CPFL` / `CEMIG` | Utilidades — dedutíveis proporcionalmente | Apenas a parte do escritório; em casa = uso misto |
| E-03 | `TELEFONE` / `INTERNET` / `VIVO` / `CLARO` / `TIM` / `OI` | Telefone/internet — dedutível (parte profissional) | Documentar o percentual de uso profissional |
| E-04 | `ADOBE` / `MICROSOFT 365` / `GOOGLE WORKSPACE` | Software — dedutível via livro caixa | Software profissional |
| E-05 | `CONTADOR` / `ESCRITÓRIO CONTÁBIL` | Honorários contábeis — dedutíveis via livro caixa | Obrigatório para muitos autônomos |
| E-06 | `PASSAGEM AÉREA` / `LATAM` / `GOL` / `AZUL` | Viagem aérea — dedutível (finalidade profissional) | Exigir destino e finalidade |
| E-07 | `HOTEL` / `BOOKING.COM` / `AIRBNB` | Hospedagem — dedutível (viagem profissional) | Finalidade profissional obrigatória |
| E-08 | `GUIA GPS` / `INSS GPS` / `CONTRIBUIÇÃO INSS` | Contribuições ao INSS — integralmente dedutíveis | Pagamento via GPS; ou retido em folha |
| E-09 | `DARF CARNÊ-LEÃO` / `DARF 0190` | Pagamentos de Carnê-Leão — NÃO dedutíveis | Antecipações de imposto; crédito contra o IRPF anual |
| E-10 | `DARF IRPF` / `SALDO DIRPF` | Pagamento anual de imposto — NÃO dedutível | Pagamento de tributo |
| E-11 | `SEGURO PROFISSIONAL` / `SEGURO RC PROFISSIONAL` | Seguro profissional — dedutível via livro caixa |  |
| E-12 | `PLANO DE SAÚDE` | Plano de saúde — dedução pessoal (DIRPF) | Não vai no livro caixa — dedução separada na Ficha de Deduções da DIRPF |
| E-13 | `ESCOLA` / `MENSALIDADE ENSINO` | Educação — dedução pessoal (limite BRL 3.561,50/ano) | Não vai no livro caixa; dedução pessoal na DIRPF |
| E-14 | `COMBUSTÍVEL` / `GASOLINA` / `POSTO` | Combustível — dedutível (veículo usado profissionalmente) | Documentar km de uso profissional; uso misto = proporção |
| E-15 | `MATERIAL DE ESCRITÓRIO` / `PAPELARIA` | Material de escritório — dedutível via livro caixa |  |
| E-16 | `TARIFA BANCÁRIA` / `TED ENVIADO` / `IOF` | Tarifas bancárias — dedutíveis via livro caixa | Encargos sobre conta profissional |
| E-17 | `ASSINATURA [plataforma]` / `MENSALIDADE` | Assinaturas de plataformas/ferramentas — dedutíveis | Ferramentas profissionais |
| E-18 | `CURSOS` / `TREINAMENTO` / `CAPACITAÇÃO` | Treinamento — dedutível via livro caixa | Desenvolvimento profissional |
| E-19 | `REEMBOLSO [cliente]` | Não dedutível (compensar com o reembolso não tributável) | Se for reembolso do cliente, reduzir a receita correspondente também |
| E-20 | `NOTA DE DÉBITO [fornecedor]` / `NF COMPRAS` | Compras para a atividade profissional — dedutíveis via livro caixa | Exigir NF-e |

## Seção 4 — Exemplos resolvidos

### Exemplo 1 — Itaú Unibanco (São Paulo, Consultor de TI)

**Banco:** Extrato Itaú Unibanco PDF/CSV
**Cliente:** Carlos Mendes, consultor de TI, São Paulo, clientes PJ e PF mistos

```
Data;Histórico;Valor;Tipo
05/01/2025;PIX RECEBIDO EMPRESA ALPHA LTDA;7.500,00;C
15/01/2025;TARIFA BANCÁRIA;12,00;D
10/02/2025;PIX RECEBIDO STARTUP BETA LTDA;5.500,00;C
28/02/2025;GUIA GPS INSS;1.557,60;D
15/03/2025;STRIPE PAYOUT;4.200,00;C
31/03/2025;DARF CARNÊ-LEÃO 0190;850,00;D
20/04/2025;TED DE FREELANCER PF PESSOA;1.800,00;C
05/06/2025;PIX RECEBIDO GAMMA TECH SA;8.200,00;C
10/07/2025;CONTADOR SILVA LTDA;800,00;D
10/10/2025;LATAM VIAGEM NEGÓCIOS;650,00;D
```

**Passo 1 — Classificação da receita**

| Histórico | Tipo | Valor bruto | Observações |
| --- | --- | --- | --- |
| PIX DE EMPRESA ALPHA (PJ) | Receita PJ | BRL 7.500 | IRRF e INSS provavelmente retidos — verificar Comprovante |
| PIX DE STARTUP BETA (PJ) | Receita PJ | BRL 5.500 | Idem — verificar Comprovante |
| STRIPE PAYOUT | Estrangeira/PJ | BRL 4.200 | Carnê-Leão a menos que Stripe Brasil PJ tenha retido |
| TED DE FREELANCER PF | Receita PF | BRL 1.800 | Carnê-Leão obrigatório |
| PIX DE GAMMA TECH (PJ) | Receita PJ | BRL 8.200 | Verificar Comprovante |

Supondo que os Comprovantes mostrem IRRF retido pelos clientes PJ a 1,5% cada. Receita bruta total PJ (anualizada): BRL 65.000; PF + exterior: BRL 24.000. Total: BRL 89.000.

Desconto simplificado: 20% × BRL 89.000 = BRL 17.800 → limitado a BRL 16.754,34
Livro caixa (real): INSS BRL 18.691,20, contabilidade BRL 9.600, software BRL 3.600, tarifas bancárias BRL 144, viagem BRL 650 = BRL 32.685,20

Livro caixa > simplificado → **livro caixa é o preferido** para o Carlos.

```
Renda bruta:            BRL 89.000,00
(−) livro caixa:        BRL 32.685,20
Renda tributável:       BRL 56.314,80
```

```
BRL 56.314,80 × 27,5% − BRL 10.853,78 = BRL 15.486,57 − BRL 10.853,78 = BRL 4.632,79
```

```
IRRF retido pelas PJs (1,5% × BRL 65.000):     BRL 975,00
Carnê-Leão pago:                                BRL 850,00 × meses pagos
Saldo de IRPF a pagar:                          BRL 4.632,79 − BRL 975 − BRL [total carnê]
```

### Exemplo 2 — Bradesco (Rio de Janeiro, Arquiteta — desconto simplificado)

**Banco:** Extrato Bradesco
**Cliente:** Ana Lima, arquiteta, Rio de Janeiro

Renda bruta: BRL 48.000 (toda de clientes PJ)
IRRF retido pelas PJs: 1,5% × BRL 48.000 = BRL 720

Desconto simplificado: 20% × BRL 48.000 = BRL 9.600 (< limite) — aplicar
Renda tributável: BRL 48.000 − BRL 9.600 = BRL 38.400

IRPF: BRL 38.400 × 22,5% − BRL 7.942,19 = BRL 8.640 − BRL 7.942,19 = **BRL 697,81**
(−) crédito de IRRF: BRL 720

Resultado: **restituição de BRL 22,19** (IRRF > IRPF)

Observação: deduzir também o INSS separadamente na DIRPF (Ficha de Deduções). Se INSS pago BRL 6.000:
Tributável: BRL 38.400 − BRL 6.000 = BRL 32.400
IRPF: BRL 32.400 × 15% − BRL 4.566,23 = BRL 4.860 − BRL 4.566,23 = BRL 293,77
Com crédito de IRRF: **restituição de BRL 426,23**

### Exemplo 3 — Banco do Brasil (Brasília, Médico)

**Banco:** Extrato BB
**Cliente:** Dr. Paulo Saraiva, médico, Brasília, recebe de hospital PJ e pacientes PF

Renda do hospital PJ (Comprovante mostra): BRL 120.000 brutos; IRRF retido 1,5% = BRL 1.800; INSS retido 11% = BRL 13.200
Pacientes PF (dinheiro/PIX): BRL 36.000 — obrigação de Carnê-Leão

Livro caixa: INSS BRL 13.200 (retido pelo empregador) + INSS próprio BRL 5.400 (contribuição complementar) + aluguel de clínica BRL 18.000 + equipamentos BRL 8.000 = BRL 44.600

Receita bruta total: BRL 156.000
(−) livro caixa: BRL 44.600
Tributável: BRL 111.400

IRPF: BRL 111.400 × 27,5% − BRL 10.740,98 = BRL 30.635 − BRL 10.740,98 = **BRL 19.894,02**
(−) IRRF: BRL 1.800 e pagamentos de Carnê-Leão

Alerta de alta renda: BRL 156.000 brutos → verificar se todos os Carnê-Leão mensais sobre renda PF foram pagos; penalidade se em atraso.

### Exemplo 4 — Nubank (São Paulo, Criadora Digital / Hotmart)

**Banco:** Extrato Nubank (PDF)
**Cliente:** Julia Torres, criadora de cursos digitais, São Paulo

Repasses da Hotmart: BRL 85.000 (líquidos das taxas Hotmart)
Gross-up: a Hotmart cobra ~9,9% + BRL 1; bruto efetivo ~BRL 95.000

Kiwify: BRL 22.000 líquidos → bruto ~BRL 24.500

Receita bruta total: BRL 119.500 — todas de plataformas (PJ)

Observação: Hotmart e Kiwify são PJs brasileiras. Retêm IRRF nos repasses. Coletar Comprovante de Rendimentos da plataforma.

Desconto simplificado: 20% × BRL 119.500 = BRL 23.900 (> limite BRL 16.754,34 → aplicar o teto BRL 16.754,34)
Livro caixa (despesas reais ~BRL 8.000): simplificado é melhor (teto BRL 16.754 > real)

Tributável: BRL 119.500 − BRL 16.754,34 = BRL 102.745,66

IRPF: BRL 102.745,66 × 27,5% − BRL 10.853,78 = BRL 28.255,06 − BRL 10.853,78 = **BRL 17.401,28**

(−) IRRF das plataformas. Alerta: DIRPF obrigatória (bruto > BRL 33.888).

### Exemplo 5 — Santander Brasil (Porto Alegre, Engenheiro)

**Banco:** Extrato Santander
**Cliente:** Ricardo Gomes, engenheiro civil, Porto Alegre

Questão: Ricardo tem renda como autônomo (BRL 60.000) e salário CLT (BRL 48.000). A DIRPF deve consolidar ambos.

Consolidação na DIRPF:
- Salário (DIRF do empregador): BRL 48.000 brutos; IRRF BRL 4.800 retido
- Autônomo (livro caixa): BRL 60.000 − BRL 22.000 (despesas) = BRL 38.000

Tributável total: BRL 48.000 + BRL 38.000 = BRL 86.000
IRPF: BRL 86.000 × 27,5% − BRL 10.853,78 = BRL 23.650 − BRL 10.853,78 = **BRL 12.796,22**
(−) IRRF salário: BRL 4.800 + Carnê-Leão pago + INSS empregador

Renda dupla — sinalizar: DIRPF complexa com Ficha de Rendimentos das duas fontes.

### Exemplo 6 — Inter Bank (Belo Horizonte, Designer Freelancer, Verificação de MEI)

**Banco:** Extrato Inter
**Cliente:** Fernanda Rocha, designer, Belo Horizonte

Primeira pergunta: **Fernanda é MEI?** Em caso afirmativo, R-BR-1 se aplica — parar.

Supondo que NÃO seja MEI (desenquadrada ou nunca registrada como MEI):
Bruto: BRL 72.000 — observação: BRL 72.000 < limite MEI BRL 81.000. Se Fernanda ainda for MEI, deve ser tributada via DAS e não IRPF sobre essa renda. PARAR — confirmar status.

Se confirmada como autônoma: prosseguir. INSS: BRL 14.400 (20% × BRL 72.000 — estimativa simplificada; o valor real depende do teto mensal). Desconto simplificado: BRL 14.400 vs. 20% (teto BRL 14.400 — igual). Despesas reais ~BRL 6.000. Usar simplificado (BRL 14.400 > BRL 6.000).

Tributável: BRL 72.000 − BRL 14.400 = BRL 57.600
IRPF: BRL 57.600 × 27,5% − BRL 10.740,98 = BRL 15.840 − BRL 10.740,98 = **BRL 5.099,02**

## Seção 5 — Regras Tier 1 (aplicar diretamente)

- **T1-BR-1 — INSS é sempre dedutível** — As contribuições ao INSS pagas (GPS, DARF ou retidas por PJ) são 100% dedutíveis da base tributável do IRPF. Deduzir na Ficha de Deduções da DIRPF independentemente da fonte de renda (livro caixa ou simplificado). Aplicar sem escalonar.
- **T1-BR-2 — IRRF retido por PJ é crédito tributário, não redução de receita** — O IRRF retido pelos clientes PJ (tipicamente 1,5% para serviços profissionais, 11% INSS) reduz o saldo de IRPF anual a pagar. A receita bruta (antes da retenção) é o valor tributável. Sempre fazer gross-up para o valor pré-retenção.
- **T1-BR-3 — Carnê-Leão é obrigatório para renda PF e do exterior** — Qualquer recebimento mensal de uma pessoa física brasileira (PF) ou do exterior — independentemente do valor — gera obrigação de Carnê-Leão (vencimento no último dia útil do mês seguinte). O não pagamento gera multa de mora (0,33%/dia até 20%). Aplicar imediatamente ao classificar fontes de renda.
- **T1-BR-4 — Pagamentos via DARF (Carnê-Leão, IRPF) não são dedutíveis** — Antecipações de imposto pagas via DARF (código 0190 para Carnê-Leão, código 1854 para saldo final de IRPF) são créditos contra a obrigação anual de IRPF, não despesas dedutíveis. Nunca incluir DARFs nas deduções do livro caixa.
- **T1-BR-5 — Renda do exterior: conversão PTAX obrigatória** — Toda renda recebida em moeda estrangeira deve ser convertida para BRL utilizando a taxa PTAX de venda do Banco Central na data do recebimento. Não utilizar qualquer outra taxa de conversão.
- **T1-BR-6 — Teto do desconto simplificado** — BRL 16.754,34 (A dedução simplificada de 20% é limitada a BRL 16.754,34 independentemente do tamanho da renda bruta. Sempre verificar o teto antes de aplicar o percentual.)

## Seção 6 — Catálogo Tier 2 (exige julgamento do revisor)

**Catálogo Tier 2**

| Código | Situação | Motivo de escalonamento | Tratamento sugerido |
| --- | --- | --- | --- |
| T2-BR-1 | Classificação MEI vs. autônomo | Regime tributário totalmente distinto — MEI paga DAS; autônomo paga IRPF + INSS separadamente | Confirmar registro no Portal do Empreendedor antes de prosseguir |
| T2-BR-2 | Renda do exterior (cripto, clientes estrangeiros) | Renda do exterior exige Carnê-Leão em BRL via PTAX; pode acionar IOF | Sinalizar — conversão PTAX + Carnê-Leão sobre todo recebimento estrangeiro |
| T2-BR-3 | Renda de aluguel | Tratamento tributário separado; Carnê-Leão com deduções diferentes | Sinalizar — renda de aluguel em Ficha separada; deduções específicas (IPTU, manutenção) |
| T2-BR-4 | Ganho de capital | Programa GCAP separado; alíquotas 15%/17,5%/20%/22,5% | Sinalizar — não incluir na Ficha de Rendimentos Tributáveis |
| T2-BR-5 | Renda em cripto / ativos digitais | IN RFB 1888/2019 e normativos posteriores; reporte complexo | Sinalizar — ganhos em cripto tributados como ganho de capital; apuração mensal se ganhos > BRL 35.000/mês |
| T2-BR-6 | Dividendos da própria empresa | Desde janeiro de 2026: IRRF de 10% acima de R$ 50.000,00 no mês por PJ; tributação mínima acima de R$ 600.000,00 no ano | Sinalizar: conferir ato de aprovação e transição (prazo sob a cautelar das ADIs 7.912 e 7.914) e somar os dividendos aos rendimentos do ano (Seção 1) |

## Seção 7 — Modelo de papel de trabalho em Excel

```
PAPEL DE TRABALHO IRPF BRASILEIRO (AUTÔNOMO / PROFISSIONAL LIBERAL)
Contribuinte: _______________  CPF: _______________  Ano-calendário: 2025

SEÇÃO A — RENDIMENTOS (Rendimentos Tributáveis)
                                        BRL
Clientes PJ — bruto (pré-IRRF):       ___________
Clientes PF / renda Carnê-Leão:       ___________
Renda do exterior (convertida PTAX):   ___________
Repasses de plataformas (gross-up):    ___________
TOTAL DA RENDA BRUTA                   ___________

SEÇÃO B — MÉTODO DE DEDUÇÃO
[ ] Desconto Simplificado: 20% × bruto = ___________  (teto: BRL 16.754,34)
[ ] Livro Caixa (despesas reais):

  Aluguel (parte profissional):        ___________
  Utilidades (profissional):           ___________
  Telefone/internet (% profissional):  ___________
  Software:                            ___________
  Honorários contábeis:                ___________
  Viagens (profissional):              ___________
  Equipamentos/materiais:              ___________
  Outras despesas documentadas:        ___________
  TOTAL LIVRO CAIXA:                   ___________

SEÇÃO C — DEDUÇÃO DE INSS (separada das anteriores)
INSS pago (GPS / retido por PJ):       ___________

SEÇÃO D — RENDA TRIBUTÁVEL
Bruto − [B] − [C] (+ outras deduções DIRPF):   ___________

SEÇÃO E — CÁLCULO DO IRPF
Imposto pelas faixas:                  ___________
(−) IRRF retido pelas PJs:             (___________)
(−) Pagamentos Carnê-Leão (DARF 0190): (___________)
SALDO DE IRPF A PAGAR / (RESTITUIÇÃO)  ___________

SEÇÃO F — ALERTAS PARA O REVISOR
[ ] Todos os Comprovantes de Rendimentos coletados dos clientes PJ?
[ ] Pagamentos de Carnê-Leão conciliados (meses com renda PF e do exterior)?
[ ] Renda do exterior convertida pela PTAX de venda na data de recebimento?
[ ] Status MEI confirmado como NÃO aplicável?
[ ] Comparação desconto simplificado vs. livro caixa realizada?
[ ] Dedução de INSS lançada na Ficha de Deduções (não no livro caixa)?
[ ] Gross-up aplicado nos repasses de plataformas (Hotmart, Kiwify, etc.)?
```

## Seção 8 — Guia de leitura de extratos bancários

### Itaú Unibanco

- Exportação: PDF ou CSV via "Extrato" no app/portal
- Colunas CSV: `Data;Histórico;Valor;Tipo` (Tipo: C = crédito, D = débito)
- Formato do valor: vírgula como decimal, ponto como separador de milhar (ex.: `7.500,00`)
- Data: DD/MM/AAAA
- Recebimentos PIX: `PIX RECEBIDO [nome do remetente]`; recebimentos TED: `TED DE [remetente]`

### Bradesco

- Exportação: CSV ou PDF pelo Internet Banking Bradesco
- Colunas: `Data;Documento;Histórico;Valor;Saldo`
- Valor positivo = crédito; negativo = débito (entre parênteses ou com sinal negativo)

### Banco do Brasil

- Exportação: CSV pelo Internet Banking do BB ("Extrato")
- Colunas variam; tipicamente `Data;Lançamento;Débito;Crédito;Saldo`
- Históricos PIX: `PIX TRANSF DE [CPF/nome]` ou `PIX CRED DE [nome]`

### Santander Brasil

- Exportação: PDF/CSV pelo Santander Online (portal/app)
- Formato padrão; PIX: `TRANSF PIX DE [nome]`, TED: `TED/DOC RECEBIDA`

### Nubank

- Exportação: extrato em PDF pelo app ("Ver extrato completo" → PDF)
- Sem CSV nativo; ferramentas de terceiros existem; históricos incluem: `Pix recebido de [nome]`, `Transferência recebida de [nome]`

### Inter Bank (Banco Inter)

- Exportação: CSV/PDF pelo app Inter → "Extrato" → "Baixar"
- Colunas: `Data;Tipo de Transação;Valor`
- PIX: `Pix Recebido` com detalhe do remetente na descrição

### Identificação de PIX

- O PIX é o sistema de pagamentos instantâneos brasileiro; identifica transações por chave CPF/CNPJ/telefone/e-mail
- Históricos PIX no extrato: `PIX RECEBIDO`, `PIX CREDIT`, `TRANSF PIX ENTRADA`
- Nome/CPF do remetente costuma vir incluído — essencial para classificar PF (→ Carnê-Leão) vs. PJ (→ IRRF retido)

## Seção 9 — Fallback de onboarding

**Comprovantes de Rendimentos faltando:**
> "Para calcular o seu IRPF com precisão, preciso do Comprovante de Rendimentos de cada cliente PJ que pagou você em 2025. Esses documentos mostram o valor bruto e o IRRF retido na fonte. Você pode solicitá-los diretamente aos seus clientes, ou consultar sua conta da Receita Federal em gov.br/receitafederal → 'Consultar Informações Prestadas por Terceiros' — as DIMEs/DIRFs dos seus clientes podem já estar no sistema."

**Verificação de status MEI:**
> "Antes de prosseguir, preciso confirmar se você está registrado como Microempreendedor Individual (MEI). Em caso afirmativo, a renda do seu negócio é tributada pelo regime do DAS, não pelo IRPF padrão, e uma skill diferente se aplica. Confira seu status em portaldoempreendedor.gov.br ou me informe seu CNPJ caso tenha um."

**Lacuna no Carnê-Leão:**
> "Vejo que você recebeu renda de clientes pessoa física (PF) ou do exterior, o que gera a obrigação do Carnê-Leão. Você tem registros dos pagamentos mensais de DARF (código 0190)? Se o Carnê-Leão não foi pago em algum mês em que houve renda PF/estrangeira, há incidência de multa de mora. Vamos identificar quais meses ficaram em aberto."

**Câmbio de renda do exterior:**
> "Para a renda recebida de clientes estrangeiros em USD ou outras moedas, preciso converter cada recebimento para BRL usando a taxa PTAX de venda do Banco Central na data exata do recebimento. Você poderia fornecer as datas e os valores em moeda estrangeira? Alternativamente, se você recebeu renda de forma regular, pode-se usar a PTAX média anual — confirme se isso é aceitável."

## Seção 10 — Material de referência

### Legislação principal

- **Lista de legislação** — RIR/2018 (Regulamento do Imposto de Renda) — Decreto 9.580/2018; Lei 7.713/1988 — rendimentos isentos de IRPF; Lei 9.250/1995 — alterações da legislação do IRPF; Lei 9.249/1995 — alíquotas de IRPJ e CSLL; Lei 15.270/2025 (lucros e dividendos, tributação mínima das altas rendas); Lei 9.430/1996 — apuração trimestral de IRPJ e demais ajustes; IN RFB 1.700/2017 — determinação e apuração do IRPJ e CSLL; IN RFB 2.178/2024 — regras do Carnê-Leão e DIRPF para o ano-calendário 2024; Instrução Normativa RFB 1.888/2019 — reporte de criptoativos; EC 132/2023, LC 214/2025, LC 227/2026 — reforma tributária (consumo); IR não é afetado estruturalmente

### Calendário de entrega e pagamento 2025 (ano-base 2024)

**Calendário de entrega e pagamento 2025 (ano-base 2024)**

| Prazo | Evento |
| --- | --- |
| Último dia útil de cada mês | DARF de Carnê-Leão referente aos recebimentos do mês anterior |
| 28 de fevereiro de 2025 | Clientes PJ devem emitir Comprovantes de Rendimentos |
| 31 de março de 2025 | Abertura da entrega da DIRPF 2025 (ano-base 2024) |
| 30 de maio de 2025 | Prazo final da entrega da DIRPF 2025 |
| 30 de maio de 2025 | 1ª parcela do saldo de IRPF (ou pagamento único com desconto) |

### Referências úteis

- Receita Federal: gov.br/receitafederal
- PGFN (denúncia espontânea): gov.br/pgfn
- Consulta de chave PIX: bacen.gov.br
- Taxas PTAX: bcb.gov.br/estabilidadefinanceira/fechamentodolar

## Disclaimer

Esta skill e seus resultados são fornecidos apenas para fins informativos e de cálculo e não constituem aconselhamento tributário, jurídico ou financeiro. A Open Accountants e seus contribuidores não se responsabilizam por quaisquer erros, omissões ou consequências decorrentes do uso desta skill. Todos os resultados devem ser revisados e assinados por um profissional qualificado (como contador, advogado tributarista ou profissional licenciado equivalente na sua jurisdição) antes de qualquer entrega ou atuação.

A versão mais atualizada e verificada desta skill é mantida em [openaccountants.com](https://openaccountants.com). Faça login para acessar a versão mais recente, solicitar uma revisão profissional de um contador licenciado e acompanhar atualizações conforme a legislação tributária mudar.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
