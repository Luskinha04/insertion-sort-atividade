import time
from insertionsort import insertion_sort_basico, insertion_sort_otimizado

# Casos de teste com 20 elementos
casos = {
    "Melhor caso": list(range(20)),  # Lista já ordenada
    "Pior caso": list(range(19, -1, -1)),  # Lista em ordem reversa
}

for nome, lista in casos.items():
    print(f"\n===== {nome.upper()} =====")

    print("\n--- Versão Básica ---")
    lista_b = lista.copy()
    print("Lista original:", lista_b)
    inicio = time.time()
    insertion_sort_basico(lista_b)
    fim = time.time()
    print("Lista ordenada:", lista_b)
    print(f"Tempo: {fim - inicio:.6f} segundos")

    print("\n--- Versão Otimizada ---")
    lista_o = lista.copy()
    print("Lista original:", lista_o)
    inicio = time.time()
    insertion_sort_otimizado(lista_o)
    fim = time.time()
    print("Lista ordenada:", lista_o)
    print(f"Tempo: {fim - inicio:.6f} segundos")
