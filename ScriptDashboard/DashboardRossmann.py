# 0.0 Pacotes e Bibliotecas

import pandas as pd
import numpy  as np
import streamlit as st
import plotly.express as px
import seaborn as sbn
from datetime import datetime

# 1.0 Carregamento dos Dados
df1_loja = pd.read_csv('DadosLoja.csv', delimiter=',', low_memory=False)
df1_faturamento = pd.read_csv('DadosFaturamento.csv', delimiter=',', low_memory=False)

# Dados Finais
df1 = df1_faturamento.merge(df1_loja, how='left', on='Store')

# Trativa de Texto
df1['Date'] = pd.to_datetime(df1['Date'], format='%Y-%m-%d')
df1['Month'] = df1['Date'].dt.strftime('%Y-%m')
df1['Year'] = df1['Date'].dt.strftime('%Y')


# Menu de Barra Lateral
st.sidebar.image('..\Imagens\LogoRossmannSideBar.jpg')
st.sidebar.write("Navegue pelo Projeto")
pagina = st.sidebar.selectbox("",["Apresentação", "Análise de Faturamento", "Monitoramento de Faturamento", "Visão Gestores"])


if pagina == "Apresentação": 

    st.title("Bem-vindo ao Projeto de Análise de Faturamento da Rossmann")

    st.image('..\Imagens\LogoRossmann.jpg')

    st.write(
        "Este projeto tem como objetivo aprimorar minhas habilidades em análise estatística de regressão aplicada ao faturamento no varejo, "
        "bem como no desenvolvimento de modelos preditivos baseados em aprendizado de máquina supervisionado e técnicas de modelagem de dados. "
        "Todas as análises realizadas estão fundamentadas em um problema real de negócio, que guia cada etapa do processo de investigação e construção do modelo."
    )

    st.write(
        "Os dados utilizados neste projeto são públicos e estão disponíveis na plataforma de competições de Ciência de Dados **Kaggle**."
    )

    st.header("Problema de Negócio")

    st.write(
        "Entre os anos de 2013 e 2015 (até julho), foi identificada uma tendência de queda no faturamento da rede de drogarias **Rossmann**. "
        "Diante desse cenário, a diretoria solicitou uma análise detalhada para entender como diferentes variáveis impactam, positiva ou negativamente, o desempenho das lojas. "
        "Além disso, considerando a dinâmica diária e semanal do varejo, foi requisitada a construção de um modelo preditivo que permita estimar o faturamento dos próximos 6 dias. "
        "Com essas previsões em mãos, a empresa poderá tomar decisões mais ágeis e estratégicas, como ativar promoções, ajustar preços e otimizar o abastecimento de estoques."
    )

    st.subheader("Destrinchando a Demanda")

    st.write("O projeto foi estruturado com base em dois grandes desafios:")

    st.markdown(
        "**1º Problema – Análise de Impacto de Variáveis:** Investigar como determinadas variáveis influenciam o faturamento das lojas. "
        "Serão utilizadas técnicas de regressão para quantificar o efeito de cada variável no desempenho financeiro."
    )

    st.markdown(
        "**2º Problema – Previsão de Faturamento:** Desenvolver um modelo preditivo capaz de estimar o faturamento total dos próximos 6 dias. "
        "Essa antecipação facilitará a implementação de estratégias de curto prazo com maior assertividade."
    )

    st.header("Entregáveis do Projeto")

    st.write(
        "Para definir os entregáveis, é fundamental considerar quem serão os principais consumidores dessas informações. "
        "Embora as demandas tenham partido da diretoria, os dados gerados também serão cruciais para os gerentes de loja, que atuam diretamente na execução das estratégias comerciais."
    )

    st.markdown(
        "**Para o 1º problema**, será entregue um relatório analítico detalhado com os coeficientes da regressão e análises de correlação. "
        "Esse material permitirá que tanto a diretoria quanto os gestores compreendam os fatores que influenciam o faturamento e ajustem suas estratégias de forma mais eficiente. "
        "Além disso, será desenvolvido um **dashboard interativo** com visualizações do desempenho da rede como um todo (foco na diretoria) e também em nível de loja (foco nos gestores)."
    )

    st.markdown(
        "**Para o 2º problema**, será implementado um modelo preditivo que fornecerá estimativas do faturamento total dos próximos 6 dias. "
        "Essas informações serão integradas ao mesmo dashboard mencionado anteriormente, permitindo um acompanhamento consolidado e estratégico das projeções futuras."
    )

