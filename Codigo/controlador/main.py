from base import *

# Función que genera un menu con las multiples opciones 
# que se desarrollaran en la sección canciones
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


# Función que genera un menu con las multiples opciones
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


#  Función que genera un menu con todas las posibles opciones de la sección de clientes
def menu_clientes():
    salir_menu = False
    while not salir_menu:
        print_line_menu('''
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
                    cliente = Cliente()
                    plan = PP_cliente()
                    dd_cliente = cliente.armar_tupla()
                    id_cliente = cliente.get_id()
                    pp_cliente = plan.armar_arreglo()
                    registro = tuple(id_cliente + pp_cliente)
                    cliente.registrar_db(dd_cliente)
                    plan.registrar_db(registro)              
                    salir = False
    
                except:
                    print_line_error('¡ERROR! El número de identificación no puede estar repetido')
                    print('')

        elif (opc == '2'):
            consulta = Cliente()
            consulta.consulta_cliente()

        elif (opc == '3'):
            consulta = Cliente()
            consulta.consulta_clientes(consulta.orden_consulta(consulta.get_clientes()))

        elif (opc == '4'):
            actualizar = Cliente()
            actualizar.actualizar_info_cliente()
            
        elif (opc == '5'):
            estado = Cliente()
            estado.actualizar_estado_suscripcion()

        elif (opc == '6'):
            salir_menu = True


# Función que getiona la sección planes_cliente a través de un menú
def menu_planes_cliente(id_cliente: int):
    salir_menu = False
    while not salir_menu:

        print_line_menu('''
                    MENU SECCIÓN PLANES CLIENTE
                1. Consultar planes de cliente
                2. Registrar otro plan
                3. Ir al menu anterior\n''')
    
        opc = input("\n\tDigite una opcion: ")
        if (opc == "1"):
            consulta = PP_cliente()
            consulta.consulta_pp_cliente(consulta.get_pp_cliente(id_cliente))
        
        elif (opc == "2"):
            plan = PP_cliente()
            plan.registrar_db(tuple([id_cliente] + plan.armar_arreglo()))
        
        elif opc == "3":
            salir_menu = True
        
        else:
            print_line_error("¡Opcion no valida. Digite una opción nuevamente!")
            

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
            cliente_validado = PP_cliente()
            id = cliente_validado.verificacion_existencia()
            id = id[0]
            if not id:
                menu_clientes()
            else:  
                menu_planes_cliente(id)

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

