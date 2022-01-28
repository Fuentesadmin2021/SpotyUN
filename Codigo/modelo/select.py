

class Read():
    pass

# Función para realizar la consulta individual de una canción por medio del id_canción registrado en la tabla canciones
def consulta_individual_cancion(con):
    cursor_obj = con.cursor()
    id = int(input('\nIngrese el id de la canción: '))
    busqueda = 'SELECT id_cancion, nombre_cancion, genero, album, interprete FROM canciones WHERE id_cancion = '
    id_busqueda = busqueda + str(id)
    cursor_obj.execute(id_busqueda)
    cancion = cursor_obj.fetchall()
    print ("\n{:<12} {:<30} {:<30} {:<30} {:<30}".format('ID', 'NOMBRE', 'GENERO', 'ALBUM', 'INTERPRETE(S)'))
    for row in cancion:
        id, nombre, genero, album, interprete = row
        print ("{:<12} {:<30} {:<30} {:30} {:30}".format(id, nombre, genero, album, interprete))

  # Función para realizar la consulta individual de una canción por medio del id_canción registrado en la tabla canciones
    def consulta_individual_cancion(self):
        cursor_obj = self.conexionbd.cursor()
        id = int(input('\nIngrese el id de la canción: '))
        cursor_obj.execute(f'SELECT id_cancion, nombre_cancion, genero, album, interprete FROM canciones WHERE id_cancion = {id}')
        cancion = cursor_obj.fetchall()
        print ("\n{:<12} {:<30} {:<30} {:<30} {:<30}".format('ID', 'NOMBRE', 'GENERO', 'ALBUM', 'INTERPRETE(S)'))
        for row in cancion:
            id, nombre, genero, album, interprete = row
            print ("{:<12} {:<30} {:<30} {:30} {:30}".format(id, nombre, genero, album, interprete))

# Función para obtener la dirección de la canción que esta en la base de datos
def obtener_dir_cancion(con) -> str:
    cursor_obj = con.cursor()
    id = input('\nIngrese el id de la canción que desea escuchar: ')
    busqueda = f'SELECT cancion FROM canciones WHERE id_cancion = {id}'
    dir_cancion = cursor_obj.execute(busqueda)
    for dir in dir_cancion:
        return dir[0]


# Función que obtiene la canción de la base de datos
def obtener_cancion_db(con, id_cancion) -> str:
    cursor_obj = con.cursor()
    sql_blob_query = "SELECT nombre_cancion, cancion from canciones where id_cancion = ?"
    cursor_obj.execute(sql_blob_query, (id_cancion,))
    filas = cursor_obj.fetchall()
    for row in filas:
        name = row[0]
        audio = row[1]
    ruta = f"../SpotyUN_Lista/{name}.mp3"
    guardar_cancion(audio, ruta)
    con.commit()
    return ruta

# Función que permite consultar la tabla de datos lista y verificar lñas entradas de la
# misma de acuerdo a la id suministrado
def consulta_tabla_listas(con, id_cliente: int):
    cursor_obj = con.cursor()
    cursor_obj.execute(f'SELECT id_cancion, nombre_cancion, interprete, album, genero FROM listas WHERE id_cliente = {id_cliente}')
    cantidad_canciones = cursor_obj.fetchall()
    print("\n{:<12} {:<30} {:<20} {:<20} {:<20}".format('ID_CANCIÓN', 'NOMBRE', 'INTERPRETE', 'ALBUM', 'GENERO'))
    for row in cantidad_canciones:
        id, nombre, interprete, album, genero = row
        print("{:<12} {:<30} {:<20} {:20} {:<20}".format(id, nombre, interprete, album, genero))