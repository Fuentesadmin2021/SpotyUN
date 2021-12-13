from manejadorbd import sql_conexion
from validacion_datos import *
from datetime import datetime


# funcion que obtiene los datos de un cliente antes de registrarlo
def cliente(con: 'sql_conexion') -> tuple:
    id_cliente = int(validacion_numero(input('Numero de identificacion: '), 12))
    nombre = validacion_letra(input('Nombre: '), 30)
    apellido = validacion_letra(input('Apellido: '), 30)
    pais = validacion_letra(input('Pais: '), 30)
    ciudad = validacion_letra(input('Ciudad: '), 30)
    celular = validacion_numero(input('Celular: '), 15)
    correo = validacion_correo(input('Correo electrónico: '), 35)
    fecha_pago = datetime.strftime(datetime.now(), '%Y-%m-%d')
    numero_tc = validacion_numero(input('Ingrese el numero de su tarjeta de credito\n' +
                                                              'sin espacios ni caracteres especiales: '), 19)
    estado_pago = 'Activo'
    planes_disponibles(con)
    plan = int(input('Ingresa el ID del plan que desea contratar: '))
    datos_cliente = (
    id_cliente, nombre, apellido, pais, ciudad, celular, correo, fecha_pago, numero_tc, estado_pago, plan)
    return datos_cliente


# funcion que registra un cliente en la base de datos
def registrar_cliente(con: 'sql_conexion', tupla: tuple):
    cursor = con.cursor()
    datos_cliente = tupla
    cursor.execute('''INSERT INTO clientes VALUES (?,?,?,?,?,?,?,?,?,?)''', datos_cliente[0:-1])
    con.commit()
    print("¡El registro se ha realizado exitosamente!")


# funcion que realiza una consulta rapida de los planes el la base de datos
def planes_disponibles(con: 'sql_conexion'):
    cursor_obj = con.cursor()
    cursor_obj.execute('SELECT * FROM  planes')
    cantidad_planes = cursor_obj.fetchall()
    print("\n{:<5} {:<20} {:<20} {:<20} ".format('ID', 'NOMBRE_PLAN', 'VALOR', 'CANTIDAD CANCIONES'))
    for row in cantidad_planes:
        id, nombre, valor, cantidad_canciones = row
        print("{:<5} {:<20} {:<20} {:<20} ".format(id, nombre, valor, cantidad_canciones))


'''funcion que realiza una consulta de todos los
clientes registradas en la base de datos'''


def consulta_tabla_clientes(con: 'sql_conexion'):
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


def consulta_individual_cliente(con: 'sql_conexion'):
    cursor_obj = con.cursor()
    id = int(input('Ingrese su identificación: '))
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


def consulta_correo_cliente(con: 'sql_conexion', id: int) -> str:
    cursor_obj = con.cursor()
    cursor_obj.execute(f'SELECT correo FROM clientes WHERE id_cliente = {id}')
    correo = cursor_obj.fetchall()
    return correo


# funcion para modificar el nombre de un cliente
def actualizar_nombre_cliente(con: 'sql_conexion'):
    cursor_obj = con.cursor()
    id = input('Ingrese su identificación para modificar el nombre: ')
    nombre = input('Ingrese el nuevo nombre: ')
    actualizar = 'UPDATE clientes SET nombre_cliente = "' + nombre + '" WHERE id_cliente = '
    id_actualizar = actualizar + id
    cursor_obj.execute(id_actualizar)
    con.commit()
    print("!Su nombre se ha actualizado exitosamente¡")


# funcion para modificar el apellido de un cliente
def actualizar_apellido_cliente(con: 'sql_conexion'):
    cursor_obj = con.cursor()
    id = input('Ingrese su identificación para modificar el apellido: ')
    apellido = input('Ingrese el nuevo apellido: ')
    actualizar = 'UPDATE clientes SET apellido = "' + apellido + '" WHERE id_cliente = '
    id_actualizar = actualizar + id
    cursor_obj.execute(id_actualizar)
    con.commit()
    print("!Su apellido se ha actualizado exitosamente¡")


