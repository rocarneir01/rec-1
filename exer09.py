9
def intersecao_arrays(array1, array2):
    return list(set(array1) & set(array2))

array1 = [1, 2, 3, 4, 5]
array2 = [3, 4, 5, 6, 7]

resultado = intersecao_arrays(array1, array2)
print("Interseção:", resultado)