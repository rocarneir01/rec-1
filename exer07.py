7
def ordenacao_crescente(array):
    for i in range(len(array)):
        menor_indice = i
        for j in range(i + 1, len(array)):
            if array[j] < array[menor_indice]:
                menor_indice = j
    
        array[i], array[menor_indice] = array[menor_indice], array[i]
    return array

numeros = [64, 34, 25, 12, 22, 11, 90]
resultado = ordenacao_crescente(numeros)

print(f"Array ordenado em ordem crescente: {resultado}")