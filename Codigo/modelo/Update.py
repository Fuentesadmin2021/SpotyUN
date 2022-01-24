from validacion_datos import *
from decorador import *

class Update():
    def __init__(self, conexionbd):
        self.conexionbd = conexionbd.cursor()
# Función para actualizar información de una tabla en la base de datos
# Funciona para cualquier tabla dentro de la base de datos
    def actualizar_info_tablas(self, info: str, nombre_columna: str, nombre_tabla: str, primary_key: str, longitud: int):
        state = True
        while state:
            try:
                id = input('\nIngrese el id: ').strip()
                if id_v := validacion_existencia_todas(self, nombre_tabla, nombre_columna, primary_key, id) == False:
                    id = int(id)
                    state = False
                else:
                    print('\nEl id ingresado no existe en la base de datos')
            except:
                print('El Id ingresado no es el correcto')
        elemento = validacion_longitud(input(f'Ingrese {info} actualizado: '), longitud)
        actualizar = f'UPDATE {nombre_tabla} SET {nombre_columna} = ? WHERE {primary_key} = ?'
        info_actualizar = (elemento, id)
        self.conexionbd.execute(actualizar, info_actualizar)
        self.conexionbd.commit()
        print_line_success(f"!{info.title()} se ha actualizado exitosamente¡")

        