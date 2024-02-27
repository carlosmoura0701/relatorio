import streamlit as st
import pandas as pd
import numpy as np

df_path = '01/BasedeDadosAdata.xlsx'

coordenadas_path = '01/COORDENADAS.xlsx'


grafico_1turno_path = '01/1TURNOGRAFICO.xlsx'
grafico_zonas_path = '01/ZONASGRAFICO.xlsx'

dfg1 = pd.read_excel(grafico_1turno_path)
dfg2 = pd.read_excel(grafico_zonas_path)

df = pd.read_excel(df_path)
df2 = pd.read_excel(coordenadas_path)

# 1 TURNO 

turno1 = df["TURNO"] == "1° TURNO"

filtered_df_turno1 = df[turno1]
qtd_pessoas_turno1 = str(len(filtered_df_turno1))

loc_data_1_turno = {
    "longitude": df2['LONGITUDE'],
    "latitude": df2['LATITUDE'],
    'color': ['#F96507','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404',
              '#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D',
              '#50D612','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612',
              '#1220D6','#1220D6','#1220D6','#1220D6','#1220D6','#1220D6','#1220D6','#1220D6','#1220D6','#1220D6','#1220D6','#1220D6','#1220D6','#1220D6','#1220D6']
}

map_df = pd.DataFrame.from_dict(loc_data_1_turno)

# 2 TURNO 

turno2 = df["TURNO"] == "2° TURNO"

filtered_df_turno2 = df[turno2]
qtd_pessoas_turno2 = str(len(filtered_df_turno2))

# 3 TURNO 

turno3 = df["TURNO"] == "3° TURNO"

filtered_df_turno3 = df[turno3]
qtd_pessoas_turno3 = str(len(filtered_df_turno3))

# COMERCIAL

turnoC = df["TURNO"] == "COMERCIAL"

filtered_df_turnoC = df[turnoC]
qtd_pessoas_turnoC = str(len(filtered_df_turnoC))

# ZL

turnoZL = df["ZONA"] == "LESTE"

filtered_df_turnoZL = df[turnoZL]
qtd_pessoas_turnoZL = str(len(filtered_df_turnoZL))

# ZN

turnoZN = df["ZONA"] == "NORTE"

filtered_df_turnoZN = df[turnoZN]
qtd_pessoas_turnoZN = str(len(filtered_df_turnoZN))

# ZO

turnoZO = df["ZONA"] == "OESTE"

filtered_df_turnoZO = df[turnoZO]
qtd_pessoas_turnoZO = str(len(filtered_df_turnoZO))

# ZS

turnoZS = df["ZONA"] == "SUL"

filtered_df_turnoZS = df[turnoZS]
qtd_pessoas_turnoZS = str(len(filtered_df_turnoZS))

df2 = pd.DataFrame({
    '1º Turno': [qtd_pessoas_turno1],
    '2º Turno': [qtd_pessoas_turno2],
    '3º Turno': [qtd_pessoas_turno3],
    'Comercial': [qtd_pessoas_turnoC]
})

df3 = pd.DataFrame({
    'ZONA LESTE': [qtd_pessoas_turnoZL],
    'ZONA NORTE': [qtd_pessoas_turnoZN],
    'ZONA OESTE': [qtd_pessoas_turnoZO],
    'ZONA SUL': [qtd_pessoas_turnoZS]
})

st.title('Relatório de funcionários Adata Eletonics')

st.subheader('Quantidade de funcionários nos turnos 1,2,3 e comercial')

st.dataframe(df2,hide_index=True,width=3000)

st.bar_chart(dfg1,x='Turno',y='Funcionários')

st.subheader('Quantidade de funcionários nas zonas Leste, Norte, Oeste e Sul')
st.dataframe(df3,hide_index=True,width=3000)

st.bar_chart(dfg2,x='Zona',y='Funcionários')

st.subheader('Mapa dos funcionários')

color = st.color_picker('Cor Adata Eletonics', '#F96507',key='0')

color = st.color_picker('Primeiro turno', '#EF0404',key='1')

color = st.color_picker('Segundo turno', '#77055D',key='3')

color = st.color_picker('Terceiro turno', '#50D612',key='5')

color = st.color_picker('Turno comercial', '#1220D6',key='7')

st.map(map_df, size=20, color='color')
