from subprocess import HIGH_PRIORITY_CLASS
from validatos.validatos import Validatos as val
from manejador_db import Manejador_db

from create import Database
from decorador import Decorador as dec

from canciones import Canciones
from clientes import Cliente
from listas_clientes import Listas_cliente
from planes import Planes
from planes_cliente import Planes_cliente


# Función que genera un menu con las multiples opciones
def menu_planes():
    planes = Planes()
    salir_menu = False
    while not salir_menu:
        dec.print_line_menu('''
                        MENU SECCIÓN PLANES
                    1. Registrar un plan
                    2. Consulta información planes
                    3. Consulta individual de la información de un plan
                    4. Actualizar la información de un plan
                    5. Eliminar un plan
                    6. Ir al menu anterior\n''')

        opc = input("\n\tDigite una opcion: ").strip()
        if (opc == '1'):
            planes.registrar_db(planes.armar_tupla())
        elif (opc == '2'):
            planes.consulta_planes_ordenados(planes.orden_consulta(planes.get_planes()))
        elif (opc == '3'):
            planes.consulta_plan()
        elif (opc == '4'):
            planes.actualizar_info_plan(planes)
        elif (opc == '5'):
            planes.eliminar_plan()

        elif (opc == '6'):
            salir_menu = True

        elif (opc == '6'):
            salir_menu = True

        else:
            dec.print_line_error("\t\n¡Opcion no valida. Digite una opción nuevamente!")


# Función que genera un menu con las multiples opciones 
# que se desarrollaran en la sección canciones
def menu_canciones():
    canciones = Canciones()
    salir_menu = False
    while not salir_menu:
        dec.print_line_menu('''
                        MENU SECCIÓN CANCIONES
                    1. Registrar una canción
                    2. Consultar canciones disponibles
                    3. Consulta individual de una canción
                    4. Actualizar datos de una canción
                    5. Ir al menu anterior\n''')

        opc = input("\n\tDigite una opcion: ").strip()
        if (opc == '1'):
            canciones.registrar_db(canciones.armar_tupla())

        elif (opc == '2'):
            canciones.consulta_canciones_ordenadas(canciones.orden_consulta(canciones.get_canciones()))

        elif (opc == '3'):
            canciones.consulta_cancion()

        elif (opc == '4'):
            canciones.actualizar_info_cancion(canciones)

        elif (opc == '5'):
            salir_menu = True

        else:
            dec.print_line_error("\t\n¡Opcion no valida. Digite una opción nuevamente!")


#  Función que genera un menu con todas las posibles opciones de la sección de clientes
def menu_clientes():
    cliente = Cliente()
    planes_cliente = Planes_cliente()
    salir_menu = False
    while not salir_menu:
        dec.print_line_menu('''
                        MENU SECCIÓN CLIENTES
                    1. Registrarse
                    2. Consulta individual cliente
                    3. Consulta general de clientes
                    4. Actualizar información de cliente
                    5. Actualizar estado de suscripción del cliente
                    6. Ir al menu anterior\n''')

        opc = input("\n\tDigite una opcion: ")
        if (opc == '1'):
            salir = True
            while salir:
                try:
                    dd_cliente = cliente.armar_tupla()
                    id_cliente = cliente.get_id()
                    pp_cliente = planes_cliente.armar_arreglo()
                    registro = tuple(id_cliente + pp_cliente)
                    cliente.registrar_db(dd_cliente)
                    planes_cliente.registrar_db(registro)
                    salir = False
                except:
                    dec.print_line_error('¡ERROR! El número de identificación no puede estar repetido')
                    print('')

        elif opc == '2':
            cliente.consulta_cliente()

        elif opc == '3':
            cliente.consulta_clientes(cliente.orden_consulta(cliente.get_clientes()))

        elif opc == '4':
            cliente.actualizar_info_cliente(cliente)

        elif opc == '5':
            cliente.actualizar_estado_suscripcion()

        elif opc == '6':
            salir_menu = True


# Función que gestiona la sección planes_cliente a través de un menú
def menu_planes_cliente():
    p_cliente = Planes_cliente()
    salir_menu = False
    while not salir_menu:

        dec.print_line_menu('''
                    MENU SECCIÓN PLANES CLIENTE
                1. Consultar plan por cliente
                2. Consulta general de planes contratados
                3. Ir al menu anterior\n''')

        opc = input("\n\tDigite una opcion: ")

        if opc == "1":
            try:
                p_cliente.consulta_planes(p_cliente.get_plan_por_cliente())

            except:
                dec.print_line_error("\t\n¡ERROR! No existe un cliente con ese número de identificación")

        elif opc == "2":
            p_cliente.consulta_planes(p_cliente.orden_consulta(p_cliente.get_planes_ordenados()))
            print('')
            print("*" * 50)
            p_cliente.consulta_agrupada()

        elif opc == "3":
            salir_menu = True

        else:
            dec.print_line_error("¡Opción no valida. Digite una opción nuevamente!")


