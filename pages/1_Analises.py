import streamlit as st



st.title("📊 Análises do Projeto")

st.markdown("""
Nesta página estão os principais resultados obtidos durante o treinamento do modelo.
""")

st.header("Feature Importance")

st.image(
    "assets/feature_importance.jpeg",
    use_container_width=True
)

st.header("Heatmap de Correlação")

st.image(
    "assets/churn_heatmap.jpeg",
    use_container_width=True
)

st.header("Churn por Tempo de Cliente")

st.image(
    "assets/churn_by_tenure.jpeg",
    use_container_width=True
)