import random

"Clases privadas"
def _validar_len(dato: str, longitud: int) -> bool:
    while (x := len(dato)) <= longitud:
        return True
def _validacion_caracteres(dato: str) -> bool:
    lcaracter = "'áéíóú ´/*+,;:{}[]()¨!|¬#$%&=?¿¡!"
    for i in dato:
        if i in lcaracter:
            return True
    else:
        return False

# funcion para validar una entrada numerica str y retornarla como int 
def validacion_numero(dato: str, longitud: int) -> int:
    while not dato.isnumeric() or not _validar_len(dato, longitud):
        dato = input('¡ERROR! Verifique e ingrese de nuevo la información: ')
    return int(dato)

# funcion para validar que una entrada sea numerica str y retornarla como str
def validacion_numeros_str(dato: str, longitud: str) -> str:
    while not dato.isnumeric() or not _validar_len(dato, longitud):
        dato = input('¡ERROR! Verifique e ingrese de nuevo la información: ')
    return (dato)

# funcion para validar que una entrada sea unicamente alfabetica
def validacion_letra(dato: str, longitud: int) -> str:
    while not (d := dato.replace(' ', '').isalpha()) or not _validar_len(dato, longitud):
        dato = input('¡ERROR! Verifique e ingrese de nuevo la información: ')
    return dato.strip()



def validacion_telefono(dato: str, longitud: int) -> str or int:
    if dato == 'N' or dato == 'n':
        dato = 'NO REGISTRA'
        return dato
    else:
        while not (d := dato.isdigit()) or not _validar_len(dato, longitud):
            dato = input('''!!!ERROR!!! Verifique e ingrese de nuevo la información: ''')
        return int(dato)

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
            dato = input('''!!!ERROR!!! Verifique e ingrese de nuevo la información: ''')

def validacion_telefono(dato: str, longitud: int) -> str:
    state = True
    while state:
        try:
            if dato == 'N' or dato == 'n':
                raise ValueError
            else:
                if _validar_len(dato, longitud):
                    return dato.upper().strip()
                    state = False
        except:
            dato = input('''!!!ERROR!!! Verifique e ingrese de nuevo la información: ''')

def validacion_decimal(dato: str, longitud: int) -> float:
    while not (d := any(i.isdigit() for i in dato)) or not _validar_len(dato, longitud):
        dato = input('''!!!ERROR!!! Verifique e ingrese de nuevo la información: ''')
    return float(dato)

def validacion_longitud(dato: str, longitud: int) -> str:
    while not _validar_len(dato, longitud):
        dato = input('''!!!ERROR!!! Verifique e ingrese de nuevo la información: ''')
    return dato.upper()

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
            dato = input('''!!!ERROR!!! Verifique e ingrese de nuevo la información: ''')

def validacion_contrasena(dato: str, longitud: int) -> str:
    dato2 = input('Ingrese nuevamente la contraseña: ').strip()
    state = False
    while not state:
        if _validacion_caracteres(dato) and len(dato) > longitud and dato == dato2:
            return dato
            state = True
        else:
            print('¡¡¡ERROR!!! Ingrese de nuevo la contraseña')
            dato = input('Ingrese contraseña: ')
            dato2 = input('Ingrese nuevamente la contraseña: ')


"-----------------------------------------------------"

def randompass() -> str:
    caracteres = '0123456789/*-+.-_,;{}[]@+?¡¿!#$%&()abcdefghijklmnñopqrstuvwxyz ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    eleccion = random.choices(caracteres, k=15)
    password = ''.join([str(i) for i in eleccion])
    return password

def codigoVerificacion() -> str:
    caracteres = ('ABCDEFHIJKLMNOPQRSTUVWXYZ', '0123456789')
    codigo = ''
    for i in [random.choices(i, k=3) for i in caracteres]:
        codigo = codigo + ''.join(str(x) for x in i)
    return codigo


