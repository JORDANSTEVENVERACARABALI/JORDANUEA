def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Llamada a la función con solo el monto total de la compra
monto_compra1 = 100
descuento1 = calcular_descuento(monto_compra1)
monto_final1 = monto_compra1 - descuento1
print(f"Monto del descuento: {descuento1}")
print(f"Monto final a pagar: {monto_final1}")

# Llamada a la función con el monto total de la compra y un porcentaje de descuento personalizado
monto_compra2 = 200
porcentaje_descuento2 = 15
descuento2 = calcular_descuento(monto_compra2, porcentaje_descuento2)
monto_final2 = monto_compra2 - descuento2
print(f"Monto del descuento: {descuento2}")
print(f"Monto final a pagar: {monto_final2}")
