import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Carregar modelo
modelo = pickle.load(open("modelo_final.pkl", "rb"))

st.set_page_config(page_title="Previsão de Doença Cardíaca", layout="centered")

st.title("Detecção de Doença Cardíaca com IA")
st.write("Preenchas os dados abaixo para realizar a predição:")

# Campos de entrada com explicações

age = st.number_input(
    "Idade",
    min_value=1,
    max_value=120,
    help="Informe a idade do paciente em anos."
)

sex = st.selectbox(
    "Sexo",
    ["Masculino", "Feminino"],
    help="Selecione o sexo biológico do paciente."
)

cp = st.selectbox(
    "Tipo de Dor no Peito (cp)",
    [0, 1, 2, 3],
    help="0 = Angina típica | 1 = Angina atípica | 2 = Dor não-anginosa | 3 = Assintomático"
)

trestbps = st.number_input(
    "Pressão arterial em repouso (mmHg)",
    help="Pressão sistólica do paciente em repouso. Ex: 120."
)

chol = st.number_input(
    "Colesterol (mg/dL)",
    help="Valor do colesterol total no sangue. Normal até 200."
)

fbs = st.selectbox(
    "Açúcar no sangue em jejum > 120 mg/dl",
    [0, 1],
    help="0 = Não | 1 = Sim (nível alto de glicose)"
)

restecg = st.selectbox(
    "Resultado do eletrocardiograma (restecg)",
    [0, 1, 2],
    help="0 = Normal | 1 = Anormalidade ST-T | 2 = Coração aumentado"
)

thalach = st.number_input(
    "Frequência cardíaca máxima (bpm)",
    help="Batimentos por minuto atingidos no esforço. Ex: 150."
)

exang = st.selectbox(
    "Angina induzida por exercício",
    [0, 1],
    help="0 = Não | 1 = Sim (dor no peito durante esforço)"
)

oldpeak = st.number_input(
    "Oldpeak (depressão do ST)",
    help="Queda no segmento ST do ECG durante esforço. Valores elevados indicam risco."
)

slope = st.selectbox(
    "Inclinação do segmento ST",
    [0, 1, 2],
    help="0 = Descendente | 1 = Plana | 2 = Ascendente (normal)"
)

ca = st.selectbox(
    "Número de vasos principais comprometidos",
    [0, 1, 2, 3, 4],
    help="Quantidade de vasos coronários obstruídos detectados"
)

thal = st.selectbox(
    "Teste de Tálio (thal)",
    [0, 1, 2, 3],
    help="0 = Normal | 1 = Defeito fixo | 2 = Normal | 3 = Defeito reversível"
)

# Converter sexo
sex = 1 if sex == "Masculino" else 0

# Botão de previsão
if st.button("🔍 Realizar Previsão"):

    entrada = np.array([[age, sex, cp, trestbps, chol, fbs,
                          restecg, thalach, exang, oldpeak,
                          slope, ca, thal]])

    resultado = modelo.predict(entrada)[0]

    if resultado == 1:
        st.error("⚠️ Risco de Doença Cardíaca Detectado")
    else:
        st.success("✅ Baixo risco de Doença Cardíaca")

