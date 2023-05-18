#Declarando el ciclo While
x="s"
while x=="s" or x=="S":
    #Lee el sueldo del trabajador
    sueldo_basico=int(input("Digite el sueldo del trabajador: "))
    #Calcula la comision
    if sueldo_basico < 655000:
        comision=sueldo_basico*0.04
        print(f"\nEl trabajador recibe comision, sueldo total es {comision+sueldo_basico:,.0f}")
    else:
        comision=0
        print(f"\nEl trabajador no recibe comision, sueldo total es {comision+sueldo_basico:,.0f}")
    #Preguntando si desea volver ejecutar el programa
    x=input("\nDesea calcular otro sueldo? (S/N): ")