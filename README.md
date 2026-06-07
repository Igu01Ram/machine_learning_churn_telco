# Previsão de Churn em Telecomunicações

## Integrantes e RAs
* Allan - 1986140  
* Leonardo Balbo - 2009203
* Igor - 1992632

## Descrição do Problema
O custo de aquisição de novos clientes é significativamente maior do que o custo de retenção. Dessa forma, a previsão de churn (cancelamento de serviços) torna-se um desafio estratégico fundamental para empresas de telecomunicações, a fim de atuar proativamente na retenção de usuários com alta probabilidade de evasão.

## Objetivo do Projeto
Desenvolver um modelo de classificação em Machine Learning capaz de prever o churn de clientes, com base em suas características contratuais, comportamentais, demográficas e financeiras.

## Dataset Utilizado e Obtenção dos Dados
O dataset utilizado é o **Telco Customer Churn** (`blastchar/telco-customer-churn`), originalmente disponibilizado no Kaggle.

**Como obter/gerar os dados:** 
Os dados são baixados automaticamente na primeira execução do notebook utilizando a biblioteca `kagglehub`. O comando responsável por essa etapa é:
```python
import kagglehub
path = kagglehub.dataset_download("blastchar/telco-customer-churn")
```
Alternativamente, o arquivo de dados local encontra-se mapeado na pasta do projeto em `data/dataset.csv`.

## Tipo de Problema de Machine Learning
Classificação Binária (prever se o cliente irá cancelar o serviço: Sim ou Não).

## Metodologia
1. **Análise Exploratória de Dados (EDA):** Análise da taxa de churn por grupos de tempo de contrato (tenure) e verificação das distribuições das variáveis.
2. **Pré-processamento:** Tratamento de valores nulos (ex: `TotalCharges`), padronização de variáveis numéricas (`StandardScaler`) e codificação de variáveis categóricas (`OneHotEncoder`).
3. **Balanceamento de Classes:** Utilização do algoritmo **SMOTE** para balancear a variável alvo (Churn) nos dados de treinamento, contornando a desproporção entre classes.
4. **Validação e Treinamento:** Utilização de validação cruzada estratificada (`StratifiedKFold` com 5 splits) e um `Pipeline` integrando o pré-processamento, balanceamento e classificação.

## Modelos Treinados
* Logistic Regression (Regressão Logística)
* Random Forest (Floresta Aleatória)
* Gradient Boosting

## Modelo Final Escolhido
O modelo final escolhido e exportado (salvo em `models/modelo_churn.pkl`) foi o **Gradient Boosting**, que apresentou o melhor conjunto de métricas e consistência para capturar os padrões de cancelamento em relação aos demais.

## Métricas de Avaliação
Os modelos foram validados e comparados com base nas seguintes métricas:
* Acurácia
* Precisão
* Recall (Sensibilidade)
* F1-Score
* AUC-ROC

## Principais Resultados
O modelo **Gradient Boosting** apresentou o seguinte desempenho médio na validação cruzada:
* **Acurácia:** ~78.6%
* **AUC-ROC:** ~0.848
* **Recall:** ~67.3%
* **F1-Score:** ~62.6%

A análise demonstrou que características contratuais e financeiras — como o tempo de contrato, valores de cobrança e certos tipos de serviços de internet — possuem forte influência na decisão de cancelamento.

## Estrutura dos Arquivos
```text
projeto_p2/
│
├── app.py                            # Arquivo principal do Streamlit (Roteador Multipage)
├── requirements.txt                  # Lista de dependências do projeto
├── README.md                         # Documentação do projeto
├── retrain.py                        # Script para re-treinamento do modelo
│
├── models/
│   └── modelo_churn.pkl              # Modelo treinado serializado (Gradient Boosting)
│
├── data/
│   └── dataset.csv                   # Base de dados estática em formato CSV
│
├── notebooks/
│   └── Trabalho_Telecom_Chrun.ipynb  # Notebook Jupyter com análise, EDA e modelagem
│
├── assets/                           # Imagens dos gráficos gerados (.jpeg)
│
├── pages/                            # Páginas da aplicação Streamlit
│   ├── 0_Inicio.py                   # Simulador de previsão de Churn (App)
│   ├── 1_Analises.py                 # Gráficos de feature importance, heatmap, etc.
│   └── 2_Sobre_o_Projeto.py          # Objetivo e resumo das metodologias
│
└── reports/                          # Relatórios gerados pelo projeto
```

## Tecnologias Utilizadas
* **Linguagem:** Python
* **Manipulação de Dados e Análise:** Pandas, Numpy
* **Machine Learning:** Scikit-learn, Imbalanced-learn (SMOTE)
* **Visualização:** Matplotlib, Seaborn
* **Web App:** Streamlit

## Instruções para Executar o Notebook
1. Certifique-se de ter o Python instalado.
2. Instale as dependências executando na linha de comando:
   ```bash
   pip install -r requirements.txt
   ```
   *(Caso não tenha instalado, instale também o pacote do Jupyter e kagglehub: `pip install jupyter kagglehub`)*
3. Inicie o Jupyter Notebook:
   ```bash
   jupyter notebook notebooks/Trabalho_Telecom_Chrun.ipynb
   ```
4. Execute as células de forma sequencial. Os dados serão obtidos e carregados automaticamente no ambiente local via `kagglehub`.

## Instruções para Executar o App Streamlit
1. Instale as bibliotecas necessárias listadas em `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
2. Inicie a aplicação via Streamlit com o seguinte comando:
   ```bash
   streamlit run app.py
   ```
3. Em caso de erro utilize os seguintes comandos:
  ```bash
      pip install --upgrade streamlit (Para que o streamlit esteja sempre na ultima versão)
    ```
      ```bash
    python -m pip install imbalanced-learn(aqui é pra baixar a biblioteca imbalanced)
    ```
   ```bash
    python -m streamlit run app.py (para rodar o projeto)
    ```
3. O aplicativo estará disponível localmente, e abrirá automaticamente no seu navegador padrão pelo endereço `http://localhost:8501`.

## Link do App Publicado


## Limitações
* O modelo é baseado em um cenário estático e não incorpora mudanças recentes no comportamento do consumidor (concept drift).
* O uso de SMOTE introduz exemplos sintéticos que beneficiam o treinamento, mas que não representam necessariamente indivíduos reais do cenário de negócios.
* O dataset não cobre variáveis textuais, demográficas profundas ou de interações em mídias sociais que poderiam aprimorar a previsibilidade do churn.
