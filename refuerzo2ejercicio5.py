#Tabla para multiplicar los numeros que el usuario desee
#Inicializando la variable para el ciclo while
x="s"
#Ciclo While
while x == "s" or x == "S":
#Leer la cantidad de numeros a multiplicar
    cont=int(input("Cuantos numeros desea multiplicar? "))
    num=[]
#Ciclo para guardar en una lista los numeros a multiplicar
    for i in range(cont):
#Leer los numeros a multiplicar
        num.append(int(input(f"\nIngrese el primer numero {i+1} que desea multiplicar: ")))
#Inicializando la variable acumulativa para guardar la multiplicacion
    res=1
#Ciclo para multiplicar los elementos de la lista ente si
    for i in num:
        res=i*res
#Mostrar la respuesta en pantalla
    print(f"\nLa multiplicacion entre {num} es: {res}")
#Cambia el valor de la variable para continuar o cerrar el ciclo while
    x=input("\nDesea hacer otra multipicacion? (S/N)")
