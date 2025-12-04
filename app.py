import streamlit as st
import pickle
import numpy as np

# ========================
# CARREGAR MODELO
# ========================
modelo = pickle.load(open("modelo_final.pkl", "rb"))

# ========================
# CONFIGURAÇÃO DA PÁGINA
# ========================
st.set_page_config(page_title="Previsão de Doença Cardíaca", layout="centered")
st.title("Detecção de Doença Cardíaca com IA")
st.write("Preencha os dados abaixo para realizar a predição:")

# ========================
# CAMPOS DE ENTRADA
# ========================

age = st.number_input("Idade", min_value=1, max_value=120)

sex = st.selectbox("Sexo", ["Masculino", "Feminino"])
sex_valor = 1 if sex == "Masculino" else 0


# ---------- DOR NO PEITO ----------
cp_opcoes = {
    0: "Angina típica",
    1: "Angina atípica",
    2: "Dor não-anginosa",
    3: "Assintomático"
}

cp = st.selectbox(
    "Tipo de Dor no Peito",
    options=list(cp_opcoes.keys()),
    format_func=lambda x: cp_opcoes[x]
)


trestbps = st.number_input("Pressão arterial em repouso (mmHg)", min_value=50, max_value=250)

chol = st.number_input("Colesterol (mg/dL)", min_value=50, max_value=600)


# ---------- GLICOSE ----------
fbs_opcoes = {
    0: "Normal (≤ 120 mg/dl)",
    1: "Alto (> 120 mg/dl)"
}

fbs = st.selectbox(
    "Açúcar no sangue em jejum",
    options=list(fbs_opcoes.keys()),
    format_func=lambda x: fbs_opcoes[x]
)


# ---------- ECG ----------
restecg_opcoes = {
    0: "Normal",
    1: "Anormalidade ST-T",
    2: "Coração aumentado"
}

restecg = st.selectbox(
    "Resultado do eletrocardiograma",
    options=list(restecg_opcoes.keys()),
    format_func=lambda x: restecg_opcoes[x]
)


thalach = st.number_input("Frequência cardíaca máxima (bpm)", min_value=60, max_value=250)


# ---------- ANGINA ----------
exang_opcoes = {
    0: "Não",
    1: "Sim"
}

exang = st.selectbox(
    "Angina induzida por exercício",
    options=list(exang_opcoes.keys()),
    format_func=lambda x: exang_opcoes[x]
)


oldpeak = st.number_input("Oldpeak (depressão ST)", min_value=0.0, max_value=10.0)


# ---------- INCLINAÇÃO ----------
slope_opcoes = {
    0: "Descendente",
    1: "Plana",
    2: "Ascendente"
}

slope = st.selectbox(
    "Inclinação ST",
    options=list(slope_opcoes.keys()),
    format_func=lambda x: slope_opcoes[x]
)


# ---------- VASOS ----------
ca_opcoes = {
    0: "0 vasos",
    1: "1 vaso",
    2: "2 vasos",
    3: "3 vasos",
    4: "4 vasos"
}

ca = st.selectbox(
    "Número de vasos comprometidos",
    options=list(ca_opcoes.keys()),
    format_func=lambda x: ca_opcoes[x]
)


# ---------- TÁLIO ----------
thal_opcoes = {
    0: "Normal",
    1: "Defeito fixo",
    2: "Normal (outra leitura)",
    3: "Defeito reversível"
}

thal = st.selectbox(
    "Resultado do teste de tálio",
    options=list(thal_opcoes.keys()),
    format_func=lambda x: thal_opcoes[x]
)


# ========================
# PREVISÃO
# ========================

if st.button("🔍 Realizar Previsão"):
    entrada = np.array([[age, sex_valor, cp,
                          trestbps, chol, fbs,
                          restecg, thalach, exang,
                          oldpeak, slope, ca, thal]])

    resultado = modelo.predict(entrada)[0]

    if resultado == 1:
        st.error("⚠️ Risco de Doença Cardíaca Detectado")
    else:
        st.success("✅ Baixo risco de Doença Cardíaca")
