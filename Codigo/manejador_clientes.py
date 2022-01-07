#--- el modulo 'datetime' importado a continuación lo utilizamos como herramienta para obtener la fecha en la cual un cliente se registra 
from datetime import datetime
from manejadorbd import *
from validacion_datos import *
from decorador import *
from manejador_planes import *

# funcion que obtiene los datos de un cliente antes de registrarlo
def cliente(con) -> tuple:
    id = validacion_numero(input('Número de identificación: '), 12)
    id_cliente = validacion_existencia_todas(con, nombre_tabla='clientes', nombre_columna='id_cliente', primary_key='id_cliente', id=id)
    while id_cliente == True:
        print('\n¡El número de identificación ya existe, por favor ingrese otro número de identificación!')
        id = validacion_numero(input('Número de identificación: '), 12)
        id_cliente = validacion_existencia_todas(con, nombre_tabla='clientes', nombre_columna='id_cliente', primary_key='id_cliente', id=id)

    nombre = validacion_letra(input('Nombre: '), 30)
    apellido = validacion_letra(input('Apellido: '), 30)
    pais = validacion_letra(input('Pais: '), 30)
    ciudad = validacion_letra(input('Ciudad: '), 30)
    celular = validacion_telefono(input('Celular: '), 15)
    correo = validacion_correo(input('Correo electrónico: '), 35)
    fecha_pago = datetime.strftime(datetime.now(), '%Y-%m-%d')
    numero_tc = validacion_tc(input('Ingrese el numero de su tarjeta de credito\n' +
                                                              'sin espacios ni caracteres especiales: '), 19)
    estado_pago = 'Activo'
    planes_disponibles(con)
    print("")
    plan = int(input('Ingresa el ID del plan que desea contratar: '))
    datos_cliente = (
        id_cliente,
        nombre,
        apellido,
        pais,
        ciudad,
        celular,
        correo,
        fecha_pago,
        numero_tc,
        estado_pago,
        plan)
    return datos_cliente


# funcion que registra un cliente en la base de datos
@decorador_funcion
def registrar_cliente(con, tupla: tuple):
    cursor = con.cursor()
    datos_cliente = tupla
    cursor.execute('''INSERT INTO clientes VALUES (?,?,?,?,?,?,?,?,?,?)''', datos_cliente[0:-1])
    con.commit()
    print("¡El registro se ha realizado exitosamente!")


# funcion que realiza una consulta rapida de los planes el la base de datos



'''funcion que realiza una consulta de todos los
clientes registradas en la base de datos'''

@decorador_funcion
def consulta_tabla_clientes(con):
    cursor_obj = con.cursor()
    cursor_obj.execute('SELECT id_cliente, nombre_cliente, apellido FROM  clientes')
    cantidad_clientes = cursor_obj.fetchall()
    orden_salida = orden_consulta(cantidad_clientes)
    print("\n{:<20} {:<20} {:<20}".format('IDENTIFICACIÓN', 'NOMBRE', 'APELLIDO'))
    for row in orden_salida:
        id, nombre, apellido = row
        print("{:<20} {:<20} {:<20}".format(id, nombre, apellido))


# función que ordena la consulta de distintas maneras
def orden_consulta(lista: list) -> tuple:
    print('''
                        ¿EN QUE ORDEN DESEA OBTENER LA CONSULTA?
                    1. Por id
                    2. Por nombre
                    3. por apellido\n''')

    opc = input("\tDigite una opcion: ")
    if (opc == '1'):
        orden = sorted(lista, key=lambda id: id[0])
        return orden

    elif (opc == '2'):
        orden = sorted(lista, key=lambda nombre: nombre[1])
        return orden

    elif (opc == '3'):
        orden = sorted(lista, key=lambda apellido: apellido[2])
        return orden


'''funcion que hace una consulta individual de un cliente 
por medio del id_cliente registrado en la base de datos'''

@decorador_funcion
def consulta_individual_cliente(con):
    cursor_obj = con.cursor()
    id = int(input('Ingrese su identificación: ').strip())
    busqueda = 'SELECT * FROM clientes WHERE id_cliente = '
    id_busqueda = busqueda + str(id)
    cursor_obj.execute(id_busqueda)
    datos_cliente = cursor_obj.fetchall()
    print("\n{:<30} {:<30} {:<30} {:<30} {:<30} ".format('IDENTIFICACION',
                                                         'NOMBRE', 'APELLIDO', 'PAIS', 'CIUDAD'))
    for row in datos_cliente:
        id, nombre, apellido, pais, ciudad, celular, correo, fecha_pago, numero_tc, estado = row
        print("{:<30} {:<30} {:<30} {:<30} {:<30} ".format(id, nombre,
                                                           apellido, pais, ciudad))

    print("\n{:<30} {:<30} {:<30} {:<30} {:<30} ".format('CELULAR', 'CORREO',
                                                         'FECHA DE PAGO', 'NUMERO TC', 'ESTADO PAGO'))
    for row in datos_cliente:
        id, nombre, apellido, pais, ciudad, celular, correo, fecha_pago, numero_tc, estado = row
        print("{:30} {:<30} {:<30} {:<30} {:<30} ".format(celular, correo,
                                                          fecha_pago, numero_tc, estado))


