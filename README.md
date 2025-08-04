# 1.0 Objetivo do Projeto

O objetivo deste projeto é desenvolver um modelo de regressão capaz de prever os próximos 6 dias de faturamento de lojas. Com isso, buscamos aprimorar habilidades em análise exploratória de dados, engenharia de atributos, modelagem de dados para problemas supervisionados e compreensão de negócios.

# 2.0 Problema de Negócio

A Rede de Drogarias Rossmann possui 3.000 lojas em 7 países europeus e mais de 30 anos de mercado. Os superintendentes solicitaram aos gerentes planos e ações para melhorar o faturamento das lojas. A primeira demanda que recebemos foi a solicitação de uma análise estatística para entender quais variáveis influenciavam positiva e negativamente o faturamento. Com a análise feita (veja aqui), e os devidos resultados e recomendações entregues, foi solicitada agora a previsão de faturamento dessas redes para as próximas 6 semanas. O intuito dessa solicitação é organizar melhor as ações de promoções, marketing e envio de orçamento. Sendo assim, os gerentes das redes conseguem saber quais variáveis impactam positiva e negativamente as vendas e, além disso, possuem uma previsão do que acontecerá nos próximos 6 dias, de modo a conseguirem ajustar as ações e estratégias semanais de vendas.

## 2.1 Proposta da Solução

A nossa proposta de solução será um modelo preditivo que forneça a previsão do total de vendas dos próximos 6 dias, com base no comportamento dos últimos 7 dias.

## 2.2 Entrega Final

A entrega final será um dashboard interativo, no qual o cliente poderá visualizar a loja, seus detalhes informativos e a previsão do total de vendas dos próximos 6 dias. Esse dashboard poderá ser acessado de qualquer local, pois estará hospedado em nuvem.

## 2.3 Base de Dados Principal

Logo abaixo, tem-se o dicionário de dados das variáveis que foram utilizadas.

| Coluna                  | Descrição                                                                                                  |
|-------------------------|------------------------------------------------------------------------------------------------------------|
| **Store**               | Identificador único para cada loja                                                                         |
| **Sales**               | Faturamento de qualquer dia específico (isso é o que você está prevendo)                                   |
| **Customers**           | Número de clientes em um dado dia                                                                          |
| **Open**                | Indicador se a loja estava aberta: 0 = fechada, 1 = aberta                                                  |
| **StateHoliday**        | Indica um feriado estadual: a = feriado público, b = Páscoa, c = Natal, 0 = Nenhum                         |
| **SchoolHoliday**       | Indica se a (Loja, Data) foi afetada pelo fechamento das escolas públicas                                  |
| **StoreType**           | Modelos de lojas: a, b, c, d                                                                               |
| **Assortment**          | Nível de sortimento: a = básico, b = extra, c = estendido                                                  |
| **CompetitionDistance** | Distância até a loja concorrente mais próxima                                                              |
| **CompetitionOpenSinceMonth/Year** | Ano e mês aproximados em que a loja concorrente mais próxima foi aberta                  |
| **Promo**               | Indica se uma loja está realizando uma promoção nesse dia                                                  |
| **Promo2**              | Promoção contínua: 0 = a loja não está participando, 1 = a loja está participando                          |
| **Promo2SinceYear/Month** | Ano e mês em que a loja começou a participar da Promo2                                                  |
| **PromoInterval**       | Meses em que a Promo2 é iniciada: "Fev, Mai, Ago, Nov"                                                     |

# Observação

Logo abaixo, você encontrará uma descrição de como foi realizado o desenvolvimento do projeto, desde a fase de análise exploratória até a modelagem, treinamento do modelo e finalização do resultado em um dashboard.

É importante ressaltar que, inicialmente, tentamos realizar a previsão de vendas das próximas 6 semanas. Para isso, realizamos engenharia de atributos e modelagem com agrupamento semanal dos dados. Entretanto, perdemos a granularidade e o detalhamento das informações, o que impactou negativamente a performance dos modelos.

Mudando a estratégia, decidi realizar a previsão do total de vendas dos próximos 6 dias, mantendo a granularidade no nível diário. Essa abordagem faz mais sentido ao considerar a realidade do varejo, onde o comportamento diário é altamente relevante devido às variações naturais desse modelo de negócio. Isso impacta diretamente o aprendizado de máquina e a capacidade de capturar essas nuances.

Para esse fim, foram realizados 5 ciclos de tentativa. Abaixo, apresento um resumo da estratégia e do planejamento utilizados no último ciclo — o ciclo 5.

# 3.0 Análise Exploratória dos Dados

Durante o processo de análise exploratória, realizamos uma avaliação geral entre as variáveis independentes e a variável alvo. Isso permitiu compreender melhor o dataset e validar as informações disponíveis. As conclusões aqui são as mesmas da análise estatística realizada anteriormente e servirão de base para a modelagem preditiva.

**Relatório**

