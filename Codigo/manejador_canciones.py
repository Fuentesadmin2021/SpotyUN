# El paquete mixer del modulo pygame importado a continuación es utilizado como herramienta para la reproducción de las canciones.
from pygame import mixer
from manejadorbd import *
from validacion_datos import *

# Esta funcion se encarga de solicitar la informacion de una cancion para su registro
def cancion() -> tuple:
    nombre = validacion_letra(input('Nombre: '), 100)
    genero = validacion_letra(input('Genero: '), 30)
    album = validacion_letra(input('Album: '), 100)
    interprete = validacion_letra(input('Interprete(s): '), 100)
    # imagen = None
    state = False
    while not state:
        try:
            nombre_cancion = input('Nombre de la canción tal cual esta almacenada en su equipo: ')
            cancion = registrar_cancion_bd(nombre_cancion)
            state = True
        except:
            print('\n¡Error en los datos de la canción en el equipo\n por favor verifique e ingrese de nuevo la información!\n ')

    datos_cancion = (nombre, genero, album, interprete, cancion)
    return datos_cancion


# Funcion que se encarga de registrar la informacion y audio de una canción en la base de datos
def registrar_cancion(con):
    cursor_obj = con.cursor()
    tupla = cancion()
    cursor_obj.execute('''INSERT INTO canciones VALUES(NULL, ?, ?, ?, ?, NULL, ?)''', tupla)
    con.commit()

def actualizar_cancion(con):
    cursor_obj = con.cursor()
    id = input('Ingrese el id de la canción a la que quiere modificar: ')
    state = False
    while not state:
        try:
            nombre_cancion = input('Nombre de la canción tal cual esta almacenada en su equipo: ')
            cancion = registrar_cancion_bd(nombre_cancion)
            state = True
        except:
            print(
                '\n¡Error en los datos de la canción en el equipo\n por favor verifique e ingrese de nuevo la información!\n ')

    actualizar = f'UPDATE canciones SET cancion = ? WHERE id_cancion = ?'
    info_cancion = (cancion, id)
    cursor_obj.execute(actualizar, info_cancion)
    con.commit()
    print("!El nombre de la cancion se ha modificado exitosamente¡")


# Función que permite modificar el 'nombre' de una canción que este almacenada en la base de datos
"""def actualizar_nombre_cancion(con):
    cursor_obj = con.cursor()
    id = int(input('Ingrese el id de la canción a la que quiere modificarle el nombre: '))
    nombre = input('Ingrese el nombre de la canción: ')
    actualizar = 'UPDATE canciones SET nombre_cancion = "'+nombre+'" WHERE id_cancion = '
    id_actualizar = actualizar + str(id)
    cursor_obj.execute(id_actualizar)
    con.commit()
    print("!El nombre de la cancion se ha modificado exitosamente¡")"""


# Función para actualizar o modificar el 'genero' de una canción que este almacenada en la base de datos
"""def actualizar_genero_cancion(con):
    cursor_obj = con.cursor()
    id = int(input('Ingrese el id de la cancion a la que quiere modificarle el genero: '))
    genero = input('Ingrese el genero de la cancion: ')
    actualizar = 'UPDATE canciones SET genero = "'+genero+'" WHERE id_cancion = '
    id_actualizar = actualizar + str(id)
    cursor_obj.execute(id_actualizar)
    con.commit()
    print("!El genero de la cancion se ha modificado exitosamente¡")"""

    
# Función para actualizar o modificar el 'album' de una canción que este almacenada en la base de datos
"""def actualizar_album_cancion(con):
    cursor_obj = con.cursor()
    id = int(input('Ingrese el id de la canción a la que quiere modificarle el nombre de su album: '))
    album = input('Ingrese el nombre del album de la canción: ')
    actualizar = 'UPDATE canciones SET album = "'+album+'" WHERE id_cancion = '
    id_actualizar = actualizar + str(id)
    cursor_obj.execute(id_actualizar)
    con.commit()
    print("!El nombre del album de la cancion se ha modificado exitosamente¡")"""

    
# Función para actualizar o modificar el 'interprete(s)' de una canción que este almacenada en la base de datos
"""def actualizar_interprete_cancion(con):
    cursor_obj = con.cursor()
    id = int(input('Ingrese el id de la canción a la que quiere modificarle el interprete: '))
    interprete = input('Ingrese el nombre del interprete(s) de la canción: ')
    actualizar = 'UPDATE canciones SET interprete = "'+interprete+'" WHERE id_cancion = '
    id_actualizar = actualizar + str(id)
    cursor_obj.execute(id_actualizar)
    con.commit()
    print("!El nombre del interprete de la canción se ha modificado exitosamente¡")"""
    