def menu_lista(id_cliente: int):
    prueba = Listas_cliente()
    state = True
    while state:
        dec.print_line_menu("""
                MENU SECCIÓN LISTAS DE REPRODUCCIÓN
            1. Crear una lista
            2. Consultar lista
            3. Actualizar lista
            4. Eliminar lista
            5. Envía correo con lista de reproducción
            6. Reproducir canciones
            7. Ir al menu anterior""")

        opc = input('\nDigite una opción: ')
        if opc == "1":
            print("\nSesión de creación de lista de reproducción\n")
            state_lista = True
            while state_lista:
                try:
                    # Se realiza el conteo de las canciones totales contratadas por el cliente de acuerdo al plan
                    # y se realizar el conteo de las canciones que ya estan en la lista de reproducción.
                    # asi tener el total de canciones faltantes para completar el plan
                    canciones = prueba.plan_cliente(id_cliente)[0]
                    salida = prueba.contar_lista(id_cliente)[0]
                    total_canciones = canciones - salida
                    print('Falta {} canciones para completar el plan'.format(total_canciones))
                    if total_canciones == 0:
                        dec.print_line_error('¡Has completado tu plan, no puedes agregar más canciones!')
                        state_lista = False
                    else:

                        prueba.consulta_tabla_canciones_lista()
                        info = prueba.info_lista(id_cliente)
                        if prueba.consulta_tabla_listas_cancion(id_cliente, info[0]):
                            dec.print_line_error('¡Ya tienes esta canción en tu lista de reproducción!')
                            state_lista = False
                        else:
                            prueba.registrar_lista_cliente(info)
                            next = False
                            while not next:
                                opc_next = input("""\n¿Desea agregar otra canción? s/n: """).lower()
                                if opc_next == 's':
                                    next = True
                                elif opc_next == 'n':
                                    opc_email = input(
                                        """\n¿Desea enviar correo electrónico con la lista de reproducción? s/n: """).lower()
                                    if opc_email == 's':
                                        prueba.enviar_mensaje(id_cliente)
                                        next = True
                                        state_lista = False
                                    elif opc_email == 'n':
                                        next = True
                                        state_lista = False
                                    else:
                                        dec.print_line_error('¡Opción no valida. Digite una opción nuevamente!')
                                else:
                                    dec.print_line_error('¡Opción no valida. Digite una opción nuevamente!')
                except:
                    dec.print_line_error('¡Canción no encontrada en la base de datos!')
        elif opc == "2":

            prueba.consulta_tabla_listas(id_cliente)
        elif opc == "3":
            state_actualizar = True
            while state_actualizar:
                try:
                    prueba.consulta_tabla_listas(id_cliente)
                    id_cancion = int(input('\nDigite el id de la canción que desea actualizar: '))
                    prueba.consulta_tabla_canciones_lista()
                    lista_info = prueba.info_lista(id_cliente)
                    prueba.actualizar_info_tabla_listas(tuple(lista_info[0:5]), id_cancion, id_cliente)
                    state_actualizar = False
                except:
                    dec.print_line_error('¡Canción no encontrada en las base de datos!')

        elif opc == "4":
            prueba.borrar_lista(id_cliente)
        elif opc == "5":
            prueba.enviar_mensaje(id_cliente)
        elif opc == "6":
            if prueba.contar_lista(id_cliente)[0] == 0:
                dec.print_line_error(
                    '¡No tienes canciones en tu lista de reproducción!\nCrea una lista para poder reproducir canciones')
            else:
                prueba.consulta_tabla_listas(id_cliente)
                tupla = prueba.get_cancion()
                id_validacion = val.existencia_tablas(prueba.con, 'listas', 'id_cancion', 'id_cancion', tupla[0])
                while id_validacion:
                    tupla = prueba.get_cancion()
                    id_validacion = val.existencia_tablas(prueba.con, 'listas', 'id_cancion', 'id_cancion', tupla[0])
                prueba.reproducir_cancion(prueba.guardar_cancion()[1], id_cliente)
        elif opc == "7":
            state = False

        else:
            print("\t\n¡Opcion no valida. Digite una opción nuevamente!")


def menu_principal():
    terminar_programa = False
    while not terminar_programa:
        dec.print_line_menu('''

                    🆂 🅿 🅾  🆃 🆈 🆄 🅽
                    
                        MENU PRINCIPAL
                    1. Sección planes
                    2. Sección canciones
                    3. Sección clientes
                    4. Sección planes cliente
                    5. Sección de lista cliente
                    6. Salir\n''')

        opc = input("\n\tDigite una opcion: ")
        if opc == '1':
            menu_planes()

        elif opc == '2':
            menu_canciones()

        elif opc == '3':
            menu_clientes()

        elif opc == '4':
            menu_planes_cliente()

        elif opc == '5':
            cliente_validado = Planes_cliente()
            id = cliente_validado.verificacion_existencia()
            if not id:
                menu_clientes()
            else:
                id = id[0]
                menu_lista(id)

        elif opc == '6':
            terminar_programa = True

        else:
            dec.print_line_error("\t¡Opción no valida. Digite una opción nuevamente!")


def main():
    database = Database()
    database.create_database()
    menu_principal()
    actualizar = Manejador_db()
    actualizar.close()


if __name__ == '__main__':
    main()
