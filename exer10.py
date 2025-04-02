10
def max_subarray(array):
    max_atual = max_global = array[0]
   
    for i in range(1, len(array)):
        max_atual = max(array[i], max_atual + array[i])
        if max_atual > max_global:
            max_global = max_atual
   
    return max_global


array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
resultado = max_subarray(array)
print("Maior soma do subarray contínuo:", resultado)