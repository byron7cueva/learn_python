"""Typing con Python"""
# https://lcmartinez.com/python-typing

from typing import Any

variable = 42

print(f"Variable: {variable}, del tipo: {type(variable)}")


variable = "Texto de prueba"

print(f"Variable: {variable}, del tipo: {type(variable)}")

# Asignarle un tipo
# variable: tipo = valor
# Python no va obligar que utilices el tipo de dato asignado para el valor que asignes a la variable
# Esa validacion es solamente a nivel de desarrollador y a nivel de editor

otra_variable: int = 44
print(f"Variable: {otra_variable}, del tipo: {type(otra_variable)}")

otra_variable = "Hola"

# Indicar que tipos de datos soporta
user_id: int | None = None


# Tipar lo que va retornar la funcion con ->
def suma_clara(a: int, b: int) -> int:
    return a + b


suma_clara(19, 30)

# Ya no es requerido importar
# from typing from List
articles: list = [{"title": "Example"}, {"title": "Example 2"}]

articles2: list[dict] = [{"title": "Example"}, {"title": "Example 2"}, "asa"]


articles3: list[list] = [["articulos", "otro"], ["articulos", "otro"]]

articles4: list[list[str]] = [["articulos", "otro"], ["articulos", "otro"]]

# int, str, list, dict, tuple, Any
# Any permite cualquier tipo de dato
articles5: list[list[Any]] = [["articulos", "otro"], ["articulos", "otro", 12]]
