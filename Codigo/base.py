"""El paquete mixer del modulo pygame importado a continuación es utilizado como
herramienta para la reproducción de las canciones a traves del método mixer"""
"""Importamos el paquete manejadorbd para relizar agunas operaciones en la base de datos"""
"""Importamos el modulo validacion_datos para realizar las diferentes validaciones de los datos
para la base de datos"""
from pygame import mixer
from decorador import *
from validatos.validatos import Validatos as val
from datetime import datetime
import sqlite3
from sqlite3 import Error
from subprocess import HIGH_PRIORITY_CLASS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Manejador_db():
    def __init__(self):
        self.con = Manejador_db.__sql_conexion(self)

    # Conexion con la base de datos
    def __sql_conexion(self):
        try:
            con = sqlite3.connect('SpotyUN_2.db')
            return con
        
        except Error:
            print(Error)

    def close(self):
        self.con.close()

    # Función para actualizar la información de uno de los campos de la tabla en la base de datos
    def actualizar_info_tablas(self, nombre_columna: str, nombre_tabla: str, primary_key: str, info = "indefinido"):
        state = True
        while state:
            try:
                id = input('Ingrese el id: ').strip()
                if id_v := val.existencia_tablas(self.con, nombre_tabla, nombre_columna, primary_key, id) == False:
                    id = int(id)
                    state = False
                    
                else:
                    print('\nEl id ingresado no existe en la base de datos')
            except:
                print('El id ingresado no es correcto')

        cursor_obj = self.con.cursor()
        cadena = f'UPDATE {nombre_tabla} SET {nombre_columna} = ? WHERE {primary_key} = ?'
        cursor_obj.execute(cadena, (info, id ))
        self.con.commit()
        print_line_success(f"!\"{info.title()}\" se ha actualizado exitosamente¡")
        
#----------------------------------------------------------------------------------------


# La clase canciones maneja toda la información relaccionada a las canciones
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
        return self._imagen

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
                print_line_error('\n¡La información entregada presenta un error, por favor verifique e ingrese nuevamente!\n')


    # Funcion que se encarga de obtener toda la información de una canción por medio del id
    def get_cancion(self):
        cursor_obj = self.con.cursor()
        id = int(input('\nIngrese el id de la canción: '))
        busqueda = 'SELECT * FROM canciones WHERE id_cancion = '
        id_busqueda = busqueda + str(id)
        cursor_obj.execute(id_busqueda)
        cancion = cursor_obj.fetchall()
        for row in cancion:
            self.__id = row[0]
            self.__nombre = row[1]
            self.__genero = row[2]
            self.__album = row[3]
            self.__interprete = row[4]
            self.__imagen = row[5]
            self.__audio = row[6]

    # La función acontinación se encarga de mostrar al usuario la informacion de una canción consultada
    def consulta_cancion(self):
        try:
            Canciones.get_cancion(self)
            cabecero = ("\n{:<12} {:<30} {:<30} {:<30} {:<30}".format('ID', 'NOMBRE', 'GENERO', 'ALBUM', 'INTERPRETE(S)'))
            datos = ("\n{:<12} {:<30} {:<30} {:30} {:30}".format(self.__id, self.__nombre, self.__genero, self.__album, self.__interprete))
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

    # Función que ordena la información obtenida de las canciones
    def orden_consulta(self, lista: list) -> tuple:
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

    # La función acontinación se encarga de mostrar al usuario el listado de todas las canciones disponibles
    def consulta_canciones(self, tupla):
        print ("\n{:<12} {:<30} {:<30} {:<30} {:<30}".format('ID', 'NOMBRE', 'GENERO', 'ALBUM', 'INTERPRETE(S)'))
        for row in tupla:
            self.__id = row[0]
            self.__nombre = row[1]
            self.__genero = row[2]
            self.__album = row[3]
            self.__interprete = row[4]
            print ("{:<12} {:<30} {:<30} {:<30} {:<30}".format(self.__id, self.__nombre, self.__genero, self.__album, self.__interprete))

    
    # Función que se encarga de armar una tupla con la información de una canción
    def armar_tupla(self):
        Canciones.set_nombre(self)
        Canciones.set_genero(self)
        Canciones.set_album(self)
        Canciones.set_interprete(self)
        Canciones.set_audio(self)

        cancion = (self.__nombre, self.__genero, self.__album, self.__interprete, self.__audio)
        return cancion 


    # Función que se encarga de registrar la información y audio de una canción en la tabla canciones
    def registrar_db(self, tupla):
        cursor_obj = self.con.cursor()
        cursor_obj.execute('''INSERT INTO canciones VALUES(NULL, ?, ?, ?, ?, NULL, ?)''', tupla)
        self.con.commit()
        print_line_success("♪ El registro de la canción se ha realizado exitosamente ♪")
    
    # Función que sirve para hacer la actualización del audio de una canción
    def actualizar_audio_db(self):
        cursor_obj = self.con.cursor()
        id = input('\nIngrese el id de la canción a la que quiere modificar: ')
        Canciones.set_audio(self)
        actualizar = f'UPDATE canciones SET cancion = ? WHERE id_cancion = ?'
        info_cancion = (self.__audio, id)
        cursor_obj.execute(actualizar, info_cancion)
        self.con.commit()
        print_line_success("\n!La cancion se ha actualizado exitosamente¡\n")

    # Función que crea un menú para actualizar de manera individual los datos básicos de una canción
    # a través de la función actualizar_info_tablas
    def actualizar_info_cancion(self):
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
            if  (opc == '1'):
                Canciones.set_nombre(self)
                Canciones.actualizar_info_tablas(self, info = self.__nombre, nombre_tabla = 'canciones', nombre_columna = 'nombre_cancion', primary_key = 'id_cancion')
            
            elif(opc == '2'):
                Canciones.set_album(self)
                Canciones.actualizar_info_tablas(self, info = self.__album, nombre_tabla = 'canciones', nombre_columna = 'album', primary_key = 'id_cancion')
            
            elif(opc == '3'):
                Canciones.set_genero(self)
                Canciones.actualizar_info_tablas(self,  info = self.__genero, nombre_tabla = 'canciones', nombre_columna = 'genero', primary_key = 'id_cancion')
            
            elif(opc == '4'):
                Canciones.set_interprete(self)
                Canciones.actualizar_info_tablas(self,  info = self.__interprete, nombre_tabla = 'canciones', nombre_columna = 'interprete', primary_key = 'id_cancion')
            
            elif(opc == '5'):
                Canciones.actualizar_audio_db(self)

            elif(opc == '6'):
                 salir_actualizar = True
            
            else:
                 print_line_error("\t¡Opcion no valida. Digite una opción nuevamente!")


    # Esta función guarda la canción en el equipo en formato mp3 -> 'mp3'
    # para posteriormente reproducirla


