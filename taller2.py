#Lee los datos de la persona
identificacion=int(input ("Ingrese el numero de identificacion de la persona: "))
nombre_P=input ("Ingrese el nombre de la persona sin apellidos: ")
apellido_P=input ("Ingrese los apellidos de la persona: ")
direccion_P=input ("Ingrese la direccion de la persona: ")
telefono_P=int(input ("Ingrese el numero de telefono: "))
edad_P=int(input ("Ingrese la edad de la persona en numeros: "))
estado_Civil=input ("Estado civil: Digite la letra dependiendo el caso:  \nCasado: C  Soltero: S  Union Libre: U\nDivorciado: D Viudo: V\n")
numero_Hijos=int(input ("Ingrese el numero de hijos: "))
estatura=int(input ("Ingrese la estatura en centimetros: "))
fecha_Contratacion=input ("Ingrese la fecha de contratacion con el siguiente formato DD/MM/AAAA: ")
sueldo_Basico=int(input ("Ingrese el sueldo basico: "))
dias_Laborados=int(input ("Ingrese los dias laborados: "))
#Verificando bono de prepension
if edad_P > 55:
    bono_prepension=sueldo_Basico*0.05
    print(f"\nTiene derecho a bono prepension por un valor de ${bono_prepension:,.0f}")
else:
    bono_prepension=0
    print("\nNo recibe bono prepension")
#Verificando paseo de fin de año
if estado_Civil=="C" or estado_Civil=="c" and numero_Hijos > 0:
    print("\nTiene derecho al paseo de fin de año")
else:
    print("\nNo tiene derecho al paseo de fin de año")
#Verificando comisiones por sueldo
if sueldo_Basico >= 1000000 and sueldo_Basico <= 1500000:
    comision1=sueldo_Basico*0.02
    print(f"\nTiene derecho a comision por valor de ${comision1:,.0f}")
elif sueldo_Basico >= 1500001 and sueldo_Basico <= 2000000:
    comision2=sueldo_Basico*0.05
    print(f"\nTiene derecho a comision por valor de ${comision2:,.0f}")
else:
    comision1=0
    comision2=0
    print("\nNo tiene derecho a comision")
#Verificando bono de alimentacion
if sueldo_Basico<1000000 and dias_Laborados>20:
    print("\nTiene derecho a bono de alimentacion")
else:
    print("\nNo tiene derecho a bono de alimentacion")