import pandas as pd

# 1. Carregar o arquivo CSV
df = pd.read_csv('dados_ordenacao.csv')
listas_para_analise = {
    "pequena_100": df["pequena_100"].dropna().astype(int).tolist(),
    "media_1000": df["media_1000"].dropna().astype(int).tolist(),
    "grande_10000": df["grande_10000"].dropna().astype(int).tolist(),
    "muito_grande_50000": df["muito_grande_50000"].dropna().astype(int).tolist(),
}


#print(df.columns)

# Agora, 'listas_para_analise' é um dicionário com 4 listas prontas para o teste.

# def selection_sort(lista):
#     n = len(lista)
#     for i in range(n):
#         indice_menor = i

#         for j in range(i + 1, n):
#             if lista[j] < lista[indice_menor]:
#                 indice_menor = j

#         lista[i], lista[indice_menor] = lista[indice_menor], lista[i]

#     return lista

def selection_sort(array):
    n = len(array)
    for i in range(n):
        indice_menor = i

        for j in range(i + 1, n):
            if array[j] < array[indice_menor]:
                indice_menor = j

        array[i], array[indice_menor] = array[indice_menor], array[i]

    return array

#numeros = listas_para_analise[nome_coluna]
# print("Lista ordenada com Selection Sort:", selection_sort(listas_para_analise["pequena_100"]))
# print("Lista ordenada com Selection Sort:", selection_sort(listas_para_analise["media_1000"]))
# print("Lista ordenada com Selection Sort:", selection_sort(listas_para_analise["grande_10000"]))
# print("Lista ordenada com Selection Sort:", selection_sort(listas_para_analise["muito_grande_50000"]))