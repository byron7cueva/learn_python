# PEP donde se definio como se debe documentar es en el PEP 257
# Docstring Conventions
# https://peps.python.org/pep-0257/

# Siempre se va usar 3 comillas porque se puede utilizar multilinea


def ejemplo_sin_docstring():
    return "Hola mundo"


def ejemplo_con_docstrings() -> str:
    """
    Esta funcion devuelve un saludo.

    Returns:
      str: Un saludo en espanol.
    """
    return "Hola, mundo!"


# Leer la documentacion
# .__doc__ almacena la documentacion
# print(ejemplo_con_docstrings.__doc__)
help(ejemplo_con_docstrings)

# Orden correcto de la documentacion
"""
Description
Args
Returns
Exception
Examples
"""

# Tips
# Se conciso y claro.
# Manten actualizada la documentacion
# Documenta ejemplos
