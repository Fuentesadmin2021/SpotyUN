# Funciones importados desde modulos propios para manejar el módulo manejador_listas
from manejador_canciones import reproducir_cancion
from manejadorbd import *
from paquetes_ad.decorador import *
from manejador_clientes import consulta_correo_cliente
# Funciones importadas para realizar el manejo y envió de los correos
# Función smtlib usada para porder enviar un correo por medio del programa
# De  email.mime.text se importa el método MIMEText para el manejo de texto dentro del correo
# De email.mime.multipart se importa el método MIMEMultipart para el manejo de multiples partes dentro del correo
# como asunto del correo, copias ocultas y demás datos de importancia para el correo
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Función para realizar la consulta de datos de la canción como id_canción, nombre_canción, interprete, album
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
        genero = row[2]
    lista_info_cancion = [id_cancion, nombre_cancion, interprete, album, genero]
    return lista_info_cancion


# Función para consultar la cantidad de canciones por plan de acuerdo al registro del cliente
def plan_cliente(con, id_cliente: int) -> int:
    cursor_obj = con.cursor()
    cursor_obj.execute(f'SELECT id_plan FROM planes_cliente WHERE id_cliente = {id_cliente}')
    id_plan_cliente = cursor_obj.fetchone()
    cursor_obj.execute(f'SELECT cantidad_canciones FROM planes WHERE id_plan = {id_plan_cliente[0]}')
    cant_canciones = cursor_obj.fetchone()
    return cant_canciones


# Función que reliza un conteo de los registros en la tabla listas de acuerdo al id_cliente suministrado
def contar_lista(con, id_cliente: int) -> str or int:
    cursor_obj = con.cursor()
    cursor_obj.execute(f'SELECT COUNT(*) FROM listas WHERE id_cliente = {id_cliente}')
    cantidad_listas = cursor_obj.fetchone()
    if cantidad_listas[0] == None:
        return 0
    return cantidad_listas


# Función para consultar las canciones existentes en la tabla canciones y mostrarlas en pantalla
def consulta_tabla_canciones_lista(con):
    cursor_obj = con.cursor()
    cursor_obj.execute('SELECT id_cancion, nombre_cancion, genero, album, interprete  FROM canciones')
    cantidad_canciones = cursor_obj.fetchall()
    print("\n{:<12} {:<20} {:<20} {:<20} {:<20}".format('ID', 'NOMBRE', 'GENERO', 'ALBUM', 'INTERPRETE(S)'))
    for row in cantidad_canciones:
        id, nombre, genero, album, interprete = row
        print("{:<12} {:<20} {:<20} {:<20} {:<20}".format(id, nombre, genero, album, interprete))


# Función para agregar en una tupla la información correspondiente para la tabla listas
# necesitamos el id_cliente y la lista info_canciones
def info_lista(con, id_cliente: int) -> tuple:
    id_c = id_cliente
    info_canciones = id_cancion_lista(con)
    info_canciones.append(id_c)
    return info_canciones


# Función para registrar la información en la tabla listas
def registrar_lista_cliente(con, tupla: tuple):
    cursor = con.cursor()
    cursor.execute('''INSERT INTO listas VALUES (?,?,?,?,?,?)''', tupla)
    con.commit()
    print_line_success("¡¡El registro se ha realizado exitosamente!!")


# Función para consultar la lista de canciones registradas en la tabla listas
# de acuerdo al id suministrado por el cliente
def consulta_tabla_listas(con, id_cliente: int):
    cursor_obj = con.cursor()
    cursor_obj.execute(f'SELECT id_cancion, nombre_cancion, interprete, album, genero FROM listas WHERE id_cliente = {id_cliente}')
    cantidad_canciones = cursor_obj.fetchall()
    print("\n{:<12} {:<30} {:<20} {:<20} {:<20}".format('ID_CANCIÓN', 'NOMBRE', 'INTERPRETE', 'ALBUM', 'GENERO'))
    for row in cantidad_canciones:
        id, nombre, interprete, album, genero = row
        print("{:<12} {:<30} {:<20} {:20} {:<20}".format(id, nombre, interprete, album, genero))


# Función que borra una lista de reproducción de la tabla listas de acuerdo al id_cliente suministrado
def borrar_lista(con, id_cliente: int) -> str:
    cursor_obj = con.cursor()
    cursor_obj.execute(f'DELETE FROM listas WHERE id_cliente = {id_cliente}')
    con.commit()
    return print('Tu lista ha sido eliminada')


# Función que consulta la información ingresa por el cliente en la tabla listas, retorna una tupla
# una tupla de listas con la información completa de la lista de reproducción
def consulta_tabla_listas_id(con, id_cliente: int) -> bool or tuple:
    cursor_obj = con.cursor()
    cursor_obj.execute(f'SELECT id_cancion, nombre_cancion, interprete, album, genero FROM listas WHERE id_cliente = {id_cliente}')
    cantidad_canciones = cursor_obj.fetchall()
    if cantidad_canciones == []:
        return False
    else:
        return cantidad_canciones


# Función para realizar la consulta de la tabla listas para poder enviarla en el correo electrónico
# Retorna un string con formato html para poderlo ingresar en la función enviar_correo
def consulta_tabla_para_html(con, id_cliente: int) -> list:
    cursor_obj = con.cursor()
    cursor_obj.execute(f'SELECT id_cancion, nombre_cancion, interprete, album, genero FROM listas WHERE id_cliente = {id_cliente}')
    cantidad_canciones = cursor_obj.fetchall()
    lista_str = ''
    for row in cantidad_canciones:
        id, nombre_cancion, interprete, album, genero = row
        lista_str += (f"<tr><td>{id}</td><td>{nombre_cancion}</td><td>{interprete}</td><td>{album}</td><td>{genero}</td></tr>")
    return lista_str


