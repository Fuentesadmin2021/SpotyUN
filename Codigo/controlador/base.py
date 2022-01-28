from paquetes_ad.decorador import *
from paquetes_ad.validaciond import *
from datetime import datetime
import sqlite3
from sqlite3 import Error
from subprocess import HIGH_PRIORITY_CLASS

def sql_conexion():
    try:
        con = sqlite3.connect('SpotyUN.db')
        return con
    
    except Error:
        print(Error)

class Actualizar():

    def __init__(self, nombre_columna: str, nombre_tabla: str, primary_key: str, info):
        self.__con = con
        self.__columna = nombre_columna
        self.__tabla = nombre_tabla
        self.__primary_key = primary_key
        self.__info = info

    
    def validar(self):
        state = True
        while state:
            try:
                id = input('\nIngrese el id: ').strip()
                if id_v := validacion_existencia_todas(self.__con, self.__tabla, self.__columna, self.__primary_key, id) == False:
                    id = int(id)
                    state = False
                else:
                    print('\nEl id ingresado no existe en la base de datos')
            except:
                print('El id ingresado no es correcto')
    
    def actualizacion_bd(self):
        cursor_obj = self.__con.cursor()
        cadena = f'UPDATE {self.__tabla} SET {self.__columna} = ? WHERE {self.__primary_key} = ?'
        cursor_obj.execute(cadena, (self.__info, id ))
        self.__con.commit()
        print_line_success(f"!{self.__info.title()} se ha actualizado exitosamente¡")






    # Función para actualizar información de una tabla en la base de datos
    # Funciona para cualquier tabla dentro de la base de datos
    def actualizar_info_tablas(self, con, nombre_columna: str, nombre_tabla: str, primary_key: str, info = "indefido"):
        state = True
        while state:
            try:
                id = input('\nIngrese el id: ').strip()
                if id_v := validacion_existencia_todas(con, nombre_tabla, nombre_columna, primary_key, id) == False:
                    id = int(id)
                    state = False
                else:
                    print('\nEl id ingresado no existe en la base de datos')
            except:
                print('El id ingresado no es correcto')

        cursor_obj = con.cursor()
        cadena = f'UPDATE {nombre_tabla} SET {nombre_columna} = ? WHERE {primary_key} = ?'
        cursor_obj.execute(cadena, (info, id ))
        con.commit()
        print_line_success(f"!{info.title()} se ha actualizado exitosamente¡")


class Canciones(Actualizar):
    def __init__(self, con):
        self.__nombre = None
        self.__genero = None
        self.__album = None
        self.__interprete = None
        self.__imagen = None
        self.__audio = None
   
    
    def set_nombre(self):
        self.__nombre = validacion_longitud(input('Nombre: '), 100)

    # def get_nombre(self):
    #     self.__nombre = 

    def set_genero(self):
        self.__genero = validacion_longitud(input('Genero: '), 30)

    def set_album(self):
        self.__album = validacion_longitud(input('Album: '), 100)
        
    def set_interprete(self):
        self.__interprete = validacion_longitud(input('Interprete(s): '), 100)
    
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
                print_line_error('\n¡Error en los datos de la canción en el equipo\n por favor verifique e ingrese de nuevo la información!\n ')

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
    def registrar_db(self, con, tupla):
        cursor_obj = con.cursor()
        cursor_obj.execute('''INSERT INTO canciones VALUES(NULL, ?, ?, ?, ?, NULL, ?)''', tupla)
        con.commit()
        print_line_success("♪ El registro de la canción se ha realizado exitosamente ♪")
    
    def actualizar_audio_db(self, con):
        cursor_obj = con.cursor()
        id = input('\nIngrese el id de la canción a la que quiere modificar: ')
        Canciones.set_audio(self)
        actualizar = f'UPDATE canciones SET cancion = ? WHERE id_cancion = ?'
        info_cancion = (self.__audio, id)
        cursor_obj.execute(actualizar, info_cancion)
        con.commit()
        print_line_success("!La cancion se ha actualizado exitosamente¡")

    # Función que crea un menú para actualizar de manera individual los datos básicos de una canción
    # a través de la función actualizar_info_tablas importada desde el modulo manejadorbd
    def actualizar_datos_cancion(self, con):
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
                mod = Actualizar(info = self.__nombre, nombre_tabla = 'canciones', nombre_columna = 'nombre_cancion', primary_key = 'id_cancion')
                Canciones.validar(self)
                Canciones.set_nombre(self)

                # Canciones.actualizar_info_tablas(self, con, info = self.__nombre, nombre_tabla = 'canciones', nombre_columna = 'nombre_cancion', primary_key = 'id_cancion')
            
            # elif(opc == '2'):
            #     # Canciones.actualizar_info_tablas(con, nombre_tabla='canciones', nombre_columna='album', primary_key='id_cancion', info='el album de la canción', longitud=100)

            # elif(opc == '3'):
            #     # Canciones.actualizar_info_tablas(con, nombre_tabla='canciones', nombre_columna='genero', primary_key='id_cancion', info='el genero de la canción', longitud=30)

            # elif(opc == '4'):
            #     Canciones.actualizar_info_tablas(con, nombre_tabla='canciones', nombre_columna='interprete', primary_key='id_cancion', info='el interprete de la canción', longitud=100)

            # elif (opc == '5'):
            #     Canciones.actualizar_cancion(con)

            # elif(opc == '6'):
            #     salir_actualizar = True
            
            # else:
            #     print_line_error("\t¡Opcion no valida. Digite una opción nuevamente!")


