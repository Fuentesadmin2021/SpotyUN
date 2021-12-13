# librerias fundamentales para funcionamiento del programa
from pygame import mixer
from validacion_datos import validacion_letra

# Función que obtiene los datos de una canción antes de registrarla
def cancion() -> tuple:
    nombre = validacion_letra(input('Nombre: '), 100)
    genero = validacion_letra(input('Genero: '), 30)
    album = validacion_letra(input('Album: '), 100)
    interprete = validacion_letra(input('Interprete(s): '), 100)
    # imagen = None
    nombre_cancion = input('Nombre de la canción tal cual esta almacenada en su equipo: ')
    cancion = registrar_cancion_bd(nombre_cancion)
    datos_cancion = (nombre, genero, album, interprete, cancion)
    return datos_cancion


# Función que registra una canción en la tabla canciones
def registrar_cancion(con: 'sql_conexion'):
    cursor_obj = con.cursor()
    insercion = cancion()
    cursor_obj.execute('''INSERT INTO canciones VALUES(NULL, ?, ?, ?, ?, NULL, ?)''', insercion)
    con.commit()

# Función para modificar el nombre de una canción
def actualizar_nombre_cancion(con: 'sql_conexion'):
    cursor_obj = con.cursor()
    id = int(input('Ingrese el id de la canción a la que quiere modificarle el nombre: '))
    nombre = input('Ingrese el nombre de la canción: ')
    actualizar = 'UPDATE canciones SET nombre_cancion = "'+nombre+'" WHERE id_cancion = '
    id_actualizar = actualizar + str(id)
    cursor_obj.execute(id_actualizar)
    con.commit()
    print("!El nombre de la cancion se ha modificado exitosamente¡")


# Función para modificar el género de una canción
def actualizar_genero_cancion(con: 'sql_conexion'):
    cursor_obj = con.cursor()
    id = int(input('Ingrese el id de la cancion a la que quiere modificarle el genero: '))
    genero = input('Ingrese el genero de la cancion: ')
    actualizar = 'UPDATE canciones SET genero = "'+genero+'" WHERE id_cancion = '
    id_actualizar = actualizar + str(id)
    cursor_obj.execute(id_actualizar)
    con.commit()
    print("!El genero de la cancion se ha modificado exitosamente¡")

    
# Función para modificar el album de una canción
def actualizar_album_cancion(con: 'sql_conexion'):
    cursor_obj = con.cursor()
    id = int(input('Ingrese el id de la canción a la que quiere modificarle el nombre de su album: '))
    album = input('Ingrese el nombre del album de la canción: ')
    actualizar = 'UPDATE canciones SET album = "'+album+'" WHERE id_cancion = '
    id_actualizar = actualizar + str(id)
    cursor_obj.execute(id_actualizar)
    con.commit()
    print("!El nombre del album de la cancion se ha modificado exitosamente¡")

    
# Función para modificar el interprete de una canción
def actualizar_interprete_cancion(con: 'sql_conexion'):
    cursor_obj = con.cursor()
    id = int(input('Ingrese el id de la canción a la que quiere modificarle el interprete: '))
    interprete = input('Ingrese el nombre del interprete(s) de la canción: ')
    actualizar = 'UPDATE canciones SET interprete = "'+interprete+'" WHERE id_cancion = '
    id_actualizar = actualizar + str(id)
    cursor_obj.execute(id_actualizar)
    con.commit()
    print("!El nombre del interprete de la canción se ha modificado exitosamente¡")
    


# Función que realiza la consulta de todas las canciones registradas en la base de datos
def consulta_tabla_canciones(con: 'sql_conexion'):
    cursor_obj = con.cursor()
    cursor_obj.execute('SELECT id_cancion, nombre_cancion, genero, album, interprete  FROM canciones')
    cantidad_canciones = cursor_obj.fetchall()
    orden_salida = orden_consulta(cantidad_canciones)
    print ("\n{:<12} {:<30} {:<30} {:<30} {:<30}".format('ID', 'NOMBRE', 'GENERO', 'ALBUM', 'INTERPRETE(S)'))
    for row in orden_salida:
        id, nombre, genero, album, interprete = row
        print ("{:<12} {:<30} {:<30} {:<30} {:<30}".format(id, nombre, genero, album, interprete))



# Función que ordena las canciones según como el usuario lo desee
def orden_consulta(lista: list) -> tuple:
    
    print('''
                        ¿COMO DESEA ORDENAR LA CONSULTA?
                    1. Por id
                    2. Por nombre
                    3. por genero
                    4. por album
                    5. Por interprete(s)\n''')

    opc = input("\tDigite una opcion: ")
    if (opc == '1'):
        orden = sorted(lista, key = lambda id : id[0])
        return orden
        
    elif(opc == '2'):
        orden = sorted(lista, key = lambda nombre : nombre[1])
        return orden
        
    elif(opc == '3'):
        orden = sorted(lista, key = lambda genero : genero[2])
        return orden

    elif(opc == '4'):
        orden = sorted(lista, key = lambda album : album[3])
        return orden

    elif(opc == '5'):
        orden = sorted(lista, key = lambda interprete : interprete[4])
        return orden


