"""Funciones que se utilizan para mostar el código de los print de las funciones todas estas funciones
reciben una cadena"""


# Función para encerrar los eventos en donde se genere algún error
def print_line_error(cadena: str):
    print("\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ⚠  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(cadena)
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ⚠  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
   
# Función para encerrar los eventos en procesos que sean realizados satisfactoriamente
def print_line_success(cadena: str):
    print("\n❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈")
    print(cadena)
    print("❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈")

# Función para encerrar los diferentes menús que se utilizan en el programa
def print_line_menu(cadena: str):
    print("\n___________________________________________________________________________________________________________________________________")
    print(cadena)
    print("___________________________________________________________________________________________________________________________________")