con = sql_conexion()
modd = Canciones(con)
modd.actualizar_datos_cancion(con)


class Plan():
    def __init__(self, con):

        self.__id = None
        self.__nombre = None
        self.__valor = None
        self.__cant_canciones = None

    def set_id(self, con):
        self.__id = validacion_numero(input('\nId del plan: '), 1)
        self.__id = validacion_existencia_todas(con, nombre_tabla = 'planes', nombre_columna = 'id_plan', primary_key = 'id_plan', id = self.__id)
        
        while self.__id == False:
            print('\t\n¡ERROR! Ya existe un plan con el \'Id plan\' ingresado. Si desea realizar el registro ingrese nuevamente la información.')
            self.__id = validacion_numero(input('\nId del plan: '), 1)
            self.__id = validacion_existencia_todas(con, nombre_tabla = 'planes', nombre_columna = 'id_plan', primary_key = 'id_plan', id = self.__id)
    
    def set_nombre(self):
        self.__nombre = input("Nombre del plan: ")

    def set_valor(self):
        self.__valor = int(validacion_numero(input("Valor plan: "),5))

    def set_cant_canciones(self):
        self.__cant_canciones = int(validacion_numero(input("Cantidad de canciones del plan: "),4))

    def armar_tupla(self):
        plan = (self.__id, self.__nombre, self.__valor, self.__cant_canciones)
        return plan

    # Función para registrar los planes en la tabla planes
    def registrar_plan(self, con, plan):
        cursor_obj = con.cursor()
        cursor_obj.execute('''INSERT INTO planes VALUES(?,?,?,?)''', plan)
        con.commit()
        print_line_success('¡El plan se ha registrado exitosamente!')



     # Función que ordena la consulta a demanda del usuario
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


    # Función que realiza la consulta de todos los planes en la tabla planes y los muestra al usuario
    def consulta_tabla_planes(self, con):
        cursor_obj = con.cursor()
        cursor_obj.execute('SELECT * FROM  planes')
        cantidad_planes = cursor_obj.fetchall()  
        orden_salida = orden_consulta(cantidad_planes)
        print ("\n{:<5} {:<15} {:<10} {:<10} ".format('ID', 'NOMBRE PLAN', 'VALOR', 'CANTIDAD CANCIONES'))
        for row in orden_salida:
            id, nombre, valor, cantidad_canciones = row
            print ("{:<5} {:<15} {:<10} {:<10} ".format(id, nombre, valor, cantidad_canciones))



    # Función que permite hacer una consulta individual de un cliente por medio de la identificacion registrada
    def consulta_individual_plan(con):
        cursor_obj = con.cursor()
        id = int(input('\nIngrese un id del plan a consultar: '))
        busqueda = 'SELECT * FROM planes WHERE id_plan = '
        id_busqueda = busqueda + str(id)
        cursor_obj.execute(id_busqueda)
        datos_plan = cursor_obj.fetchall()
        print("\n{:<5} {:<15} {:<10} {:<10} ".format('ID', 'NOMBRE_PLAN', 'VALOR', 'CANTIDAD CANCIONES'))
        for row in datos_plan:
            id, nombre, valor, cantidad_canciones = row
            print("{:<5} {:<15} {:<10} {:<10} ".format(id, nombre, valor, cantidad_canciones))


    # Función que despliegue el menú de actualización de valores dentro de la sección planes
    def actualizar_datos_plan(con):
        salir_actualizar = False
        while not salir_actualizar:
            print_line_menu('''
                                ACTUALIZAR INFORMACIÓN PLAN
                            1. Nombre
                            2. Valor
                            3. Cantidad de canciones
                            4. Ir al menu anterior\n''')

            opc = input("\n\tDigite una opcion: ")
            if (opc == '1'):
                actualizar_info_tablas(con, 'el nombre', nombre_columna='nombre_plan', nombre_tabla='planes', primary_key='id_plan', longitud=15)
                
            elif(opc == '2'):
                actualizar_info_tablas(con, 'el valor', nombre_columna='valor', nombre_tabla='planes', primary_key='id_plan', longitud=5)

            elif(opc == '3'):
                actualizar_info_tablas(con, 'la cantidad de canciones', nombre_columna='cantidad_canciones', nombre_tabla='planes', primary_key='id_plan', longitud=4)
                
            elif(opc == '4'):
                salir_actualizar = True
            
            else:
                print_line_error("\t\n¡Opcion no valida. Digite una opción nuevamente!")


