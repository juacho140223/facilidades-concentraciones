# Univesidad Central del Ecuador
# Carrera de Petroleos
# Materia: Facilidades de Producción
# Integrantes: Ana Paula Carrasco, Vanessa Chamorro, Juan Salazar

# Aplicativo de concentraciones

print("Cálculo de la cantidad de galones necesarios según su concentraciones")

Qf=int(input("Ingrese los barriles de fluido producidos por dia: "))
BSW=int(input("Ingrese el porcentaje de BSW: "))
pa_time=int(input("Ingrese el tiempo que dura el bombeo del principio activo en horas: "))

# Calculo
Qw=Qf*BSW/100
Qo=Qf-Qw

def mostrar_menu(opciones):
    print('Seleccione un principio activo:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()

def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()

def menu_principal():
    opciones = {
        '1': ('Demulsificante (30 ppm)', accion1),
        '2': ('Biocida (500 ppm)', accion2),
        '3': ('Antiescala (35 ppm)', accion3),
        '4': ('Salir', salir)
    }

    generar_menu(opciones, '4')


def accion1():
    ppm=35
    gal=Qo*42/24*pa_time
    result=(gal*ppm)/(1000000-ppm)
    print("Para inyectar demulsificante es necesario ",result," galones")
    print("en ",pa_time," horas de bombeo para una producción")
    print("de ",Qf," BFPD con un BSW de ",BSW," %")

def accion2():
    ppm=500
    gal=Qw*42/24*pa_time
    result=(gal*ppm)/(1000000-ppm)
    print("Para inyectar biocida es necesario ",result," galones")
    print("en ",pa_time," horas de bombeo para una producción")
    print("de ",Qf," BFPD con un BSW de ",BSW," %")

def accion3():
    ppm=30
    gal=Qw*42/24*pa_time
    result=(gal*ppm)/(1000000-ppm)
    print("Para inyectar antiescala es necesario ",result," galones")
    print("en ",pa_time," horas de bombeo para una producción")
    print("de ",Qf," BFPD con un BSW de ",BSW," %")

def salir():
    print('Saliendo')

if __name__ == '__main__':
    menu_principal()