#----------------------------------------------------------------------------------------

# c = Canciones()
# c.registrar_db(c.armar_tupla())

# c.reproducir_cancion(c.guardar_cancion()[1])
# x = Canciones(con)
# x.consulta_canciones(x.orden_consulta(x.get_canciones()))
# cancion = Canciones()
# cancion.actualizar_info_cancion()
# can2 = Canciones()
# can2.registrar_db(con, can2.armar_tupla())


class Planes(Manejador_db):
    def __init__(self):
        Manejador_db.__init__(self)
        self.__id = None
        self.__nombre = None
        self.__valor = None
        self.cant_canciones = None

    def set_id(self):
        self.__id = val.numero(input('\nId del plan: '), 1)
        validacion = val.existencia_tablas(self.con, nombre_tabla = 'planes', nombre_columna = 'id_plan', primary_key = 'id_plan', id = self.__id)

        while validacion == False:
            print('\t\n¡ERROR! Ya existe un plan con el \'Id plan\' ingresado. Si desea realizar el registro ingrese nuevamente la información.')
            self.__id = val.numero(input('\nId del plan: '), 1)
            validacion = val.existencia_tablas(self.con, nombre_tabla = 'planes', nombre_columna = 'id_plan', primary_key = 'id_plan', id = self.__id)
    
    def set_nombre(self):
        self.__nombre = input("Nombre del plan: ")

    def set_valor(self):
        self.__valor = int(val.numero(input("Valor plan: "),5))

    def set_cant_canciones(self):
        self.cant_canciones = int(val.numero(input("Cantidad de canciones del plan: "),4))


    # Función que se encarga obtener toda la información de un plan por medio del id
    def get_plan(self):
        cursor_obj = self.con.cursor()
        self.__id = int(input('\n Ingrese el id del plan: '))
        busqueda = 'SELECT * FROM planes WHERE id_plan = '
        id_busqueda = busqueda + str(self.__id)
        cursor_obj.execute(id_busqueda)
        plan = cursor_obj.fetchall()
        for row in plan:
            self.__id = row[0]
            self.__nombre = row[1]
            self.__valor = row[2]
            self.cant_canciones = row[3]

    # La función acontinación se encarga de mostrar al usuario la informacion de una canción consultada
    def consulta_plan(self):
        try:
            Planes.get_plan(self)
            cabecero =("\n{:<5} {:<15} {:<10} {:<10} ".format('ID', 'NOMBRE_PLAN', 'VALOR', 'CANTIDAD CANCIONES'))
            datos = ("\n{:<5} {:<15} {:<10} {:<10} ".format(self.__id, self.__nombre, self.__valor, self.cant_canciones))
            print(cabecero, datos)
        except ValueError:
            print("\n El id ingresado no es valido")

        except TypeError:
            print("\n No se encontro información relaccionada")

    # Funcion que obtiene la información de todos los planes y la retorna en una lista
    def get_planes(self):
        cursor_obj = self.con.cursor()
        cursor_obj.execute('SELECT * FROM planes')
        lista_planes = cursor_obj.fetchall()
        return lista_planes

    
    # Función que ordena la información obtenida de las canciones
    def orden_consulta(self, lista: list) -> tuple:
        print_line_menu('''
                            ¿EN QUE ORDEN DESEA OBTENER LA CONSULTA?
                        1. Por id
                        2. Por nombre
                        3. por valor
                        4. por cantidad de canciones a las que puede acceder\n''')

        opc = input("\n\tDigite una opcion: ")
        if (opc == '1'):
            orden = sorted(lista, key = lambda id : id[0])
            return orden
            
        elif(opc == '2'):
            orden = sorted(lista, key = lambda nombre : nombre[1])
            return orden
            
        elif(opc == '3'):
            orden = sorted(lista, key = lambda valor : valor[2])
            return orden

        elif(opc == '4'):
            orden = sorted(lista, key = lambda cantidad_canciones : cantidad_canciones[3])
            return orden  


    # La función acontinación se encarga de mostrar al usuario el listado de todas los planes disponibles
    def consulta_planes(self, tupla):
        print ("\n{:<5} {:<15} {:<10} {:<10} ".format('ID', 'NOMBRE PLAN', 'VALOR', 'CANTIDAD CANCIONES'))
        for row in tupla:
            self.__id = row[0]
            self.__nombre = row[1]
            self.__valor = row[2]
            self.cant_canciones = row[3]
            print ("{:<5} {:<15} {:<10} {:<10} ".format(self.__id, self.__nombre, self.__valor, self.cant_canciones))
            
    # Función que se encarga de armar una tupla con la información de un plan
    def armar_tupla(self):
        Planes.set_id(self)
        Planes.set_nombre(self)
        Planes.set_valor(self)
        Planes.set_cant_canciones(self)
    
        plan = (self.__id, self.__nombre, self.__valor, self.cant_canciones)
        return plan

    # Función que se encarga de registrar la información de un plan en la tabla planes
    def registrar_db(self, tupla):
        cursor_obj = self.con.cursor()
        cursor_obj.execute('''INSERT INTO planes VALUES(?,?,?,?)''', tupla)
        self.con.commit()
        print_line_success('¡El plan se ha registrado exitosamente!')

    # Función que crea un menú para actualizar de manera individual los datos básicos de un plan
    # a través de la función actualizar_info_tablas
    def actualizar_info_plan(self):
        salir_actualizar = False
        while not salir_actualizar:

            print_line_menu('''
                                ACTUALIZAR INFORMACIÓN PLAN
                            1. Nombre
                            2. Valor
                            3. Cantidad de canciones
                            4. Ir al menu anterior\n''')

            opc = input("\n\tDigite una opcion: ").strip()
            if (opc == '1'):
                Planes.set_nombre(self)
                Planes.actualizar_info_tablas(self, info = self.__nombre, nombre_tabla = 'planes', nombre_columna = 'nombre_plan', primary_key = 'id_plan')
                
            elif(opc == '2'):
                Planes.set_valor(self)
                Planes.actualizar_info_tablas(self, info = self.__valor, nombre_tabla = 'planes', nombre_columna = 'nombre_plan', primary_key = 'id_plan')

            elif(opc == '3'):
                Planes.set_cant_canciones(self)
                Planes.actualizar_info_tablas(self, info = self.cant_canciones, nombre_tabla = 'planes', nombre_columna = 'nombre_plan', primary_key = 'id_plan')

            elif(opc == '4'):
                salir_actualizar = True
            
            else:
                print_line_error("\t\n¡Opcion no valida. Digite una opción nuevamente!")

    # La función acontinuación se encarga de eliminar un plan de la base de datos con el id
    def eliminar_plan(self):
        self.__id = val.numero(input('\nId del plan: '), 1)
        cursor_obj = self.con.cursor()
        cursor_obj.execute(f'DELETE FROM planes WHERE id_plan = {self.__id}')
        self.con.commit()
        print_line_success('¡ El plan se ha eliminado exitosamente')        
        
        
