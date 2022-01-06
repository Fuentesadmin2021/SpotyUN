import random

"Clases privadas"

# Función para validar la longitud de un cadena retorna un booleano
def _validar_len(dato: str, longitud: int) -> bool:
    while (x := len(dato)) <= longitud:
        return True

# Función para validar si existe o no algún caracter especial en la cadena retorna un boolean
def _validacion_caracteres(dato: str) -> bool:
    lcaracter = "'áéíóú ´/*+,;:{}[]()¨!|¬#$%&=?¿¡!"
    for i in dato:
        if i in lcaracter:
            return True
    else:
        return False



# Función para validar una entrada numerica str y retornarla como str
# es necesario convertir el número a int siempre y cuadno se requiera
def validacion_numero(dato: str, longitud: int) -> str:
    while not dato.isnumeric() or not _validar_len(dato, longitud):
        dato = input('¡ERROR! Verifique e ingrese de nuevo la información: ')
    return dato



# Función para validar que una entrada sea unicamente alfabetica
def validacion_letra(dato: str, longitud: int) -> str:
    while not (d := dato.replace(' ', '').isalpha()) or not _validar_len(dato, longitud):
        dato = input('¡ERROR! Verifique e ingrese de nuevo la información: ')
    return dato.strip()


# Función para validar que un número sea acorde a la longitud
def validacion_telefono(dato: str, longitud: int) -> str or int:
    while not (d := dato.isdigit()) or not _validar_len(dato, longitud):
        dato = input('''¡ERROR! Verifique e ingrese de nuevo la información: ''')
    return int(dato)

# Función para validar la longitud y escritura acepta para un correo electrónico
def validacion_correo(dato: str, longitud: int) -> str:
    state = True
    while state:
        try:
            if (dato == 'N' or dato == 'n'):
                raise ValueError
            if _validacion_caracteres(dato):
                raise ValueError
            else:
                a = _validar_len(dato, longitud)
                dato_list = dato.split('@')
                if a and ('.') in dato_list[1]:
                    return dato.lower()
                    state = False
                else:
                    raise ValueError
        except:
            dato = input('''¡ERROR! Verifique e ingrese de nuevo la información: ''')


# Función para validar si un número decimal es correcto
def validacion_decimal(dato: str, longitud: int) -> float:
    while not (d := any(i.isdigit() for i in dato)) or not _validar_len(dato, longitud):
        dato = input('''¡ERROR! Verifique e ingrese de nuevo la información: ''')
    return float(dato)


# Función publica para validar solo la longitud de entrada
def validacion_longitud(dato: str, longitud: int) -> str:
    while not _validar_len(dato, longitud):
        dato = input('''¡ERROR! Verifique e ingrese de nuevo la información: ''')
    return dato.upper()


# Función para la autenticación de un usuario dentro de la plataforma
def validacion_usuario(dato: str, longitud: int) -> str:
    state = False
    while not state:
        try:
            if not _validacion_caracteres(dato) and len(dato) > longitud:
                return dato.lower().strip()
                state = True
            else:
                raise ValueError
        except:
            dato = input('''¡ERROR! Verifique e ingrese de nuevo la información: ''')

# Función para el proceso de autenticación
# Verifica que una contraseña sea correcta o no
def validacion_contrasena(dato: str, longitud: int) -> str:
    dato2 = input('Ingrese nuevamente la contraseña: ').strip()
    state = False
    while not state:
        if _validacion_caracteres(dato) and len(dato) > longitud and dato == dato2:
            return dato
            state = True
        else:
            print('¡ERROR! Ingrese de nuevo la contraseña')
            dato = input('Ingrese contraseña: ')
            dato2 = input('Ingrese nuevamente la contraseña: ')


"-----------------------------------------------------"

# Función para crear una contraseña aleatoria y opcional
def randompass() -> str:
    caracteres = '0123456789/*-+.-_,;{}[]@+?¡¿!#$%&()abcdefghijklmnñopqrstuvwxyz ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    eleccion = random.choices(caracteres, k=15)
    password = ''.join([str(i) for i in eleccion])
    return password


# Función para crear un código de verificación para iniciar sesión
def codigoVerificacion() -> str:
    caracteres = ('ABCDEFHIJKLMNOPQRSTUVWXYZ', '0123456789')
    codigo = ''
    for i in [random.choices(i, k=3) for i in caracteres]:
        codigo = codigo + ''.join(str(x) for x in i)
    return codigo


