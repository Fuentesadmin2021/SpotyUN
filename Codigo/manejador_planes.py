from manejadorbd import sql_conexion
import validacion_datos

# funcion que pide los datos de un plan antes de registrarlo
def plan():
    id_plan = validacion_datos.validacion_numero(input("id plan: "),1)
    nombre_plan = input("nombre: ")
    valor = validacion_datos.validacion_numero(input("Valor plan: "),5)
    cant_canciones = validacion_datos.validacion_numero(input("Cantidad de canciones: "),4)
    datos_plan = (id_plan, nombre_plan, valor, cant_canciones)
    return datos_plan

# funcion para registrar los planes en la base de datos
def registrar_plan(con):
    insercion = plan()
    cursor_obj=con.cursor()
    cursor_obj.execute('''INSERT INTO planes VALUES(?,?,?,?)''', insercion)
    con.commit()

# Funcion que permite modificar el nombre de un plan
def actualizar_nombre_plan(con):
    cursor_obj = con.cursor()
    id = int(input('Ingrese el id del plan al que quiere modificarle el nombre: '))
    nombre = input("Ingrese el nombre del plan: ")
    actualizar = 'UPDATE planes SET nombre_plan = "'+nombre+'" WHERE id_plan = '
    id_actualizar = actualizar + str(id)
    cursor_obj.execute(id_actualizar)
    print("!El nombre del plan se ha modificado exitosamente¡")
    con.commit()

# Funcion que permite modificar el valor de un plan
def actualizar_valor_plan(con):
    cursor_obj = con.cursor()
    id = int(input('Ingrese el id del plan al que quiere modificarle el valor: '))
    valor = input("Ingrese el valor del plan: ")
    actualizar = 'UPDATE planes SET valor = "'+valor+'" WHERE id_plan = '
    id_actualizar = actualizar + str(id)
    cursor_obj.execute(id_actualizar)
    print("!La información se ha modificado exitosamente¡")
    con.commit()

# Funcion que permite modificar el valor de un plan
def actualizar_cantidad_canciones_plan(con):
    cursor_obj = con.cursor()
    id = int(input('Ingrese el id del plan al que quiere modificarle la cantidad de canciones: '))
    cantidad = input("Ingrese la cantidad de canciones del plan: ")
    actualizar = 'UPDATE planes SET cantidad_canciones = "'+cantidad+'" WHERE id_plan = '
    id_actualizar = actualizar + str(id)
    cursor_obj.execute(id_actualizar)
    print("!La información se ha modificado exitosamente¡")
    con.commit()
   
'''funcion que hace una consulta de todos los
planes registradas en la base de datos y los 
muestra al usuario'''
def consulta_tabla_planes(con):
    cursor_obj = con.cursor()
    cursor_obj.execute('SELECT * FROM  planes')
    cantidad_planes = cursor_obj.fetchall()  
    orden_salida = orden_consulta(cantidad_planes)
    print ("\n{:<5} {:<20} {:<20} {:<20} ".format('ID', 'NOMBRE', 'VALOR', 'CANTIDAD CANCIONES'))
    for row in orden_salida:
        id, nombre, valor, cantidad_canciones = row
        print ("{:<5} {:<20} {:<20} {:<20} ".format(id, nombre, valor, cantidad_canciones))

# funcion que ordena la consulta de distintas maneras
def orden_consulta(lista):
    print('''
                        ¿EN QUE ORDEN DESEA OBTENER LA CONSULTA?
                    1. Por id
                    2. Por nombre
                    3. por valor
                    4. por cantidad de canciones a las que puede acceder\n''')

    opc = input("\tDigite una opcion: ")
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

'''funcion que permite hacer una consulta individual
de un cliente por medio de su identificacion registrada'''
def consulta_individual_plan(con):
    cursor_obj = con.cursor()
    id = int(input('Ingrese un id: '))
    busqueda = 'SELECT * FROM planes WHERE id_plan = '
    id_busqueda = busqueda + str(id)
    cursor_obj.execute(id_busqueda)
    datos_plan = cursor_obj.fetchall()
    print ("\n{:<5} {:<15} {:<10} {:<10} ".format('ID', 'NOMBRE', 'VALOR', 'CANTIDAD CANCIONES'))
    for row in datos_plan:
        id, nombre, valor, cantidad_canciones = row
        print ("{:<5} {:<15} {:<10} {:<10} ".format(id, nombre, valor, cantidad_canciones))

# funcion que crea un menu para actualizar de manera individual los datos basicos de un plan
def actualizar_datos_plan(con):
    salir_actualizar = False
    while not salir_actualizar:
        print('''
                            ACTUALIZAR INFORMACIÓN PLAN
                        1. Nombre
                        2. Valor
                        3. Cantidad de canciones
                        4. Ir al menu anterior\n''')

        opc = input("\tDigite una opcion: ")
        if (opc == '1'):
            actualizar_nombre_plan(con)
            
        elif(opc == '2'):
            actualizar_valor_plan(con)

        elif(opc == '3'):
            actualizar_cantidad_canciones_plan(con)
            
        elif(opc == '4'):
            salir_actualizar = True
                

#mi_conexion = sql_conexion()
# menu_planes(mi_conexion)
# registrar_plan(mi_conexion)
# actualizar_nombre_plan(mi_conexion)
# actualizar_valor_plan(mi_conexion)
# actualizar_cantidad_canciones_plan(mi_conexion)
#consulta_tabla_planes(mi_conexion)
# consulta_individual_plan(mi_conexion)
