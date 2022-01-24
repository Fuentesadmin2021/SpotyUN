class Create():
    def __init__(self, conexionbd):
        self.conexionbd = conexionbd

    def tabla_canciones(self):
        self.conexionbd.cursor().execute("""CREATE TABLE IF NOT EXISTS canciones(
                            id_cancion INTEGER PRIMARY KEY AUTOINCREMENT,
                            nombre_cancion CHAR(100) NOT NULL,
                            genero CHAR(5) NOT NULL,
                            album  CHAR(100) NOT NULL,
                            interprete CHAR(100) NOT NULL,
                            imagen BLOB,
                            cancion BLOB)""")
        self.conexionbd.commit()


    # Función para crear la tabla 'planes' en la base de datos
    def tabla_planes(self):
        self.conexionbd.cursor().execute("""CREATE TABLE IF NOT EXISTS planes(
                            id_plan INT(1) PRIMARY KEY UNIQUE,
                            nombre_plan TEXT(15) NOT NULL,
                            valor INT(5) NOT NULL,
                            cantidad_canciones SHORT(4))""")

        self.conexionbd.commit()


    # Función para crear la tabla 'clientes' en la base de datos
    def tabla_clientes(self):
        self.conexionbd.cursor().execute("""CREATE TABLE IF NOT EXISTS clientes(
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

        self.conexionbd.commit()


    # Función para crear la tabla 'listas' en la base de datos
    def tabla_listas(self):
        self.conexionbd.cursor().execute("""CREATE TABLE IF NOT EXISTS listas(
                            id_cancion INTEGER(10),
                            nombre_cancion TEXT(100) NOT NULL,
                            interprete TEXT(100) NOT NULL,
                            album TEXT(100) NOT NULL,
                            genero TEXT(30) NOT NULL,
                            id_cliente INTEGER(12))""")

        self.conexionbd.commit()


    # Función para crear la tabla 'planes_cliente' en la base de datos
    def tabla_planes_por_cliente(self):
        self.conexionbd.cursor().execute("""CREATE TABLE IF NOT EXISTS planes_cliente(
                            id_cliente INTEGER(12) NOT NULL,
                            id_plan INT(1) NOT NULL)""")

        self.conexionbd.commit()