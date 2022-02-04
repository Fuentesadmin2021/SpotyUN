import sqlite3
from sqlite3 import Error

from decorador import Decorador as dec
from validatos.validatos import Validatos as val

class Manejador_db():
    def __init__(self):
        self.con = Manejador_db.__sql_conexion(self)

    # Conexion con la base de datos
    def __sql_conexion(self):
        try:
            con = sqlite3.connect('SpotyUN_2.db')
            return con
        
        except Error:
            print(Error)

    def close(self):
        self.con.close()

    # Función para actualizar la información de uno de los campos de la tabla en la base de datos
    def actualizar_info_tablas(self, nombre_columna: str, nombre_tabla: str, primary_key: str, info: str, clase):
        state = True
        while state:
            try:
                id = input('Ingrese el id: ').strip()
                if id_v := val.existencia_tablas(self.con, nombre_tabla, nombre_columna, primary_key, id) == False:
                    id = int(id)
                    state = False
                    
                else:
                    print('\nEl id ingresado no existe en la base de datos')
            except:
                print('El id ingresado no es correcto')

        cursor_obj = self.con.cursor()
        cadena = f'UPDATE {nombre_tabla} SET {nombre_columna} = ? WHERE {primary_key} = ?'
        cursor_obj.execute(cadena, (getattr(clase, 'set_', input(f'Ingresa el {info} a actualizar: ')), id))
        self.con.commit()
        dec.print_line_success(f"!Registro actualizado exitosamente¡")
        