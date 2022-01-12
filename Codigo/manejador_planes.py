from manejadorbd import *
from validacion_datos import *
from decorador import *


def planes_disponibles(con):
    cursor_obj = con.cursor()
    cursor_obj.execute('SELECT * FROM  planes')
    cantidad_planes = cursor_obj.fetchall()
    print("\n{:<5} {:<20} {:<20} {:<20} ".format('ID', 'NOMBRE_PLAN', 'VALOR', 'CANTIDAD CANCIONES'))
    for row in cantidad_planes:
        id, nombre, valor, cantidad_canciones = row
        print("{:<5} {:<20} {:<20} {:<20} ".format(id, nombre, valor, cantidad_canciones))
# Función que pide los datos de un plan antes de registrarlo



def plan(con) -> tuple:
    id = validacion_numero(input('Número de identificación del plan: '), 1)
    id_plan = validacion_existencia_todas(con, nombre_tabla='planes', nombre_columna='id_plan', primary_key='id_plan', id=id)
    while id_plan == False:
        print('\t\n¡ERROR! Ya existe un plan con el \'Id plan\' ingresado. Si desea realizar el registro ingrese nuevamente la información.')
        id = validacion_numero(input('Número de identificación del plan: '), 1)
        id_plan = validacion_existencia_todas(con, nombre_tabla='planes', nombre_columna='id_plan', primary_key='id_plan', id=id)

    nombre_plan = input("Nombre del plan: ")
    valor = int(validacion_numero(input("Valor plan: "),5))
    cant_canciones = int(validacion_numero(input("Cantidad de canciones del plan: "),4))
    datos_plan = (id_plan, nombre_plan, valor, cant_canciones)
    return datos_plan

#

# Función para registrar los planes en la tabla planes

def registrar_plan(con):
    tupla = plan(con)
    cursor_obj = con.cursor()
    cursor_obj.execute('''INSERT INTO planes VALUES(?,?,?,?)''', tupla)
    print_line_success('¡El plan se ha registrado exitosamente!')
    con.commit()

   
# Función que realiza la consulta de todos los planes en la tabla planes y los muestra al usuario
def consulta_tabla_planes(con):
    cursor_obj = con.cursor()
    cursor_obj.execute('SELECT * FROM  planes')
    cantidad_planes = cursor_obj.fetchall()  
    orden_salida = orden_consulta(cantidad_planes)
    print ("\n{:<5} {:<15} {:<10} {:<10} ".format('ID', 'NOMBRE PLAN', 'VALOR', 'CANTIDAD CANCIONES'))
    for row in orden_salida:
        id, nombre, valor, cantidad_canciones = row
        print ("{:<5} {:<15} {:<10} {:<10} ".format(id, nombre, valor, cantidad_canciones))


# Función que ordena la consulta de distintas maneras
def orden_consulta(lista: list) -> tuple:
    print('''
                        ¿EN QUE ORDEN DESEA OBTENER LA CONSULTA?
                    1. Por id
                    2. Por nombre
                    3. por valor
                    4. por cantidad de canciones a las que puede acceder\n''')

    opc = input("\tDigite una opcion: ")
    if (opc == '1'):
        orden = sorted(lista, key = lambda id : id[0])
        return orden
        
    elif(opc == '2'):
        orden = sorted(lista, key = lambda nombre : nombre[1])
        return orden
        
    elif(opc == '3'):
        orden = sorted(lista, key = lambda valor : valor[2])
        return orden

    elif(opc == '4'):
        orden = sorted(lista, key = lambda cantidad_canciones : cantidad_canciones[3])
        return orden  


# Función que permite hacer una consulta individual de un cliente por medio de su identificacion registrada
def consulta_individual_plan(con):
    cursor_obj = con.cursor()
    id = int(input('Ingrese un id: '))
    busqueda = 'SELECT * FROM planes WHERE id_plan = '
    id_busqueda = busqueda + str(id)
    cursor_obj.execute(id_busqueda)
    datos_plan = cursor_obj.fetchall()
    print ("\n{:<5} {:<15} {:<10} {:<10} ".format('ID', 'NOMBRE_PLAN', 'VALOR', 'CANTIDAD CANCIONES'))
    for row in datos_plan:
        id, nombre, valor, cantidad_canciones = row
        print ("{:<5} {:<15} {:<10} {:<10} ".format(id, nombre, valor, cantidad_canciones))

# Función que realiza la gestión del la sección planes por medio de menú
def actualizar_datos_plan(con):
    salir_actualizar = False
    while not salir_actualizar:
        print('''
                            ACTUALIZAR INFORMACIÓN PLAN
                        1. Nombre
                        2. Valor
                        3. Cantidad de canciones
                        4. Ir al menu anterior\n''')

        opc = input("\tDigite una opcion: ")
        if (opc == '1'):
            actualizar_info_tablas(con, 'el nombre', nombre_columna='nombre_plan', nombre_tabla='planes', primary_key='id_plan', longitud=15)
            
        elif(opc == '2'):
            actualizar_info_tablas(con, 'el valor', nombre_columna='valor', nombre_tabla='planes', primary_key='id_plan', longitud=5)

        elif(opc == '3'):
            actualizar_info_tablas(con, 'la cantidad de canciones', nombre_columna='cantidad_canciones', nombre_tabla='planes', primary_key='id_plan', longitud=4)
            
        elif(opc == '4'):
            salir_actualizar = True
        
        else:
            print("\t\n¡Opcion no valida. Digite una opción nuevamente!")
        


                
"""----------------------------- Pruebas -----------------------------"""