#----------------------------------------------------------------------------------------

# plan = Planes()
# plan.registrar_db(plan.armar_tupla())
# p = Planes(con)
# p.consulta_plan()
# n =  Planes(con)
# n.consulta_planes(n.orden_consulta(n.get_planes()))
# a = Planes(con)
# a.actualizar_info_plan()

class Cliente(Manejador_db):
    def __init__(self):
        Manejador_db.__init__(self)
        self.__id = None
        self.__nombre = None
        self.__apellido = None
        self.__pais = None
        self.__ciudad = None
        self.__celular = None
        self.__correo = None
        self.__fecha_pago = None
        self.__numero_tc = None
        self.__estado_pago = None

    def set_id(self):
        self.__id = val.numero(input('\nNúmero de identificación: '), 12)
        validacion = val.existencia_tablas(self.con, nombre_tabla = 'clientes', nombre_columna = 'id_cliente', primary_key = 'id_cliente', id = self.__id)
        while validacion == False:
            print('\n¡El número de identificación ya existe, por favor ingrese otro número de identificación!')
            self.__id = val.numero(input('Número de identificación: '), 12)
            validacion = val.existencia_tablas(self.con, nombre_tabla = 'clientes', nombre_columna = 'id_cliente', primary_key = 'id_cliente', id = self.__id)
    
    def set_nombre(self):
        self.__nombre = val.letra(input('Nombre: '), 30)

    def set_apellido(self):
        self.__apellido = val.letra(input('Apellido: '), 30)

    def set_pais(self):   
        self.__pais = val.letra(input('Pais: '), 30)

    def set_ciudad(self):
        self.__ciudad = val.letra(input('Ciudad: '), 30)

    def set_celular(self):
        self.__celular = val.telefono(input('Celular: '), 15)

    def set_correo(self):
        self.__correo = val.correo(input('Correo electrónico: '), 45)

    def set_fecha_pago(self):
        self.__fecha_pago = datetime.strftime(datetime.now(), '%Y-%m-%d')

    def set_numero_tc(self):
        self.__numero_tc = val.numero(input('Tarjeta de credito (sin espacios ni caracteres especiales): '), 19)

    def set_estado_pago(self):
        self.__estado_pago = 'Activo'

    def get_id(self):
        return [self.__id]
        

    # Funcion que se encarga de obtener toda la información de un cliente por medio del id
    def get_cliente(self):
        cursor_obj  = self.con.cursor()
        id = int(input('\nIngrese su identificación: ').strip())
        busqueda = 'SELECT * FROM clientes WHERE id_cliente = '
        id_busqueda = busqueda + str(id)
        cursor_obj.execute(id_busqueda)
        cliente = cursor_obj.fetchall()
        for row in cliente:
            self.__id = row[0]
            self.__nombre = row[1]
            self.__apellido = row[2]
            self.__pais = row[3]
            self.__ciudad = row[4]
            self.__celular = row[5]
            self.__correo = row[6]
            self.__fecha_pago = row[7]
            self.__numero_tc = row[8]
            self.__estado_pago = row [9]

    # La función acontinación se encarga de mostrar al usuario la información que dio cuando realizo su registro
    def consulta_cliente(self):
        try:
            Cliente.get_cliente(self)
            cabecero_0 = ("\n{:<30} {:<30} {:<30} {:<30} {:<30} ".format('IDENTIFICACION', 'NOMBRE', 'APELLIDO', 'PAIS', 'CIUDAD'))
            datos_0 = ("\n{:<30} {:<30} {:<30} {:<30} {:<30} ".format(self.__id, self.__nombre, self.__apellido, self.__pais, self.__ciudad))
            cabecero_1 = ("\n{:<30} {:<30} {:<30} {:<30} {:<30} ".format('CELULAR', 'CORREO', 'FECHA DE PAGO', 'NUMERO TC', 'ESTADO PAGO'))
            datos_1 = ("\n{:30} {:<30} {:<30} {:<30} {:<30} ".format(self.__celular,  self.__correo, self.__fecha_pago, self.__numero_tc, self.__estado_pago))
            print(cabecero_0, datos_0, cabecero_1, datos_1)

        except ValueError:
            print("\n El id ingresado no es valido")

        except TypeError:
            print("\n No se encontro información relaccionada")
            
    # Función que obtiene la información de todas los clientes y la retorna en una lista
    def get_clientes(self):
        cursor_obj = self.con.cursor()
        cursor_obj.execute('SELECT id_cliente, nombre_cliente, apellido FROM  clientes')
        lista_clientes = cursor_obj.fetchall()
        return lista_clientes

    # Función que ordena la información obtenida de los clientes
    def orden_consulta(self, lista: list) -> tuple:
        print_line_menu('''
                            ¿EN QUE ORDEN DESEA OBTENER LA CONSULTA?
                        1. Por id
                        2. Por nombre
                        3. por apellido\n''')

        opc = input("\n\tDigite una opcion: ")
        if (opc == '1'):
            orden = sorted(lista, key=lambda id: id[0])
            return orden

        elif (opc == '2'):
            orden = sorted(lista, key=lambda nombre: nombre[1])
            return orden

        elif (opc == '3'):
            orden = sorted(lista, key=lambda apellido: apellido[2])
            return orden


    # La función acontinación se encarga de mostrar un listado de la información basica de los clientes
    def consulta_clientes(self, tupla):
        print("\n{:<20} {:<20} {:<20}".format('IDENTIFICACIÓN', 'NOMBRE', 'APELLIDO'))
        for row in tupla:
            self.__id = row[0]
            self.__nombre = row[1]
            self.__apellido = row[2]
            print("{:<20} {:<20} {:<20}".format(self.__id, self.__nombre, self.__apellido))


    # Función que se encarga de armar una tupla con la información de un cliente
    def armar_tupla(self):
        Cliente.set_id(self)
        Cliente.set_nombre(self)
        Cliente.set_apellido(self)
        Cliente.set_pais(self)
        Cliente.set_ciudad(self)
        Cliente.set_celular(self)
        Cliente.set_correo(self)
        Cliente.set_fecha_pago(self)
        Cliente.set_numero_tc(self)
        Cliente.set_estado_pago(self)
    
        cliente = (self.__id, self.__nombre, self.__apellido, self.__pais, self.__ciudad,
        self.__celular, self.__correo, self.__fecha_pago, self.__numero_tc, self.__estado_pago)
        return cliente

    # Función que se encarga de registrar la información de un cliente en la base de datos
    def registrar_db(self, tupla):
        cursor_obj = self.con.cursor()
        cursor_obj.execute('''INSERT INTO clientes VALUES (?,?,?,?,?,?,?,?,?,?)''', tupla)
        self.con.commit()
        
    # Función que crea un menu para actualizar de manera individual los datos básicos de un cliente
    # a través de su id y la función actualizar_info_tablas
    def actualizar_info_cliente(self):
        salir_actualizar = False
        while not salir_actualizar:

            print_line_menu('''
                                    ACTUALIZAR DATOS CLIENTE
                                1. Nombre
                                2. Apellido
                                3. Celular
                                4. Tarjeta de crédito
                                5. País
                                6. Ciudad
                                7. Correo
                                8. Ir al menu anterior\n''')

            opc = input("\n\tDigite una opcion: ").strip()
            if (opc == '1'):
                Cliente.set_nombre(self)
                Cliente.actualizar_info_tablas(self,  info = self.__nombre, nombre_tabla = 'clientes', nombre_columna = 'nombre_cliente',  primary_key = 'id_cliente')

            elif (opc == '2'):
                Cliente.set_apellido(self)
                Cliente.actualizar_info_tablas(self,  info = self.__apellido, nombre_tabla = 'clientes', nombre_columna = 'apellido',  primary_key = 'id_cliente')

            elif (opc == '3'):
                Cliente.set_celular(self)
                Cliente.actualizar_info_tablas(self,  info = self.__celular, nombre_tabla = 'clientes', nombre_columna = 'celular',  primary_key = 'id_cliente')
            
            elif (opc == '4'):
                Cliente.set_numero_tc(self)
                Cliente.actualizar_info_tablas(self,  info = self.__numero_tc, nombre_tabla = 'clientes', nombre_columna = 'numero_tc',  primary_key = 'id_cliente')
                
            elif (opc == '5'):
                Cliente.set_pais(self)
                Cliente.actualizar_info_tablas(self,  info = self.__pais, nombre_tabla = 'clientes', nombre_columna = 'pais',  primary_key = 'id_cliente')
                
            elif (opc == '6'):
                Cliente.set_ciudad(self)
                Cliente.actualizar_info_tablas(self,  info = self.__ciudad, nombre_tabla = 'clientes', nombre_columna = 'ciudad',  primary_key = 'id_cliente')

            elif (opc == '7'):
                Cliente.set_correo(self)
                Cliente.actualizar_info_tablas(self,  info = self.__correo, nombre_tabla = 'clientes', nombre_columna = 'correo',  primary_key = 'id_cliente')

            elif (opc == '8'):
                salir_actualizar = True
            
            else:
                print_line_error("¡Opcion no valida. Digite una opción nuevamente!")

    def actualizar_estado_suscripcion(self):
        salir = False
        while not salir:
            
            print_line_menu('''
                        Para cambiar su estado de suscripción elija una opción
                        1. Activo
                        2. Inactivo''')

            opc = input("\n\tDigite una opcion: ").strip()
            if (opc == '1'):
                self.__estado_pago = 'Activo'
                Cliente.actualizar_info_tablas(self, info = self.__estado_pago,  nombre_tabla = 'clientes', nombre_columna = 'estado_pago', primary_key = 'id_cliente')
                salir = True
            elif (opc == '2'):
                self.__estado_pago = 'Inactivo'
                Cliente.actualizar_info_tablas(self, info = self.__estado_pago,  nombre_tabla = 'clientes', nombre_columna = 'estado_pago', primary_key = 'id_cliente')
                salir = True
            else:
                print_line_error("¡Opcion no valida. Digite una opción nuevamente!")
                
     
