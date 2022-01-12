"""El paquete mixer del modulo pygame importado a continuación es utilizado como
herramienta para la reproducción de las canciones a traves del método mixer"""
"""Importamos el paquete manejadorbd para relizar agunas operaciones en la base de datos"""
"""Importamos el modulo validacion_datos para realizar las diferentes validaciones de los datos
para la base de datos"""
from pygame import mixer
from manejadorbd import *
from validacion_datos import *


# Esta función se encarga de solicitar la informacion de una canción para su registro
# el método validacion_longitud nos sirve para verificar solo la longitud del dato ingresado
# retorna uan tupla con todos los datos necesarios y validados
def cancion() -> tuple:
    nombre = validacion_longitud(input('\nNombre: '), 100)
    genero = validacion_longitud(input('Genero: '), 30)
    album = validacion_longitud(input('Album: '), 100)
    interprete = validacion_longitud(input('Interprete(s): '), 100)
    # imagen = None
    state = False
    while not state:
        try:
            nombre_cancion = input('Nombre de la canción tal cual esta almacenada en su equipo: ')
            cancion = registrar_cancion_bd(nombre_cancion)
            state = True
        except:
            print_line_error('\n¡Error en los datos de la canción en el equipo\n por favor verifique e ingrese de nuevo la información!\n ')

    datos_cancion = (nombre, genero, album, interprete, cancion)
    return datos_cancion


# Función que se encarga de registrar la información y audio de una canción en la tabla canciones
def registrar_cancion(con):
    cursor_obj = con.cursor()
    tupla = cancion()
    cursor_obj.execute('''INSERT INTO canciones VALUES(NULL, ?, ?, ?, ?, NULL, ?)''', tupla)
    con.commit()
    print_line_success("¡¡El registro se ha realizado exitosamente!!")

# Función para relizar la actualización del archivo .mp3 binario dentro de la tabla canciones
def actualizar_cancion(con):
    cursor_obj = con.cursor()
    id = input('\nIngrese el id de la canción a la que quiere modificar: ')
    state = False
    while not state:
        try:
            nombre_cancion = input('Nombre de la canción tal cual esta almacenada en su equipo: ')
            cancion = registrar_cancion_bd(nombre_cancion)
            state = True
        except:
            print_line_error('\n¡Error en los datos de la canción en el equipo\n por favor verifique e ingrese de nuevo la información!\n ')

    actualizar = f'UPDATE canciones SET cancion = ? WHERE id_cancion = ?'
    info_cancion = (cancion, id)
    cursor_obj.execute(actualizar, info_cancion)
    con.commit()
    print_line_success("!El nombre de la cancion se ha modificado exitosamente¡")


# Función que ordena la consulta de la canciones segun el usuario lo desee
def orden_consulta(lista: list) -> tuple:
    
    print_line_menu('''
                        ¿COMO DESEA ORDENAR LA CONSULTA?
                    1. Por id
                    2. Por nombre
                    3. por genero
                    4. por album
                    5. Por interprete(s)\n''')

    opc = input("\n\tDigite una opcion: ")
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


# Función para obtener la dirección de la canción que esta en la base de datos
def obtener_dir_cancion(con) -> str:
    cursor_obj = con.cursor()
    id = input('\nIngrese el id de la canción que desea escuchar: ')
    busqueda = f'SELECT cancion FROM canciones WHERE id_cancion = {id}'
    dir_cancion = cursor_obj.execute(busqueda)
    for dir in dir_cancion:
        return dir[0]


# Función que convierte a binario una cancion -> 'blob-bin'
def registrar_cancion_bd(audio: str) -> bytes:
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


# Función que permite reproducir la canción
def reproducir_cancion_function(con, id_cancion):
    mixer.init()
    cancion = obtener_cancion_db(con, id_cancion)
    mixer.music.load(cancion)
    mixer.music.set_volume(0.7)
    mixer.music.play()

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

# Función que permite manejar el estado de reproducción de una canción con sus diferentes estados
# La canción se reroducirá a penas se realice el llama de la función reproducir_cancion_function
# Uso de mixer.music.pause para pausar la canción
# Uso de mixer.music.unpause para reanudar la canción
# Uso de mixer.music.stop para detener la canción

def reproducir_cancion(con, id_cancion: int, id_cliente: int):
    reproducir_cancion_function(con, id_cancion)
    reproducir = True
    while reproducir:
        try:
            print("\n\tpulse p para detener canción")
            print("\tpulse r para reanudar canción")
            print("\tpulse e para elegir otra canción")
            print("\tPulse s para salir")

            opcion = input(">>> ")

            if opcion =="p":
                mixer.music.pause()
            elif opcion =="r":
                mixer.music.unpause()
            elif opcion == "e":
                consulta_tabla_listas(con, id_cliente)
                id_cancion = int(input('\nDigite el id de la canción que desea reproducir: '))
                id_validacion = validacion_existencia_todas(con, 'listas', 'id_cancion', 'id_cancion', id_cancion)
                while id_validacion != False:
                    id_cancion = int(input('\nDigite el id de la canción que desea reproducir: '))
                    id_validacion = validacion_existencia_todas(con, 'listas', 'id_cancion', 'id_cancion', id_cancion)
                reproducir_cancion_function(con, id_cancion)
            elif opcion =="s":
                mixer.music.stop()
                reproducir = False
        except:
            pass

# Función que permite realizar una consulta de la tabla de datos canciones
# para imprimirlas en pantalla
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
# a través de la función actualizar_info_tablas importada desde el modulo manejadorbd
def actualizar_datos_cancion(con):
    salir_actualizar = False
    while not salir_actualizar:

        print_line_menu('''
                            ACTUALIZAR INFORMACIÓN CANCIÓN
                        1. Nombre
                        2. Album
                        3. Genero
                        4. Interprete
                        5. Canción
                        6. Ir al menu anterior\n''')

        opc = input("\n\tDigite una opcion: ").strip()
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
            print_line_error("\t¡Opcion no valida. Digite una opción nuevamente!")

