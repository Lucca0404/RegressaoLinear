# 🎧 README.md: Análise de Características de Áudio do Spotify

## 🔎 Visão Geral do Projeto

Este projeto utiliza técnicas de Regressão e Classificação por Machine Learning (ML) para analisar a relação entre as características técnicas de áudio fornecidas pela API do Spotify (como Energia, Dancabilidade e Volume) e as propriedades musicais (Gênero e Loudness).

O objetivo principal foi validar diversas hipóteses estatísticas e preditivas sobre o comportamento do áudio em larga escala, culminando na otimização de um classificador de gênero.

### 🛠️ Tecnologias Utilizadas

| Categoria | Ferramenta | Uso Principal |
| :--- | :--- | :--- |
| **Linguagem** | Python 3.x | Desenvolvimento e execução. |
| **Análise de Dados** | Pandas, NumPy | Manipulação, limpeza e preparação de dados. |
| **Estatística/Regressão** | `statsmodels` | Relatórios acadêmicos e validação estatística (P-valor, R²). |
| **Machine Learning** | `scikit-learn` | Regressão Logística, Naive Bayes, Random Forest e Pipelines. |
| **Otimização** | `scikit-learn` | `RandomizedSearchCV` para ajuste de hiperparâmetros. |
| **Visualização** | Matplotlib, Seaborn | Gráficos e Matriz de Confusão. |

---

## 🚀 Módulo 1: Regressão e Validação de Hipóteses (H1 a H3)

### 📈 Resumo dos Resultados

| Hipótese | Modelo | Veredito | Descoberta Principal |
| :--- | :--- | :--- | :--- |
| **H1: Energia vs Volume** | Regressão Linear Simples | **Validada Forte** (R² ≈ 0.58) | A Energia é o maior preditor do Volume (`Loudness`). |
| **H2: Fatores vs Dancabilidade** | Regressão Linear Múltipla | **Validada Moderada** (R² ≈ 0.24) | A **Valência** (felicidade) é o fator que mais impulsiona a Dancabilidade. |
| **H3: BPM vs Dancabilidade** | Regressão Polinomial | **Validada** (R² ≈ 0.10) | A relação é uma **curva** (U Invertido), provando uma zona ideal de tempo para dançar (aprox. 120-130 BPM). |

---

## 🎧 Módulo 2: Classificação e Distinção de Gêneros (H4 e H5)

| Hipótese | Modelo | Resultado | Descoberta Principal |
| :--- | :--- | :--- | :--- |
| **H4: Prever Gênero** | Naive Bayes | Acurácia CV: **0.1764** | O modelo é fraco, mas **extremamente estável** (DP baixo), confirmando que a tarefa multiclasse é complexa. |
| **H5: Pop vs Rock** | Regressão Logística | Acurácia: **0.7325** | **Alta Distinção:** O modelo separa Pop (Dancabilidade alta) de Rock (Valência/Energia mais baixa) com sucesso. |

---

## ⚙️ Módulo 3: Otimização e Validação do Modelo (Fase 5)

A Classificação Multiclasse (H4), sendo o problema mais complexo, foi escolhida para a fase de otimização.

### 5.1 Validação Cruzada (Cross-Validation)

* **Modelo Base:** Naive Bayes
* **Acurácia Média (5 Folds):** **0.1764**
* **Desvio Padrão (Estabilidade):** **0.0053**
* **Conclusão:** A baixa variação entre os *folds* confirma que o modelo é estável, mas o baixo *score* exige um algoritmo mais poderoso.

### 5.2 Otimização de Hiperparâmetros (Random Search)

O **RandomizedSearchCV** foi aplicado ao **Random Forest Classifier** para encontrar o melhor desempenho em um tempo de execução limitado (trade-off Tempo vs. Acurácia).

| Parâmetro | Tipo de Otimização | Valores Testados |
| :--- | :--- | :--- |
| `n_estimators` | Aleatória (randint) | 50 a 250 |
| `max_depth` | Aleatória (randint) | 10 a 40 |
| `min_samples_leaf` | Aleatória (randint) | 1 a 10 |
| **Iterações** | `n_iter=10` | 10 combinações |

#### 🏆 Resultados do Random Forest Otimizado

| Métrica | Valor | Trade-off / Conclusão |
| :--- | :--- | :--- |
| **Melhor Acurácia CV Média** | **[INSERIR VALOR AQUI]** | (Média dos 3 Folds, valor mais importante do Random Search). |
| **Melhores Parâmetros** | **[INSERIR DICIONÁRIO AQUI]** | (Ex: `{'n_estimators': 180, 'max_depth': 25, 'min_samples_leaf': 1}`). |
| **Acurácia Final no Dataset** | **[INSERIR VALOR AQUI]** | (Deve ser o valor mais alto, indicando o pico de desempenho). |

---

### 📂 Como Executar o Projeto

1.  **Carregar os Dados:** Faça o upload do arquivo `dataset_limpo.csv` para o seu ambiente (Ex: Google Colab).
2.  **Execute o Notebook:** O código está organizado em células sequenciais que replicam as fases de limpeza, regressão e classificação/otimização.
