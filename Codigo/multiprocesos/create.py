from paquetes_ad.decorador import *
import sqlite3
from sqlite3 import Error

def sql_conexion():
    try:
        con = sqlite3.connect('SpotyUN.db')
        return con
    
    except Error:
        print(Error)

class Database():

    def __init__(self, conexionbd):
        self.__conexionbd = conexionbd
        self.__data_canciones = None
        self.__data_planes = None 
        self.__data_clientes = None
        self.__data_pp_cliente = None
        self.__data_listas = None

    def __tabla_canciones(self):
        cursor_obj = self.__conexionbd.cursor()
        self.__data_canciones = cursor_obj.execute("""CREATE TABLE IF NOT EXISTS canciones(
                                                    id_cancion INTEGER PRIMARY KEY AUTOINCREMENT,
                                                    nombre_cancion CHAR(100) NOT NULL,
                                                    genero CHAR(5) NOT NULL,
                                                    album  CHAR(100) NOT NULL,
                                                    interprete CHAR(100) NOT NULL,
                                                    imagen BLOB,
                                                    cancion BLOB)""")
        self.__conexionbd.commit()

    # Función para crear la tabla 'planes' en la base de datos
    def __tabla_planes(self):
        cursor_obj = self.__conexionbd.cursor()
        self.__data_planes = cursor_obj.execute("""CREATE TABLE IF NOT EXISTS planes(
                                                    id_plan INT(1) PRIMARY KEY UNIQUE,
                                                    nombre_plan TEXT(15) NOT NULL,
                                                    valor INT(5) NOT NULL,
                                                    cantidad_canciones SHORT(4))""")
        self.__conexionbd.commit()


    # Función para crear la tabla 'clientes' en la base de datos
    def __tabla_clientes(self):
        cursor_obj = self.__conexionbd.cursor()
        self.__data_clientes = cursor_obj.execute("""CREATE TABLE IF NOT EXISTS clientes(
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
        self.__conexionbd.commit()


    # Función para crear la tabla 'listas' en la base de datos
    def __tabla_listas(self):
        cursor_obj = self.__conexionbd.cursor()
        self.__data_pp_cliente = cursor_obj.execute("""CREATE TABLE IF NOT EXISTS listas(
                                                    id_cancion INTEGER(10),
                                                    nombre_cancion TEXT(100) NOT NULL,
                                                    interprete TEXT(100) NOT NULL,
                                                    album TEXT(100) NOT NULL,
                                                    genero TEXT(30) NOT NULL,
                                                    id_cliente INTEGER(12))""")
        self.__conexionbd.commit()


    # Función para crear la tabla 'planes_cliente' en la base de datos
    def __tabla_planes_por_cliente(self):
        cursor_obj = self.__conexionbd.cursor()
        self.__data_listas = cursor_obj.execute("""CREATE TABLE IF NOT EXISTS planes_cliente(
                                                id_cliente INTEGER(12) NOT NULL,
                                                id_plan INT(1) NOT NULL,
                                                cantidad_canciones SHORT(4))""")
        self.__conexionbd.commit()

    
    def create_database(self):
        Database.__tabla_canciones(self)
        Database.__tabla_planes(self)
        Database.__tabla_clientes(self)
        Database.__tabla_planes_por_cliente(self)
        Database.__tabla_listas(self)
        database = ( self.__data_canciones, self.__data_planes, self.__data_clientes, self.__data_pp_cliente, self.__data_listas)


con = sql_conexion()
database = Database(con)
database.create_database()
