def decorador_menu(func):
    def envoltura(*args, **kwargs):
        print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        func(*args, **kwargs)
    return envoltura

def decorador_funcion(func):
    def envoltura(*args, **kwargs):
        print("\n***********************************************************************************************************************************")
        func(*args, **kwargs)
        print("*************************************************************************************************************************************")
    return envoltura