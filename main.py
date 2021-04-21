import json

try:
    with open('base_de_datos.json','r')as archivo:
        print("Leyendo base de datos...")
        lista_estudiantes = json.load(archivo)
        print("Base de datos cargada exitosamente")

except:
    print("Creando nueva base de datos...")
    lista_estudiantes = []

def calculo_promedio(lista_notas_estudiante):
    total_suma = 0
    cantidad_notas = len(lista_notas_estudiante)

    for nota in lista_notas_estudiante:
        total_suma = total_suma + nota

    if cantidad_notas >= 1:
        promedio = total_suma / cantidad_notas
    else:
        promedio = 0
    return promedio

def no_cursos_asignados(lista_notas_estudiante):
     cantidad_cursos = len(lista_notas_estudiante)
     return cantidad_cursos

def calculo_cursos_aprobados(lista_notas_estudiante):
    total_cursosa = 0
    for nota in lista_notas_estudiante:
        if nota >= 61:
            total_cursosa = total_cursosa + 1
        else:
            total_cursosa = total_cursosa + 0
    numero_cursosaprobados = total_cursosa
    return numero_cursosaprobados

def calculo_porcentaje_ca(lista_notas_estudiante):
    no_cursos = no_cursos_asignados(lista_notas_estudiante)
    no_cursos_aprobados = calculo_cursos_aprobados(lista_notas_estudiante)
    if no_cursos >= 1:
        porcentaje_notas = (no_cursos_aprobados * 100) / no_cursos
    else:
        porcentaje_notas = 0

    porcentaje_notas = str(porcentaje_notas)
    return porcentaje_notas

def ingresar_usuario():
     nombre = input("Ingrese su nombre completo: ")
     carnet = input("Ingrese carnet: ")
     for i in lista_estudiantes:
        while i['carnet'] == carnet:
            print ("Usuario ya registrado")
            ingresar_usuario()
            return
     anno_ingreso = carnet[0:4]
     lista_notas = []
     opcion_notas = input("Desea ingresar una nota? (y / n): ")
     while opcion_notas == 'y' or opcion_notas == 'Y':
        nueva_nota = input("Ingrese la nota: ")
        # convertir en entero
        nueva_nota = int(nueva_nota)
        lista_notas.append(nueva_nota)
        opcion_notas = input("Desea ingresar otra nota? (y / n): ")

     promedio_notas = calculo_promedio(lista_notas)
     no_cursos = no_cursos_asignados(lista_notas)
     no_cursos_aprobados = calculo_cursos_aprobados(lista_notas)
     porcentaje_cursos_aprobados = calculo_porcentaje_ca(lista_notas)

     estudiante = {
        'nombre': nombre,
        'carnet': carnet,
        'notas': lista_notas,
        'promedio': promedio_notas,
        'annio_de_ingreso': anno_ingreso,
        'cursos_asignados': no_cursos,
        'cursos_aprobados': no_cursos_aprobados,
        'p_cursos_aprobados': porcentaje_cursos_aprobados + ' %' 

     }
     lista_estudiantes.append(estudiante)
     return

def cantidad_estudiantes():
    no_estudiantes = len(lista_estudiantes)
    print(f'Hay {no_estudiantes} estudiantes en el sistema')
    return

def mostrar_estudiantes():
    for i in lista_estudiantes:
        print("Nombre: ", i["nombre"])
        print("carnet: ", i["carnet"])
        print("Notas: ", i["notas"])
        print("Promedio", i["promedio"])
        print("Año de ingreso", i["annio_de_ingreso"])
        print("Cursos Asignados", i["cursos_asignados"])
        print("Cursos aprobados", i["cursos_aprobados"])
        print("Porcentaje de cursos aprobados", i["p_cursos_aprobados"])
        print("----------------------------------------------------------------")
    return

def busqueda_carnet():
    buscar = input("Ingrese el No. de Carnet: ")
    for i in lista_estudiantes:
        if i['carnet'] == buscar:
            print("Nombre: ", i["nombre"])
            print("carnet: ", i["carnet"])
            print("Notas: ", i["notas"])
            print("Promedio:", i["promedio"])
            print("Año de ingreso:", i["annio_de_ingreso"])
            print("Cursos Asignados:", i["cursos_asignados"])
            print("Cursos aprobados:", i["cursos_aprobados"])
            print("Porcentaje de cursos aprobados:", i["p_cursos_aprobados"])
        else:
            print("Elemento no encontrado")
            return

def salir():
    with open('base_de_datos.json','w')as archivo:
        print("Guardando base de datos...")
        json.dump(lista_estudiantes, archivo)

def menu():
    mensaje_menu = """ \*\ MENÚ /*/
    1. Ingresar un Usuario
    2. Buscar un Usuario
    3. Mostrar Usuarios
    0. SALIR
    Seleccione una opción: """
    opcion = input(mensaje_menu)
    if opcion == '1':
        ingresar_usuario()
    if opcion == '2':
        busqueda_carnet()
    if opcion == '3':
        cantidad_estudiantes()
        print("----------------------------------------------------------------")
        mostrar_estudiantes()
    if opcion == '0':
        print("Opciones de salida" )
        print("1.Guardar y salir " )
        print("2.Salir sin guardar." )
        quis = int(input(("Ingrese (1 / 2): ")))
        if quis == 1:
            salir()

        return

    menu()
    return
menu()

#AUTORES:
#Sergio Vinicio Bay Elel 1990-20-16960
#Luis Eduardo Higueros Muñoz 1990-20-25321
#Julio Henry Martínez González 1990-20-25451