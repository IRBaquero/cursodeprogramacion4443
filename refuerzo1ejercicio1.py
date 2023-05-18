#Lee los datos del trabajador
sueldo_base = int(input("Ingrese su sueldo basico: "))
venta1= int(input("Ingrese el valor de la primera venta: "))
venta2= int(input("Ingrese el valor de la segunda venta: "))
venta3= int(input("Ingrese el valor de la tercera venta: "))
#Calcula el valor de la comision
comision = (venta1+venta2+venta3)*0.10
#Calcula el sueldo con comision del trabajador
sueldo_total = sueldo_base+comision
#Muestra el valor de la comision y el sueldo total
print(f"\nLa comision es de {comision:,.0f} y el sueldo total es {sueldo_total:,.0f}")