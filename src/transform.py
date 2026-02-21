import pandas as pd

def transformar_dados(df):
    print("🛠️ Transformando dados (Agregação Anual)...")

    df.columns = [col.strip().lower() for col in df.columns]

    colunas_vendas = [col for col in df.columns if 'sales_month_' in col]
    
    df['total_units_sold'] = df[colunas_vendas].sum(axis=1)

    df['total_revenue'] = df['price'] * df['total_units_sold']

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