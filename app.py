import streamlit as st
import pickle
import numpy as np

modelo = pickle.load(open("modelo_final.pkl", "rb"))

st.set_page_config(page_title="Previsão de Doença Cardíaca", layout="centered")
st.title("Detecção de Doença Cardíaca com IA")
st.write("Preencha os dados abaixo para realizar a predição:")

age = st.number_input("Idade", min_value=1, max_value=120)

sex = st.selectbox(
    "Sexo",
    ["Masculino", "Feminino"]
)
sex_valor = 1 if sex == "Masculino" else 0

cp = st.selectbox(
    "Tipo de Dor no Peito",
    {
        "Angina típica": 0,
        "Angina atípica": 1,
        "Dor não-anginosa": 2,
        "Assintomático": 3
    }
)

trestbps = st.number_input("Pressão arterial em repouso (mmHg)")

chol = st.number_input("Colesterol (mg/dL)")

fbs = st.selectbox(
    "Açúcar no sangue em jejum",
    {
        "Normal (≤ 120 mg/dl)": 0,
        "Alto (> 120 mg/dl)": 1
    }
)

restecg = st.selectbox(
    "Eletrocardiograma em repouso",
    {
        "Normal": 0,
        "Anormalidade ST-T": 1,
        "Coração aumentado": 2
    }
)

thalach = st.number_input("Frequência cardíaca máxima (bpm)")

exang = st.selectbox(
    "Angina induzida por exercício",
    {
        "Não": 0,
        "Sim": 1
    }
)

oldpeak = st.number_input("Oldpeak (depressão ST)")

slope = st.selectbox(
    "Inclinação ST",
    {
        "Descendente": 0,
        "Plana": 1,
        "Ascendente": 2
    }
)

ca = st.selectbox(
    "Número de vasos com obstrução",
    {
        "0 vasos": 0,
        "1 vaso": 1,
        "2 vasos": 2,
        "3 vasos": 3,
        "4 vasos": 4
    }
)

thal = st.selectbox(
    "Resultado do teste de tálio",
    {
        "Normal": 0,
        "Defeito fixo": 1,
        "Normal (segundo tipo)": 2,
        "Defeito reversível": 3
    }
)

if st.button("🔍 Realizar Previsão"):
    entrada = np.array([[age, sex_valor, cp, trestbps, chol, fbs,
                          restecg, thalach, exang, oldpeak,
                          slope, ca, thal]])

    resultado = modelo.predict(entrada)[0]

    if resultado == 1:
        st.error("⚠️ Risco de Doença Cardíaca Detectado")
    else:
        st.success("✅ Baixo risco de Doença Cardíaca")
