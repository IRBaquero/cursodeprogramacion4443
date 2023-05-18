cantidad_hombres=int(input("Ingrese la cantidad de hombres que hay en el grupo: "))
cantidad_mujeres=int(input("Ingrese la cantidad de mujeres que hay en el grupo: "))
#Calcula la cantidad de estudiantes
total_estudiantes=cantidad_hombres+cantidad_mujeres
#Calcula el procentaje de hombres
porcentaje_h=round((cantidad_hombres*100)/total_estudiantes,1)
#Calcula el procentaje de mujeres
porcentaje_m=round((cantidad_mujeres*100)/total_estudiantes,1)
#Muestra el procentaje de hombres y mujeres del grupo
print(f"\nEl porcentaje de hombres es {porcentaje_h}% y el poncetaje de mujeres es {porcentaje_m}%")