# l = Cliente(con)
# l.consulta_cliente()
# d = Cliente(con)
# d.consulta_clientes(d.orden_consulta(d.get_clientes()))
# a = Cliente(con)
# a.actualizar_info_cliente()

#----------------------------------------------------------------------------------------

# PP_cliente = (planes por cliente)
class PP_cliente(Planes):
    def __init__(self):
        Planes.__init__(self)
        self.__id_cliente = None
        self.__id_plan_c = None

    def set_id_cliente(self):
        self.__id_cliente = val.numero(input('Ingrese su identificación: '), 12)
        
    def set_id_plan_c(self):
        PP_cliente.consulta_planes(self, PP_cliente.get_planes(self))
        self.__id_plan_c = val.numero(input('\nIngrese el id del plan que desea contratar: '), 1)
        validacion = val.existencia_tablas(self.con, nombre_tabla = 'planes', nombre_columna = 'id_plan', primary_key='id_plan', id = self.__id_plan_c )
        while validacion != False :
            print_line_error('¡No existe un plan con ese id, por favor ingrese uno que sea valido!')
            self.__id_plan_c = val.numero(input('\nIngrese el id del plan que desea contratar: '), 1)
            validacion = val.existencia_tablas(self.con, nombre_tabla = 'planes', nombre_columna = 'id_plan', primary_key = 'id_plan', id = self.__id_plan_c)

    # La función acontinuación se encarga de obtener la cantidad de canciones que ofrece el plan que contrato
    def get_cant_canciones(self):
        cursor_obj = self.con.cursor()
        busqueda = 'SELECT cantidad_canciones FROM planes WHERE id_plan = '
        id_busqueda = busqueda + str(self.__id_plan_c)
        cursor_obj.execute(id_busqueda)
        cant_canciones = cursor_obj.fetchall()
        for row in cant_canciones:
            self.cant_canciones = row[0]

    # Función que obtiene el id del plan y la cantidad de canciones, de los planes contratados por el cliente
    def get_pp_cliente(self, id_cliente):
        cursor_obj = self.con.cursor()
        cursor_obj.execute(f'SELECT * FROM planes_cliente WHERE id_cliente = {id_cliente}')
        lista_pp_cliente = cursor_obj.fetchall()
        return lista_pp_cliente

    # La función acontinuación se encarga de mostrar al usuario los datos basicos del los planes que ha contratado
    def consulta_pp_cliente(self, tupla):
        print ("\n{:<15} {:<20} {:<15} ".format('ID CLIENTE', 'ID PLAN', 'CANTIDAD CANCIONES'))
        for row in tupla:
            self.__id_cliente = row[0]
            self.__id_plan_c = row[1]
            self.cant_canciones = row[2]
            
        print ("{:<15} {:<20} {:<15} ".format(self.__id_cliente, self.__id_plan_c, self.cant_canciones))
        

    # La función acontinuación se encarga de verificar si un cliente esta registrado o no
    # con el fin de dar paso a la seccion de 'Planes cliente' unicamente si ya ha realizado su registro
    def verificacion_existencia(self) -> bool or int:
        cursor_obj = self.con.cursor()
        PP_cliente.set_id_cliente(self)
        cursor_obj.execute(f'SELECT id_cliente FROM planes_cliente WHERE id_cliente = {self.__id_cliente}')
        self.__id_cliente = cursor_obj.fetchone()
        if self.__id_cliente == None:
            print('¡Antes de poder registrar otro plan o lista de reproducción debes ser un cliente registrado!')
            return False
        else:
            print_line_success('¡Validación de usuario exitosa!')
            return self.__id_cliente
           

    #  Función que se encarga de armar una tupla con el el id del plan contratado por el cliente
    def armar_arreglo(self):
        PP_cliente.set_id_plan_c(self)
        PP_cliente.get_cant_canciones(self)
        plan_c = [self.__id_plan_c, self.cant_canciones]
        return plan_c
       
    #  función que se encarga de registrar el id('identificación') del cliente y el id del plan que contrato
    def registrar_db(self, tupla):
        cursor_obj = self.con.cursor()
        cursor_obj.execute('''INSERT INTO planes_cliente VALUES(?,?,?)''', tupla)
        self.con.commit()
        print_line_success('¡Su registro se ha realizado exitosamente!')

    
    
