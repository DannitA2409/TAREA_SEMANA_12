# Tarea seamana 16: Trabajo con Archivos de Texto en Python

# CREACIÓN DEL ARCHIVO

# Crea un archivo llamado "my_notes.txt"
archivo = open("my_notes.txt", "w")

# Escribe tres líneas de notas
archivo.write("Hoy aprendí a usar archivos de texto en Python.\n")
archivo.write("Los modos 'w' y 'r' sirven para escribir y leer.\n")
archivo.write("Siempre debo cerrar los archivos después de usarlos.\n")

# Cierra el archivo
archivo.close()

# LECTURA DE ARCHIVO

# Abre el archivo para leer su contenido
archivo = open("my_notes.txt", "r")

linea = archivo.readline()  # Lee la primera línea
# Lee linea por línea hasta el final del archivo
while linea:
    print(linea.strip())  # Elimina los saltos de línea
    linea = archivo.readline()

# Cierra el archivo después de leer
archivo.close()


