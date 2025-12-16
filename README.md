# 🫀 Predição de Doenças Cardíacas – Seleção e Deploy de Modelo com Árvore de Decisão

Este projeto demonstra o processo completo de criação, avaliação e deploy de um modelo de Machine Learning, utilizando um dataset real de doenças cardíacas. O foco principal do projeto é o uso de uma Árvore de Decisão, desde a análise inicial no Google Colab até o deploy da aplicação utilizando Streamlit.

## 📊 Dataset

O dataset utilizado foi obtido no Kaggle:

Heart Disease Dataset
https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset

O conjunto de dados contém informações clínicas de pacientes, como idade, sexo, pressão arterial, colesterol, frequência cardíaca, entre outras variáveis, com o objetivo de prever a presença ou ausência de doença cardíaca.

## 🧠 Tecnologias Utilizadas

- Python 3
- Pandas
- NumPy
- Scikit-learn
- Google Colab
- Streamlit
- Pickle (.pkl)

## 🔁 Etapas do Projeto

### 1) Download e Preparação do Dataset

- O dataset foi baixado diretamente do Kaggle.
- O treinamento foi realizado no ambiente do Google Colab.
- Os dados foram carregados utilizando Pandas.
- Foi realizada análise exploratória, verificação de valores ausentes e separação entre variáveis de entrada (features) e variável alvo (target).

### 2) Treinamento dos Modelos

Foram treinados dois modelos de Machine Learning para comparação de desempenho.

Regressão Logística:
- Utilizada como modelo base.
- Adequada para problemas de classificação binária.
- Serviu como referência inicial de desempenho.

Árvore de Decisão:
- Modelo capaz de capturar relações não lineares.
- Possui boa interpretabilidade.
- Apresentou melhor desempenho nos testes realizados.

### 3) Avaliação dos Resultados

Os modelos foram avaliados com métricas de classificação, como:
- Acurácia
- Comparação direta entre os modelos

Resultado:
O modelo de Árvore de Decisão apresentou melhor desempenho em relação à Regressão Logística e foi escolhido como modelo final do projeto.

### 4) Exportação do Modelo

Após a definição do modelo mais eficaz, ele foi exportado utilizando a biblioteca Pickle, permitindo seu reaproveitamento sem necessidade de novo treinamento.

Exemplo:
with open("modelo_final.pkl", "wb") as f:
    pickle.dump(modelo_arvore, f)

Arquivo gerado:
- modelo_final.pkl

## 🚀 Deploy do Modelo

### 5) Criação da Aplicação (app.py)

Foi desenvolvido um pequeno script em Python responsável pelo deploy do modelo treinado, utilizando Streamlit.

A aplicação realiza:
- Carregamento do modelo salvo (modelo_final.pkl)
- Coleta dos dados de entrada via interface gráfica
- Execução da predição
- Exibição do resultado ao usuário

### 6) Executando a Aplicação Localmente

Instalação das dependências:
pip install streamlit scikit-learn pandas numpy

Execução:
streamlit run app.py

## 🌐 Deploy com Streamlit Cloud

Para disponibilizar a aplicação online, foi utilizado o Streamlit Community Cloud.

Passo a passo:
1. Subir o projeto para um repositório no GitHub contendo:
   - app.py
   - modelo_final.pkl
   - requirements.txt
   - README.txt

2. Acessar:
https://streamlit.io/cloud

3. Conectar a conta do GitHub.

4. Selecionar o repositório e o arquivo app.py.

5. Clicar em Deploy.

O Streamlit irá:
- Instalar automaticamente as dependências
- Executar a aplicação
- Gerar um link público para acesso

## 📁 Estrutura do Projeto

app.py
modelo_final.pkl
requirements.txt
README.txt

## ✅ Conclusão

Este projeto apresenta um pipeline completo de Machine Learning, abrangendo:
- Análise e preparação de dados
- Treinamento e comparação de modelos
- Seleção do modelo mais eficaz
- Persistência do modelo treinado
- Deploy de uma aplicação web para inferência

O projeto demonstra, de forma prática, como transformar um modelo de Machine Learning em uma aplicação acessível ao usuário final.
