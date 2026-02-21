from src.extract import ler_dados
from src.transform import transformar_dados
from src.load import salvar_dados

def run_pipeline():
    input_path = "data/raw/ecommerce_sales_analysis.csv"
    output_path = "data/processed/vendas_processadas.csv"
    
    try:
        df_raw = ler_dados(input_path)
        
        df_clean = transformar_dados(df_raw)
        
        salvar_dados(df_clean, output_path)
        
        print("\n🚀 Pipeline executado com sucesso!")
        
    except Exception as e:
        print(f"❌ Erro no pipeline: {e}")

if __name__ == "__main__":
    run_pipeline()