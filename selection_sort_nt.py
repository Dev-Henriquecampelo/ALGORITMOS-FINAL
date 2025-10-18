import pandas as pd

# 1. Carregar o arquivo CSV
df = pd.read_csv('dados_ordenacao.csv')
listas_para_analise = {}

# 2. Processar cada coluna e armazenar como lista Python
for nome_coluna in df.columns:
    # .dropna() remove os valores NaN,  .astype(int) garante que sejam interios
    lista_limpa = df[nome_coluna].dropna().astype(int).tolist()
    listas_para_analise[nome_coluna] = lista_limpa

    # Agora, 'listas_para_analise' é um dicionário com 4 listas prontas para o teste.

    print(listas_para_analise)



    def selection_sort(lista):
        n = len(lista)
        for i in range(n):
            indice_menor + i
           
            for j in range(i + 1,n):
                if lista[j] < lista[indice_menor]:
                    indice_menor = j
            
            lista[i], lista[indice_menor] = lista[indice_menor], lista[i]

        return lista

numeros = [0,100]
print("Lista ordenada com Selection Sort: ", selection_sort(numeros))

