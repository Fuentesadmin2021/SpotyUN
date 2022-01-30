from paquetes_ad.decorador import *
from base import *

# Función que genera un menu con todas las multiples opciones 
# que se desarrollaran en el menu canciones
def menu_canciones():
    salir_menu = False
    while not salir_menu:
        print_line_menu('''
                        MENU SECCIÓN CANCIONES
                    1. Registrar una canción
                    2. Consultar canciones disponibles
                    3. Consulta individual de una canción
                    4. Actualizar datos de una canción
                    5. Ir al menu anterior\n''')

        opc = input("\n\tDigite una opcion: ").strip()
        if (opc == '1'):
            cancion = Canciones()
            cancion.registrar_db(cancion.armar_tupla())

        elif (opc == '2'):
            consulta = Canciones()
            consulta.consulta_canciones(consulta.orden_consulta(consulta.get_canciones()))

        elif (opc == '3'):
            consulta = Canciones()
            consulta.consulta_cancion()

        elif (opc == '4'):
            actualizar = Canciones()
            actualizar.actualizar_info_cancion()

        elif (opc == '5'):
                salir_menu = True

        else:
             print_line_error("\t\n¡Opcion no valida. Digite una opción nuevamente!")


# Función que genera un menu con todas las posibles opciones de la sección de planes
def menu_planes():
    salir_menu = False
    while not salir_menu:
        print_line_menu('''
                        MENU SECCIÓN PLANES
                    1. Registrar un plan
                    2. Consulta información planes
                    3. Consulta individual de la información de un plan
                    4. Actualizar la información de un plan
                    5. Eliminar un plan
                    6. Ir al menu anterior\n''')

        opc = input("\n\tDigite una opcion: ").strip()
        if (opc == '1'):
            plan = Planes()
            plan.registrar_db(plan.armar_tupla())
          
        elif (opc == '2'):
            consulta = Planes()
            consulta.consulta_planes(consulta.orden_consulta(consulta.get_planes()))
        
        elif (opc == '3'):
            consulta = Planes()
            consulta.consulta_plan()

        elif (opc == '4'):
            actualizar = Planes()
            actualizar.actualizar_info_plan()

        elif (opc == '5'):
            eliminar = Planes()
            eliminar.eliminar_plan()

        elif (opc == '6'):
            salir_menu = True

        else:
            print_line_error("\t\n¡Opcion no valida. Digite una opción nuevamente!")



    
def menu_principal():
    terminar_programa = False
    while not terminar_programa:
        print_line_menu('''

                    🆂 🅿 🅾  🆃 🆈 🆄 🅽
                    
                        MENU PRINCIPAL
                    1. Sección planes
                    2. Sección canciones
                    3. Sección clientes
                    4. Sección planes cliente
                    5. Sección de lista cliente
                    6. Salir\n''')

        opc = input("\n\tDigite una opcion: ")
        if (opc == '1'):
            menu_planes()

        elif (opc == '2'):
            menu_canciones()

        elif (opc == '3'):
            menu_clientes()

        elif (opc == '4'):
            id = verificacion_cliente()
            if not id:
                menu_clientes()
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
            print_line_error("\t¡Opcion no valida. Digite una opción nuevamente!")

def main():
    menu_principal()

if __name__ == '__main__':
    main()

