import streamlit as st
import pandas as pd

dataframe = pd.read_csv("./data/tracks.csv")

st.title("Meu Dashboard com Streamlit🍳")
st.subheader("Dados Brutos:")
st.dataframe(dataframe)
st.caption("Dados das Músicas")

#Prepara um filtro para os dados
colunas_selecionadas = st.multiselect(
    "Selecione as colunas para exibição:",
    dataframe.columns
)
print(dataframe['duration_ms'])
duracao_selecionada = st.slider(
    "Filtro de Ano de Lançamento",
    0,# dataframe.duration_ms.min()[0],
    100# dataframe.duration_ms.max()[0]
)
df_filtrado = dataframe[colunas_selecionadas]
if duracao_selecionada != None:
    df_filtrado = df_filtrado.query("duration_ms >= @duracao_selecionada")
st.dataframe(df_filtrado)
st.caption("Conjunto de dados Filtrados")
