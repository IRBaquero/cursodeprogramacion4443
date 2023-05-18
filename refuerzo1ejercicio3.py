#Lee la calificacion de los 3 parciales
parial1=float(input("Digite la calificacion del primer parcial: "))
parial2=float(input("Digite la calificacion del segundo parcial: "))
parial3=float(input("Digite la calificacion del tercer parcial: "))
#Calcula la calificacion
nota_final=round((parial1+parial2+parial3)/3,2)
#Muestra la calificacion final
print(f"\nSu calificacion final es {nota_final}")