class Listas_cliente(Canciones, Manejador_db):
    def __init__(self):
        Canciones.__init__(self)
        Manejador_db.__init__(self)
        
# Función para realizar la consulta de datos de la canción como id_canción, nombre_canción, interprete, album
    def id_cancion_lista(self) -> list:
        canciones = input('\nIngrese el id de cancion que desea agregar a su lista: ')
        while canciones == '0':
            break
        cursor_obj = self.con.cursor()
        cursor_obj.execute(f"SELECT * FROM canciones WHERE id_cancion = {canciones}")
        filas = cursor_obj.fetchall()
        for row in filas:
            id_cancion = row[0]
            nombre_cancion = row[1]
            interprete = row[4]
            album = row[3]
            genero = row[2]
        lista_info_cancion = [id_cancion, nombre_cancion, interprete, album, genero]
        return lista_info_cancion

    def guardar_cancion(self):
        ruta = f"../SpotyUN_Lista/{self._Canciones__nombre}.mp3"
        try:
            with open(ruta, 'wb') as file:
                return file.write(self._Canciones__audio), ruta
        except:
            pass

    # La función acontinuación se encarga de reproducir la canción que el usuario elija ingresando el id
    def reproducir_cancion(self, dir_cancion, id_cliente):
        mixer.init()
        mixer.music.load(dir_cancion)
        mixer.music.set_volume(0.7)
        mixer.music.play()
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
                    Listas_cliente.consulta_tabla_listas(self, id_cliente)
                    Listas_cliente.get_cancion(self)
                    id_validacion = val.existencia_tablas(self.con, 'listas', 'id_cancion', 'id_cancion', self._Canciones__id)
                    while id_validacion != False:
                        Listas_cliente.get_cancion(self)
                        id_validacion = val.existencia_tablas(self.con, 'listas', 'id_cancion', 'id_cancion', self._Canciones__id)
                    Listas_cliente.reproducir_cancion(self, Listas_cliente.guardar_cancion(self)[1], id_cliente)
                elif opcion =="s":
                    mixer.music.stop()
                    reproducir = False
            except:
                pass

    # Función para consultar la cantidad de canciones por plan de acuerdo al registro del cliente
    def plan_cliente(self, id_cliente: int) -> int:
        cursor_obj = self.con.cursor()
        cursor_obj.execute(f'SELECT id_plan FROM planes_cliente WHERE id_cliente = {id_cliente}')
        id_plan_cliente = cursor_obj.fetchone()
        cursor_obj.execute(f'SELECT cantidad_canciones FROM planes WHERE id_plan = {id_plan_cliente[0]}')
        cant_canciones = cursor_obj.fetchone()
        return cant_canciones


    # Función que reliza un conteo de los registros en la tabla listas de acuerdo al id_cliente suministrado
    def contar_lista(self, id_cliente: int) -> str or int:
        cursor_obj = self.con.cursor()
        cursor_obj.execute(f'SELECT COUNT(*) FROM listas WHERE id_cliente = {id_cliente}')
        cantidad_listas = cursor_obj.fetchone()
        if cantidad_listas[0] == None:
            return 0
        return cantidad_listas


    # Función para consultar las canciones existentes en la tabla canciones y mostrarlas en pantalla
    def consulta_tabla_canciones_lista(self):
        cursor_obj = self.con.cursor()
        cursor_obj.execute('SELECT id_cancion, nombre_cancion, genero, album, interprete  FROM canciones')
        cantidad_canciones = cursor_obj.fetchall()
        print("\n{:<12} {:<20} {:<20} {:<20} {:<20}".format('ID', 'NOMBRE', 'GENERO', 'ALBUM', 'INTERPRETE(S)'))
        for row in cantidad_canciones:
            id, nombre, genero, album, interprete = row
            print("{:<12} {:<20} {:<20} {:<20} {:<20}".format(id, nombre, genero, album, interprete))


    # Función para agregar en una tupla la información correspondiente para la tabla listas
    # necesitamos el id_cliente y la lista info_canciones
    def info_lista(self, id_cliente: int) -> tuple:
        id_c = id_cliente
        info_canciones = Listas_cliente.id_cancion_lista(self)
        info_canciones.append(id_c)
        return info_canciones


    # Función para registrar la información en la tabla listas
    def registrar_lista_cliente(self, tupla: tuple):
        cursor = self.con.cursor()
        cursor.execute('''INSERT INTO listas VALUES (?,?,?,?,?,?)''', tupla)
        self.con.commit()
        print_line_success("¡¡El registro se ha realizado exitosamente!!")


    # Función para consultar la lista de canciones registradas en la tabla listas
    # de acuerdo al id suministrado por el cliente
    def consulta_tabla_listas(self, id_cliente: int):
        cursor_obj = self.con.cursor()
        cursor_obj.execute(f'SELECT id_cancion, nombre_cancion, interprete, album, genero FROM listas WHERE id_cliente = {id_cliente}')
        cantidad_canciones = cursor_obj.fetchall()
        print("\n{:<12} {:<30} {:<20} {:<20} {:<20}".format('ID_CANCIÓN', 'NOMBRE', 'INTERPRETE', 'ALBUM', 'GENERO'))
        for row in cantidad_canciones:
            id, nombre, interprete, album, genero = row
            print("{:<12} {:<30} {:<20} {:20} {:<20}".format(id, nombre, interprete, album, genero))


    # Función que borra una lista de reproducción de la tabla listas de acuerdo al id_cliente suministrado
    def borrar_lista(self, id_cliente: int) -> str:
        cursor_obj = self.con.cursor()
        cursor_obj.execute(f'DELETE FROM listas WHERE id_cliente = {id_cliente}')
        self.con.commit()
        return print('Tu lista ha sido eliminada')
    
    def verificacion_existencia(self) -> bool or int:
        cursor_obj = self.con.cursor()
        PP_cliente.set_id_cliente(self)
        cursor_obj.execute(f'SELECT id_cliente FROM planes_cliente WHERE id_cliente = {self.__id_cliente}')
        self.__id_cliente = cursor_obj.fetchone()
        if self.__id_cliente == None:
            print('¡Antes de poder registrar otro plan o lista de reproducción debes ser un cliente registrado!')
            return False
        else:
            print_line_success('¡Validación de usuario exitosa!')
            return self.__id_cliente

    # Función que consulta la información ingresa por el cliente en la tabla listas, retorna una tupla
    # una tupla de listas con la información completa de la lista de reproducción
    def consulta_tabla_listas_id(self, id_cliente: int) -> bool or tuple:
        cursor_obj = self.con.cursor()
        cursor_obj.execute(f'SELECT id_cancion, nombre_cancion, interprete, album, genero FROM listas WHERE id_cliente = {id_cliente}')
        cantidad_canciones = cursor_obj.fetchall()
        if cantidad_canciones == []:
            return False
        else:
            return cantidad_canciones

    # Función que obtiene el correo del cliente
    def consulta_correo_cliente(self, id_cliente: int) -> str:
        cursor_obj = self.con.cursor()
        cursor_obj.execute(f'SELECT correo FROM clientes WHERE id_cliente = {id_cliente}')
        correo = cursor_obj.fetchall()
        return correo


    # Función para realizar la consulta de la tabla listas para poder enviarla en el correo electrónico
    # Retorna un string con formato html para poderlo ingresar en la función enviar_correo
    def consulta_tabla_para_html(self, id_cliente: int) -> list:
        cursor_obj = self.con.cursor()
        cursor_obj.execute(f'SELECT id_cancion, nombre_cancion, interprete, album, genero FROM listas WHERE id_cliente = {id_cliente}')
        cantidad_canciones = cursor_obj.fetchall()
        lista_str = ''
        for row in cantidad_canciones:
            id, nombre_cancion, interprete, album, genero = row
            lista_str += (f"<tr><td>{id}</td><td>{nombre_cancion}</td><td>{interprete}</td><td>{album}</td><td>{genero}</td></tr>")
        return lista_str


    # Función para enviar el mensaje con la lista de reproducción del cliente
    def enviar_mensaje(self, id_cliente: int):
        info_tabla = Listas_cliente.consulta_tabla_para_html(self, id_cliente)
        canciones_plan= Listas_cliente.plan_cliente(self, id_cliente)[0]
        canciones_lista = Listas_cliente.contar_lista(self, id_cliente)[0]
        canciones_disponibles = canciones_plan - canciones_lista
        mensaje = MIMEMultipart()
        mensaje['Subject'] = 'CONFIRMACION DE LISTA DE REPRODUCCIÓN'
        html = f"""\
            <html>
            <head></head>
            <body>
                <p>Hi! Spotynauta<br>
                Envio tu lista de reproducción ;)               
                <br>
                <table class="default" border="2" "cellspacing="10" bordercolor="#ffffff">
                    <tr>
                    <th>Id canción</th><th>Nombre de canción</th><th>Interprete</th><th>Album</th><th>Género</th>
                    </tr>            
                    {info_tabla} 
                </table>
                <br>Información de tu plan:<br>
                
                <br>  Canciones totales del plan: {canciones_plan}<br>
                <br>  Canciones totales en tu lista: {canciones_lista}<br>
                    
                <br> Canciones disponibles de tu plan: {canciones_disponibles}<br>
                
                </p>
            </body>
            </html>
            """
        mensaje.attach(MIMEText(html, 'html'))
        texto = mensaje.as_string()
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        correo = Listas_cliente.consulta_correo_cliente(self, id_cliente)
        servidor.login('ovillalbaunal@gmail.com', 'programacion_segundo_semestre_2021')
        servidor.sendmail('ovillalbaunal@gmail.com', correo, texto)
        servidor.quit()
        print_line_success("Envio exitoso")


    # Función para realizar la actualizacíón de un registro completo de la tabla listas
    def actualizar_info_tabla_listas(self, tupla: tuple, id_cancion: int, id_cliente: int):
        cursor_obj = self.con.cursor()
        act_listas = (f"""UPDATE listas 
                        SET id_cancion = ?,
                            nombre_cancion = ?,
                            interprete = ?,
                            album = ?,
                            genero = ?
                        WHERE id_cancion = {id_cancion} and id_cliente = {id_cliente}""")
        cursor_obj.execute(act_listas, tupla)
        self.con.commit()


    # Función que despliega el menu de sección de listas de reproducción
    


# Pruebas


    
# ----------------------------------------------------------------------------

# Registro Cliente

# d_cliente = Cliente()
# p_cliente = PP_cliente()
# dd_cliente = d_cliente.armar_tupla()
# id_cliente = d_cliente.get_id()
# pp_cliente = p_cliente.armar_arreglo()
# registro = tuple(id_cliente + pp_cliente)
# d_cliente.registrar_db(dd_cliente)
# p_cliente.registrar_db(registro)

# consultar plan
'''
ag = PP_cliente()
ag.set_id_cliente()
x = (ag.verificacion_existencia())
print(x[0])
ag.consulta_plan()
'''

# agregar plan
'''
p = PP_cliente()
p.consulta_planes(p.get_planes)
p.armar_arreglo()
'''






