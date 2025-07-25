# 1.0 Objetivo do Projeto

O objetivo deste projeto é desenvolver um modelo de regressão capaz de prever os próximos 6 dias de faturamento de lojas. Com esse objetivo, temos o foco em aprimorar habilidade em análise exploratóra de dados, engenharia de atributos, modelagem de dados para problemas supervisionados e compreensão de negócios.


# 2.0 Problema de Negócio

A Rede de Drogarias Rossmann possui 3.000 lojas em 7 países europeus e mais de 30 anos de mercado. Os superintendentes solicitaram aos gerentes planos e ações para melhorar o faturamento das lojas. A primeira demanda que nós recebemos foi a solicitação de uma análise estatística para entender quais variáveis influenciavam positiva e negativamente o faturmento. Com a análise feita (veja aqui) e os devidos resultados e recomendações entregues, nos solicitaram agora a previsão do faturamento dessas redes para a próxima 6 semanas. O intuito dessa solicitação é organizar melhor as ações de promoções, marketing e envio de orçamento. Sendo assim, os gerentes das redes conseguem saber quais variàveis impactam positivamente e negativamente nas vendas e, além disso, possuem uma previsão do que acontecerá nos próximos 6 dias, de modo, a conseguir ajustar as ações e estratégias semanais de vendas.

## 2.1 Proposta da Solução

A nossa proposta de solução será um modelo preditivo que consegue nos dar a previsão do total de vendas dos próximos 6 dias baseado no comportamento dos últimos 7 dias.

## 2.2 Entrega Final

A entrega final, será um dashboard interativo em que o cliente poderá ver a loja, o seu detalhamento de informações e, também a previsão do total de vendas dos próximos 6 dias. Esse dashboard poderá ser acessado de qualquer local, pois o mesmo estará hospedado em nuvem.

## 2.3 Dicionário de Dados

|Store| Identificador único para cada loja|
|Sales| Faturamento de qualquer dia específico|
|Customers| O número de clientes em um dado dia|
|Open| Um indicador se a loja estava aberta: 0 = fechada, 1 = aberta|
|StateHoliday| Indica um feriado estadual. a = feriado público, b = feriado de Páscoa, c = Natal, 0 = Nenhum.|
|SchoolHoliday| Indica se a (Loja, Data) foi afetada pelo fechamento das escolas públicas|
|StoreType| Diferencia entre 4 modelos de lojas diferentes: a, b, c, d.|
|Assortment| Descreve um nível de sortimento: a = básico, b = extra, c = estendido.|
|CompetitionDistance|Distância em metros até a loja concorrente mais próxima.|
|CompetitionOpenSinceMonth/Year| Dá o ano aproximado e o mês em que a loja concorrente mais próxima foi aberta.
|Promo|Indica se uma loja está realizando uma promoção nesse dia|
|Promo2| Promo2 é uma promoção contínua e consecutiva para algumas lojas: 0 = a loja não está participando, 1 = a loja está participando.|
|Promo2SinceYear/Month|Descreve o ano e a semana do calendário em que a loja começou a participar da Promo2|
|PromoInterval| Descreve os intervalos consecutivos em que a Promo2 é iniciada, nomeando os meses em que a promoção é reiniciada. Por exemplo, "Fev, Mai, Ago, Nov" significa que cada rodada começa em fevereiro, maio, agosto e novembro de qualquer ano para aquela loja.|