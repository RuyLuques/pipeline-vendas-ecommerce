# 🚀 Pipeline de Análise de Vendas E-commerce

Este projeto implementa um pipeline de dados (ETL) robusto em Python para processar e consolidar métricas de vendas anuais de um e-commerce. O objetivo é transformar dados brutos de vendas mensais em insights de faturamento e performance de produtos.

## 🏗️ Arquitetura do Projeto

O projeto foi estruturado seguindo boas práticas de engenharia de software, separando as responsabilidades em módulos distintos:

- **Extract (`src/extract.py`)**: Recuperação dos dados brutos em CSV.
- **Transform (`src/transform.py`)**: Limpeza de nomes de colunas, tratamento de nulos, agregação de vendas mensais em anuais e cálculo de receita total.
- **Load (`src/load.py`)**: Exportação dos dados transformados para uma camada de consumo (`data/processed`).
- **Orquestração (`main.py`)**: Ponto de entrada que coordena a execução de todo o fluxo.



## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.9+
* **Biblioteca Principal:** Pandas (Processamento de dados)
* **Automação:** GitHub Actions (CI/CD)
* **Ambiente:** Venv (Virtual Environment)

## 📊 O Desafio Técnico

O dataset original (`ecommerce_sales_analysis.csv`) apresentava os dados de vendas distribuídos horizontalmente em 12 colunas (jan-dez). 
A lógica de transformação implementada:
1.  Normalizou os nomes das colunas para evitar erros de case-sensitivity.
2.  Consolidou as 12 colunas de vendas em uma métrica única de `total_units_sold`.
3.  Calculou a `total_revenue` com base no preço unitário.
4.  Rankeou os produtos por faturamento para facilitar a análise de Pareto.

## 🚀 Como Executar

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU_USUARIO/pipeline-vendas-ecommerce.git](https://github.com/SEU_USUARIO/pipeline-vendas-ecommerce.git)