import pandas as pd
import time
import matplotlib.pyplot as plt

# LER ARQUIVO CSV
df = pd.read_csv('dados_ordenacao.csv')
listas_para_analise = {
    "pequena_100": df["pequena_100"].dropna().astype(int).tolist(),
    "media_1000": df["media_1000"].dropna().astype(int).tolist(),
    "grande_10000": df["grande_10000"].dropna().astype(int).tolist(),
    "muito_grande_50000": df["muito_grande_50000"].dropna().astype(int).tolist(),
}




# IMPLEMENTAÇÃO DOS ALGORITMOS DE ORDENAÇÃO
def bubble_sort(arr):
  n = len(arr)
  for i in range(n):
    swapped = false
    for j in range(0, n - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        swapped = True
    if not swapped:
    break
  return arr

def insertion_sort(arr):
  for i in range(1, len(arr)):
    chave = arr[i]
    j = i - 1
    while j > 0 and arr[j] > chave:
      arr[j + 1] = arr[j]
      j-=1
    arr[j + 1] = chave
  return arr

# FALTA 2 ALGORITMOS



# TESTAR E MEDIR O TEMPO DE CADA ALGORITMO
algoritmos = {'bubble sort': bubble_sort,
              'insertion sort': insertion_sort
              # FALTA O "SELECTION SORT" E O "MERGE SORT" SEREM ADICIONADOS AQUI
              }

tempo_coletados = {alg: {} for alg in algortimos}
print('\n Iniciando medições de desempenho...\n')

for nome_tamanho, lista_dados in lista_para_analise.items():
  print(f'\n Lista: {nome_tamanho} ({len(lista_dados)} elementos)')
  for nome_alg, funcao in algoritmos.items():
    lista_teste = list(lista_dados)
    inicio = time.perf_counter()
    funcao(lista_teste)
    fim = time.perf_counter()
    tempos_coletados[nome_alg][nome_tamanho] = fim - inicio
    print(f'{nome_alg}: {fim - inicio:.6f} segundos.')


# GRÁFICOS COMPARATIVOS
tamanhos_n = sorted([int(''.join(filter(str.isdigit, nome))) for nome in lista_para_analise.keys()])
plt.figure(figsize=(9, 6))

for nome_alg, resultados in tempos_coletados.items():
  tempos = [resultado[nome] for nome in sorted(resultados.keys(), key=lambda x: int(''.join(filter(str.isdigit, x))))]
  plt.plot(tamanho_n, tempos, marker='o', label=nome_alg)

plt.xlabel('Tamanho da Lista (N)')
plt.ylabel('Tempo de Execução (segundos)')
plt.title('Comparação de Desempenho dos Algoritmos de Ordenação')
plt.grid(True)
plt.legend()
plt.show()

# RESULTADOS FINAIS
print(f'\nResultados finais (em segundos):\n')
for nome_alg, resultados in tempos_coletados.items():
  print(f'--- {nome_alg} ---')
  for nome_lista, tempo in resultados.items():
    print(f'{nome_lista}: {tempo:.6f}')
  print()