# Función para realizar una consulta de todas las canciones registradas en la base de datos



# Función que ordena la consulta de la canciones segun el usuario lo desee
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


# Función para realizar la consulta individual de una canción por medio del id_canción registrado en al base de datos
def consulta_individual_cancion(con):
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


# Función para obtener la dirección de la canción que esta en la base de datos
def obtener_dir_cancion(con):
    cursor_obj = con.cursor()
    id = int(input('Ingrese el id de la canción que desea escuchar: '))
    busqueda = 'SELECT cancion FROM canciones WHERE id_cancion = '
    id_busqueda = busqueda + str(id)
    dir_cancion = cursor_obj.execute(id_busqueda)
    for dir in dir_cancion:
        return dir[0]


# Función que convierte a binario una cancion -> 'blob-bin'
def registrar_cancion_bd(audio):
    cancion = f'../Canciones/{audio}.mp3'
    with open(cancion, 'rb') as file:
        blob = file.read()
        return blob

# Función que guarda la canción en el equipo en formato mp3 -> 'mp3':
def guardar_cancion(data: bin, filename: str):
    try:
        with open(filename, 'wb') as file:
            return file.write(data)
    except:
        pass


# Función que obtiene la canción de la base de datos
def obtener_cancion_db(con) -> str:
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
def reproducir_cancion_function(con):
    mixer.init()
    cancion = obtener_cancion_db(con)
    mixer.music.load(cancion)
    mixer.music.set_volume(0.7)
    mixer.music.play()


def reproducir_cancion(con):
    reproducir_cancion_function(con)
    reproducir = True
    while reproducir:
        try:
            print("\tpulse p para detener canción")
            print("\tpulse r para reanudar canción")
            print("\tpulse e para elegir otra canción")
            print("\tPulse s para salir")

            opcion = input(">>> ")

            if opcion =="p":
                mixer.music.pause()
            elif opcion =="r":
                mixer.music.unpause()
            elif opcion == "e":
                reproducir_cancion_function(con)
            elif opcion =="s":
                mixer.music.stop()
                reproducir = False
        except:
            pass


def consulta_tabla_canciones(con):
    cursor_obj = con.cursor()
    cursor_obj.execute('SELECT id_cancion, nombre_cancion, genero, album, interprete  FROM canciones')
    cantidad_canciones = cursor_obj.fetchall()
    orden_salida = orden_consulta(cantidad_canciones)
    print ("\n{:<12} {:<30} {:<30} {:<30} {:<30}".format('ID', 'NOMBRE', 'GENERO', 'ALBUM', 'INTERPRETE(S)'))
    for row in orden_salida:
        id, nombre, genero, album, interprete = row
        print ("{:<12} {:<30} {:<30} {:<30} {:<30}".format(id, nombre, genero, album, interprete))

# Función que crea un menú para actualizar de manera individual los datos básicos de una canción
def actualizar_datos_cancion(con):
    salir_actualizar = False
    while not salir_actualizar:

        print('''
                            ACTUALIZAR INFORMACIÓN CANCIÓN
                        1. Nombre
                        2. Album
                        3. Genero
                        4. Interprete
                        5. Canción
                        6. Ir al menu anterior\n''')

        opc = input("\tDigite una opcion: ").strip()
        if (opc == '1'):
            actualizar_info_tablas(con, nombre_tabla='canciones', nombre_columna='nombre_cancion', primary_key='id_cancion', info='el nombre de la canción', longitud=100)
        
        elif(opc == '2'):
            actualizar_info_tablas(con, nombre_tabla='canciones', nombre_columna='album', primary_key='id_cancion', info='el album de la canción', longitud=100)

        elif(opc == '3'):
            actualizar_info_tablas(con, nombre_tabla='canciones', nombre_columna='genero', primary_key='id_cancion', info='el genero de la canción', longitud=30)

        elif(opc == '4'):
            actualizar_info_tablas(con, nombre_tabla='canciones', nombre_columna='interprete', primary_key='id_cancion', info='el interprete de la canción', longitud=100)

        elif (opc == '5'):
            actualizar_cancion(con)

        elif(opc == '6'):
            salir_actualizar = True
        
        else:
            print("\t\n¡Opcion no valida. Digite una opción nuevamente!")

