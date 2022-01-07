'''Acontinuación se importan todos los modulos con las funciones necesarias para que el programa funcione correctamente.
 El modulo "main.py" funcionara como panel principal del programa.
 Las librerias para cumplir con algunas funciones del programa estan importadas al inicio de cada modulo. Si es necesaria alguna'''

from manejadorbd import *
from manejador_canciones import *
from manejador_clientes import *
from manejador_planes import *
from manejador_planes_cliente import *
from manejador_listas import *
from decorador import *


# Función que genera un menu con todas las posibles opciones de la seccion de canciones
@decorador_menu
def menu_canciones(con):
    salir_canciones = False
    while not salir_canciones:

        print('''
                        MENU SECCIÓN CANCIONES
                    1. Registrar una canción
                    2. Consultar canciones disponibles
                    3. Consulta individual de una canción
                    4. Actualizar datos de una canción
                    5. Ir al menu anterior\n''')

        opc = input("\tDigite una opcion: ").strip()
        if (opc == '1'):
            registrar_cancion(con)

        elif (opc == '2'):
            consulta_tabla_canciones(con)

        elif (opc == '3'):
            consulta_individual_cancion(con)

        elif (opc == '4'):
            actualizar_datos_cancion(con)

        elif (opc == '5'):
            salir_canciones = True

        else:
             print("\t\n¡Opcion no valida. Digite una opción nuevamente!")


# Función que genera un menu con todas las posibles opciones de la seccion de clientes
@decorador_menu
def menu_clientes(con):
    salir = False
    while not salir:

        print('''
                        MENU SECCIÓN CLIENTES
                    1. Registrarse
                    2. Consulta individual cliente
                    3. Consulta general de clientes
                    4. Actualizar información de cliente
                    5. Actualizar estado de suscripción del cliente
                    6. Ir al menu anterir\n''')

        opc = input("\tDigite una opcion: ")
        if (opc == '1'):
            salir = True
            while salir:
                try:
                    info = cliente(con)
                    info_plan_cliente = plan_desde_cliente(info)
                    registrar_cliente(con, info)
                    registrar_plan_cliente(con, info_plan_cliente)
                    salir = False
                except:
                    print('¡ERROR! El número de identificación no puede estar repetido')
                    print('')

        elif (opc == '2'):
            consulta_individual_cliente(con)

        elif (opc == '3'):
            consulta_tabla_clientes(con)

        elif (opc == '4'):
            actualizar_datos_cliente(con)

        elif (opc == '5'):
            print("""Cambiar el estado de suscripción del cliente, las palabras permitidas son:
                    1. Activo
                    2. Inactivo\n""")
            actualizar_info_tablas(con, 'el estado de suscripción', nombre_columna='estado_pago', nombre_tabla='clientes', primary_key='id_cliente', longitud=15)
            print('\t\n¡Estado de suscripción actualizado!')

        elif (opc == '6'):
            salir = True
          


# Función que genera un menu con todas las posibles opciones de la seccion de canciones
@decorador_menu
def menu_planes(con):
    salir_planes = False
    while not salir_planes:

        print('''
                        MENU SECCIÓN PLANES
                    1. Registrar un plan
                    2. Consulta imformación planes
                    3. Consulta individual de la información de un plan
                    4. Actualizar la información de un plan
                    5. Ir al menu anterior\n''')

        opc = input("\tDigite una opcion: ").strip()
        if (opc == '1'):
            registrar_plan(con)

        elif (opc == '2'):
            consulta_tabla_planes(con)

        elif (opc == '3'):
            consulta_individual_plan(con)

        elif (opc == '4'):
            actualizar_datos_plan(con)

        elif (opc == '5'):
            salir_planes = True

        else:
            print("\t\n¡Opcion no valida. Digite una opción nuevamente!")


# Función que genera un menú pricipal que permite gestionar todo el programa
@decorador_menu
def menu_principal(con):
    terminar_programa = False
    while not terminar_programa:
        print('''
                        MENU PRINCIPAL
                    1. Sección planes
                    2. Sección canciones
                    3. Sección clientes
                    4. Sección planes cliente
                    5. Sección de lista cliente
                    6. Salir\n''')

        opc = input("\tDigite una opcion: ")
        if (opc == '1'):
            menu_planes(con)

        elif (opc == '2'):
            menu_canciones(con)

        elif (opc == '3'):
            menu_clientes(con)

        elif (opc == '4'):
            id = verificacion_cliente(con)
            if not id:
                menu_clientes(con)
            else:
                menu_planes_cliente(con, id)

        elif (opc == '5'):
            id = verificacion_cliente(con)
            if not id:
                menu_clientes(con)
            else:
                menu_lista(con, id)

        elif (opc == '6'):
            terminar_programa = True

        else:
            print("\t\n¡Opcion no valida. Digite una opción nuevamente!")

# La funcion 'main()' a continuacion es la encargada de ejecutar todo el programa
def main():
    conexion_bd = sql_conexion()
    crear_tabla_canciones(conexion_bd)
    crear_tabla_planes(conexion_bd)
    crear_tabla_clientes(conexion_bd)
    crear_tabla_listas(conexion_bd)
    crear_tabla_planes_por_cliente(conexion_bd)
    menu_principal(conexion_bd)

if __name__ == '__main__':
    main()
