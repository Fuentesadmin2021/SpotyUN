# Se importa la librería sqlite3 para el manejo de una base de datos a través de Python
# De este módulo sqlite3 se importa el método Error que generará una excepción en caso de error
# de la conexión con la base de datos
import sqlite3
from sqlite3 import Error
from xml.dom import minicompat
from validacion_datos import *
from decorador import *

class  ManejadorBD():
        
# Función para crear la bases de datos y la conexion con la base
    def sql_conexion(self):
        try:
            con = sqlite3.connect('SpotyUN.db')
            return con
        
        except Error:
            print(Error)

    # Función que elimina toda la información de una tabla
    def eliminar_info_tablas(self, con, nombre_tabla: str):
        cursor_obj = con.cursor()
        cursor_obj.execute(f'DELETE from {self.nombre_tabla}')
        con.commit()


# Función que borrar la información de una tabla de acuerdo al primary_key sumistrado
    def borrar_info(self, con, nombre_tabla: str, primary_key: str, id):
        cursor = con.cursor()
        self.id = id
        borrar = f'DELETE FROM {self.nombre_tabla} WHERE {self.primary_key} = {id}'
        cursor.execute(borrar)
        con.commit()
        print_line_success(f"Su registro a sido eliminado de la tabla {self.nombre_tabla} ;)")


# Función para borrar cualquier tabla
    def borrar(self, con, nombre_tabla):
        cursorObj = con.cursor()
        cursorObj.execute(f'DROP TABLE {self.nombre_tabla}')
        con.commit()


# Función para cerrar la base de datos
    def close(con):
        con.close()


# Función para crear la tabla 'canciones' en la base de datos
def crear_tabla_canciones(con):
    cursor_obj = con.cursor()
    cursor_obj.execute("""CREATE TABLE IF NOT EXISTS canciones(
                        id_cancion INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre_cancion TEXT(100) NOT NULL,
                        genero TEXT(30) NOT NULL,
                        album  TEXT(100) NOT NULL,
                        interprete TEXT(100) NOT NULL,
                        imagen BLOB,
                        cancion BLOB)""")
    con.commit()


# Función para crear la tabla 'planes' en la base de datos
def crear_tabla_planes(con):
    cursor_obj = con.cursor()
    cursor_obj.execute("""CREATE TABLE IF NOT EXISTS planes(
                        id_plan INT(1) PRIMARY KEY UNIQUE,
                        nombre_plan TEXT(15) NOT NULL,
                        valor INT(5) NOT NULL,
                        cantidad_canciones SHORT(4))""")

    con.commit()


# Función para crear la tabla 'clientes' en la base de datos
def crear_tabla_clientes(con):
    cursor_obj = con.cursor()
    cursor_obj.execute("""CREATE TABLE IF NOT EXISTS clientes(
                        id_cliente INTEGER(12) PRIMARY KEY UNIQUE,
                        nombre_cliente TEXT(30) NOT NULL,
                        apellido TEXT(30) NOT NULL,
                        pais TEXT(30) NOT NULL,
                        ciudad TEXT(30) NOT NULL,
                        celular TEXT(15) NOT NULL,
                        correo TEXT(45) NOT NULL,
                        fecha_pago TEXT(10) NOT NULL,
                        numero_tc TEXT(20) NOT NULL,
                        estado_pago TEXT(15))""")

    con.commit()


# Función para crear la tabla 'listas' en la base de datos
def crear_tabla_listas(con):
    cursor_obj = con.cursor()
    cursor_obj.execute("""CREATE TABLE IF NOT EXISTS listas(
                        id_cancion INTEGER(10),
                        nombre_cancion TEXT(100) NOT NULL,
                        interprete TEXT(100) NOT NULL,
                        album TEXT(100) NOT NULL,
                        genero TEXT(30) NOT NULL,
                        id_cliente INTEGER(12))""")

    con.commit()


# Función para crear la tabla 'planes_cliente' en la base de datos
def crear_tabla_planes_por_cliente(con):
    cursor_obj = con.cursor()
    cursor_obj.execute("""CREATE TABLE IF NOT EXISTS planes_cliente(
                        id_cliente INTEGER(12) NOT NULL,
                        id_plan INT(1) NOT NULL)""")

    con.commit()


# Función para actualizar información de una tabla en la base de datos
# Funciona para cualquier tabla dentro de la base de datos
def actualizar_info_tablas(con, info: str, nombre_columna: str, nombre_tabla: str, primary_key: str, longitud: int):
    cursor_obj = con.cursor()
    state = True
    while state:
        try:
            id = input('\nIngrese el id: ').strip()
            if id_v := validacion_existencia_todas(con, nombre_tabla, nombre_columna, primary_key, id) == False:
                id = int(id)
                state = False
            else:
                print('\nEl id ingresado no existe en la base de datos')
        except:
            print('El Id ingresado no es el correcto')
    elemento = validacion_longitud(input(f'Ingrese {info} actualizado: '), longitud)
    actualizar = f'UPDATE {nombre_tabla} SET {nombre_columna} = ? WHERE {primary_key} = ?'
    info_actualizar = (elemento, id)
    cursor_obj.execute(actualizar, info_actualizar)
    con.commit()
    print_line_success(f"!{info.title()} se ha actualizado exitosamente¡")




"""----------------------------- Pruebas -----------------------------"""

miConexion = ManejadorBD()
print(miConexion.sql_conexion())
