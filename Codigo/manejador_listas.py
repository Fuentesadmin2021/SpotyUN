#--------------- El conjunto de modulos importadados a continuación es utilizado como herramienta para el envio de correos---------------
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#----------------------------------------------------------------------------------------------------------------------------------------
from manejador_clientes import consulta_correo_cliente, verificacion_cliente
from manejador_canciones import reproducir_cancion
from manejadorbd import sql_conexion
from decorador import *

# Función para realizar la consulta de datos de la canción como id_canción, nombre_canción, interprete, album
@decorador_funcion
def id_cancion_lista(con) -> list:
    canciones = input('\nIngrese el id de cancion que desea agregar a su lista: ')
    while canciones == '0':
        break
    cursor_obj = con.cursor()
    cursor_obj.execute(f"SELECT * FROM canciones WHERE id_cancion = {canciones}")
    filas = cursor_obj.fetchall()
    for row in filas:
        id_cancion = row[0]
        nombre_cancion = row[1]
        interprete = row[4]
        album = row[3]
    lista_info_cancion = [id_cancion, nombre_cancion, interprete, album]
    return type(lista_info_cancion)

# Función para consultar la cantidad de canciones por plan de acuerdo al registro del cliente
def plan_cliente(con, id: int) -> int:
    cursor_obj = con.cursor()
    cursor_obj.execute(f'SELECT id_plan FROM planes_cliente WHERE id_cliente = {id}')
    id_plan_cliente = cursor_obj.fetchone()
    cursor_obj.execute(f'SELECT cantidad_canciones FROM planes WHERE id_plan = {id_plan_cliente[0]}')
    cant_canciones = cursor_obj.fetchone()
    return cant_canciones

# Función para consultar las canciones existentes y mostrarlas en pantalla
def consulta_tabla_canciones_lista(con):
    cursor_obj = con.cursor()
    cursor_obj.execute('SELECT id_cancion, nombre_cancion, genero, album, interprete  FROM canciones')
    cantidad_canciones = cursor_obj.fetchall()
    print("\n{:<12} {:<20} {:<20} {:<20} {:<20}".format('ID', 'NOMBRE', 'GENERO', 'ALBUM', 'INTERPRETE(S)'))
    for row in cantidad_canciones:
        id, nombre, genero, album, interprete = row
        print("{:<12} {:<20} {:<20} {:20} {:20}".format(id, nombre, genero, album, interprete))

# Función para agregar en un tupla la información correspondiente para la tabla listas
# necestamos el id_cliente y la lista info_canciones
def info_lista(con, id_cliente: int) -> tuple:
    id_c = id_cliente
    info_canciones = id_cancion_lista(con)
    info_canciones.append(id_c)
    return info_canciones

# Función para registrar la información en la tabla listas
def registrar_lista_cliente(con, tupla: tuple):
    cursor = con.cursor()
    cursor.execute('''INSERT INTO listas VALUES (?,?,?,?,?)''', tupla)
    con.commit()
    print("¡¡El registro se ha realizado exitosamente!!")


# Función para consultar la lista de canciones registradas por el cliente
def consulta_tabla_listas(con, id_c: int):
    cursor_obj = con.cursor()
    cursor_obj.execute(f'SELECT id_cancion, nombre_cancion, interprete, album FROM listas WHERE id_cliente = {id_c}')
    cantidad_canciones = cursor_obj.fetchall()
    print("\n{:<12} {:<30} {:<20} {:<20}".format('ID_CANCIÓN', 'NOMBRE', 'INTERPRETE', 'ALBUM'))
    for row in cantidad_canciones:
        id, nombre, interprete, album = row
        print("{:<12} {:<30} {:<20} {:20}".format(id, nombre, interprete, album))


# Función que borra una lista de la base de datos
def borrar_lista(con, id_cliente: int) -> str:
    cursor_obj = con.cursor()
    cursor_obj.execute(f'DELETE FROM listas WHERE id_cliente = {id_cliente}')
    con.commit()
    return 'Tu lista ha sido eliminada'


