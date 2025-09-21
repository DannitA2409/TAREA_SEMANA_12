ciudades = ["Quito", "Guayaquil", "Cuenca"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 4

# matriz 3D (ciudad x semana x día)
temperaturas = [
    [   # Quito
        [20, 22, 21, 19, 18, 20, 21],   # Semana 1
        [23, 22, 20, 21, 19, 20, 22],   # Semana 2
        [21, 20, 19, 22, 23, 21, 20],   # Semana 3
        [22, 21, 20, 21, 20, 22, 23]    # Semana 4
    ],
    [   # Guayaquil
        [28, 30, 29, 31, 32, 30, 29],   # Semana 1
        [30, 31, 32, 33, 31, 29, 30],   # Semana 2
        [29, 30, 31, 32, 30, 31, 30],   # Semana 3
        [31, 32, 33, 32, 31, 30, 29]    # Semana 4
    ],
    [   # Cuenca
        [15, 16, 14, 15, 16, 15, 14],   # Semana 1
        [17, 16, 15, 16, 15, 16, 17],   # Semana 2
        [16, 15, 15, 14, 15, 16, 15],   # Semana 3
        [17, 16, 15, 17, 16, 15, 16]    # Semana 4
    ]
]

# Función
def calcular_promedios(ciudades, dias, semanas, temperaturas):
    for i, ciudad in enumerate(ciudades):  # Recorre ciudades
        suma_total = 0
        conteo = 0
        for semana in range(semanas):      # Recorre semanas
            for dia in range(len(dias)):   # Recorre días
                suma_total += temperaturas[i][semana][dia]
                conteo += 1
        promedio_ciudad = suma_total / conteo
        print(f"Ciudad: {ciudad} → Promedio total = {promedio_ciudad:.2f}°C")

#Llamada a la función
calcular_promedios(ciudades, dias, semanas, temperaturas)