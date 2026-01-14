try:
    numero = 10 / 0
except ZeroDivisionError: # Se debe poner el tipo de error
    print("No se puede dividir por 0")


try:
    print(x)
except NameError:
    print("La variable no ha sido definida")
finally:
    print("Esto sera ejecutado siendo exitoso o no el bloque")