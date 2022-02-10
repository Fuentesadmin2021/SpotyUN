from manejador_db import Manejador_db

class Database(Manejador_db):

    def __init__(self):
        Manejador_db.__init__(self)

        self.__tabla_canciones = ("""CREATE TABLE IF NOT EXISTS canciones(
                                    id_cancion INTEGER PRIMARY KEY AUTOINCREMENT,
                                    nombre_cancion CHAR(100) NOT NULL,
                                    genero CHAR(5) NOT NULL,
                                    album  CHAR(100) NOT NULL,
                                    interprete CHAR(100) NOT NULL,
                                    imagen BLOB,
                                    cancion BLOB)""")

   
        self.__tabla_planes = ("""CREATE TABLE IF NOT EXISTS planes(
                                id_plan INT(1) PRIMARY KEY UNIQUE,
                                nombre_plan TEXT(15) NOT NULL,
                                valor INT(5) NOT NULL,
                                cantidad_canciones SHORT(4))""")


        self.__tabla_clientes = ("""CREATE TABLE IF NOT EXISTS clientes(
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

        self.__tabla_listas =  ("""CREATE TABLE IF NOT EXISTS listas(
                                id_cancion INTEGER(10),
                                nombre_cancion TEXT(100) NOT NULL,
                                interprete TEXT(100) NOT NULL,
                                album TEXT(100) NOT NULL,
                                genero TEXT(30) NOT NULL,
                                id_cliente INTEGER(12))""")

        
        self.__tabla_pp_planes = ("""CREATE TABLE IF NOT EXISTS planes_cliente(
                                id_cliente INTEGER(12) NOT NULL,
                                id_plan INT(1) NOT NULL)""")



    def __create_tables(self, query):
        cursor_obj = self.con.cursor()
        cursor_obj.execute(query)
        self.con.commit()


    def create_database(self):
        Database.__create_tables(self, self.__tabla_canciones)
        Database.__create_tables(self, self.__tabla_planes)
        Database.__create_tables(self, self.__tabla_clientes)
        Database.__create_tables(self, self.__tabla_pp_planes)
        Database.__create_tables(self, self.__tabla_listas)