# Función que realiza la consulta individual de una canción por medio del id_canción registrado en al base de datos
def consulta_individual_cancion(con: 'sql_conexion'):
    cursor_obj = con.cursor()
    id = int(input('Ingrese el id de la canción: '))
    busqueda = 'SELECT id_cancion, nombre_cancion, genero, album, interprete FROM canciones WHERE id_cancion = '
    id_busqueda = busqueda + str(id)
    cursor_obj.execute(id_busqueda)
    cancion = cursor_obj.fetchall()
    print ("\n{:<12} {:<30} {:<30} {:<30} {:<30}".format('ID', 'NOMBRE', 'GENERO', 'ALBUM', 'INTERPRETE(S)'))
    for row in cancion:
        id, nombre, genero, album, interprete = row
        print ("{:<12} {:<30} {:<30} {:30} {:30}".format(id, nombre, genero, album, interprete))





# Función que obtiene la dirección de la canción que esta en la base de datos
def obtener_dir_cancion(con: 'sql_conexion'):
    cursor_obj = con.cursor()
    id = int(input('Ingrese el id de la canción que desea escuchar: '))
    busqueda = 'SELECT cancion FROM canciones WHERE id_cancion = '
    id_busqueda = busqueda + str(id)
    dir_cancion = cursor_obj.execute(id_busqueda)
    for dir in dir_cancion:
        return dir[0]


# Función que convierte a binario una cancion
def registrar_cancion_bd(audio: str) -> 'blob-bin':
    cancion = f'../Canciones/{audio}.mp3'
    with open(cancion, 'rb') as file:
        blob = file.read()
        return blob

# Función que guarda la canción en el equipo en formato mp3
def guardar_cancion(data: bin, filename: str) -> 'mp3':
    with open(filename, 'wb') as file:
        return file.write(data)


# Función que obtiene la canción de la base de datos
def obtener_cancion_db(con: 'sql_conexion') -> str:
    cursor_obj = con.cursor()
    sql_blob_query = "SELECT nombre_cancion, cancion from canciones where id_cancion = ?"
    id = input('Ingrese el id de la canción que desea reproducir: ')
    cursor_obj.execute(sql_blob_query, (id,))
    filas = cursor_obj.fetchall()
    for row in filas:
        name = row[0]
        audio = row[1]
    ruta = f"../SpotyUN_Lista/{name}.mp3"
    guardar_cancion(audio, ruta)
    con.commit()
    return ruta


# Función que permite reproducir la canción
def reproducir_cancion(con: 'sql_conexion'):
    mixer.init()
    cancion = obtener_cancion_db(con)
    mixer.music.load(cancion)
    mixer.music.set_volume(0.7)
    mixer.music.play()

    reproducir = True
    while reproducir:
        print("\tpulse p para detener canción")
        print("\tpulse r para reanudar canción")
        print("\tpulse e para elegir otra canción")
        print("\tPulse s para salir")

        opcion = input(">>> ")

        if opcion =="p":
            mixer.music.pause()
        elif opcion =="r":
            mixer.music.unpause()
        elif opcion =="s":
            mixer.music.stop()
            reproducir = False
        elif opcion =="e":
            mixer.music.stop()
            cancion = reproducir_cancion(con)
            mixer.music.load(cancion)
            mixer.music.set_volume(0.7)
            mixer.music.play()


# Función que crea un menú para actualizar de manera individual los datos básicos de una canción
def actualizar_datos_cancion(con: 'sql_conexion'):
    salir_actualizar = False
    while not salir_actualizar:

        print('''
                            ACTUALIZAR INFORMACIÓN CANCIÓN
                        1. Nombre
                        2. Album
                        3. Genero
                        4. Interprete
                        5. Ir al menu anterior\n''')

        opc = input("\tDigite una opcion: ")
        if (opc == '1'):
            actualizar_nombre_cancion(con)
        
        elif(opc == '2'):
            actualizar_album_cancion(con)

        elif(opc == '3'):
            actualizar_genero_cancion(con)

        elif(opc == '4'):
            actualizar_interprete_cancion(con)
  
        elif(opc == '5'):
            salir_actualizar = True


# Función que creara un directorio donde se almacenaran las canciones a reproducir
def crear_directorio_repro() -> str:
    import subprocess
    ruta = subprocess.call(['mkdir', 'Canciones_reproducidas'], shell=True)
    return ruta

