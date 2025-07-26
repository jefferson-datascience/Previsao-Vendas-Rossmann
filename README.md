# 1.0 Objetivo do Projeto

O objetivo deste projeto é desenvolver um modelo de regressão capaz de prever os próximos 6 dias de faturamento de lojas. Com esse objetivo, temos o foco em aprimorar habilidade em análise exploratóra de dados, engenharia de atributos, modelagem de dados para problemas supervisionados e compreensão de negócios.


# 2.0 Problema de Negócio

A Rede de Drogarias Rossmann possui 3.000 lojas em 7 países europeus e mais de 30 anos de mercado. Os superintendentes solicitaram aos gerentes planos e ações para melhorar o faturamento das lojas. A primeira demanda que nós recebemos foi a solicitação de uma análise estatística para entender quais variáveis influenciavam positiva e negativamente o faturmento. Com a análise feita (veja aqui) e os devidos resultados e recomendações entregues, nos solicitaram agora a previsão do faturamento dessas redes para a próxima 6 semanas. O intuito dessa solicitação é organizar melhor as ações de promoções, marketing e envio de orçamento. Sendo assim, os gerentes das redes conseguem saber quais variàveis impactam positivamente e negativamente nas vendas e, além disso, possuem uma previsão do que acontecerá nos próximos 6 dias, de modo, a conseguir ajustar as ações e estratégias semanais de vendas.

## 2.1 Proposta da Solução

A nossa proposta de solução será um modelo preditivo que consegue nos dar a previsão do total de vendas dos próximos 6 dias baseado no comportamento dos últimos 7 dias.

## 2.2 Entrega Final

A entrega final, será um dashboard interativo em que o cliente poderá ver a loja, o seu detalhamento de informações e, também a previsão do total de vendas dos próximos 6 dias. Esse dashboard poderá ser acessado de qualquer local, pois o mesmo estará hospedado em nuvem.

## 2.3 Base de Dados Principal

Logo abaixo, tem-se o dicionário de dados das variávies que foram utilizadas.

| Coluna                  | Descrição                                                                                                  |
|-------------------------|------------------------------------------------------------------------------------------------------------|
| **Store**               | Identificador único para cada loja                                                                         |
| **Sales**               | Faturamento de qualquer dia específico (isso é o que você está prevendo)                                   |
| **Customers**           | Número de clientes em um dado dia                                                                          |
| **Open**                | Indicador se a loja estava aberta: 0 = fechada, 1 = aberta                                                 |
| **StateHoliday**        | Indica um feriado estadual: a = feriado público, b = Páscoa, c = Natal, 0 = Nenhum                         |
| **SchoolHoliday**       | Indica se a (Loja, Data) foi afetada pelo fechamento das escolas públicas                                  |
| **StoreType**           | Modelos de lojas: a, b, c, d                                                                               |
| **Assortment**          | Nível de sortimento: a = básico, b = extra, c = estendido                                                  |
| **CompetitionDistance** | Distância até a loja concorrente mais próxima                                                              |
| **CompetitionOpenSinceMonth/Year** | Ano e mês aproximados em que a loja concorrente mais próxima foi aberta                         |
| **Promo**               | Indica se uma loja está realizando uma promoção nesse dia                                                  |
| **Promo2**              | Promoção contínua: 0 = a loja não está participando, 1 = a loja está participando                          |
| **Promo2SinceYear/Month** | Ano e semana em que a loja começou a participar da Promo2                                                |
| **PromoInterval**       | Meses em que a Promo2 é iniciada: "Fev, Mai, Ago, Nov"                                                     |


# Observação
Logo abaixo, você encontrará uma descrição de como foi realizado o desenvolvimento do projeto, desde a fase de análise exploratória até a modelagem e treinamento do modelo e finalização do resultado em um dashboard. Importante ressaltar, que, inicialmente, tentamos realizar a previsão de vendas das próximas 6 semanas. Para isso, realizamos uma engenharia de atributos e modelagem, que obtivéssemo um agrupamento semanal dos dados. Entretanto, com isso, perdemos a granularidade e o detalhamento dos dados, impactanto negativamente a performance dos modelos criados. 

Mudando a estratégia, decidi realizar a previsão do total de vendas dos próximos 6 dias, mantendo a granularidade dos dados no nível de dia. Isso faz mais sentido, pois, entendido a realidade de negócio em que se está inserido o problema que, no caso, é o varejo, o comportamento diário é extremamente importante dada como são as variações desse modelo de negócio, impactanto no aprendizado de máquina no entendimento dos detalhes de variações e complexidades.

Para esse fim, foram realizados 5 ciclos de tentativas. Portanto, logo abaixo, mencionarei o resumo de toda a estratégia e planejamento utilizada no último ciclo, no caso, ciclo 5. 

# 3.0 Análise Exploratória dos Dados