elif pagina == "Análise de Faturamento":

    st.header("Variáveis para a Análise de Faturamento")

    st.write(
        "Para que uma análise seja consistente, é fundamental conhecer as variáveis envolvidas. A seguir, estão listadas as variáveis selecionadas para compreender o impacto de cada uma no faturamento:"
    )

    st.write("As variáveis fornecidas para a análise estatística foram:")

    st.markdown("**Store**: Identificador único para cada loja.")
    st.markdown("**Sales**: Faturamento da loja em um determinado dia.")
    st.markdown("**Customers**: Número de clientes em um dado dia.")
    st.markdown("**Open**: Indica se a loja estava aberta (1) ou fechada (0).")
    st.markdown(
        "**StateHoliday**: Indica feriados estaduais. 'a' = feriado público, 'b' = Páscoa, 'c' = Natal, '0' = nenhum. Em geral, as lojas estão fechadas nesses dias."
    )
    st.markdown("**SchoolHoliday**: Indica se a loja foi afetada por fechamento de escolas públicas.")
    st.markdown("**StoreType**: Tipo da loja, classificados como a, b, c ou d.")
    st.markdown("**Assortment**: Nível de sortimento: 'a' = básico, 'b' = extra, 'c' = estendido.")
    st.markdown("**CompetitionDistance**: Distância (em metros) até o concorrente mais próximo.")
    st.markdown("**CompetitionOpenSinceMonth/Year**: Mês e ano de abertura do concorrente mais próximo.")
    st.markdown("**Promo**: Indica se há promoção ativa na loja naquele dia.")
    st.markdown("**Promo2**: Indica se a loja participa da Promo2 (0 = não, 1 = sim).")
    st.markdown("**Promo2SinceYear/Month**: Ano e mês em que a loja passou a participar da Promo2.")
    st.markdown(
        "**PromoInterval**: Meses em que a Promo2 é reiniciada. Ex: 'Fev, Mai, Ago, Nov' indica relançamentos nesses meses."
    )

    st.header("Análise das Variáveis Escolhidas no Faturamento")

    st.write(
        "Com base no entendimento das variáveis, foi realizada uma análise exploratória para verificar como cada uma se relaciona com o faturamento. Abaixo estão os principais destaques:"
    )

    st.markdown("- **Day of Week**: Os primeiros dias da semana apresentam maior faturamento. Sextas, sábados e domingos têm queda nas vendas.")
    st.image('../Imagens/DayOfWeekVSSales.png')

    st.markdown("- **Customers**: Mais clientes resultam diretamente em maior faturamento.")
    st.image('../Imagens/DayOfWeekVSSales.png')

    st.markdown("- **CompetitionDistance**: Há uma leve tendência de queda no faturamento conforme a distância do concorrente diminui. Lojas com concorrentes " \
                "próximos tendem a promover mais, aumentando as vendas.")
    st.image('../Imagens/CompetitonDistanceVSSales.png')

    st.markdown("- **Promo**: Promoções aumentam significativamente o volume de vendas.")
    st.image('../Imagens/PromoVSSales.png')

    st.markdown("- **SchoolHoliday**: Lojas próximas a escolas tendem a ter maior faturamento durante os feriados escolares, devido à maior movimentação de segunda a sábado.")
    st.image('../Imagens/SchoolHolidayVSSales.png')

    st.markdown("- **Promo2**: Promoções contínuas perdem eficácia ao longo do tempo, pois os clientes não repetem a compra com tanta frequência.")
    st.image('../Imagens/SchoolHolidayVSSales.png')

    st.markdown("- **StateHoliday**: O faturamento tende a ser menor em dias de feriado.")
    st.image('../Imagens/StateHolidayVSSales.png')

    st.markdown("- **Assortment**: Lojas com sortimento intermediário performam melhor. Sortimentos básicos não atendem bem à demanda, e sortimentos excessivos" \
                " incluem produtos de baixa rotatividade.")
    st.image('../Imagens/AssortmentVSSales.png')

    st.markdown("- **StoreType**: Lojas do tipo 'b' apresentam maior faturamento médio.")
    st.image('../Imagens/StoreTypeVSSales.png')

    st.markdown("- **CompetitionOpenSinceYear/Month**: O tempo de abertura do concorrente mais próximo não apresentou impacto significativo nas vendas.")
    st.image('../Imagens/CompetitionOpenSinceYearVSSales.png')
    st.image('../Imagens/CompetitionOpenSinceMonthVSSales.png')

    st.header("Análise de Correlação")

    st.write(
        "Utilizando os métodos de correlação de Pearson e Spearman, foram identificadas variáveis com relação significativa ao faturamento e baixa colinearidade entre si. As principais correlações são:"
    )

    st.markdown("- **Promo**: Correlação positiva (0.43). Promoções atraem mais clientes.")
    st.markdown("- **PublicHoliday**: Correlação negativa (-0.20). Vendas caem durante feriados.")
    st.markdown("- **DayOfWeek**: Correlação negativa (-0.18). Vendas reduzem no final de semana.")
    st.markdown("- **Customers**: Correlação forte (0.79). Mais clientes = mais faturamento.")
    st.markdown("- **Assortment**: Correlação positiva (0.12). Mais variedade = mais vendas.")
    st.markdown("- **Promo2**: Correlação levemente negativa (-0.10). Promoções contínuas perdem eficácia com o tempo.")

    st.header("Análise de Impacto de Variável")

    st.write("As variáveis que mais influenciam o faturamento das lojas Rossmann foram identificadas com base na análise de regressão. São elas:")

    st.markdown("**Promo**: Aumento médio de US\$ 559.85 por dia (variação: US\$ 556.31 – US\$ 563.39).")
    st.markdown("**Promo2**: Impacto positivo menor, com aumento médio de US\$ 126.21 por dia (variação: US\$ 122.81 – US\$ 129.61).")
    st.markdown("**PublicHoliday**: Redução média de US\$ 23.67 (variação: US\$ 20.36 – US\$ 26.99).")
    st.markdown("**DayOfWeek**: Redução média de US\$ 49.14 por dia ao longo da semana (variação: US\$ 45.68 – US\$ 52.60).")
    st.markdown("**Customers**: Cada aumento no número de clientes resulta em incremento médio de US\$ 1,750.82 (variação: US\$ 1,747.19 – US\$ 1,754.33).")
    st.markdown("**Assortment**: Maior variedade aumenta o faturamento em média US\$ 313.05 (variação: US\$ 309.73 – US\$ 316.37).")

    st.header("Recomendações")

    st.markdown("1. Intensificar ações de vendas no início da semana, evitando os finais de semana.")
    st.markdown("2. Expandir o sortimento das lojas com variedade básica, otimizando o mix de produtos.")
    st.markdown("3. Priorizar promoções pontuais e estratégicas em vez de promoções contínuas.")
    st.markdown("4. Implementar ações que aumentem o fluxo de clientes nas lojas.")


