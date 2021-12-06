import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from manejador_clientes import consulta_correo_cliente
from manejador_canciones import reproducir_cancion
from manejadorbd import sql_conexion

def verificacion_cliente(con):
    id_cliente = input('Ingrese su identificacion: ')
    cursor_obj = con.cursor()
    cursor_obj.execute(f'SELECT id_cliente FROM clientes WHERE id_cliente = {id_cliente}')
    id = cursor_obj.fetchone()
    if id == None:
        print('¡Antes de poder crear una lista debes ser un cliente registrado!')
        return False
    else:
        return int(id[0])


def id_cancion_lista(con):
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
    return lista_info_cancion


def plan_cliente(con, id):
    cursor_obj = con.cursor()
    cursor_obj.execute(f'SELECT id_plan_contrato FROM planes_cliente WHERE id_cliente = {id}')
    id_plan_cliente = cursor_obj.fetchone()
    cursor_obj.execute(f'SELECT cantidad_canciones FROM planes WHERE id_plan = {id_plan_cliente[0]}')
    cant_canciones = cursor_obj.fetchone()
    return cant_canciones


def consulta_tabla_canciones_lista(con):
    cursor_obj = con.cursor()
    cursor_obj.execute('SELECT id_cancion, nombre_cancion, genero, album, interprete  FROM canciones')
    cantidad_canciones = cursor_obj.fetchall()
    print ("\n{:<12} {:<20} {:<20} {:<20} {:<20}".format('ID', 'NOMBRE', 'GENERO', 'ALBUM', 'INTERPRETE(S)'))
    for row in cantidad_canciones:
        id, nombre, genero, album, interprete = row
        print ("{:<12} {:<20} {:<20} {:20} {:20}".format(id, nombre, genero, album, interprete))


def info_lista(con, id_cliente):
    id_c = id_cliente
    info_canciones = id_cancion_lista(con)
    info_canciones.append(id_c)
    return info_canciones


def registrar_lista_cliente(con, listas):
    cursor = con.cursor()
    cursor.execute('''INSERT INTO listas VALUES (?,?,?,?,?)''', listas)
    con.commit()
    print("¡¡El registro se ha realizado exitosamente!!")

# funcion que busca en la base de datos una lista y la imprime
def consulta_tabla_listas(con, id_c):
    cursor_obj = con.cursor()
    cursor_obj.execute(f'SELECT id_cancion, nombre_cancion, interprete, album FROM listas WHERE id_cliente = {id_c}')
    cantidad_canciones = cursor_obj.fetchall()
    print ("\n{:<12} {:<30} {:<20} {:<20}".format('ID_CANCIÓN', 'NOMBRE', 'INTERPRETE', 'ALBUM'))
    for row in cantidad_canciones:
        id, nombre, interprete, album = row
        print ("{:<12} {:<30} {:<20} {:20}".format(id, nombre, interprete, album))


# funcion que borra una lista de la base de datos
def borrar_lista(con, id_cliente):
    cursor_obj = con.cursor()
    cursor_obj.execute(f'DELETE FROM listas WHERE id_cliente = {id_cliente}')
    con.commit()
    return 'Tu lista ha sido eliminada'


def consulta_tabla_listas_email(con, id_c: int):
    cursor_obj = con.cursor()
    cursor_obj.execute(f'SELECT id_cancion, nombre_cancion, interprete, album FROM listas WHERE id_cliente = {id_c}')
    cantidad_canciones = cursor_obj.fetchall()
    lista_str = ''
    for row in cantidad_canciones:
        id, nombre, interprete, album = row
        lista_str += ("\n{:<20} {:<40} {:<60} {:60}".format(id, nombre, interprete, album))
    return lista_str


def enviar_mensaje(con, id_c: int):
    titulo_lista = ("\n{:<20} {:<40} {:<60} {:<60}".format('ID_CANCIÓN', 'NOMBRE', 'INTERPRETE', 'ALBUM'))
    mensaje = MIMEMultipart()
    mensaje['Subject'] = 'CONFIRMACION DE LISTA DE REPRODUCCIÓN'
    cuerpo = f'{titulo_lista}\n{consulta_tabla_listas_email(con, id_c)}'
    mensaje.attach(MIMEText(cuerpo, 'plain'))
    texto = mensaje.as_string()
    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    correo = consulta_correo_cliente(con, id_c)
    servidor.login('ovillalbaunal@gmail.com', 'la cambio despues del parcial')
    servidor.sendmail('ovillalbaunal@gmail.com', correo, texto)
    servidor.quit()
    print("Envio exitoso")


def menu_lista(con, id):
    state = True
    while state:
        opc = input("""
            MENU SECCIÓN LISTAS DE REPRODUCCIÓN
        1. Crear una lista
        2. Consultar lista
        3. Actualizar lista
        4. Eliminar lista
        5. Envia por correo lista
        6. Reproducir canciones
        7. Ir al menu anterior
    
        Digite una opción: """)
        if opc == "1":
            print("Ya estas registrado puedes crear una lista\nNúmero de canciones que puedes agregar: ", plan_cliente(con, id))
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
            elif opc_r =="2":
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
