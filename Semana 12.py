# Definición de la matriz 3D para representar las temperaturas diarias
# Se asume una matriz de 2 ciudades, 7 días de la semana y 4 semanas
temperaturas = [
    [   # Ciudad 1
        [25, 26, 27, 28, 29, 30, 31],  # Semana 1
        [24, 25, 26, 27, 28, 29, 30],  # Semana 2
        [23, 24, 25, 26, 27, 28, 29],  # Semana 3
        [22, 23, 24, 25, 26, 27, 28]   # Semana 4
    ],
    [   # Ciudad 2
        [28, 29, 30, 31, 32, 33, 34],  # Semana 1
        [27, 28, 29, 30, 31, 32, 33],  # Semana 2
        [26, 27, 28, 29, 30, 31, 32],  # Semana 3
        [25, 26, 27, 28, 29, 30, 31]   # Semana 4
    ]
]

# Función para calcular el promedio de temperaturas por ciudad y semana
def calcular_promedio_temperaturas(temperaturas):
    for ciudad, ciudad_temperaturas in enumerate(temperaturas, 1):
        print(f"Promedio de temperaturas para la Ciudad {ciudad}:")
        for semana, semana_temperaturas in enumerate(ciudad_temperaturas, 1):
            promedio = sum(semana_temperaturas) / len(semana_temperaturas)
            print(f"Semana {semana}: {promedio:.2f} °C")
        print()

# Calcular y mostrar el promedio de temperaturas por ciudad y semana
calcular_promedio_temperaturas(temperaturas)
