#ValorNetoDeUnProducto
producto = input ("Ingrese el nombre del producto: ")
valorProducto = int(input("Ingrese el valor del producto: "))
valorNeto = float(1.19)
valorSinIva = float(valorProducto / valorNeto)
valorSiniva_round = valorSinIva.__round__()

print("-----Detalle producto----")
print(f"NOMBRE PRODUCTO: {producto}")
print(f"VALOR PRODUCTO: {valorProducto}")
print(f"VALOR PRODUCTO SIN IVA: {valorSiniva_round}")