Durante o processo de análise exploratória, realizamos uma análise geral entre nossas variáveis independentes e a variável alvo. Isso permitiu compreender melhor nosso dataset e validar as informações disponíveis. As conclusões aqui, são as mesmas da análise estatística que realizamos anteriormente. Eles servirão de base para a tomada de decisão na modelagem de dados preditiva.

**Relatório**

- **Day of Week**: Durante os primeiros dias da semana, o faturamento é maior. Com a chegada do fim de semana, o volume diminui devido à menor movimentação de pessoas nas drogarias durante sextas, sábados e domingos.
- **Customers**: O aumento do número de clientes nas drogarias resulta em maior faturamento, pois mais pessoas estão realizando compras.
- **CompetitionDistance**: Analisando o gráfico, percebemos uma leve tendência de queda na regressão. Lojas com concorrentes mais próximos tendem a realizar mais promoções, aumentando o volume de vendas. Com um concorrente mais distante, as promoções não são tão frequentes, impactando menos o volume de vendas.
- **Open**: Lojas abertas possuem um maior volume de vendas.
- **Promo**: Lojas em promoção tendem a ter um maior volume de vendas, já que esse é o objetivo da promoção.
- **SchoolHoliday**: Lojas afetadas por feriados escolares têm um faturamento maior, pois estão localizadas próximas a escolas, resultando em maior movimentação de segunda a sábado.
- **Promo2**: Promoções têm efeito apenas por um período limitado. Após os clientes adquirirem os produtos, eles não compram novamente tão rapidamente. Promoções prolongadas perdem força.
- **StateHoliday**: O faturamento é maior em datas que não são feriados.
- **Assortment**: Drogarias com uma variedade básica ou estendida faturam menos que drogarias com uma variedade intermediária. Variedade básica não atende a todas as necessidades, enquanto variedade excessiva inclui produtos de baixa rotatividade, impactando o volume de vendas.
- **StoreType**: Todas as lojas faturam, mas as do tipo b possuem maior faturamento.
- **CompetitionOpenSinceYearMonth**: Não há diferença significativa entre o tempo de abertura de um competidor e as vendas, indicando que as lojas mantêm suas vendas de forma constante.

## 4.0 Engenharia de Atributos

Para atingir nosso objetivo, foi feita uma modelagem de dados para atingir esse objetivo. Para isso criamos as seguintes variáveis:

|              Variável            | Descrição                                                |
|----------------------------------|----------------------------------------------------------|
|           PublicHoliday          | Feriado público no dia de hoje                           |
|            SalesLastDay          | Vendas do último dia                                     |
|       MeanSalesLastSevenDays     | Média das vendas dos últimos 7 dias                      | 
|      TotalSalesLastSevenDays     | Total de Vendas dos últimos 7 dias                       | 
|      TotalPromoLastSevenDays     | Quantidade de promoções ativadas nos últimos 7 dias      |
|     TotalPromo2LastSevenDays     | Quantidade de promoções 2 ativadas nos últimos 7 dias    |
|  TotalSchoolHolidayLastSevenDay  | Quantidade de feriados escolares nos últimos 7 dias      |
| TotalPublicHolidaysLastSevenDays | Quantidade de feriados públicos dos últimos 7 dias       |
|       TotalSalesNextSixDays      | Nossa variável alvo: Total de vendas dos próximos 6 dias |


## 5.0 Separação dos Dados para Aprendizam de Máquina e Pré-Processamento dos Dados

Nessa etapa separamos os dados entre treino, validação e teste para avaliar o modelo e realizamos a etapa do Pré-Processamento. De modo a facilitar o script de produção, utilizamos pipelines.

## 6.0 Modelos Utilizados

Ao todo, foram testados 10 modelos para avaliar qual teria melhor performance e aderência. As métricas utilizadas foram: Média Absoluta do Erro - MAE, Média Absoluta de Percentual do Erro - MAPE e Erro Médio da Raiz Quadrática - RMSE. Logo Abaixo temos:

### Capacidade de Aprendizado

|Métricas|Regressão Linear|  Ridge  |  Lasso  |   Tree  | ExtraTree | LinearSRV | ExtraTrees | Gradient Boosting | Random Forest | XGBoost |
|--------|----------------|---------|---------|---------|-----------|-----------|------------|-------------------|---------------|---------|
|   MAE	 |     4855.23	  | 4855.23	| 4855.06 |	5822.31 |  6418.07	|  4824.58	|  5667.48	 |      4184.25	     |    5597.25	 | 3945.42 |
|  MAPE	 |      11.94	  |  11.94	|  11.94  |	 14.50	|   16.37	|   11.51	|   14.38	 |       10.20	     |     13.96	 |   9.63  |
|  RMSE	 |     6669.82	  | 6669.82	| 6669.83 |	5822.31	|  8400.15	|  6802.10	|  7512.42	 |      5745.90	     |    7532.91	 | 5392.12 |