import pandas as pd
import time

# 1. Carregar o arquivo CSV
df = pd.read_csv('dados_ordenacao.csv')
listas_para_analise = {}

# 2. Processar cada coluna e armazenar como lista Python
for nome_coluna in df.columns:
    # .dropna() remove os valores NaN,  .astype(int) garante que sejam interios
    lista_limpa = df[nome_coluna].dropna().astype(int).tolist()
    listas_para_analise[nome_coluna] = lista_limpa

    # Agora, 'listas_para_analise' é um dicionário com 4 listas prontas para o teste.

    #print(listas_para_analise)


    #  Função Selection Sort
    def selection_sort(arr):
        arr = arr.copy() # evita modificar a original
        n = len(arr)

        for i in range(n):
            indice_menor = i
           
            for j in range(i + 1,n):
                if arr[j] < arr[indice_menor]:
                    indice_menor = j
            
            arr[i], arr[indice_menor] = arr[indice_menor], arr[i]

        return arr
    


numeros = lista_limpa
print("Lista ordenada com Selection Sort: ", selection_sort(numeros))

inicio = time.time()
ordenada = selection_sort(lista_limpa)
final = time.time()

tp_total = (final-inicio)