def consulta_correo_cliente(con, id: int) -> str:
    cursor_obj = con.cursor()
    cursor_obj.execute(f'SELECT correo FROM clientes WHERE id_cliente = {id}')
    correo = cursor_obj.fetchall()
    return correo


# Función para verificar si un cliente esta registrado o no
def verificacion_cliente(con) -> bool or int:
    id_cliente = input('Ingrese su identificacion: ')
    cursor_obj = con.cursor()
    cursor_obj.execute(f'SELECT id_cliente FROM clientes WHERE id_cliente = {id_cliente}')
    id = cursor_obj.fetchone()
    if id == None:
        print('¡Antes de poder registrar otro plan debes ser un cliente registrado!')
        return False
    else:
        return int(id[0])

# funcion que elimina el registro de un cliente en la base de datos



# funcion que crea un menu para actualizar de manera individual los datos basicos de un cliente
def actualizar_datos_cliente(con):
    salir_actualizar_datos = False
    while not salir_actualizar_datos:

        print('''
                                ACTUALIZAR DATOS CLIENTE
                            1. Nombre
                            2. Apellido
                            3. Celular
                            4. Tarjeta de crédito
                            5. País
                            6. Ciudad
                            7. Correo
                            8. Estado de subcripción
                            9. Ir al menu anterior\n''')

        opc = input("\tDigite una opcion: ").strip()
        if (opc == '1'):
            actualizar_info_tablas(con, 'el nombre', nombre_columna='nombre_cliente', nombre_tabla_='clientes', primary_key='id_cliente', longitud=30)

        elif (opc == '2'):
            actualizar_info_tablas(con, 'el apellido', nombre_columna='apellido', nombre_tabla='clientes', primary_key='id_cliente', longitud=30)

        elif (opc == '3'):
            actualizar_info_tablas(con, 'el celular', nombre_columna='celular', nombre_tabla='clientes', primary_key='id_cliente', longitud=15)
        
        elif (opc == '4'):
            actualizar_info_tablas(con, 'la tarjeto de crédito', nombre_columna='numero_tc', nombre_tabla='clientes', primary_key='id_cliente', longitud=19)
            
        elif (opc == '5'):
            actualizar_info_tablas(con, 'el país', nombre_columna='pais', nombre_tabla='clientes', primary_key='id_cliente', longitud=30)
            
        elif (opc == '6'):
            actualizar_info_tablas(con, 'la ciudad', nombre_columna='ciudad', nombre_tabla='clientes', primary_key='id_cliente', longitud=30)

        elif (opc == '7'):
            actualizar_info_tablas(con, 'el correo', nombre_columna='correo', nombre_tabla='clientes', primary_key='id_cliente', longitud=35)

        elif (opc == '8'):
            actualizar_info_tablas(con, 'el estado de suscripción', nombre_columna='estado_pago', nombre_tabla='clientes', primary_key='id_cliente', longitud=15)

        elif (opc == '9'):
            salir_actualizar_datos = True
        
        else:
            print("\t\n¡Opcion no valida. Digite una opción nuevamente!")


"""----------------------------- Pruebas -----------------------------"""

def actualizar_info_tablas(con, info: str, nombre_columna: str, nombre_tabla: str, primary_key: str, longitud: int):
    cursor_obj = con.cursor()
    state = True
    while state:
        id = input('Ingrese el id: ').strip()
        if id_v := validacion_existencia_todas(con, nombre_tabla, nombre_columna, primary_key, id) == True:
            id = int(id)
            state = False
        else:
            print('\nEl id ingresado no existe en la base de datos')
    elemento = validacion_longitud(input(f'Ingrese el nuevo {info}: '), longitud)
    actualizar = f'UPDATE {nombre_tabla} SET {nombre_columna} = ? WHERE {primary_key} = ?'
    info_actualizar = (elemento, id)
    cursor_obj.execute(actualizar, info_actualizar)
    con.commit()
    print(f"!Su {info} se ha actualizado exitosamente¡")