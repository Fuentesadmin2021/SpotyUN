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
            cliente_validado = PP_cliente()
            id = cliente_validado.verificacion_existencia()[0]            
            if not id:
                menu_clientes()
            else:
                menu_lista(id)

        elif (opc == '6'):
            terminar_programa = True

        else:
            print_line_error("\t¡Opcion no valida. Digite una opción nuevamente!")

def menu_lista(id_cliente: int):
        state = True
        while state:
            print_line_menu("""
                MENU SECCIÓN LISTAS DE REPRODUCCIÓN
            1. Crear una lista
            2. Consultar lista
            3. Actualizar lista
            4. Eliminar lista
            5. Envia correo con lista de reproducción
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
                        total_canciones = Listas_cliente.plan_cliente(id_cliente) - Listas_cliente.contar_lista(id_cliente)
                        print('Falta {} canciones para completar el plan'.format(total_canciones))
                        if total_canciones == 0:
                            print_line_error('¡Has completado tu plan, no puedes agregar más canciones!')
                            state_lista = False
                        else:
                            Listas_cliente.consulta_tabla_canciones_lista()
                            info = Listas_cliente.info_lista(id_cliente)
                            Listas_cliente.registrar_lista_cliente(info)
                            next = False
                            while not next:
                                opc_next = input("""\n¿Desea agregar otra canción? s/n: """).lower()
                                if opc_next == 's':
                                    next = True
                                elif opc_next == 'n':
                                    next = True
                                    state_lista = False
                                else:
                                    print_line_error('¡Opción no valida. Digite una opción nuevamente!')
                    except:
                        print_line_error('¡Canción no encontrada en la base de datos!')
            elif opc == "2":
                Listas_cliente.consulta_tabla_listas(id_cliente)
            elif opc == "3":
                state_actualizar = True
                while state_actualizar:
                    try:
                        Listas_cliente.consulta_tabla_listas(id_cliente)
                        id_cancion = int(input('\nDigite el id de la canción que desea actualizar: '))
                        Listas_cliente.consulta_tabla_canciones_lista()
                        lista_info = Listas_cliente.info_lista(id_cliente)
                        Listas_cliente.actualizar_info_tabla_listas(tuple(lista_info[0:5]), id_cancion, id_cliente)
                        state_actualizar = False
                    except:
                        print_line_error('¡Canción no encontrada en las base de datos!')

            elif opc == "4":
                Listas_cliente.borrar_lista(id_cliente)
            elif opc == "5":
                Listas_cliente.enviar_mensaje(id_cliente)
            elif opc == "6":
                if Listas_cliente.contar_lista(id_cliente)[0] == 0:
                    print_line_error('¡No tienes canciones en tu lista de reproducción!\nCrea una lista para poder reproducir canciones')
                else:
                    Listas_cliente.consulta_tabla_listas(id_cliente)
                    id_cancion = int(input('\nDigite el id de la canción que desea reproducir: '))
                    id_validacion = val.existencia_tablas('listas', 'id_cancion', 'id_cancion', id_cancion)
                    while id_validacion != False:
                        id_cancion = int(input('\nDigite el id de la canción que desea reproducir: '))
                        id_validacion = val.existencia_tablas('listas', 'id_cancion', 'id_cancion', id_cancion)
                    Listas_cliente.reproducir_cancion(id_cancion, id_cliente)
            elif opc == "7":
                state = False

            else:
                print("\t\n¡Opcion no valida. Digite una opción nuevamente!")

def main():
    menu_principal()

if __name__ == '__main__':
    main()