# Función para enviar el mensaje con la lista de reproducción del cliente
def enviar_mensaje(con, id_cliente: int):
    info_tabla = consulta_tabla_para_html(con, id_cliente)
    canciones_plan= plan_cliente(con, id_cliente)[0]
    canciones_lista = contar_lista(con, id_cliente)[0]
    canciones_disponibles = canciones_plan - canciones_lista
    mensaje = MIMEMultipart()
    mensaje['Subject'] = 'CONFIRMACION DE LISTA DE REPRODUCCIÓN'
    html = f"""\
        <html>
          <head></head>
          <body>
            <p>Hi! Spotynauta<br>
               Envio tu lista de reproducción ;)               
               <br>

              <table class="default" border="2" "cellspacing="10" bordercolor="#ffffff">
                <tr>
                <th>Id canción</th><th>Nombre de canción</th><th>Interprete</th><th>Album</th><th>Género</th>
                </tr>            
                {info_tabla} 
              </table>
              <br>Información de tu plan:<br>
              
              <br>  Canciones totales del plan: {canciones_plan}<br>
              <br>  Canciones totales en tu lista: {canciones_lista}<br>
                
              <br> Canciones disponibles de tu plan: {canciones_disponibles}<br>
              
            </p>
          </body>
        </html>
        """
    mensaje.attach(MIMEText(html, 'html'))
    texto = mensaje.as_string()
    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    correo = consulta_correo_cliente(con, id_cliente)
    servidor.login('conectandotropadelta@gmail.com', 'conectandodelta')
    servidor.sendmail('conectandotropadelta@gmail.com', correo, texto)
    servidor.quit()
    print_line_success("Envio exitoso")



# Función para realizar la actualizacíón de un registro completo de la tabla listas
def actualizar_info_tabla_listas(con, tupla: tuple, id_cancion: int, id_cliente: int):
    cursor_obj = con.cursor()
    act_listas = (f"""UPDATE listas 
                    SET id_cancion = ?,
                        nombre_cancion = ?,
                        interprete = ?,
                        album = ?,
                        genero = ?
                    WHERE id_cancion = {id_cancion} and id_cliente = {id_cliente}""")
    cursor_obj.execute(act_listas, tupla)
    con.commit()


# Función que despliega el menu de sección de listas de reproducción
def menu_lista(con, id_cliente: int):
    state = True
    while state:
        print_line_menu("""
            MENU SECCIÓN LISTAS DE REPRODUCCIÓN
        1. Crear una lista
        2. Consultar lista
        3. Actualizar lista
        4. Eliminar lista
        5. Envia correo con lista de reproducción
        6. Reproducir canciones
        7. Ir al menu anterior""")
    
        opc = input('\nDigite una opción: ')
        if opc == "1":
            print("\nSesión de creación de lista de reproducción\n")
            state_lista = True
            while state_lista:
                try:
                    # Se realiza el conteo de las canciones totales contratadas por el cliente de acuerdo al plan
                    # y se realizar el conteo de las canciones que ya estan en la lista de reproducción.
                    # asi tener el total de canciones faltantes para completar el plan
                    total_canciones = plan_cliente(con, id_cliente)[0] - contar_lista(con, id_cliente)[0]
                    print('Falta {} canciones para completar el plan'.format(total_canciones))
                    if total_canciones == 0:
                        print_line_error('¡Has completado tu plan, no puedes agregar más canciones!')
                        state_lista = False
                    else:
                        consulta_tabla_canciones_lista(con)
                        info = info_lista(con, id_cliente)
                        registrar_lista_cliente(con, info)
                        next = False
                        while not next:
                            opc_next = input("""\n¿Desea agregar otra canción? s/n: """).lower()
                            if opc_next == 's':
                                next = True
                            elif opc_next == 'n':
                                next = True
                                state_lista = False
                            else:
                                print_line_error('¡Opción no valida. Digite una opción nuevamente!')
                except:
                    print_line_error('¡Canción no encontrada en la base de datos!')
        elif opc == "2":
            consulta_tabla_listas(con, id_cliente)
        elif opc == "3":
            state_actualizar = True
            while state_actualizar:
                try:
                    consulta_tabla_listas(con, id_cliente)
                    id_cancion = int(input('\nDigite el id de la canción que desea actualizar: '))
                    consulta_tabla_canciones_lista(con)
                    lista_info = info_lista(con, id_cliente)
                    actualizar_info_tabla_listas(con, tuple(lista_info[0:5]), id_cancion, id_cliente)
                    state_actualizar = False
                except:
                    print_line_error('¡Canción no encontrada en las base de datos!')

        elif opc == "4":
            borrar_lista(con, id_cliente)
        elif opc == "5":
            enviar_mensaje(con, id_cliente)
        elif opc == "6":
            if contar_lista(con, id_cliente)[0] == 0:
                print_line_error('¡No tienes canciones en tu lista de reproducción!\nCrea una lista para poder reproducir canciones')
            else:
                consulta_tabla_listas(con, id_cliente)
                id_cancion = int(input('\nDigite el id de la canción que desea reproducir: '))
                id_validacion = validacion_existencia_todas(con, 'listas', 'id_cancion', 'id_cancion', id_cancion)
                while id_validacion != False:
                    id_cancion = int(input('\nDigite el id de la canción que desea reproducir: '))
                    id_validacion = validacion_existencia_todas(con, 'listas', 'id_cancion', 'id_cancion', id_cancion)
                reproducir_cancion(con, id_cancion, id_cliente)
        elif opc == "7":
            state = False

        else:
            print("\t\n¡Opcion no valida. Digite una opción nuevamente!")





"""----------------------------- Pruebas -----------------------------"""

