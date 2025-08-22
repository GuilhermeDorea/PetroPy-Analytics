'''Application to display data provided by the API'''
import streamlit as st
import requests
import pandas as pd

def get_data(uf):
    '''Catch data from the API defined in api_manager.py'''
    url = f"http://localhost:5000/stations/{uf}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao buscar dados da API: {e}")
        return None

ufs = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG",
        "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]

ufs_names =["Acre","Alagoas","Amapá","Amazonas","Bahia","Ceará","Distrito Federal","Espírito Santo",
    "Goiás","Maranhão","Mato Grosso","Mato Grosso do Sul","Minas Gerais","Pará","Paraíba","Paraná",
    "Pernambuco","Piauí","Rio de Janeiro","Rio Grande do Norte","Rio Grande do Sul","Rondônia",
    "Roraima","Santa Catarina","São Paulo","Sergipe","Tocantins"]

fuel_full_names = {
    'gas': 'Gasoline',
    'addgas': 'Additive Gasoline',
    'ethanol': 'Ethanol',
    'cng': 'Natural Gas (CNG)',
    'diesel': 'Diesel',
    'diesel_s10': 'Diesel S10'
}

## Dashboard displays
# Dashboard Title
st.title("⛽ Brasil Mean fuel prices")

# Seletor de Estado na barra lateral
st.sidebar.header("Filters")
selected_uf_name = st.sidebar.selectbox("Select a state (UF)", ufs_names)
selected_uf = ufs[ufs_names.index(selected_uf_name)]

# Search prices button
if st.sidebar.button("Search Prices"):
    data = get_data(selected_uf)
    st.header(f"State: {selected_uf_name}")

    # Remove empty values from exibition and creates a Data frame for plotting
    prices = {k: v for k, v in data['mean_prices'].items() if v is not None}
    df_prices = pd.DataFrame(list(prices.items()), columns=['Fuel', 'Mean prices (R$)'])
    df_prices['Fuel'] = df_prices['Fuel'].map(fuel_full_names)
    # Plot graphs
    st.subheader("Mean value bar chart")
    st.bar_chart(df_prices.set_index('Fuel'))

    # Show table
    st.subheader("Table data")
    st.table(df_prices)
