# Creación y escritura de notas en el archivo
with open("my_notes.txt", "w") as file:
    # Escribir notas en el archivo
    file.write("Nota 1: Pagar la luz (mañana).\n")
    file.write("Nota 2: Pagar el Internet .\n")
    file.write("Nota 3: Hacer los Practicos de esta semana .\n")

# Lectura del archivo y mostrando contenido en la consola
with open("my_notes.txt", "r") as file:
    # Leer y mostrar cada línea del archivo
    for line in file:
        print(line.strip())  # Utilizamos strip() para eliminar caracteres de nueva línea

# Cierre del archivo
file.close()  # Aunque no es necesario debido al uso del bloque 'with', es buena práctica cerrar el archivo manualmente
