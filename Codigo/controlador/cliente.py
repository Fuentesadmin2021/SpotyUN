from paquetes_ad.validaciond import *
from datetime import datetime
import sqlite3
from sqlite3 import Error
def sql_conexion():
    try:
        con = sqlite3.connect('SpotyUN.db')
        return con
    
    except Error:
        print(Error)

con = sql_conexion()


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
        cliente = (self.__id, self.__nombre, self.__apellido, self.__pais, self.__ciudad,
        self.__celular, self.__correo, self.__fecha_pago, self.__numero_tc, self.__estado_pago)
        return cliente


mi_cliente = Cliente(con)
mi_cliente.set_id(con)

  
     planes_disponibles(con)
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