# Crear el diccionario
informacion_personal = {
    "nombre": "Jordan Steven Vera Carabali ",
    "edad": 18,
    "ciudad": "Sucumbios - Shushufindi ",
}

# Acceder al valor de "ciudad" y modificarlo
informacion_personal["ciudad"] = "Shushufindi"

# Agregar la clave "profesion"
informacion_personal["profesion"] = "Bachiller"

# Verificar si la clave "telefono" existe y agregarla si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "096 824 8709"

# Eliminar la clave "edad"
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario final
print("Diccionario final:")
print(informacion_personal)
