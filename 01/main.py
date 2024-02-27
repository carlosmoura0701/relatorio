import streamlit as st
import pandas as pd
import numpy as np

df_path = '01/BasedeDadosAdata.xlsx'

turno_1_coordenadas_path = '01/1TURNO.xlsx'
turno_2_coordenadas_path = '01/2TURNO.xlsx'
turno_3_coordenadas_path = '01/3TURNO.xlsx'
turno_comercial_coordenadas_path = '01/COMERCIAL.xlsx'

grafico_1turno_path = '01/1TURNOGRAFICO.xlsx'
grafico_zonas_path = '01/ZONASGRAFICO.xlsx'

dfg1 = pd.read_excel(grafico_1turno_path)
dfg2 = pd.read_excel(grafico_zonas_path)

df = pd.read_excel(df_path)
df_turno1_coordenadas = pd.read_excel(turno_1_coordenadas_path)
df_turno2_coordenadas = pd.read_excel(turno_2_coordenadas_path)
df_turno3_coordenadas = pd.read_excel(turno_3_coordenadas_path)
df_comercial_coordenadas = pd.read_excel(turno_comercial_coordenadas_path)

# 1 TURNO 

turno1 = df["TURNO"] == "1° TURNO"

filtered_df_turno1 = df[turno1]
qtd_pessoas_turno1 = str(len(filtered_df_turno1))

loc_data_1_turno = {
    "longitude": df_turno1_coordenadas['LONGITUDE'],
    "latitude": df_turno1_coordenadas['LATITUDE'],
    'color': ['#F96507','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404','#EF0404']
}

map_df_1_turno = pd.DataFrame.from_dict(loc_data_1_turno)

# 2 TURNO 

turno2 = df["TURNO"] == "2° TURNO"

filtered_df_turno2 = df[turno2]
qtd_pessoas_turno2 = str(len(filtered_df_turno2))

loc_data_2_turno = {
    "longitude": df_turno2_coordenadas['LONGITUDE'],
    "latitude": df_turno2_coordenadas['LATITUDE'],
    'color': ['#F96507','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D','#77055D']
}

map_df_2_turno = pd.DataFrame.from_dict(loc_data_2_turno)

# 3 TURNO 

turno3 = df["TURNO"] == "3° TURNO"

filtered_df_turno3 = df[turno3]
qtd_pessoas_turno3 = str(len(filtered_df_turno3))

loc_data_3_turno = {
    "longitude": df_turno3_coordenadas['LONGITUDE'],
    "latitude": df_turno3_coordenadas['LATITUDE'],
    'color': ['#F96507','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612','#50D612']
}

map_df_3_turno = pd.DataFrame.from_dict(loc_data_3_turno)

# COMERCIAL

turnoC = df["TURNO"] == "COMERCIAL"

filtered_df_turnoC = df[turnoC]
qtd_pessoas_turnoC = str(len(filtered_df_turnoC))

loc_data_C_turno = {
    "longitude": df_comercial_coordenadas['LONGITUDE'],
    "latitude": df_comercial_coordenadas['LATITUDE'],
    'color': ['#F96507','#1220D6','#1220D6','#1220D6','#1220D6','#1220D6','#1220D6','#1220D6','#1220D6','#1220D6','#1220D6','#1220D6','#1220D6','#1220D6','#1220D6','#1220D6']
}

map_df_C_turno = pd.DataFrame.from_dict(loc_data_C_turno)

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

st.subheader('Quantidade de funcionários nos turno 1,2,3 e comercial')

st.dataframe(df2,hide_index=True,width=3000)

st.bar_chart(dfg1,x='Turno',y='Funcionários')

st.subheader('Quantidade de funcionários nas zonas Leste, Norte, Oeste e Sul')
st.dataframe(df3,hide_index=True,width=3000)

st.bar_chart(dfg2,x='Zona',y='Funcionários')

st.subheader('Mapa dos funcionários do primeiro turno')

color = st.color_picker('Cor Adata Eletonics', '#F96507',key='0')
color2 = st.color_picker('Cor dos funcionários', '#EF0404',key='1')

st.map(map_df_1_turno, size=20, color='color')

st.subheader('Mapa dos funcionários do segundo turno')

color = st.color_picker('Cor Adata Eletonics', '#F96507',key='2')
color2 = st.color_picker('Cor dos funcionários', '#77055D',key='3')

st.map(map_df_2_turno, size=20, color='color')

st.subheader('Mapa dos funcionários do terceiro turno')

color = st.color_picker('Cor Adata Eletonics', '#F96507',key='4')
color2 = st.color_picker('Cor dos funcionários', '#50D612',key='5')

st.map(map_df_3_turno, size=20, color='color')

st.subheader('Mapa dos funcionários do turno comercial')

color = st.color_picker('Cor Adata Eletonics', '#F96507',key='6')
color2 = st.color_picker('Cor dos funcionários', '#1220D6',key='7')

st.map(map_df_C_turno, size=20, color='color')

#st.subheader(len(filtered_df_turno1))

#st.dataframe(df) 
