def bubble_sort(arr):
    """
    Implementación del algoritmo de ordenación de la burbuja.

    Parámetros:
        arr (list): La lista que se desea ordenar.

    Retorna:
        None. La lista se ordena in-place.
    """
    n = len(arr)
    for i in range(n):
        # Últimos i elementos ya están en su lugar
        for j in range(0, n-i-1):
            # Intercambiar si el elemento encontrado es mayor que el siguiente elemento
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def ordenar_fila(matriz, fila):
    """
    Función que ordena una fila específica de una matriz en orden ascendente.

    Parámetros:
        matriz (list): La matriz bidimensional.
        fila (int): El índice de la fila que se desea ordenar.

    Retorna:
        list: La fila ordenada.
    """
    fila_ordenada = list(matriz[fila])
    bubble_sort(fila_ordenada)
    return fila_ordenada

# Definimos una matriz de ejemplo
matriz_ejemplo = [
    [9, 4, 7],
    [2, 5, 1],
    [6, 3, 8]
]

# Fila que deseamos ordenar
fila_a_ordenar = 1

# Ordenamos la fila especificada en la matriz
fila_ordenada = ordenar_fila(matriz_ejemplo, fila_a_ordenar)

# Mostramos la matriz original
print("Matriz original:")
for fila in matriz_ejemplo:
    print(fila)

# Mostramos la matriz con la fila ordenada
matriz_ejemplo[fila_a_ordenar] = fila_ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz_ejemplo:
    print(fila)
