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
        cursor_obj = self.conexionbd.cursor()
        cursor_obj.execute(f'UPDATE {nombre_tabla} SET {nombre_columna} = {elemento} WHERE {primary_key} = {id}')
        self.conexionbd.commit()
        print_line_success(f"!{info.title()} se ha actualizado exitosamente¡")

class Update_canciones(Update):
    def __init__(self, conexionbd):
        super().__init__(conexionbd)

    # Función para relizar la actualización del archivo .mp3 binario dentro de la tabla canciones
    def actualizar_cancion(self):
        cursor_obj = self.conexionbd.cursor()
        id = input('\nIngrese el id de la canción a la que quiere modificar: ')
        state = False
        while not state:
            try:
                nombre_cancion = input('Nombre de la canción tal cual esta almacenada en su equipo: ')
                cancion = escribir_cancion_binario(nombre_cancion)
                state = True
            except:
                print_line_error('\n¡Error en los datos de la canción en el equipo\n por favor verifique e ingrese de nuevo la información!\n ')

        cursor_obj.execute(f'UPDATE canciones SET cancion = {cancion} WHERE id_cancion = {id}')
        self.conexionbd.commit()
        print_line_success("!La cancion se ha actualizado exitosamente¡")

  
