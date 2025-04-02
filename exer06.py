6

def remover_duplicados(array):
    return list(set(array))


numeros = [1, 2, 2, 3, 4, 4, 5]
array_sem_duplicados = remover_duplicados(numeros)

print(f"Array original: {numeros}")
print(f"Array sem duplicados: {array_sem_duplicados}")