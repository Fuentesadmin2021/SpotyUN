import sqlite3
from sqlite3 import Error

# función para crear la bases de datos
def sql_conexion():
    try:
        con = sqlite3.connect('SpotyUN.db')
        return con
    
    except Error:
        print(Error)

# función para crear la tabla 'canciones' en la base de datos
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

# función para crear la tabla 'planes' en la base de datos
def crear_tabla_planes(con):
    cursor_obj = con.cursor()
    cursor_obj.execute("""CREATE TABLE IF NOT EXISTS planes(
                        id_plan INT(1) PRIMARY KEY UNIQUE,
                        nombre_plan TEXT(15) NOT NULL,
                        valor SHORT(5) NOT NULL,
                        cantidad_canciones SHORT(4))""")

    con.commit()

# funcion para crear la tabla 'clientes' en la base de datos
def crear_tabla_clientes(con):
    cursor_obj = con.cursor()
    cursor_obj.execute("""CREATE TABLE IF NOT EXISTS clientes(
                        id_cliente INTEGER(12) PRIMARY KEY UNIQUE,
                        nombre_cliente TEXT(30) NOT NULL,
                        apellido TEXT(30) NOT NULL,
                        pais TEXT(30) NOT NULL,
                        ciudad TEXT(30) NOT NULL,
                        celular TEXT(15) NOT NULL,
                        correo TEXT(35) NOT NULL,
                        fecha_pago TEXT(10) NOT NULL,
                        numero_tc TEXT(20) NOT NULL,
                        estado_pago TEXT(10))""")

    con.commit()

# funcion que crea la tabla 'listas' en la base de datos
def crear_tabla_listas(con):
    cursor_obj = con.cursor()
    cursor_obj.execute("""CREATE TABLE IF NOT EXISTS listas(
                        id_cancion INTEGER(10),
                        nombre_cancion TEXT(100) NOT NULL,
                        interprete TEXT(100) NOT NULL,
                        album TEXT(100) NOT NULL,
                        id_cliente INTEGER(12))""")

    con.commit()

# funcion que crea la tabla 'planes cliente' en la base de datos
def crear_tabla_planes_por_cliente(con):
    cursor_obj = con.cursor()
    cursor_obj.execute("""CREATE TABLE IF NOT EXISTS planes_cliente(
                        id_cliente INTEGER(12) NOT NULL,
                        id_plan INT(1) NOT NULL)""")

    con.commit()


# función para borrar tablas
def borrar(con, nombre_tabla):
    cursorObj = con.cursor()
    cursorObj.execute(f'DROP TABLE {nombre_tabla}')
    con.commit()

# función para cerrrar la base de datos
def close(con):
    con.close()

# mi_conexion = sql_conexion()
# borrar(mi_conexion, 'canciones')

