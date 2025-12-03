import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Carregar modelo
modelo = pickle.load(open("modelo_final.pkl", "rb"))

st.set_page_config(page_title="Previsão de Doença Cardíaca", layout="centered")

st.title("🫀 Detecção de Doença Cardíaca com IA")
st.write("Preencha os dados abaixo para realizar a predição:")

# Campos de entrada
age = st.number_input("Idade", min_value=1, max_value=120)
sex = st.selectbox("Sexo", ["Masculino", "Feminino"])
cp = st.selectbox("Tipo de Dor no Peito (cp)", [0,1,2,3])
trestbps = st.number_input("Pressão arterial em repouso")
chol = st.number_input("Colesterol")
fbs = st.selectbox("Açúcar no sangue > 120 mg/dl", [0,1])
restecg = st.selectbox("Eletrocardiograma (restecg)", [0,1,2])
thalach = st.number_input("Frequência cardíaca máxima")
exang = st.selectbox("Angina induzida por exercício", [0,1])
oldpeak = st.number_input("Oldpeak")
slope = st.selectbox("Inclinação do pico do exercício", [0,1,2])
ca = st.selectbox("Número de vasos principais", [0,1,2,3,4])
thal = st.selectbox("Thal", [0,1,2,3])

# Converter sexo
sex = 1 if sex == "Masculino" else 0

# Botão de previsão
if st.button("🔍 Realizar Previsão"):

    entrada = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach,
                          exang, oldpeak, slope, ca, thal]])

    resultado = modelo.predict(entrada)[0]

    if resultado == 1:
        st.error("⚠️ Risco de Doença Cardíaca Detectado")
    else:
        st.success("✅ Baixo risco de Doença Cardíaca")
