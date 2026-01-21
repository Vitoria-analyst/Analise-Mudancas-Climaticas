# 🌍 Climate & Health Impact Monitor CLI (2015-2025)

> **Uma ferramenta de linha de comandos (CLI) robusta para análise e visualização de dados climáticos e de saúde global.**

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 📋 Sobre o Projeto

Este projeto consiste numa aplicação modular desenvolvida em **Python** para monitorizar a correlação entre as alterações climáticas e indicadores de saúde pública global no período de 2015 a 2025.

A ferramenta processa o dataset *"Global Climate & Health Impact Tracker"*, permitindo ao utilizador navegar interativamente por estatísticas descritivas, visualizar tendências de poluição (PM2.5) e gerar relatórios automáticos sobre o impacto de ondas de calor na saúde cardiovascular e respiratória.

### 🚀 Funcionalidades Principais

* **💻 Interface Interativa (CLI):** Menu de navegação robusto com validação de entradas e tratamento de erros (Try-Except) para garantir a estabilidade da execução.
* **📊 Análise Exploratória Automática:** Cálculo de estatísticas globais e rankings ("Top 5") de países com piores índices de qualidade do ar e doenças.
* **📈 Visualização Avançada:** Geração de 7 tipos de gráficos, incluindo Heatmaps de temperatura por região (usando *Seaborn*) e curvas de tendência temporal.
* **💾 Persistência de Dados e Logs:**
    * Sistema de logs em memória que regista toda a sessão de análise.
    * Exportação automática de relatórios em `.txt` e gráficos em `.png` para uma pasta dedicada de resultados.
* **🧹 Data Cleaning:** Validação de integridade do dataset e conversão de tipos temporais na ingestão.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Manipulação de Dados:** Pandas (Dataframes, GroupBy, Pivot Tables)
* **Visualização:** Matplotlib, Seaborn (Heatmaps)
* **Sistema:** Módulo `os` (gestão agnóstica de diretórios Windows/Linux/Mac) e `time` (UX).

---

## 📂 Estrutura do Projeto

```
├── AnaliseMudancasClimaticas.py   # Script principal da aplicação
├── global_climate_2015_2025.csv   # Dataset (Fonte: Kaggle)
├── requirements.txt               # Dependências do projeto
├── README.md                      # Documentação
└── resultados/                    # Pasta gerada automaticamente com os relatórios exportados
```
---
## ⚙️ Destaques Técnicos
1. Tratamento e Pivoting de Dados
Para a geração dos mapas de calor (Heatmaps), foi implementada uma transformação complexa de dados:

Conversão do formato "longo" para "largo" (matriz) utilizando groupby e unstack.

Isso permitiu cruzar Regiões vs. Anos para visualizar a evolução da temperatura média global.

2. Formatação de Saída (UX no Terminal)
Ao contrário de prints simples, a ferramenta utiliza f-strings com espaçamento fixo e alinhamento manual para simular tabelas legíveis diretamente no terminal, melhorando a experiência do utilizador sem necessidade de interface gráfica pesada.

3. Gestão de Ficheiros (File I/O)
O script utiliza o módulo os.path para criar dinamicamente a pasta /resultados/, garantindo que o software funcione sem erros em qualquer sistema operativo (Windows, macOS ou Linux).

## 🖥️ Como Executar
Clone o repositório:

git clone [https://github.com/SEU_USUARIO/NOME_DO_REPO.git](https://github.com/SEU_USUARIO/NOME_DO_REPO.git)

Instale as dependências:

pip install -r requirements.txt

Execute a ferramenta:

python AnaliseMudancasClimaticas.py

Interaja com o Menu: Escolha as opções numéricas (1-7) para carregar dados, visualizar gráficos ou exportar relatórios.
---
## 👩‍💻 Autora
Vitória Rodrigues - [LinkedIn](https://www.linkedin.com/in/vitoria-rodrigues-/)

Desenvolvido na UC de Programação e Algoritmos - Universidade de Aveiro