# Función para realizar la consulta de la tabla listas para poder enviarla en el correo electrónico
def consulta_tabla_listas_email(con, id_c: int) -> list:
    cursor_obj = con.cursor()
    cursor_obj.execute(f'SELECT id_cancion, nombre_cancion, interprete, album FROM listas WHERE id_cliente = {id_c}')
    cantidad_canciones = cursor_obj.fetchall()
    lista_str = ''
    for row in cantidad_canciones:
        id, nombre, interprete, album = row
        lista_str += ("\n{:<20} {:<40} {:<40} {:40}".format(id, nombre, interprete, album))
    return lista_str


# Función para enviar el mensaje con la lista de reproducción del cliente
def enviar_mensaje(con, id_c: int):
    titulo_lista = ("\n{:<20} {:<40} {:<60} {:<60}".format('ID_CANCIÓN', 'NOMBRE', 'INTERPRETE', 'ALBUM'))
    mensaje = MIMEMultipart()
    mensaje['Subject'] = 'CONFIRMACION DE LISTA DE REPRODUCCIÓN'
    cuerpo = f'Señor usuario su lista de reproducción se muestra a continuación:\n\n\n{titulo_lista}\n{consulta_tabla_listas_email(con, id_c)}'
    mensaje.attach(MIMEText(cuerpo, 'plain'))
    texto = mensaje.as_string()
    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    correo = consulta_correo_cliente(con, id_c)
    servidor.login('conectandotropadelta@gmail.com', 'conectandodelta')
    servidor.sendmail('conectandotropadelta@gmail.com', correo, texto)
    servidor.quit()
    print("Envio exitoso")


# Función para realizar la gestión de la sección listas de reproducción
def menu_lista(con, id: int):
    state = True
    while state:
        opc = input("""
            MENU SECCIÓN LISTAS DE REPRODUCCIÓN
        1. Crear una lista
        2. Consultar lista
        3. Actualizar lista
        4. Eliminar lista
        5. Envia correo con lista de reproducción
        6. Reproducir canciones
        7. Ir al menu anterior
    
        Digite una opción: """)
        if opc == "1":
            print("Ya estas registrado puedes crear una lista\nNúmero de canciones que puedes agregar: ",
                  plan_cliente(con, id)[0])
            cont_canciones = 1
            state_lista = True
            while state_lista and cont_canciones <= plan_cliente(con, id)[0]:
                try:
                    consulta_tabla_canciones_lista(con)
                    lista_info = info_lista(con, id)
                    registrar_lista_cliente(con, lista_info)
                    print('Falta {} canciones para completar el plan'.format(
                        plan_cliente(con, id)[0] - cont_canciones))
                    cont_canciones += 1
                    salir = input("\n¡¡Registro exitoso!!\n¿Desea agregar otra canción? y/n: ")
                    if salir == 'y' or salir == 'Y':
                        state_lista = False
                    else:
                        continue
                except:
                    print('¡Canción no encontrada en la base de datos!')
        elif opc == "2":
            consulta_tabla_listas(con, id)
            print('''¿Desea reproducir alguna canción?
                                1. Si
                                2. No''')

            opc_r = input('Digite una opción: ')
            if opc_r == "1":
                reproducir_cancion(con)
            elif opc_r == "2":
                pass
        elif opc == "3":
            print('Esta opción aun no ha sido implementada en nuestro programa')
            pass
        elif opc == "4":
            borrar_lista(con, id)
        elif opc == "5":
            enviar_mensaje(con, id)
        elif opc == "6":
            consulta_tabla_listas(con, id)
            print('\n')
            reproducir_cancion(con)

        elif opc == "7":
            state = False

        else:
            print("\t\n¡Opcion no valida. Digite una opción nuevamente!")



"""----------------------------- Pruebas -----------------------------"""

