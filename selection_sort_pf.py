import pandas as pd

# 1. Carregar o arquivo CSV
df = pd.read_csv('dados_ordenacao.csv')
listas_para_analise = {}

# 2. Processar cada coluna e armazenar como lista Python
for nome_coluna in df.columns:
    # .dropna() remove os valores NaN, .astype(int) garante que sejam inteiros
    lista_limpa = df[nome_coluna].dropna().astype(int).tolist()
    listas_para_analise[nome_coluna] = lista_limpa

# Agora, 'listas_para_analise' é um dicionário com 4 listas prontas para o teste.

print(listas_para_analise)