from decorador import *

class  Borrar():
    def __init__(self, conexionbd):
        self.conexionbd = conexionbd
    

    # Función que elimina toda la información de una tabla
    def eliminar_info_tablas(self, nombre_tabla: str):
        cursor_obj = self.conexionbd.cursor()
        cursor_obj.execute(f'DELETE from {nombre_tabla}')
        self.conexionbd.commit()


    # Función que borrar la información de una tabla de acuerdo al primary_key sumistrado
    def borrar_info(self,nombre_tabla: str, primary_key: str):        
        id = input("\nId de la información a eliminar: ")
        cursor_obj = self.conexionbd.cursor()
        cursor_obj.execute(f'DELETE FROM {nombre_tabla} WHERE {primary_key} = {id}')
        self.conexionbd.commit()
        print_line_success(f"Su registro a sido eliminado de la tabla {nombre_tabla} ;)")


    # Función para borrar cualquier tabla
    def borrar_tabla(self, nombre_tabla):
        cursor_obj = self.conexionbd.cursor()
        cursor_obj.execute(f'DROP TABLE {nombre_tabla}')
        self.conexionbd.commit()