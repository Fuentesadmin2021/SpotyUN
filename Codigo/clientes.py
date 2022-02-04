from planes_cliente import Planes_cliente
from manejador_db import Manejador_db
from decorador import Decorador as dec
from validatos.validatos import Validatos as val
from datetime import datetime


class Cliente(Manejador_db):
    def __init__(self):
        Manejador_db.__init__(self)
        Planes_cliente.__init__(self)
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
            
    def get_correo_cliente(self, id_cliente: int) -> str:
        cursor_obj = self.con.cursor()
        cursor_obj.execute(f'SELECT correo FROM clientes WHERE id_cliente = {id_cliente}')
        correo = cursor_obj.fetchall()
        return correo

    def consulta_correo_cliente(self, id_cliente: int) -> str:
        cursor_obj = self.con.cursor()
        cursor_obj.execute(f'SELECT correo FROM clientes WHERE id_cliente = {id_cliente}')
        correo = cursor_obj.fetchall()
        return correo
    
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
        dec.print_line_menu('''
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

            dec.print_line_menu('''
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
                dec.print_line_error("¡Opcion no valida. Digite una opción nuevamente!")

    def actualizar_estado_suscripcion(self):
        salir = False
        while not salir:
            
            dec.print_line_menu('''
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
                dec.print_line_error("¡Opcion no valida. Digite una opción nuevamente!")
                
    def verificacion_existencia(self) -> bool or int:
        cursor_obj = self.con.cursor()
        Planes_cliente.set_id_cliente(self)
        cursor_obj.execute(f'SELECT id_cliente FROM planes_cliente WHERE id_cliente = {self.__id_cliente}')
        self.__id_cliente = cursor_obj.fetchone()
        if self.__id_cliente == None:
            print('¡Antes de poder registrar otro plan o lista de reproducción debes ser un cliente registrado!')
            return False
        else:
            dec.print_line_success('¡Validación de usuario exitosa!')
            return self.__id_cliente