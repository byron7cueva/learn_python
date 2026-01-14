# Funciones
def mi_funcion():
    print("Hola Mundo desde una funcion")

mi_funcion()

# Esperamos Argunmentos
def saludar(nombre: str):
    print(f"Hola {nombre}")

# Pasamos Parametros
saludar("Byron")


# Esperamos Argunmentos
# Es importante pasar todos los valores que espera la funcion
# Es importante el orden
def saludar2(nombre: str, apellido: str):
    print(f"Hola {nombre} {apellido}")

saludar2("Byron", "Cueva")

# Hacer que el argumento tenga un valor por defecto y que no sea requerido
def saludar3(nombre: str, apelido: str = ""):
    print(f"Hola {nombre} {apelido}")

saludar3("Luis")

# Devolver un valor
def sumar(a: int, b: int):
    return a + b

resultado = sumar(3,4)
print(resultado)

# Cuando todavia no defino lo que va hacer la funcion
def funcion():
    pass

funcion()