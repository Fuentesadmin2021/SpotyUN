from paquetes_ad.decorador import *


class Insertar():
    def __init__(self, conexionbd):
        self.conexionbd = conexionbd

    # Función que se encarga de registrar la información y audio de una canción en la tabla canciones
    def registrar_cancion(self, tupla: tuple):
        cursor_obj = self.conexionbd.cursor()
        cursor_obj.execute('''INSERT INTO canciones VALUES(NULL, ?, ?, ?, ?, NULL, ?)''', tupla)
        self.conexionbd.commit()
        print_line_success("♪ El registro de la canción se ha realizado exitosamente ♪")

    
    # Función para registrar los planes en la tabla planes
    def registrar_plan(self, tupla: tuple):        
        cursor_obj = self.conexionbd.cursor()
        cursor_obj.execute('''INSERT INTO planes VALUES(?,?,?,?)''', tupla)
        self.conexionbd.commit()
        print_line_success('¡El plan se ha registrado exitosamente!')


    # Función que registra un cliente en la tabla clientes
    def registrar_cliente(self, tupla: tuple):
        cursor_obj = self.conexionbd.cursor()
        datos_cliente = tupla
        cursor_obj.execute('''INSERT INTO clientes VALUES (?,?,?,?,?,?,?,?,?,?)''', datos_cliente[0:-1])
        self.conexionbd.commit()
        print_line_success("¡El registro se ha realizado exitosamente!")


    # Función que registra plan en la tabla planes_cliente
    def registrar_plan_cliente(self, datos: tuple):
        cursor_obj=self.conexionbd.cursor()
        insercion = datos
        cursor_obj.execute('''INSERT INTO planes_cliente VALUES(?,?)''', insercion)
        self.conexionbd.commit()


    # Función para registrar la información en la tabla listas
    def registrar_lista_cliente(self, tupla: tuple):
        cursor = self.conexionbd.cursor()
        cursor.execute('''INSERT INTO listas VALUES (?,?,?,?,?,?)''', tupla)
        self.conexionbd.commit()
        print_line_success("¡¡El registro se ha realizado exitosamente!!")