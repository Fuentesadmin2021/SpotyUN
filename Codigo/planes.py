'''Se importan de los modulos las Clases necesarias para el funcionamiento del programa'''
from manejador_db import Manejador_db
from decorador import Decorador as dec
from validatos.validatos import Validatos as val


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
        dec.print_line_menu('''
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


    def consulta_planes_ordenados(self, tupla):
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
        dec.print_line_success('¡El plan se ha registrado exitosamente!')

    # Función que crea un menú para actualizar de manera individual los datos básicos de un plan
    # a través de la función actualizar_info_tablas
    def actualizar_info_plan(self, clase):
        salir_actualizar = False
        while not salir_actualizar:

            dec.print_line_menu('''
                                ACTUALIZAR INFORMACIÓN PLAN
                            1. Nombre
                            2. Valor
                            3. Cantidad de canciones
                            4. Ir al menu anterior\n''')

            opc = input("\n\tDigite una opcion: ").strip()
            if (opc == '1'):
                Planes.actualizar_info_tablas(self, clase = clase, info = 'nombre', nombre_tabla = 'planes', nombre_columna = 'nombre_plan', primary_key = 'id_plan')
                
            elif(opc == '2'):
                Planes.actualizar_info_tablas(self, clase = clase, info = 'valor', nombre_tabla = 'planes', nombre_columna = 'valor', primary_key = 'id_plan')

            elif(opc == '3'):
                Planes.actualizar_info_tablas(self, clase = clase, info = 'cantidad de canciones', nombre_tabla = 'planes', nombre_columna = 'cantidad_canciones', primary_key = 'id_plan')

            elif(opc == '4'):
                salir_actualizar = True
            
            else:
                dec.print_line_error("\t\n¡Opcion no valida. Digite una opción nuevamente!")

    # La función acontinuación se encarga de eliminar un plan de la base de datos con el id
    def eliminar_plan(self):
        self.__id = val.numero(input('\nId del plan: '), 1)
        cursor_obj = self.con.cursor()
        cursor_obj.execute(f'DELETE FROM planes WHERE id_plan = {self.__id}')
        self.con.commit()
        dec.print_line_success('¡ El plan se ha eliminado exitosamente')        
        
        