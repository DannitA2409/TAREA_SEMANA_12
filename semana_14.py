# Definición de la función
def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100) # Cálculo de valor de descuento
    return descuento


# Primera llamada a la función
# Solo con el monto (se aplica el descuento por defecto del 10%)
monto1 = 100
descuento1 = calcular_descuento(monto1)
monto_final1 = monto1 - descuento1

print("Primera compra:")
print("Monto total: $", monto1)
print("Descuento aplicado: $", descuento1)
print("Monto final a pagar: $", monto_final1)
print("---------------")