- **Day of Week**: Durante os primeiros dias da semana, o faturamento é maior. Com a chegada do fim de semana, o volume diminui devido à menor movimentação de pessoas nas drogarias às sextas, sábados e domingos.
- **Customers**: O aumento no número de clientes resulta em maior faturamento, pois mais pessoas realizam compras.
- **CompetitionDistance**: Analisando o gráfico, nota-se uma leve tendência de queda na regressão. Lojas com concorrentes mais próximos tendem a fazer mais promoções, aumentando o volume de vendas. Concorrentes distantes resultam em menos promoções e menor impacto.
- **Open**: Lojas abertas naturalmente possuem maior volume de vendas.
- **Promo**: Lojas com promoções ativas tendem a vender mais, conforme esperado.
- **SchoolHoliday**: Lojas afetadas por feriados escolares geralmente têm maior faturamento, por estarem próximas a escolas e apresentarem mais movimento de segunda a sábado.
- **Promo2**: Promoções prolongadas perdem força após certo tempo, pois os clientes não repetem a compra com frequência.
- **StateHoliday**: O faturamento tende a ser maior em dias que não são feriados.
- **Assortment**: Drogarias com sortimento intermediário apresentam maior faturamento. Sortimento básico não atende todas as necessidades, enquanto sortimento extenso pode conter produtos de baixa rotatividade.
- **StoreType**: Todas as lojas faturam, mas as do tipo b possuem maior desempenho.
- **CompetitionOpenSinceYearMonth**: Não há diferença significativa entre o tempo de abertura de concorrentes e as vendas, indicando estabilidade no desempenho das lojas.

## 4.0 Engenharia de Atributos

Para atingir nosso objetivo, foi realizada uma modelagem de dados e criação das seguintes variáveis:

|              Variável            | Descrição                                                |
|----------------------------------|----------------------------------------------------------|
|           PublicHoliday          | Feriado público no dia atual                             |
|            SalesLastDay          | Vendas do último dia                                     |
|       MeanSalesLastSevenDays     | Média das vendas dos últimos 7 dias                      | 
|      TotalSalesLastSevenDays     | Total de vendas dos últimos 7 dias                       | 
|      TotalPromoLastSevenDays     | Quantidade de promoções ativadas nos últimos 7 dias      |
|     TotalPromo2LastSevenDays     | Quantidade de promoções 2 ativadas nos últimos 7 dias    |
|  TotalSchoolHolidayLastSevenDay  | Quantidade de feriados escolares nos últimos 7 dias      |
| TotalPublicHolidaysLastSevenDays | Quantidade de feriados públicos dos últimos 7 dias       |
|       TotalSalesNextSixDays      | Variável alvo: total de vendas dos próximos 6 dias       |

## 5.0 Separação dos Dados para Aprendizado de Máquina e Pré-Processamento dos Dados

Nesta etapa, os dados foram divididos entre treino, validação e teste, visando avaliar corretamente o modelo. Para facilitar a execução do script em produção, utilizamos pipelines no pré-processamento.

## 6.0 Modelos Utilizados

Ao todo, foram testados 10 modelos para avaliar qual teria melhor desempenho. As métricas utilizadas foram: Erro Médio Absoluto (MAE), Erro Percentual Absoluto Médio (MAPE) e Raiz do Erro Quadrático Médio (RMSE). Veja os resultados:

#### Capacidade de Aprendizado

| Métricas | Regressão Linear | Ridge | Lasso | Tree | ExtraTree | LinearSVR | ExtraTrees | Gradient Boosting | Random Forest | XGBoost |
|----------|------------------|-------|--------|------|-----------|-----------|-------------|-------------------|----------------|---------|
| MAE      | 4855.23          | 4855.23 | 4855.06 | 5822.31 | 6418.07 | 4824.58 | 5667.48     | 4184.25           | 5597.25        | 3945.42 |
| MAPE     | 11.94            | 11.94   | 11.94   | 14.50  | 16.37   | 11.51   | 14.38       | 10.20             | 13.96          | 9.63    |
| RMSE     | 6669.82          | 6669.82 | 6669.83 | 5822.31 | 8400.15 | 6802.10 | 7512.42     | 5745.90           | 7532.91        | 5392.12 |

#### Capacidade de Generalização

| Métricas | Regressão Linear | Ridge | Lasso | Tree | ExtraTree | LinearSVR | ExtraTrees | Gradient Boosting | Random Forest | XGBoost |
|----------|------------------|-------|--------|------|-----------|-----------|-------------|-------------------|----------------|---------|
| MAE      | 4856.71          | 4856.71 | 4856.55 | 7762.46 | 6394.32 | 4827.67 | 5652.12     | 4196.03           | 5581.37        | 4010.41 |
| MAPE     | 11.97            | 11.97   | 11.97   | 14.48  | 16.35   | 11.55   | 14.37       | 10.24             | 13.94          | 9.78    |
| RMSE     | 6688.36          | 6688.36 | 6688.37 | 5802.89 | 8366.53 | 6815.55 | 7503.71     | 5781.90           | 7517.66        | 5516.65 |

Podemos observar que o modelo com melhor performance foi o **XGBoost**, sendo portanto nosso **modelo campeão**.

## 7.0 Validação Cruzada

Na validação cruzada, o modelo demonstrou estabilidade. Utilizamos as três métricas principais. Os resultados foram:

* Desvio padrão do MAPE: 0.04 — Média: 9.78  
* Desvio padrão do MAE: 17.21 — Média: 4018.16  
* Desvio padrão do RMSE: 26.99 — Média: 5522.66

## 8.0 Hiperparametrização

Utilizando a técnica `RandomizedSearchCV` com foco na redução do MAPE, foi possível melhorar a métrica para **MAPE = 9.0**.

## 9.0 Treinamento e Validação Final

Na fase final, unimos os dados de treino e validação, retreinamos o modelo e o avaliamos com os dados de teste (dados nunca vistos anteriormente). As performances obtidas foram:

* MAE: 3625.82  
* MAPE: 8.55  
* RMSE: 5322.55