# funcion para modificar el numero de celular de un cliente
def actualizar_celular_cliente(con: 'sql_conexion'):
    cursor_obj = con.cursor()
    id = input('Ingrese su identificación para modificar su numero celular: ')
    celular = input('Ingrese su nuevo numero de celular: ')
    actualizar = 'UPDATE clientes SET celular = "' + celular + '" WHERE id_cliente = '
    id_actualizar = actualizar + id
    cursor_obj.execute(id_actualizar)
    con.commit()
    print("!Su numero de celular se ha actualizado exitosamente¡")


# funcion para modificar el correo de un cliente
def actualizar_correo_cliente(con: 'sql_conexion'):
    cursor_obj = con.cursor()
    id = input('Ingrese su identificación para modificar su correo: ')
    correo = input('Ingrese su nuevo correo: ')
    actualizar = 'UPDATE clientes SET correo = "' + correo + '" WHERE id_cliente = '
    id_actualizar = actualizar + id
    cursor_obj.execute(id_actualizar)
    con.commit()
    print("!Su dirección de correo se ha actualizado exitosamente¡")


# funcion para modificar el numero de tarjeta de credito de un cliente registrada inicialmente
def actualizar_tarjeta_credito_cliente(con: 'sql_conexion'):
    cursor_obj = con.cursor()
    id = input('Ingrese su identificación para modificar su TC: ')
    tc = input('Ingrese su nuevo numero de Tarjeta Credito: ')
    actualizar = 'UPDATE clientes SET numero_tc = "' + tc + '" WHERE id_cliente = '
    id_actualizar = actualizar + id
    cursor_obj.execute(id_actualizar)
    con.commit()
    print("!Su numero de Tarjeta de Credito se ha actualizado exitosamente¡")


# funcion para modificar el pais que registro el cliente inicialmente
def actualizar_pais_cliente(con: 'sql_conexion'):
    cursor_obj = con.cursor()
    id = input('Ingrese su identificación para modificar el pais: ')
    pais = input('Ingrese su pais: ')
    actualizar = 'UPDATE clientes SET pais = "' + pais + '" WHERE id_cliente = '
    id_actualizar = actualizar + id
    cursor_obj.execute(id_actualizar)
    con.commit()
    print("!Su pais registrado se ha actualizado exitosamente¡")


# funcion para modificar la ciudad que registro el cliente inicialmente
def actualizar_ciudad_cliente(con: 'sql_conexion'):
    cursor_obj = con.cursor()
    id = input('Ingrese su identificación para modificar la ciudad: ')
    ciudad = input('Ingrese su nueva ciudad: ')
    actualizar = 'UPDATE clientes SET ciudad = "' + ciudad + '" WHERE id_cliente = '
    id_actualizar = actualizar + id
    cursor_obj.execute(id_actualizar)
    con.commit()
    print("!La cuidad registrada se ha actualizado exitosamente¡")


# Función para verificar si un cliente esta registrado o no
def verificacion_cliente(con: 'sql_conexion') -> False or int:
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
def borrar_cliente(con: 'sql_conexion'):
    cursor = con.cursor()
    id = input("Identificación cliente: ")
    borrar = "DELETE FROM clientes WHERE id_cliente = %s" % id
    cursor.execute(borrar)
    con.commit()
    print("\nSu registro a sido eliminado :)")


# funcion que crea un menu para actualizar de manera individual los datos basicos de un cliente
def actualizar_datos_cliente(con: 'sql_conexion'):
    print('''
                            ACTUALIZAR DATOS CLIENTE
                        1. Nombre
                        2. Apellido
                        3. Celular
                        4. Tarjeta de credito
                        5. Pais
                        6. Ciudad
                        7. Correo
                        8. Ir al menu anterior\n''')

    opc = input("\tDigite una opcion: ")
    if (opc == '1'):
        actualizar_nombre_cliente(con)
        # salir = True

    elif (opc == '2'):
        actualizar_apellido_cliente(con)
        # salir = True

    elif (opc == '3'):
        actualizar_celular_cliente(con)
        # salir = True

    elif (opc == '4'):
        actualizar_tarjeta_credito_cliente(con)
        # salir = True

    elif (opc == '5'):
        actualizar_pais_cliente(con)
        # salir = True

    elif (opc == '6'):
        actualizar_ciudad_cliente(con)
        # salir = True

    elif (opc == '7'):
        actualizar_correo_cliente(con)

    elif (opc == '8'):
        pass


"""----------------------------- Pruebas -----------------------------"""