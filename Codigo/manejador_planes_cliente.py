# Funciones importadas para lo modulos o procesos dentro del modulo manejador_planes_cliente.py
from manejador_clientes import planes_disponibles
from controlador.decorador import *

# Función que obtiene los datos para registrar un plan
# Esta Información es capturada cuando el cliente hace el registro por primera vez
def plan_desde_cliente(info_cliente: tuple) -> tuple:
    id_cliente = info_cliente[0]
    id_plan = info_cliente[-1]
    datos = (id_cliente, id_plan)
    return datos

# Función que registra plan en la tabla planes_cliente
def registrar_plan_cliente(con, datos: tuple):
    cursor_obj=con.cursor()
    insercion = datos
    cursor_obj.execute('''INSERT INTO planes_cliente VALUES(?,?)''', insercion)
    con.commit()


# Función que pide a un usuario los datos necesarios para registrar un plan
def plan_cliente(con, id_cliente: int) -> tuple:
    id_cliente_ = id_cliente
    planes_disponibles(con)
    id_plan = input('\nIngresa el ID del plan que quieres contratar: ')
    datos = (id_cliente_, id_plan)
    return datos


# Función que consulta los planes contratados por el cliente
def consulta_planes_cliente(con, id_cliente: int):
    cursor_obj = con.cursor()
    cursor_obj.execute(f'SELECT * FROM planes_cliente WHERE id_cliente = {id_cliente}')
    planes = cursor_obj.fetchall()
    print ("\n{:<15} {:<20} ".format('ID CLIENTE', 'ID PLAN'))
    for row in planes:
        id_cliente_, id_plan, = row
        print ("{:<15} {:<20} ".format(id_cliente_, id_plan))


# Función que agrega plan a la base de datos
def agregar_plan_cliente(con, nuevo_plan: tuple) -> str:
    cursor_obj = con.cursor()
    cursor_obj.execute('''INSERT INTO planes_cliente VALUES(?,?)''', nuevo_plan)
    con.commit()
    return'¡has agregado otro plan exitosamente!'


# Función que consulta el plan contratado por el cliente
def consulta_individual_plan_cliente(con, id_cliente: int):
    cursor_obj = con.cursor()
    id_plan = input("\nIngrese el ID del plan contratado que desea consultar: ")
    info_plan = cursor_obj.execute(f'SELECT * FROM planes WHERE id_plan = {id_plan}')
    info_plan = cursor_obj.fetchall()
    print ("\n{:<15} {:<15} {:<15} {:<15} {:<20} ".format('ID CLIENTE', 'ID PLAN', 'NOMBRE', 'VALOR', 'CANTIDAD CANCIONES'))
    for row in info_plan:
        id_plan, nombre, valor, cantidad_canciones = row
        print ("{:<15} {:<15} {:<15} {:<15} {:<20} ".format(id_cliente, id_plan, nombre, valor, cantidad_canciones))

  
# Función que getiona la sección planes_cliente a través de un menú
def menu_planes_cliente(con, id_cliente: int):
    state = True
    while state:
        opc = input("""
                    MENU SECCIÓN PLANES CLIENTE
                1. Consulta individual de un plan
                2. Consultar planes de cliente
                3. Registrar otro plan
                4. Ir al menu anterior
                
                Digite una opción: """)
        
        if opc == "1":
            consulta_individual_plan_cliente(con, id_cliente)

        elif opc == "2":
            consulta_planes_cliente(con, id_cliente)

        elif opc == "3":
            nuevo_plan = plan_cliente(con, id_cliente)
            agregar_plan_cliente(con, nuevo_plan)

        elif opc == "4":
            state = False
        
        else:
            print_line_error("¡Opcion no valida. Digite una opción nuevamente!")
            




