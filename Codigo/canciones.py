'''Del modulo manejador_db importamos la Clase ManejadorDB para poder
utilizar la conexón con la base de datos'''
from manejador_db import Manejador_db
'''Del modulo decorador se importa la clase decorador para poder
darle formato a los diferentes print que aparecen en el programa'''
from decorador import Decorador as dec
'''Se generó un paquete de instalación por medio pip para poder utilizar la librería
validatos, creada para el proyecto, para poder validar los datos ingresados por el usuario'''
from validatos.validatos import Validatos as val

"""El paquete mixer del modulo pygame importado a continuación es utilizado como
herramienta para la reproducción de las canciones a traves del método mixer"""
"""Importamos el paquete manejadorbd para relizar agunas operaciones en la base de datos"""
from pygame import mixer


'''Se genera la clase Canciones'''
class Canciones(Manejador_db):
    def __init__(self):
        Manejador_db.__init__(self)
        self.__id = None
        self.__nombre = None
        self.__genero = None
        self.__album = None
        self.__interprete = None
        self.__imagen = None
        self.__audio = None

    # Acontinuacion estan los setters y getters necesarios, seguido de funciones adicionales para su manipulación
    def set_nombre(self):
        self.__nombre = val.longitud(input('Nombre: '), 100)

    def set_genero(self):
        self.__genero = val.longitud(input('Genero: '), 30)

    def set_album(self):
        self.__album = val.longitud(input('Album: '), 100)

    def set_interprete(self):
        self.__interprete = val.longitud(input('Interprete(s): '), 100)

    def set_imagen(self):
        state = False
        while not state:
            try:
                self.__imagen = input('Nombre de la imágen tal cual esta almacenada en su equipo: ')
                self.__imagen = f'../Imagenes/{self.__imagen}.jpg'

                with open(self.__imagen, 'rb') as file:
                    self.__imagen = file.read()
                    state = True
                    return self.__imagen
            except:
                dec.print_line_error(
                    '\n¡La información entregada presenta un error, por favor verifique e ingrese nuevamente!\n')

    def set_audio(self) -> bytes:
        state = False
        while not state:
            try:
                self.__audio = input('Nombre de la canción tal cual esta almacenada en su equipo: ')
                self.__audio = f'../Canciones/{self.__audio}.mp3'
                with open(self.__audio, 'rb') as file:
                    self.__audio = file.read()
                    state = True
                    return self.__audio
            except:
                dec.print_line_error(
                    '\n¡La información entregada presenta un error, por favor verifique e ingrese nuevamente!\n')

    def guardar_imagen(self):
        ruta = f"../Descargas/Imagenes/{self.__nombre}.jpg"
        try:
            with open(ruta, 'wb') as file:
                return file.write(self.__imagen), ruta
        except:
            pass

    #Método para que guarda la canción extraida desde la base de datos en el equipo
    def guardar_cancion(self):
        ruta = f"..\\SpotyUN_Lista\\Canciones\\{self.__nombre}.mp3"
        try:
            with open(ruta, 'wb') as file:
                return file.write(self.__audio), ruta
        except:
            pass


    def consulta_tabla_listas(self, id_cliente: int):
        cursor_obj = self.con.cursor()
        cursor_obj.execute(
            f'SELECT id_cancion, nombre_cancion, interprete, album, genero FROM listas WHERE id_cliente = {id_cliente}')
        cantidad_canciones = cursor_obj.fetchall()
        print("\n{:<12} {:<30} {:<20} {:<20} {:<20}".format('ID_CANCIÓN', 'NOMBRE', 'INTERPRETE', 'ALBUM', 'GENERO'))
        for row in cantidad_canciones:
            id, nombre, interprete, album, genero = row
            print("{:<12} {:<30} {:<20} {:20} {:<20}".format(id, nombre, interprete, album, genero))

    # Funcion que se encarga de obtener toda la información de una canción por medio del id
    def get_cancion(self):
        cursor_obj = self.con.cursor()
        id = int(input('\nIngrese el id de la canción: '))
        busqueda = 'SELECT * FROM canciones WHERE id_cancion = '
        id_busqueda = busqueda + str(id)
        cursor_obj.execute(id_busqueda)
        cancion = cursor_obj.fetchall()
        #print(len(cancion))
        if len(cancion) != 0:
            for row in cancion:
                self.__id = row[0]
                self.__nombre = row[1]
                self.__genero = row[2]
                self.__album = row[3]
                self.__interprete = row[4]
                self.__imagen = row[5]
                self.__audio = row[6]
            return self.__id, self.__nombre, self.__genero, self.__album, self.__interprete, self.__imagen, self.__audio
        else:
            return False

    # La función acontinación se encarga de mostrar al usuario la informacion de una canción consultada
    def consulta_cancion(self):
        try:
            tupla = Canciones.get_cancion(self)
            cabecero = (
                "\n{:<12} {:<30} {:<30} {:<30} {:<30}".format('ID', 'NOMBRE', 'GENERO', 'ALBUM', 'INTERPRETE(S)'))
            datos = ("\n{:<12} {:<30} {:<30} {:30} {:30}".format(tupla[0], tupla[1], tupla[2], tupla[3], tupla[4]))
            print(cabecero, datos)

        except ValueError:
            print("\nEl id ingresado no es valido")

        except TypeError:
            print("\nNo se encontro información relaccionada con el id ingresado")

    # Función que obtiene la información de todas las canciones y la retorna en una lista
    def get_canciones(self):
        cursor_obj = self.con.cursor()
        cursor_obj.execute('SELECT id_cancion, nombre_cancion, genero, album, interprete  FROM canciones')
        lista_canciones = cursor_obj.fetchall()
        return lista_canciones

    # Función que obtiene la información de todas las canciones y la retorna en una lista
    def get_lista_canciones(self):
        cursor_obj = self.con.cursor()
        cursor_obj.execute('SELECT * FROM canciones')
        lista_canciones = cursor_obj.fetchall()
        return lista_canciones
    #Función para reproducir una canción
    def reproducir_cancion(self, dir_cancion):
        mixer.init()
        mixer.music.load(dir_cancion)
        mixer.music.set_volume(0.2)
        mixer.music.play()

    #Función que muestra el menú de opciones para el usuario
    def menu_canciones_reproduccion(self, id_cliente):
        while True:
            try:
                print("\n\tpulse p para detener canción")
                print("\tpulse r para reanudar canción")
                print("\tpulse e para elegir otra canción")
                print("\tPulse s para salir")
                opcion = input(">>> ")
                if opcion == "p":
                    mixer.music.pause()
                elif opcion == "r":
                    mixer.music.unpause()
                elif opcion == "e":
                    Canciones.consulta_tabla_listas(self, id_cliente)
                    while not self.get_cancion():
                        dec.print_line_error('¡Esta canción no esta en tu lista de reproducción!')
                        Canciones.consulta_tabla_listas(id_cliente)
                    Canciones.reproducir_cancion(self, Canciones.guardar_cancion(self)[1])
                elif opcion == "s":
                    mixer.music.stop()
                    break
            except:
                dec.print_line_error('La canción ya se esta reproduciendo')

    # Función que ordena la información obtenida de las canciones
    def orden_consulta(self, lista: list) -> tuple:
        dec.print_line_menu('''
                            ¿COMO DESEA ORDENAR LA CONSULTA?
                        1. Por id
                        2. Por nombre
                        3. por genero
                        4. por album
                        5. Por interprete(s)\n''')

        opc = input("\n\tDigite una opcion: ")
        if (opc == '1'):
            orden = sorted(lista, key=lambda id: id[0])
            return orden

        elif (opc == '2'):
            orden = sorted(lista, key=lambda nombre: nombre[1])
            return orden

        elif (opc == '3'):
            orden = sorted(lista, key=lambda genero: genero[2])
            return orden

        elif (opc == '4'):
            orden = sorted(lista, key=lambda album: album[3])
            return orden

        elif (opc == '5'):
            orden = sorted(lista, key=lambda interprete: interprete[4])
            return orden

    # La función acontinación se encarga de mostrar al usuario el listado de todas las canciones disponibles
    def consulta_canciones_ordenadas(self, tupla):
        print("\n{:<12} {:<30} {:<30} {:<30} {:<30}".format('ID', 'NOMBRE', 'GENERO', 'ALBUM', 'INTERPRETE(S)'))
        for row in tupla:
            self.__id = row[0]
            self.__nombre = row[1]
            self.__genero = row[2]
            self.__album = row[3]
            self.__interprete = row[4]
            print("{:<12} {:<30} {:<30} {:<30} {:<30}".format(self.__id, self.__nombre, self.__genero, self.__album,
                                                              self.__interprete))

    # Función que se encarga de armar una tupla con la información de una canción
    def armar_tupla(self):
        Canciones.set_nombre(self)
        Canciones.set_genero(self)
        Canciones.set_album(self)
        Canciones.set_interprete(self)
        Canciones.set_imagen(self)
        Canciones.set_audio(self)

        cancion = (self.__nombre, self.__genero, self.__album, self.__interprete, self.__imagen, self.__audio)
        return cancion

        # Función que se encarga de registrar la información y audio de una canción en la tabla canciones

    def registrar_db(self, tupla):
        cursor_obj = self.con.cursor()
        cursor_obj.execute('''INSERT INTO canciones VALUES(NULL, ?, ?, ?, ?, ?, ?)''', tupla)
        self.con.commit()
        dec.print_line_success("♪ El registro de la canción se ha realizado exitosamente ♪")

    # Función que sirve para hacer la actualización del audio de una canción
    def actualizar_imagen_db(self):
        cursor_obj = self.con.cursor()
        id = input('\nIngrese el id de la imagen que quiere modificar: ')
        Canciones.set_imagen(self)
        actualizar = f'UPDATE canciones SET imagen = ? WHERE id_cancion = ?'
        info_imagen = (self.__imagen, id)
        cursor_obj.execute(actualizar, info_imagen)
        self.con.commit()
        dec.print_line_success("\n!La imágen se ha actualizado exitosamente¡\n")

    # Función que sirve para hacer la actualización del audio de una canción
    def actualizar_audio_db(self):
        cursor_obj = self.con.cursor()
        id = input('\nIngrese el id de la canción que quiere modificar: ')
        Canciones.set_audio(self)
        actualizar = f'UPDATE canciones SET cancion = ? WHERE id_cancion = ?'
        info_cancion = (self.__audio, id)
        cursor_obj.execute(actualizar, info_cancion)
        self.con.commit()
        dec.print_line_success("\n!La cancion se ha actualizado exitosamente¡\n")

    # Función que crea un menú para actualizar de manera individual los datos básicos de una canción
    # a través de la función actualizar_info_tablas
    def actualizar_info_cancion(self, clase):
        salir_actualizar = False
        while not salir_actualizar:

            dec.print_line_menu('''
                                ACTUALIZAR INFORMACIÓN CANCIÓN
                            1. Nombre
                            2. Album
                            3. Genero
                            4. Interprete
                            5. Imagen
                            6. Canción
                            7. Ir al menu anterior\n''')

            opc = input("\n\tDigite una opcion: ").strip()
            if (opc == '1'):

                Canciones.actualizar_info_tablas(self, clase=clase, info='nombre', nombre_tabla='canciones',
                                                 nombre_columna='nombre_cancion', primary_key='id_cancion')

            elif (opc == '2'):
                Canciones.actualizar_info_tablas(self, clase=clase, info='album', nombre_tabla='canciones',
                                                 nombre_columna='album', primary_key='id_cancion')

            elif (opc == '3'):
                Canciones.actualizar_info_tablas(self, clase=clase, info='genero', nombre_tabla='canciones',
                                                 nombre_columna='genero', primary_key='id_cancion')

            elif (opc == '4'):
                Canciones.actualizar_info_tablas(self, clase=clase, info='interprete', nombre_tabla='canciones',
                                                 nombre_columna='interprete', primary_key='id_cancion')

            elif (opc == '5'):
                Canciones.actualizar_imagen_db(self)

            elif (opc == '6'):
                Canciones.actualizar_audio_db(self)

            elif (opc == '7'):
                salir_actualizar = True

            else:
                dec.print_line_error("\t¡Opcion no valida. Digite una opción nuevamente!")

    # Esta función guarda la canción en el equipo en formato mp3 -> 'mp3'
    # para posteriormente reproducirla