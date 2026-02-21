import pandas as pd

def transformar_dados(df):
    """Transforma dados de vendas mensais em métricas anuais por produto."""
    print("🛠️ Transformando dados (Agregação Anual)...")

    # 1. Limpar nomes das colunas
    df.columns = [col.strip().lower() for col in df.columns]

    # 2. Identificar colunas de vendas (sales_month_1 até sales_month_12)
    colunas_vendas = [col for col in df.columns if 'sales_month_' in col]
    
    # 3. Criar coluna de Total de Unidades Vendidas (Soma dos 12 meses)
    df['total_units_sold'] = df[colunas_vendas].sum(axis=1)

    # 4. Calcular Receita Total (Preço * Unidades Vendidas)
    # O dataset usa a coluna 'price'
    df['total_revenue'] = df['price'] * df['total_units_sold']

    # 5. Selecionar apenas as colunas principais para o relatório final
    colunas_finais = [
        'product_name', 
        'category', 
        'price', 
        'total_units_sold', 
        'total_revenue', 
        'review_score'
    ]
    
    df_final = df[colunas_finais].sort_values(by='total_revenue', ascending=False)

    return df_final