def calcular_temperatura_promedio(datos):
    temperaturas_promedio_ciudades = {}

    for ciudad, semanas in datos.items():
        suma_temperaturas = 0
        total_dias = 0

        for semana, temperaturas in semanas.items():
            suma_temperaturas += sum(temperaturas)
            total_dias += len(temperaturas)

        temperatura_promedio = suma_temperaturas / total_dias
        temperaturas_promedio_ciudades[ciudad] = temperatura_promedio

    return temperaturas_promedio_ciudades

# Ejemplo de datos: temperaturas de 3 ciudades durante 4 semanas
datos = {
    'Quito': {
        'Semana1': [20, 22, 21, 19, 20],
        'Semana2': [22, 24, 23, 21, 22],
        'Semana3': [21, 20, 19, 18, 21],
        'Semana4': [19, 18, 20, 19, 20]
    },
    'Shushufindi': {
        'Semana1': [30, 32, 31, 29, 30],
        'Semana2': [32, 34, 33, 31, 32],
        'Semana3': [31, 30, 29, 28, 31],
        'Semana4': [29, 28, 30, 29, 30]
    },
    'Cuenca': {
        'Semana1': [18, 20, 19, 17, 18],
        'Semana2': [20, 22, 21, 19, 20],
        'Semana3': [19, 18, 17, 16, 19],
        'Semana4': [17, 16, 18, 17, 18]
    }
}

# Calcula la temperatura promedio de cada ciudad
temperaturas_promedio = calcular_temperatura_promedio(datos)

# Imprime los resultados
for ciudad, temperatura_promedio in temperaturas_promedio.items():
    print(f'Temperatura promedio en {ciudad}: {temperatura_promedio:.2f}°C')
