# Tarea seamana 16: Trabajo con Archivos de Texto en Python

# Crea un archivo llamado "my_notes.txt"
archivo = open("my_notes.txt", "w")

# Escribe tres líneas de notas
archivo.write("Nota 1: Hoy aprendí a usar archivos de texto en Python.\n")
archivo.write("Nota 2: Los modos 'w' y 'r' sirven para escribir y leer.\n")
archivo.write("Nota 3: Siempre debo cerrar los archivos después de usarlos.\n")

# Cierra el archivo
archivo.close()



