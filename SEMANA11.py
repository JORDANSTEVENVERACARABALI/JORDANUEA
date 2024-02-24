def buscar_valor(matriz, valor):
    """
    Función que busca un valor específico en una matriz bidimensional.

    Parámetros:
        matriz (list): La matriz bidimensional donde se realizará la búsqueda.
        valor: El valor que se desea encontrar en la matriz.

    Retorna:
        tuple: La posición (fila, columna) del valor si se encuentra, None en caso contrario.
    """
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            if matriz[fila][columna] == valor:
                return fila, columna
    return None

# Definimos una matriz de ejemplo
matriz_ejemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Valor que deseamos buscar
valor_buscado = 5

# Realizamos la búsqueda en la matriz de ejemplo
posicion = buscar_valor(matriz_ejemplo, valor_buscado)

# Verificamos si se encontró el valor y mostramos un mensaje
if posicion:
    fila, columna = posicion
    print(f"El valor {valor_buscado} se encontró en la posición ({fila}, {columna}) de la matriz.")
else:
    print(f"El valor {valor_buscado} no se encontró en la matriz.")
