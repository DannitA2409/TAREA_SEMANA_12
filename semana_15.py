# Tarea semana 15: Trabajando con Diccionarios en Python

# Crear diccionario con información personal ficticia
informacion_personal = {
    "nombre": "Danna López",
    "edad": 21,
    "ciudad": "Guayaquil"
}
print(f"Diccionario inicial: {informacion_personal}")


# ACCEDER Y MODIFICAR VALORES
print("\n---------------------------------------- Accediendo y modificando valores ----------------------------------------")

# Acceder al valor de la clave "ciudad"
ciudad_actual = informacion_personal["ciudad"]
print(f"Ciudad actual: {ciudad_actual}")

# Modificar la ciudad
informacion_personal["ciudad"] = "Quito"
print(f"Ciudad modificada: {informacion_personal['ciudad']}")

# Agregar nueva clave-valor para "profesion"
informacion_personal["profesion"] = "Ingeniera en tecnologías de la información"
print(f"Profesión agregada: {informacion_personal['profesion']}")
print("Diccionario después de modificaciones:")
print(informacion_personal)


# VERIFICAR EXISTENCIA DE CLAVES
print("\n---------------------------------------- Verificando existencia de claves ----------------------------------------")

# Verificar si existe la clave "telefono"
if "telefono" in informacion_personal:
    print("La clave 'telefono' ya existe en el diccionario")
else:
    # Agregar teléfono ficticio si no existe
    informacion_personal["telefono"] = "0912345678"
    print(f"Teléfono agregado: {informacion_personal['telefono']}")

print("Diccionario con teléfono:")
print(informacion_personal)


# ELIMINAR UNA CLAVE
# Verificar si la clave existe antes de eliminarla (buena práctica)
if "edad" in informacion_personal:
    edad_eliminada = informacion_personal.pop("edad")
    print(f"Edad eliminada: {edad_eliminada}")
else:
    print("La clave 'edad' no existe en el diccionario")

print("Diccionario sin edad:")
print(informacion_personal)