class Cliente():
    def __init__(self, con):
        
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
        self.__id_plan = None

    def set_id(self, con):
        self.__id = validacion_numero(input('\nNúmero de identificación del cliente: '), 12)
        self.__id = validacion_existencia_todas(con, nombre_tabla = 'clientes', nombre_columna = 'id_cliente', primary_key = 'id_cliente', id = self.__id)

        while self.__id == False:
            print('\n¡El número de identificación ya existe, por favor ingrese otro número de identificación!')
            self.__id = validacion_numero(input('Número de identificación: '), 12)
            self.__id = validacion_existencia_todas(con, nombre_tabla = 'clientes', nombre_columna = 'id_cliente', primary_key = 'id_cliente', id = self.__id)

    def set_nombre(self):
        self.__nombre = validacion_letra(input('Nombre: '), 30)

    def set_apellido(self):
        self.__apellido = validacion_letra(input('Apellido: '), 30)

    def set_pais(self):   
        self.__pais = validacion_letra(input('Pais: '), 30)

    def set_ciudad(self):
        self.__ciudad = validacion_letra(input('Ciudad: '), 30)

    def set_celular(self):
        self.__celular = validacion_telefono(input('Celular: '), 15)

    def set_correo(self):
        self.__correo = validacion_correo(input('Correo electrónico: '), 45)

    def set_fecha_pago(self):
        self.__fecha_pago = datetime.strftime(datetime.now(), '%Y-%m-%d')

    def set_numero_tc(self):
        self.__numero_tc = validacion_tc(input('Ingrese el numero de su tarjeta de credito\n sin espacios ni caracteres especiales: '), 19)

    def set_estado_pago(self):
        self.estado_pago = 'Activo'
        
    def armar_tupla(self):
        Cliente.set_id(self, con)
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


con = sql_conexion()
actualizar = Canciones(con)
actualizar.actualizar_datos_cancion(con)
# mi_cancion = Canciones()
# mi_cancion.registrar_db(con, mi_cancion.armar_tupla())
# mi_cliente = Cliente(con)
# mi_cliente.armar_tupla(con)
# mi_plan = Plan(con)


  
    #  planes_disponibles(con)
    # plan = validacion_numero(input('\nNúmero identificador del plan: '), 1)
    # id_plan = validacion_existencia_todas(con, nombre_tabla='planes', nombre_columna='id_plan', primary_key='id_plan', id=plan)
    # while id_plan != False :
    #         print_line_error('¡El número identificador del plan no existe, por favor ingrese otro identificasor que sea valido!')
    #         plan = validacion_numero(input('\nNúmero identificador  del plan: '), 1)
    #         id_plan = validacion_existencia_todas(con, nombre_tabla='planes', nombre_columna='id_plan', primary_key='id_plan', id=plan)


    # datos_cliente = (
    #     id_cliente,
    #     nombre,
    #     apellido,
    #     pais,
    #     ciudad,
    #     celular,
    #     correo,
    #     fecha_pago,
    #     numero_tc,
    #     estado_pago,
    #     plan)
    # return datos_cliente