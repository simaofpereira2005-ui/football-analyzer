# 🏆 World Cup 2026 Predictor (Data Science & Poisson Distribution)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)]https://football-analyzer-ifpkpaveeawzuyfpa4hpyf.streamlit.app/

Este é um projeto *Full-Stack* de Engenharia de Dados e Machine Learning (Estatística Clássica) que prevê resultados de jogos de futebol do Mundial de 2026. A aplicação extrai dados reais em tempo real, processa-os numa base de dados SQL, e utiliza a **Distribuição de Poisson** para calcular o *Expected Goals* (xG) e as probabilidades de Vitória, Empate e Derrota.

---

## ✨ Funcionalidades Principais

* **Extração de Dados (ETL):** Integração com a API `football-data.org` para extrair resultados atualizados do Mundial de 2026.
* **Armazenamento Robusto:** Arquitetura de base de dados relacional usando `SQLite3` para guardar e agregar estatísticas de golos (Casa/Fora).
* **Motor Matemático Predito:** Cálculo dinâmico das Forças de Ataque e Defesa de cada seleção para gerar a variável $\lambda$ (Lambda/xG).
* **Algoritmo de Probabilidades:** Aplicação da Fórmula de Poisson numa matriz cruzada (0-5 golos) para calcular percentagens exatas de resultados.
* **Sugestões de Aposta:** Lógica de negócio integrada para sugerir apostas de valor (ex: *Over/Under 2.5*, *Draw No Bet*) baseadas em limites de risco estatístico.
* **Interface Web Interativa:** *Dashboard* visual construído inteiramente em Python com a framework `Streamlit`.

---

## 🛠️ Stack Tecnológica

* **Linguagem:** Python 3
* **Front-End / UI:** Streamlit
* **Base de Dados:** SQLite3 (Nativa do Python)
* **API / Rede:** `requests`
* **Segurança de Variáveis:** `python-dotenv`
* **Matemática:** Módulo `math` (Standard Library)

---

## 🚀 Como Correr o Projeto Localmente

Se quiseres clonar e correr este laboratório no teu próprio computador, segue estes passos:

**1. Clonar o Repositório**
```bash
git clone [https://github.com/o-teu-nome/football-analyzer.git](https://github.com/o-teu-nome/football-analyzer.git)
cd football-analyzer
