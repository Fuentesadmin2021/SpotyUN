# def registrar_imagen_cancion():
#     imagen = f'../Imagenes/drink_wine.jpg'
#     with open(imagen, 'rb') as f:
#         blob = f.read()
#         return blob


def registrar_cancion_bd():
    cancion = f'../Canciones/drink_wine.mp3'
    with open(cancion, 'rb') as file:
        blob = file.read()
        return blob

def write_file(data, filename):
    '''Convert binary data and write it on Hard Disk'''
    with open(filename, 'wb') as file:
        audio = file.write(data)



audio_path = registrar_cancion_bd()
audio = f"{audio_path}"
