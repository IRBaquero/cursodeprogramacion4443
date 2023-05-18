#Lee los datos de la compra
valor_compra = int(input("Ingrese el valor total de la compra: "))
#Calcula el descuento
descuento=valor_compra*0.15
#Calcula el valor a pagar
Valor_final=valor_compra-descuento
#Muestra el valor a pagar
print(f"\nEl valor de la compra con el 15% de descuento es de {Valor_final:,.0f}")