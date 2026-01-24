class DivisionError(Exception):
    """Error en operacion"""

    pass


a = 0
b = 0

try:
    a = int(input("Digita un numero: "))
    b = int(input("Digita otro numero: "))
    # raise sirve para lanzar excepciones y detener la ejecicion del codigo
    if b == 2:
        raise DivisionError("No esta permitido el calcul por 2")

    resultado = a / b
    print(f"Resultado: {resultado}")
except ValueError:
    print("El calor que digito no es un numero valido")
except ZeroDivisionError:
    print("No esta permitido dividir por 0")
except Exception as e:  # Exception es una clase base de excepciones
    print(f"E: {e}, type: {type(e)}")
finally:
    print("Print desde finally")

# https://docs.python.org/3/library/exceptions.html
# Tips
# Solo utiliza try - except solo en la parte de codigo donde se espera un posible error
# Se mas especifico captura un exception especifico
# Cada que se captura un error procura logearlo o mostrarlo en la consola
