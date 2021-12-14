from manejadorbd import sql_conexion
from manejador_clientes import planes_disponibles
from manejador_clientes import verificacion_cliente

info_cliente = (1016048190, 'oscar', 'vil', 'colom', 'bogota', 321546, 'o@.c', '2012-12-12', '321654987', 'Activo', 1)
# Función que obtiene los datos para registrar un plan
# información capturada cuando el cliente hace el registro por primera vez
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
def plan_cliente(con, id: int) -> tuple:
    id_cliente = id
    planes_disponibles(con)
    id_plan = input('Ingresa el ID del plan que quieres contratar: ')   
    datos = (id_cliente, id_plan)
    return datos


# Función que consulta los planes contratados por el cliente
def consulta_planes_cliente(con, id: int):
    cursor_obj = con.cursor()
    cursor_obj.execute(f'SELECT * FROM planes_cliente WHERE id_cliente = {id}')
    planes = cursor_obj.fetchall()
    print ("\n{:<15} {:<20} ".format('ID CLIENTE', 'ID PLAN'))
    for row in planes:
        id_cliente, id_plan, = row
        print ("{:<15} {:<20} ".format(id_cliente, id_plan))  


# Función que agrega plan a la base de datos
def agregar_plan_cliente(con, nuevo_plan: tuple) -> str:
    cursor_obj = con.cursor()
    cursor_obj.execute('''INSERT INTO planes_cliente VALUES(?,?)''', nuevo_plan)
    con.commit()
    return'¡has agregado otro plan exitosamente!'


# Función que consulta el plan contratado por el cliente
def consulta_individual_plan_cliente(con, id: int):
    cursor_obj = con.cursor()
    id_plan = input("Ingrese el ID del plan contratado que desea consultar:")
    info_plan = cursor_obj.execute(f'SELECT * FROM planes WHERE id_plan = {id_plan}')
    info_plan = cursor_obj.fetchall()
    print ("\n{:<15} {:<15} {:<15} {:<15} {:<20} ".format('ID CLIENTE', 'ID PLAN', 'NOMBRE', 'VALOR', 'CANTIDAD CANCIONES'))
    for row in info_plan:
        id_plan, nombre, valor, cantidad_canciones = row
        print ("{:<15} {:<15} {:<15} {:<15} {:<20} ".format(id, id_plan, nombre, valor, cantidad_canciones))

  
# Función que getiona la sección planes_cliente a través de un menú
def menu_planes_cliente(con, id):
    state = True
    while state:
        opc = input("""
                    MENU SECCIÓN PLANES CLIENTE
                1. Registrar otro plan
                2. Consultar planes de cliente
                3. Consulta individual de un plan
                4. Ir al menu anterior
                
                Digite una opción: """)
        
        if opc == "1":
            nuevo_plan = plan_cliente(con, id)
            agregar_plan_cliente(con, nuevo_plan)

        elif opc == "2":
            consulta_planes_cliente(con, id)

        elif opc == "3":
            consulta_individual_plan_cliente(con, id)

        elif opc == "4":
            state = False
            

# print(plan_desde_cliente(info_cliente))


