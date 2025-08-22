'''Application to display data provided by the API'''
import streamlit as st
import requests
import pandas as pd
import plotly.express as px

def buscar_dados(uf):
    '''Catch data from the API defined in api_manager.py'''
    url = f"http://localhost:5000/stations/{uf}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao buscar dados da API: {e}")
        return None
    
# Lista de UFs do Brasil para o seletor
ufs = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG",
        "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]

def get_country_data():
    'Function to get the data from each state'
    country_data = []
    for uf in ufs:
        country_data.append(buscar_dados(uf))
    return country_data

fuel_full_names = {
    'gas': 'Gasoline',
    'addgas': 'Additive Gasoline',
    'ethanol': 'Ethanol',
    'cng': 'Natural Gas (CNG)',
    'diesel': 'Diesel',
    'diesel_s10': 'Diesel S10'
}
# Título do Dashboard
st.title("⛽ Brasil Mean fuel prices")

# Seletor de Estado na barra lateral
st.sidebar.header("Filters")
uf_selecionada = st.sidebar.selectbox("Select a state (UF)", ufs)


df_mapa = pd.DataFrame({
    'uf': ['SP', 'RJ', 'BA', 'MG'],
    'preco_medio': [5.85, 6.10, 5.95, 5.70]
})

st.header("Mapa de Preço Médio por Estado")

fig = px.choropleth(
    df_mapa,
    geojson="https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson",
    locations='uf',             # A coluna do DataFrame com as siglas dos estados
    featureidkey='properties.sigla', # ATENÇÃO: A chave neste arquivo é 'sigla' e não 'UF'
    color='preco_medio',        # A coluna que definirá a cor de cada estado
    color_continuous_scale="Reds",
    scope="south america",
    title="Preço Médio da Gasolina por Estado",
    labels={'preco_medio': 'Preço Médio (R$)', 'uf': 'Estado'}
)

# Ajusta o zoom para focar nos estados e remove o mapa base
fig.update_geos(fitbounds="locations", visible=False)

st.plotly_chart(fig)

# Botão para iniciar a busca
if st.sidebar.button("Search Prices"):
    data = buscar_dados(uf_selecionada)
    print(data)
    st.header(f"State: {data['state']}")

    # Remove empty values from exibition and creates a Data frame for plotting
    precos = {k: v for k, v in data['mean_prices'].items() if v is not None}
    df_precos = pd.DataFrame(list(precos.items()), columns=['Fuel', 'Mean prices (R$)'])
    df_precos['Fuel'] = df_precos['Fuel'].map(fuel_full_names)
    print(df_precos.head())
    # Plot graphs
    st.subheader("Mean value bar chart")
    st.bar_chart(df_precos.set_index('Fuel'))

    # Show table
    st.subheader("Table data")
    st.table(df_precos)

