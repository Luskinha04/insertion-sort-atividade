def insertion_sort_basico(array):
    n = len(array)
    for i in range(1, n):
        chave = array[i]
        j = i - 1
        while j >= 0 and array[j] > chave:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = chave
        print(f"Iteração {i}: {array}")


def insertion_sort_otimizado(array):
    n = len(array)
    for i in range(1, n):
        chave = array[i]
        j = i - 1
        trocou = False
        while j >= 0 and array[j] > chave:
            array[j + 1] = array[j]
            j -= 1
            trocou = True
        array[j + 1] = chave
        print(f"Iteração {i}: {array}")
        if not trocou:
            print(f"Lista já ordenada! Encerrando na iteração {i}")
            break
