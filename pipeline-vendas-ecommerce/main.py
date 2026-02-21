from src.extract import ler_dados
from src.transform import transformar_dados
from src.load import salvar_dados

def run_pipeline():
    # Caminhos (ajuste o nome do arquivo se necessário)
    input_path = "data/raw/ecommerce_sales_analysis.csv"
    output_path = "data/processed/vendas_processadas.csv"
    
    try:
        # Step 1: Extract
        df_raw = ler_dados(input_path)
        
        # Step 2: Transform
        df_clean = transformar_dados(df_raw)
        
        # Step 3: Load
        salvar_dados(df_clean, output_path)
        
        print("\n🚀 Pipeline executado com sucesso!")
        
    except Exception as e:
        print(f"❌ Erro no pipeline: {e}")

if __name__ == "__main__":
    run_pipeline()