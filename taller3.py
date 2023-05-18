def verificar_bono_pre_pension(edad, sueldo_basico):
    if edad > 55:
        bono_prepension=sueldo_basico*0.05
        return bono_prepension
    else:
        return 0

def verificar_paseo_diciembre(estado_civil, numero_hijos):
    if estado_civil == "c" or estado_civil == "C" and numero_hijos > 0:
        return True
    else:
        return False

def verificar_comision(sueldo_basico):
    if sueldo_basico >= 1000000 and sueldo_basico <= 1500000:
        comision=sueldo_basico*0.02
        return comision
    elif sueldo_basico >= 1500001 and sueldo_basico <= 2000000:
        comision=sueldo_basico*0.05
        return comision
    else:
        return 0

def verificar_bono_alimentacion(sueldo, dias_laborados):
    if sueldo<1000000 and dias_laborados>20:
        return True
    else:
        return False

def ejecutar():
    identificacion=int(input ("Ingrese el numero de identificacion de la persona: "))
    nombre_P=input ("Ingrese el nombre de la persona sin apellidos: ")
    apellido_P=input ("Ingrese los apellidos de la persona: ")
    direccion_P=input ("Ingrese la direccion de la persona: ")
    telefono_P=int(input ("Ingrese el numero de telefono: "))
    edad=int(input ("Ingrese la edad de la persona en numeros: "))
    estado_civil=input ("Estado civil: Digite la letra dependiendo el caso:  \nCasado: C  Soltero: S  Union Libre: U\nDivorciado: D Viudo: V\nSeleccione una opcion: ")
    numero_hijos=int(input ("Ingrese el numero de hijos: "))
    estatura=int(input ("Ingrese la estatura en centimetros: "))
    fecha_Contratacion=input ("Ingrese la fecha de contratacion con el siguiente formato DD/MM/AAAA: ")
    sueldo_basico=int(input ("Ingrese el sueldo basico: "))
    dias_laborados=int(input ("Ingrese los dias laborados: "))

    bono_pre_pension = verificar_bono_pre_pension(edad, sueldo_basico)
    paseo_diciembre = verificar_paseo_diciembre(estado_civil, numero_hijos)
    comision = verificar_comision(sueldo_basico)
    bono_alimentacion = verificar_bono_alimentacion(sueldo_basico, dias_laborados)

    print("\nBeneficios:")
    if bono_pre_pension > 0:
        print("- Bono pre-pensión: ${:.2f}".format(bono_pre_pension))
    if paseo_diciembre:
        print("- Paseo en diciembre")
    if comision > 0:
        print("- Comisión: ${:.2f}".format(comision))
    if bono_alimentacion :
        print("- Bono de alimentación")
    if bono_pre_pension == 0 and not paseo_diciembre and comision == 0 and not bono_alimentacion:
        print("El trabajador no cumple con los requisitos para ningún beneficio.")
ejecutar()