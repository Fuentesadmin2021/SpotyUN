from multiprocesos.conexion import sql_conexion
from multiprocesos.create  import Database

def close(con):
    con.close()

def main():
    conexion_bd = sql_conexion()
    objeto_creacion = Database(conexion_bd)
    objeto_creacion.tabla_canciones()	
    objeto_creacion.tabla_planes()
    objeto_creacion.tabla_clientes()
    objeto_creacion.tabla_listas()
    objeto_creacion.tabla_planes_por_cliente()

    """
    crear_tabla_canciones(conexion_bd)
    crear_tabla_planes(conexion_bd)
    crear_tabla_clientes(conexion_bd)
    crear_tabla_listas(conexion_bd)
    crear_tabla_planes_por_cliente(conexion_bd)
    menu_principal(conexion_bd)"""
    close(conexion_bd)

if __name__ == '__main__':
    main()

#dejar aca funciones mientras tanto
 
