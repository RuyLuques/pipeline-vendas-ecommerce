import pandas as pd
import os

def ler_dados(caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_arquivo}")
    
    print(f"📦 Extraindo dados de: {caminho_arquivo}")
    return pd.read_csv(caminho_arquivo)