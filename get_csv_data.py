'''Application to get the data from CSV files and load it in the Data bank, all data avaible at:
https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/serie-historica-de-precos-de-combustiveis '''

import pandas as pd
from sqlalchemy import create_engine

# 1 - CSV reading and formating
CSV_FILE = 'Preços semestrais - AUTOMOTIVOS_2025_01.csv'
df = pd.read_csv(f'data/{CSV_FILE}', encoding='latin-1', sep=';')

df.rename(columns={
    'ï»¿Regiao - Sigla': 'regions',
    'Estado - Sigla': 'states',
    'Revenda': 'gas_station',
    'Produto': 'product',
    'Valor de Venda': 'price'
}, inplace=True)

df['price'] = pd.to_numeric(df['price'].str.replace(',', '.'), errors='coerce')
df.dropna(subset=['price'], inplace=True)

# 2 - New df to separate rows by gas stations
stations = df.pivot_table(index=['regions', 'states', 'gas_station'],
                           columns='product',values='price').reset_index()

# print(stations.head()) #Test print, uncomment to debug

# 3 - Create and save data in a databank, erases old db, for development purposes
# renames some variables to better API handle

stations.rename(columns={
    'DIESEL': 'diesel',
    'DIESEL S10': 'diesel_s10',
    'ETANOL': 'ethanol',
    'GASOLINA': 'gas',
    'GASOLINA ADITIVADA': 'addgas',
    'GNV': 'cng'
}, inplace=True)
stations.insert(0, 'id', stations.index + 1)

engine = create_engine('sqlite:///instance/gas_data.db')
stations.to_sql('station', engine, if_exists='replace', index=False)
