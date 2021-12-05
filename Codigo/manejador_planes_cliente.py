from manejador_planes import registrar_plan
from manejadorbd import sql_conexion
from manejador_clientes import cliente

# funcion que obtiene los datos necesarios para que un usuario registre un plan
def plan_desde_cliente(con, func_cliente):
    id_cliente = func_cliente[0]
    id_plan = func_cliente[-1]
    datos = (id_cliente, id_plan)
    print('Envio exitoso de información')
    return datos

def plan_cliente():
    id_cliente = input('Ingrese id cliente: ')
    id_plan = input('Ingrese id plan: ')
    datos = (id_plan, id_cliente)
    print('registro exitoso en plan_cliente')
    return datos

def registrar_plan_cliente(con, datos):
    cursor_obj=con.cursor()
    insercion = datos
    cursor_obj.execute('''INSERT INTO planes_cliente VALUES(?,?)''', insercion)
    con.commit()

def plan(con, id_cliente):
    cursor_obj = con.cursor()
    cursor_obj.execute(f'SELECT id_plan FROM planes_cliente WHERE dni_cliente = {id_cliente}')
    id_plan = cursor_obj.fetchone()
    return id_plan

"""mi_conexion = sql_conexion()
datos = plan_cliente()
registrar_plan_cliente(mi_conexion, datos)"""

