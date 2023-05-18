#declarando variable
x="s"
alumnos=[]
promedio_general=0
#declarando el ciclo while
while x=="s" or x=="S":
    calificaciones=[]
    #captura de las 5 calificaciones
    calificaciones.append(float(input("Digite la calificacion del primer parcial: ")))
    calificaciones.append(float(input("Digite la calificacion del segundo parcial: ")))
    calificaciones.append(float(input("Digite la calificacion del tercer parcial: ")))
    calificaciones.append(float(input("Digite la calificacion del cuarto parcial: ")))
    calificaciones.append(float(input("Digite la calificacion del quinto parcial: ")))
    #calcular el promedio del alumno
    promedio_alum=sum(calificaciones)/len(calificaciones)
    print(f"\nEl promedio del alumno es {promedio_alum:,.2f}")
    alumnos.append(promedio_alum)
    x=input("\nDesea ingresar las calificaciones de otro alumno (S/N)")
#Calcular el promedio general
promedio_general=sum(alumnos)/len(alumnos)
print(f"\nEl promedio general de los {len(alumnos)} alumnos es {promedio_general:,.2f}")