import streamlit as st
import pandas as pd
import joblib



@st.cache_resource
def load_model():
    return joblib.load("models/modelo_churn.pkl")

model = load_model()

st.title("📊 Previsão de Churn de Clientes")
st.markdown("Sistema de previsão de cancelamento de clientes utilizando Machine Learning.")

st.header("👤 Dados do Cliente")

col1, col2, col3 = st.columns(3)

with col1:
    gender = st.selectbox("Gênero", ["Masculino", "Feminino"])
    senior = st.selectbox("Idoso", ["Sim", "Não"])
    partner = st.selectbox("Possui Parceiro", ["Sim", "Não"])
    dependents = st.selectbox("Possui Dependentes", ["Sim", "Não"])

with col2:
    tenure = st.slider("Tempo como Cliente (Meses)", 0, 72, 12)
    contract = st.selectbox(
        "Contrato",
        ["Mensal", "Um ano", "Dois anos"]
    )
    paperless = st.selectbox(
        "Fatura Digital",
        ["Sim", "Não"]
    )

with col3:
    monthly = st.number_input(
        "Cobrança Mensal",
        min_value=0.0,
        value=70.0
    )
    total = st.number_input(
        "Cobrança Total",
        min_value=0.0,
        value=1000.0
    )

st.header("📡 Serviços")

c1, c2 = st.columns(2)

with c1:
    phone = st.selectbox("Serviço de Telefone", ["Sim", "Não"])
    multiple = st.selectbox(
        "Múltiplas Linhas",
        ["Sim", "Não", "Sem serviço de telefone"]
    )
    internet = st.selectbox(
        "Serviço de Internet",
        ["DSL", "Fibra óptica", "Não"]
    )
    security = st.selectbox(
        "Segurança Online",
        ["Sim", "Não", "Sem serviço de internet"]
    )

with c2:
    backup = st.selectbox(
        "Backup Online",
        ["Sim", "Não", "Sem serviço de internet"]
    )
    protection = st.selectbox(
        "Proteção de Dispositivo",
        ["Sim", "Não", "Sem serviço de internet"]
    )
    support = st.selectbox(
        "Suporte Técnico",
        ["Sim", "Não", "Sem serviço de internet"]
    )
    tv = st.selectbox(
        "Streaming de TV",
        ["Sim", "Não", "Sem serviço de internet"]
    )

movies = st.selectbox(
    "Streaming de Filmes",
    ["Sim", "Não", "Sem serviço de internet"]
)

payment = st.selectbox(
    "Método de Pagamento",
    [
        "Cheque Eletrônico",
        "Cheque por Correio",
        "Transferência Bancária (automática)",
        "Cartão de Crédito (automático)"
    ]
)

if st.button("🔍 Analisar Cliente"):

    map_yes_no = {"Sim": "Yes", "Não": "No"}
    map_gender = {"Masculino": "Male", "Feminino": "Female"}
    map_contract = {"Mensal": "Month-to-month", "Um ano": "One year", "Dois anos": "Two year"}
    map_multiple = {"Sim": "Yes", "Não": "No", "Sem serviço de telefone": "No phone service"}
    map_internet = {"DSL": "DSL", "Fibra óptica": "Fiber optic", "Não": "No"}
    map_service = {"Sim": "Yes", "Não": "No", "Sem serviço de internet": "No internet service"}
    map_payment = {
        "Cheque Eletrônico": "Electronic check",
        "Cheque por Correio": "Mailed check",
        "Transferência Bancária (automática)": "Bank transfer (automatic)",
        "Cartão de Crédito (automático)": "Credit card (automatic)"
    }

    senior_val = 1 if senior == "Sim" else 0
    high_risk_val = 1 if (tenure <= 12 and monthly > 70.35) else 0

    cliente = pd.DataFrame([{
        'gender': map_gender[gender],
        'SeniorCitizen': senior_val,
        'Partner': map_yes_no[partner],
        'Dependents': map_yes_no[dependents],
        'PhoneService': map_yes_no[phone],
        'PaperlessBilling': map_yes_no[paperless],
        'MultipleLines': map_multiple[multiple],
        'InternetService': map_internet[internet],
        'OnlineSecurity': map_service[security],
        'OnlineBackup': map_service[backup],
        'DeviceProtection': map_service[protection],
        'TechSupport': map_service[support],
        'StreamingTV': map_service[tv],
        'StreamingMovies': map_service[movies],
        'Contract': map_contract[contract],
        'PaymentMethod': map_payment[payment],
        'tenure': tenure,
        'MonthlyCharges': monthly,
        'TotalCharges': total,
        'high_risk_profile': high_risk_val
    }])

    pred = model.predict(cliente)[0]
    prob = model.predict_proba(cliente)[0][1]

    st.divider()

    st.subheader("Resultado")

    st.progress(float(prob))

    if pred == 1:
        st.error(
            f"⚠️ Alta chance de cancelamento ({prob:.2%})"
        )
    else:
        st.success(
            f"✅ Cliente com boa chance de permanência ({1-prob:.2%})"
        )