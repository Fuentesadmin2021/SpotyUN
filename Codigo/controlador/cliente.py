from validacion_datos import *

class Cliente():
    def __init__(self, id, nombre, apellido, pais, ciudad, celular, correo, fecha_pago, numero_tc, estado_pago, id_plan):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.pais = pais
        self.ciudad = ciudad
        self.celular = celular
        self.correo = correo
        self.fecha_pago = fecha_pago
        self.numero_tc = numero_tc
        self.estado_pago = estado_pago
        self.id_plan = id_plan

    def cliente(con) -> tuple:
        id = validacion_numero(input('\nNúmero de identificación del cliente: '), 12)
    id_cliente = validacion_existencia_todas(con, nombre_tabla='clientes', nombre_columna='id_cliente', primary_key='id_cliente', id=id)
    while id_cliente == False:
        print('\n¡El número de identificación ya existe, por favor ingrese otro número de identificación!')
        id = validacion_numero(input('Número de identificación: '), 12)
        id_cliente = validacion_existencia_todas(con, nombre_tabla='clientes', nombre_columna='id_cliente', primary_key='id_cliente', id=id)
    nombre = validacion_letra(input('Nombre: '), 30)
    apellido = validacion_letra(input('Apellido: '), 30)
    pais = validacion_letra(input('Pais: '), 30)
    ciudad = validacion_letra(input('Ciudad: '), 30)
    celular = validacion_telefono(input('Celular: '), 15)
    correo = validacion_correo(input('Correo electrónico: '), 45)
    fecha_pago = datetime.strftime(datetime.now(), '%Y-%m-%d')
    numero_tc = validacion_tc(input('Ingrese el numero de su tarjeta de credito\n' +
                                                              'sin espacios ni caracteres especiales: '), 19)
    estado_pago = 'Activo'

    planes_disponibles(con)

    plan = validacion_numero(input('\nNúmero identificador del plan: '), 1)
    id_plan = validacion_existencia_todas(con, nombre_tabla='planes', nombre_columna='id_plan', primary_key='id_plan', id=plan)
    while id_plan != False :
            print_line_error('¡El número identificador del plan no existe, por favor ingrese otro identificasor que sea valido!')
            plan = validacion_numero(input('\nNúmero identificador  del plan: '), 1)
            id_plan = validacion_existencia_todas(con, nombre_tabla='planes', nombre_columna='id_plan', primary_key='id_plan', id=plan)


    datos_cliente = (
        id_cliente,
        nombre,
        apellido,
        pais,
        ciudad,
        celular,
        correo,
        fecha_pago,
        numero_tc,
        estado_pago,
        plan)
    return datos_cliente