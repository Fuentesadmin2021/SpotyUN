"""De la librería datetime se importa la clase datetime, la cuál nos permite registrar
de manera automática la fecha y hora del registro del cliente en el metodo cliente"""
"""Se importa los diferentes modulos para el manejo de modulos dentro de cliente"""
"""Importamos el modulo validacion_datos para realizar las diferentes validaciones de los datos
para la base de datos"""
"""Se importa el modulo decorador para relizar lo diferentes decoradores de los metodos"""
from datetime import datetime
from manejador_planes import *
from manejadorbd import *
from validacion_datos import *
from paquetes_ad.decorador import *


# Función que obtiene los datos de un cliente antes de registrarlo retornando una tupla
# De acuerdo al origen y necesidad de los datos vamos a realizar las diferentes validaciones
# para el registro de los datos, se usan metodos del modulo validacion_datos como
# validar_nombre, validar_apellido, validar_dni, validar_telefono, validar_email, validar_fecha
# También se verfica la existencia en la tabla clientes y planes del id suministrado para evitar duplicados
# o posibles errores de registro



# Función que registra un cliente en la tabla clientes
def registrar_cliente(con, tupla: tuple):
    cursor = con.cursor()
    datos_cliente = tupla
    cursor.execute('''INSERT INTO clientes VALUES (?,?,?,?,?,?,?,?,?,?)''', datos_cliente[0:-1])
    con.commit()
    print_line_success("¡El registro se ha realizado exitosamente!")


# Función que permite relizar la consulta de los clientes registrados en la tabla clientes
def consulta_tabla_clientes(con):
    cursor_obj = con.cursor()
    cursor_obj.execute('SELECT id_cliente, nombre_cliente, apellido FROM  clientes')
    cantidad_clientes = cursor_obj.fetchall()
    orden_salida = orden_consulta(cantidad_clientes)
    print("\n{:<20} {:<20} {:<20}".format('IDENTIFICACIÓN', 'NOMBRE', 'APELLIDO'))
    for row in orden_salida:
        id, nombre, apellido = row
        print("{:<20} {:<20} {:<20}".format(id, nombre, apellido))


# Función que ordena la consulta a demanda del usuario
def orden_consulta(lista: list) -> tuple:
    print_line_menu('''
                        ¿EN QUE ORDEN DESEA OBTENER LA CONSULTA?
                    1. Por id
                    2. Por nombre
                    3. por apellido\n''')

    opc = input("\n\tDigite una opcion: ")
    if (opc == '1'):
        orden = sorted(lista, key=lambda id: id[0])
        return orden

    elif (opc == '2'):
        orden = sorted(lista, key=lambda nombre: nombre[1])
        return orden

    elif (opc == '3'):
        orden = sorted(lista, key=lambda apellido: apellido[2])
        return orden


# Función que permite realizar la consulta individual de un cliente por medio de su id
def consulta_individual_cliente(con):
    cursor_obj = con.cursor()
    id = int(input('\nIngrese su identificación: ').strip())
    busqueda = 'SELECT * FROM clientes WHERE id_cliente = '
    id_busqueda = busqueda + str(id)
    cursor_obj.execute(id_busqueda)
    datos_cliente = cursor_obj.fetchall()
    print("\n{:<30} {:<30} {:<30} {:<30} {:<30} ".format('IDENTIFICACION', 'NOMBRE', 'APELLIDO', 'PAIS', 'CIUDAD'))
    for row in datos_cliente:
        id, nombre, apellido, pais, ciudad, celular, correo, fecha_pago, numero_tc, estado = row
        print("{:<30} {:<30} {:<30} {:<30} {:<30} ".format(id, nombre,
                                                           apellido, pais, ciudad))

    print("\n{:<30} {:<30} {:<30} {:<30} {:<30} ".format('CELULAR', 'CORREO', 'FECHA DE PAGO', 'NUMERO TC', 'ESTADO PAGO'))
    for row in datos_cliente:
        id, nombre, apellido, pais, ciudad, celular, correo, fecha_pago, numero_tc, estado = row
        print("{:30} {:<30} {:<30} {:<30} {:<30} ".format(celular, correo,
                                                          fecha_pago, numero_tc, estado))


# FUnción que permite relizar la consulta del correo del cliente de acuerdo a su id
def consulta_correo_cliente(con, id_cliente: int) -> str:
    cursor_obj = con.cursor()
    cursor_obj.execute(f'SELECT correo FROM clientes WHERE id_cliente = {id_cliente}')
    correo = cursor_obj.fetchall()
    return correo


# Función para verificar si un cliente esta registrado o no
# La cuál nos permite dar a paso a sección de la aplicación de acuerdo a la existencia del cliente
def verificacion_cliente(con) -> bool or int:
    id_cliente = input('\nIngrese su identificación: ')
    cursor_obj = con.cursor()
    cursor_obj.execute(f'SELECT id_cliente FROM clientes WHERE id_cliente = {id_cliente}')
    id = cursor_obj.fetchone()
    if id == None:
        print('¡Antes de poder registrar otro plan o lista de reproducción debes ser un cliente registrado!')
        return False
    else:
        print_line_success('¡Validación de usuario exitosa!')
        return int(id[0])


# Función que crea un menu para actualizar de manera individual los datos básicos de un cliente
# a través de su id y la función actualizar_info_tablas
def actualizar_datos_cliente(con):
    salir_actualizar_datos = False
    while not salir_actualizar_datos:

        print_line_menu('''
                                ACTUALIZAR DATOS CLIENTE
                            1. Nombre
                            2. Apellido
                            3. Celular
                            4. Tarjeta de crédito
                            5. País
                            6. Ciudad
                            7. Correo
                            8. Ir al menu anterior\n''')

        opc = input("\n\tDigite una opcion: ").strip()
        if (opc == '1'):
            actualizar_info_tablas(con, 'el nombre', nombre_columna='nombre_cliente', nombre_tabla='clientes', primary_key='id_cliente', longitud=30)

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
            actualizar_info_tablas(con, 'el correo', nombre_columna='correo', nombre_tabla='clientes', primary_key='id_cliente', longitud=45)


        elif (opc == '8'):
            salir_actualizar_datos = True
        
        else:
            print_line_error("¡Opcion no valida. Digite una opción nuevamente!")


"""----------------------------- Pruebas -----------------------------"""

