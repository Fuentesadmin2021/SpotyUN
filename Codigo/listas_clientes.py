from clientes import Cliente
from canciones import Canciones
from manejador_db import Manejador_db
''' Funciones importadas para realizar el manejo y envió de los correos
# Función smtlib usada para porder enviar un correo por medio del programa
# De  email.mime.text se importa el método MIMEText para el manejo de texto dentro del correo
# De email.mime.multipart se importa el método MIMEMultipart para el manejo de multiples partes dentro del correo
# como asunto del correo, copias ocultas y demás datos de importancia para el correo'''
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from decorador import Decorador as dec


class Listas_cliente(Canciones, Cliente, Manejador_db):
    def __init__(self):
        Manejador_db.__init__(self)
        Cliente.__init__(self)
        Canciones.__init__(self)
        
# Función para realizar la consulta de datos de la canción como id_canción, nombre_canción, interprete, album
    def id_cancion_lista(self) -> list:
        canciones = input('\nIngrese el id de cancion que desea agregar a su lista: ')
        while canciones == '0':
            break
        cursor_obj = self.con.cursor()
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

        # La función a continuación se encarga de reproducir la canción que el usuario elija ingresando el id

    # Función para consultar la cantidad de canciones por plan de acuerdo al registro del cliente
    def plan_cliente(self, id_cliente: int) -> int:
        cursor_obj = self.con.cursor()
        cursor_obj.execute(f'SELECT id_plan FROM planes_cliente WHERE id_cliente = {id_cliente}')
        id_plan_cliente = cursor_obj.fetchone()
        cursor_obj.execute(f'SELECT cantidad_canciones FROM planes WHERE id_plan = {id_plan_cliente[0]}')
        cant_canciones = cursor_obj.fetchone()
        return cant_canciones

    # Función que reliza un conteo de los registros en la tabla listas de acuerdo al id_cliente suministrado
    def contar_lista(self, id_cliente: int) -> str or int:
        cursor_obj = self.con.cursor()
        cursor_obj.execute(f'SELECT COUNT(*) FROM listas WHERE id_cliente = {id_cliente}')
        cantidad_listas = cursor_obj.fetchone()
        if cantidad_listas[0] is None:
            return 0
        return cantidad_listas

    # Función para consultar las canciones existentes en la tabla canciones y mostrarlas en pantalla
    def consulta_tabla_canciones_lista(self):
        cursor_obj = self.con.cursor()
        cursor_obj.execute('SELECT id_cancion, nombre_cancion, genero, album, interprete  FROM canciones')
        cantidad_canciones = cursor_obj.fetchall()
        print("\n{:<12} {:<45} {:<20} {:<20} {:<20}".format('ID', 'NOMBRE', 'GENERO', 'ALBUM', 'INTERPRETE(S)'))
        for row in cantidad_canciones:
            id, nombre, genero, album, interprete = row
            print("{:<12} {:<45} {:<20} {:<20} {:<20}".format(id, nombre, genero, album, interprete))

    # Función para agregar en una tupla la información correspondiente para la tabla listas
    # necesitamos el id_cliente y la lista info_canciones
    def info_lista(self, id_cliente: int) -> tuple:
        id_c = id_cliente
        info_canciones = Listas_cliente.id_cancion_lista(self)
        info_canciones.append(id_c)
        return info_canciones

    # Función para registrar la información en la tabla listas
    def registrar_lista_cliente(self, tupla: tuple):
        cursor = self.con.cursor()
        cursor.execute('''INSERT INTO listas VALUES (?,?,?,?,?,?)''', tupla)
        self.con.commit()
        dec.print_line_success("¡¡El registro se ha realizado exitosamente!!")

    # Función para consultar la lista de canciones registradas en la tabla listas
    # de acuerdo al id suministrado por el cliente
    def consulta_tabla_listas(self, id_cliente: int):
        cursor_obj = self.con.cursor()
        cursor_obj.execute(f'SELECT id_cancion, nombre_cancion, interprete, album, genero FROM listas WHERE id_cliente = {id_cliente}')
        cantidad_canciones = cursor_obj.fetchall()
        print("\n{:<12} {:<30} {:<20} {:<20} {:<20}".format('ID_CANCIÓN', 'NOMBRE', 'INTERPRETE', 'ALBUM', 'GENERO'))
        for row in cantidad_canciones:
            id, nombre, interprete, album, genero = row
            print("{:<12} {:<30} {:<20} {:20} {:<20}".format(id, nombre, interprete, album, genero))

    # Función que borra una lista de reproducción de la tabla listas de acuerdo al id_cliente suministrado
    def borrar_lista(self, id_cliente: int) -> str:
        cursor_obj = self.con.cursor()
        cursor_obj.execute(f'DELETE FROM listas WHERE id_cliente = {id_cliente}')
        self.con.commit()
        return dec.print_line_success('Tu lista ha sido eliminada')

    # Función que consulta la información ingresa por el cliente en la tabla listas, retorna una tupla
    # una tupla de listas con la información completa de la lista de reproducción
    def consulta_tabla_listas_id(self, id_cliente: int) -> bool or tuple:
        cursor_obj = self.con.cursor()
        cursor_obj.execute(f'SELECT id_cancion, nombre_cancion, interprete, album, genero FROM listas WHERE id_cliente = {id_cliente}')
        cantidad_canciones = cursor_obj.fetchall()
        if not cantidad_canciones:
            return False
        else:
            return cantidad_canciones

    def consulta_tabla_listas_cancion(self, id_cliente: int, id_cancion: int) -> bool or tuple:
        cursor_obj = self.con.cursor()
        cursor_obj.execute(f'SELECT COUNT (*) FROM listas WHERE id_cliente = {id_cliente} AND id_cancion = {id_cancion}')
        cantidad_canciones = cursor_obj.fetchone()
        if cantidad_canciones[0] >= 1:
            return True
        else:
            return False

    # Función que obtiene el correo del cliente

    # Función para realizar la consulta de la tabla listas para poder enviarla en el correo electrónico
    # Retorna un string con formato html para poderlo ingresar en la función enviar_correo
    def consulta_tabla_para_html(self, id_cliente: int) -> list:
        cursor_obj = self.con.cursor()
        cursor_obj.execute(f'SELECT id_cancion, nombre_cancion, interprete, album, genero FROM listas WHERE id_cliente = {id_cliente}')
        cantidad_canciones = cursor_obj.fetchall()
        lista_str = ''
        for row in cantidad_canciones:
            id, nombre_cancion, interprete, album, genero = row
            lista_str += (f"<tr><td>{id}</td><td>{nombre_cancion}</td><td>{interprete}</td><td>{album}</td><td>{genero}</td></tr>")
        return lista_str

    # Función para enviar el mensaje con la lista de reproducción del cliente
    def enviar_mensaje(self, id_cliente: int):
        info_tabla = Listas_cliente.consulta_tabla_para_html(self, id_cliente)
        canciones_plan= Listas_cliente.plan_cliente(self, id_cliente)[0]
        canciones_lista = Listas_cliente.contar_lista(self, id_cliente)[0]
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
        correo = Listas_cliente.get_correo_cliente(self, id_cliente)
        servidor.login('ovillalbaunal@gmail.com', 'programcion_segundo')
        servidor.sendmail('ovillalbaunal@gmail.com', correo, texto)
        servidor.quit()
        dec.print_line_success("Envio exitoso")


    # Función para realizar la actualizacíón de un registro completo de la tabla listas
    def actualizar_info_tabla_listas(self, tupla: tuple, id_cancion: int, id_cliente: int):
        cursor_obj = self.con.cursor()
        act_listas = (f"""UPDATE listas 
                        SET id_cancion = ?,
                            nombre_cancion = ?,
                            interprete = ?,
                            album = ?,
                            genero = ?
                        WHERE id_cancion = {id_cancion} and id_cliente = {id_cliente}""")
        cursor_obj.execute(act_listas, tupla)
        self.con.commit()


    # Función que despliega el menu de sección de listas de reproducción
    
