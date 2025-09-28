# Tarea semana 15: Trabajando con Diccionarios en Python

# Crear diccionario con información personal ficticia
informacion_personal = {
    "nombre": "Danna López",
    "edad": 21,
    "ciudad": "Guayaquil"
}
print(f"Diccionario inicial: {informacion_personal}")
print()

# ACCEDER Y MODIFICAR VALORES
print("-------- Accediendo y modificando valores ---------")

# Acceder al valor de la clave "ciudad"
ciudad_actual = informacion_personal["ciudad"]
print(f"Ciudad actual: {ciudad_actual}")

# Modificar la ciudad
informacion_personal["ciudad"] = "Quito"
print(f"Ciudad modificada: {informacion_personal['ciudad']}")

# Agregar nueva clave-valor para "profesion"
informacion_personal["profesion"] = "Ingeniera en tecnologías de la información"
print(f"Profesión agregada: {informacion_personal['profesion']}")
print(f"Diccionario después de modificaciones: {informacion_personal}")

