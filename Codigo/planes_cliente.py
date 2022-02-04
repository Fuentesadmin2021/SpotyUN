from planes import Planes
from validatos.validatos import Validatos as val
from decorador import Decorador as dec


class Planes_cliente(Planes):
    def __init__(self):
        Planes.__init__(self)
        self.__id_cliente = None
        self.__id_plan_c = None

    def set_id_cliente(self):
        self.__id_cliente = val.numero(input('Ingrese su identificación: '), 12)
        
    def set_id_plan_c(self):
        Planes_cliente.consulta_planes(self, Planes_cliente.get_planes(self))
        self.__id_plan_c = val.numero(input('\nIngrese el id del plan que desea contratar: '), 1)
        validacion = val.existencia_tablas(self.con, nombre_tabla = 'planes', nombre_columna = 'id_plan', primary_key='id_plan', id = self.__id_plan_c )
        while validacion != False :
            dec.print_line_error('¡No existe un plan con ese id, por favor ingrese uno que sea valido!')
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
        Planes_cliente.set_id_cliente(self)
        cursor_obj.execute(f'SELECT id_cliente FROM planes_cliente WHERE id_cliente = {self.__id_cliente}')
        self.__id_cliente = cursor_obj.fetchone()
        if self.__id_cliente == None:
            print('¡Antes de poder registrar otro plan o lista de reproducción debes ser un cliente registrado!')
            return False
        else:
            dec.print_line_success('¡Validación de usuario exitosa!')
            return self.__id_cliente

    #  Función que se encarga de armar una tupla con el el id del plan contratado por el cliente
    def armar_arreglo(self):
        Planes_cliente.set_id_plan_c(self)
        Planes_cliente.get_cant_canciones(self)
        plan_c = [self.__id_plan_c, self.cant_canciones]
        return plan_c
    
    #  función que se encarga de registrar el id('identificación') del cliente y el id del plan que contrato
    def registrar_db(self, tupla):
        cursor_obj = self.con.cursor()
        cursor_obj.execute('''INSERT INTO planes_cliente VALUES(?,?,?)''', tupla)
        self.con.commit()
        dec.print_line_success('¡Su registro se ha realizado exitosamente!')

    
    