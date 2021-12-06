from manejadorbd import sql_conexion
from manejador_clientes import planes_disponibles


# funcion que obtiene los datos para registrar un plan, cuando un cliente se registra
def plan_desde_cliente(con, func_cliente):
    id_cliente = func_cliente[0]
    id_plan = func_cliente[-1]
    datos = (id_cliente, id_plan)
    return datos

# funcion que registra plan en la base de datos
def registrar_plan_cliente(con, datos):
    cursor_obj=con.cursor()
    insercion = datos
    cursor_obj.execute('''INSERT INTO planes_cliente VALUES(?,?)''', insercion)
    con.commit()


#------------------------------------------------------------------------------------------

# esta funcion valida que el cliente ya este registrado
def verificacion_cliente_plan(con):
    id_cliente = input('Ingrese su identificacion: ')
    cursor_obj = con.cursor()
    cursor_obj.execute(f'SELECT id_cliente FROM clientes WHERE id_cliente = {id_cliente}')
    id = cursor_obj.fetchone()
    if id == None:
        print('¡Antes de poder registrar otro plan debes ser un cliente registrado!')
        return False
    else:
        return int(id[0])

# funcion que pide a un usuario los datos necesarios para registrar un plan
def plan_cliente(con, id):
    id_cliente = id
    planes_disponibles(con)
    id_plan = input('Ingresa el ID del plan que quieres contratar: ')   
    datos = (id_cliente, id_plan)
    return datos

# funcion que consulta los planes de un cliente
def consulta_planes_cliente(con, id):
    cursor_obj = con.cursor()
    cursor_obj.execute(f'SELECT * FROM planes_cliente WHERE id_cliente = {id}')
    planes = cursor_obj.fetchall()
    print ("\n{:<15} {:<20} ".format('ID CLIENTE', 'ID PLAN'))
    for row in planes:
        id_cliente, id_plan, = row
        print ("{:<15} {:<20} ".format(id_cliente, id_plan))  


# funcion que agrega plan a la base de datos
def agregar_plan_cliente(con, nuevo_plan):
    cursor_obj = con.cursor()
    cursor_obj.execute('''INSERT INTO planes_cliente VALUES(?,?)''',nuevo_plan)
    con.commit()
    return'¡has agregado otro plan exitosamente!'

# esta funcion obtiene la información del plan que el cliente contrato y desea consultar
def consulta_individual_plan_cliente(con, id):
    cursor_obj = con.cursor()
    id_plan = input("Ingrese el ID del plan contratado que desea consultar:")
    info_plan = cursor_obj.execute(f'SELECT * FROM planes WHERE id_plan = {id_plan}')
    info_plan = cursor_obj.fetchall()
    print ("\n{:<15} {:<15} {:<15} {:<15} {:<20} ".format('ID CLIENTE', 'ID PLAN', 'NOMBRE', 'VALOR', 'CANTIDAD CANCIONES'))
    for row in info_plan:
        id_plan, nombre, valor, cantidad_canciones = row
        print ("{:<15} {:<15} {:<15} {:<15} {:<20} ".format(id, id_plan, nombre, valor, cantidad_canciones))

  
# funcion para que crea el menu de clientes
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
            