elif pagina == "Monitoramento de Faturamento":

    # ======================= Construção de Filtro da Seção =======================
    
    # Montagem dos containers
    filtro_monitoramento1, filtro_monitoramento2 = st.columns(2) 

    # Construção dos filtros de loja e tipo de estoque
    with filtro_monitoramento1:
        selection_store = st.multiselect('Filtre o tipo de loja', ["a", "b", "c", "d"], default=["a", "b", "c", "d"])
    
    with filtro_monitoramento2:
        selection_assortment = st.multiselect('Filtre o tipo de estoque da loja', ["a", "b", "c"], default=["a", "b", "c"])

    # Construção do Dataset
    df1 = df1[(df1['StoreType'].isin(selection_store)) & (df1['Assortment'].isin(selection_assortment))].sort_values(by=['Date'], ascending=True)

    # 2.0 Modelagem de Dados 
    assortment = df1_loja['Assortment'].value_counts().reset_index().rename(columns={'count':'Qtd.'})
    store_type = df1_loja['StoreType'].value_counts().reset_index().rename(columns={'count':'Qtd.'})


    # ======================= Construção dos indicadores gerais de acompanhamento =======================
    
    # Total de Faturamento
    total_sales = df1[df1['Date'] == df1['Date'].max()]['Sales'].sum()

    # Total de Clientes
    total_customers =  df1[df1['Date'] == df1['Date'].max()]['Customers'].sum()

    # Total de Lojas
    fat_medio_client = np.round(df1[df1['Date'] == df1['Date'].max()]['Sales'].sum()/df1[df1['Date'] == df1['Date'].max()]['Customers'].sum(), 2)

    card1, card2, card3 = st.columns(3)
    card1.metric(label='Faturamento Total Hoje',value=total_sales, border=True)
    card2.metric(label='Total de Cliente Hoje', value=total_customers, border=True)
    card3.metric(label='Faturamento Médio por Cliente', value=fat_medio_client, border=True)


    # ======================= Acompanhamento de Faturamento =======================

    # Título da Seção 
    st.title('**Faturamento das Lojas**')

    # --------------------- GRÁFICO FATURAMENTO 30 DIAS ------------------

    # Definição de Container para armazenar o gráfico
    container_fat = st.container(border=True)

    # Cabeçalho do gráfico
    container_fat.markdown('**Faturamento - Últimos 30 Dias**')
            
    # Data Limite para obter os últimos 30 dias de faturamento
    data_limite = df1['Date'].max() - pd.Timedelta(days=30)

    # Construção datasets para os gráficos
    serie_historica_vendas_diario = df1[['Date', 'Sales']][df1['Date'] >= data_limite].groupby('Date').sum().reset_index()
            
    # Gráfico
    container_fat.line_chart(data=serie_historica_vendas_diario, x='Date', y='Sales',  use_container_width=True)

    # ------------------------- GRÁFICO DE FATURAMENTO MENSAL E ANUAL ------------------------------------

    # Containers para o faturamento mensal e anual
    graf1, graf2 = st.columns(2)


    # ------------------ Faturamento visão mensal ----------------------
    with graf1:

        # Definição de Container
        container_graf1 = st.container(border=True)

        # Cabeçalho do gráfico
        container_graf1.markdown('**Faturamento - Visão Mensal**')
        
        # Construção datasets para os gráficos
        serie_historica_vendas_mensal = df1[['Month', 'Sales']].groupby('Month').sum().reset_index()

        # Gráfico
        container_graf1.line_chart(data=serie_historica_vendas_mensal, 
                                   x='Month', 
                                   y='Sales',  
                                   use_container_width=True)


    # --------------------- Faturamento Visão Anual ------------------------
    with graf2:

        # Definição de Container 
        container_graf2 = st.container(border=True)

        # Cabeçalho do gráfico
        container_graf2.markdown("**Faturamento - Visão Anual**")

        # Construção datasets para os gráficos
        serie_historia_vendas_anual = df1[['Year', 'Sales']].groupby('Year').sum().reset_index()

        # Gráfico
        container_graf2.bar_chart(data=serie_historia_vendas_anual,
                    x='Year',
                    y='Sales',
                    use_container_width=True)   


    # ------------------ Tabela para Acompanhamento das Faturamento das Lojas - TOP 10 ------------------
    st.subheader(f"Participação das Lojas no Faturamento de {df1['Year'].max()}")

    # Definição de container para armazenar tabela
    container_graf3 = st.container(border=False)

    # Título da Tabela
    container_graf3.markdown(f"**Faturamento das Lojas - Top 10**")
        
    # Modelagem de Dados
    top_10_lojas = df1[df1['Year']==df1['Year'].max()].groupby(by='Store')['Sales'].sum().reset_index().sort_values(by=['Sales'], ascending=False).iloc[0:10, :].reset_index(drop=True)
    sales_year = df1[df1['Year']==df1['Year'].max()]['Sales'].sum()
    top_10_lojas['Perc. Part.'] = (top_10_lojas['Sales']/sales_year)*100

    # Tabela estilizada 
    styled_table = top_10_lojas.style.hide(axis="index").set_table_styles(
            [{'selector': 'th, td', 'props': [('font-size', '12px')]}]
        )

    # Exibir no Streamlit
    container_graf3.dataframe(styled_table, use_container_width=True)

    # Definição de Container para acompanhamento na paticipação do faturamento por tipo de loja e tipo de estoque
    graf4, graf5 = st.columns(2)

    with graf4:

        container_graf4 = st.container(border=True)

        # Título da Tabela
        container_graf4.markdown(f"**Tipos de Loja**")

        # Construção do Dataset
        faturamento_tipo_loja = df1[df1['Year']==df1['Year'].max()].groupby(by='StoreType')['Sales'].sum().reset_index().sort_values(by=['Sales'], ascending=False).reset_index(drop=True)
    
    # Construção do Gráfico
        pie_storetype = px.pie(data_frame=faturamento_tipo_loja, values='Sales', names='StoreType')
        
        # Exibição do Resultado
        container_graf4.plotly_chart(pie_storetype)

    with graf5:

        container_graf5 = st.container(border=True)

        # Título da Tabela
        container_graf5.markdown(f"**Tipo de Estoque**")

        # Construção do Dataset
        faturamento_tipo_loja = df1[df1['Year']==df1['Year'].max()].groupby(by='Assortment')['Sales'].sum().reset_index().sort_values(by=['Sales'], ascending=False).reset_index(drop=True)
    
    # Construção do Gráfico
        pie_assortment = px.pie(data_frame=faturamento_tipo_loja, values='Sales', names='Assortment')
        
        # Exibição do Resultado
        container_graf5.plotly_chart(pie_assortment)



    # --------------------------- Acompanhamento das Movimentações de Clientes ---------------------------

    # Título da Seção
    st.title('**Movimentações de Clientes**')

    container_mov_clientes = st.container(border=True)

    # Cabeçalho do gráfico
    container_mov_clientes.markdown('**Movimentações Clientes - Últimos 30 Dias**')

    # Construção datasets para os gráficos
    serie_historica_clientes_diario = df1[['Date', 'Customers']][df1['Date'] >= data_limite].groupby('Date').sum().reset_index()
        
    # Gráfico
    container_mov_clientes.line_chart(data=serie_historica_clientes_diario, 
                x='Date', 
                y='Customers',  
                use_container_width=True
                )

    # Definindo containers para acompanhamento de clientes -  visão Mensal e Anual
    graf6, graf7 = st.columns(2)

    # Container de Clientes
    with graf6:

        container_graf6 = st.container(border=True) 

        # Cabeçalho do gráfico
        container_graf6.markdown('**Movimentação de Clientes - Visão Mensal**')
        
        # Construção datasets para os gráficos
        serie_historica_clientes_mensal = df1[['Month', 'Customers']].groupby('Month').sum().reset_index()
        
        # Gráfico
        container_graf6.line_chart(data=serie_historica_clientes_mensal, 
                    x='Month', 
                    y='Customers',  
                    use_container_width=True
                    )
        
    with graf7:

        # Definição do Container
        container_graf7 = st.container(border=True)

        # Cabeçalho do gráfico
        container_graf7.markdown("**Movimentações de Clientes - Visão Anual**")

        # Construção datasets para os gráficos
        serie_historia_clientes_anual = df1[['Year', 'Customers']].groupby('Year').sum().reset_index()

        # Gráfico
        container_graf7.bar_chart(data=serie_historia_clientes_anual,
                    x='Year',
                    y='Customers',
                    use_container_width=True)   
        
