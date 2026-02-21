import sqlite3
import pandas as pd
import os

def salvar_dados(df, caminho_csv):
    """Salva os dados em CSV e também em um banco SQLite."""
    # 1. Salva em CSV
    os.makedirs(os.path.dirname(caminho_csv), exist_ok=True)
    df.to_csv(caminho_csv, index=False)
    
    # 2. Salva em SQLite (Diferencial para entrevista)
    conn = sqlite3.connect("data/vendas_ecommerce.db")
    df.to_sql("vendas_analise", conn, if_exists="replace", index=False)
    conn.close()
    
    print(f"✅ Dados salvos em CSV e no Banco SQLite!")