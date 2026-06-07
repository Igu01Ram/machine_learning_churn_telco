import streamlit as st



st.title("📖 Sobre o Projeto")

st.markdown("""
## Objetivo

O objetivo deste projeto é prever a probabilidade de cancelamento (Churn) de clientes de uma empresa de telecomunicações utilizando técnicas de Machine Learning.

---

## Dataset

Foi utilizado o conjunto de dados:

**Telco Customer Churn**

O dataset contém informações sobre:

- Perfil do cliente
- Serviços contratados
- Tipo de contrato
- Forma de pagamento
- Tempo de permanência
- Custos mensais e totais

---

## Modelos Avaliados

Foram avaliados:

- Logistic Regression
- Random Forest
- Gradient Boosting

---

## Técnicas Utilizadas

- Pipeline
- One Hot Encoding
- Ordinal Encoding
- MinMaxScaler
- SMOTE
- Validação Cruzada
- AUC-ROC
- F1-Score

---

## Resultado

O melhor modelo foi selecionado com base em:

- Recall
- F1-Score
- AUC-ROC

e posteriormente utilizado para gerar as previsões disponibilizadas neste sistema.
""")