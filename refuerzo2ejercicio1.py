#Lee el numero de la tabla a desplegar y el numero hasta el cual desea ver el resultado
num_tabla=int(input("Digite el numero de la tabla que desea ver: "))
limit=int(input("Hasta que numero desea ver el resultado: "))+1
print(f"La tabla del {num_tabla} es:")
#Calcula la tabla del numero dado desde el 1 hasta el limite indicado e imprime por pantalla
for i in range(1,limit,1):
    res=num_tabla*i
    print(f"{num_tabla} * {i} = {res}")