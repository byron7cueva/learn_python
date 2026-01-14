print('"Hola mundo"')

ingles = "I'm Byron"

# Respeta los saltos de linea
multiples = """
Hola
Mundo
"""

print(ingles)
print(multiples)

# Metodos para strings
palabra = "Murcielago"
print(len(palabra))  # Cantidad de caracteres

# Palabra si esta incluida en otra
texto = "Este curso de fundamentos de Python"
esta_incluida = "Python" in texto
no_esta_incluida = "Javascript" not in texto
print(f"La palabra Python esta incluida: {esta_incluida}")
print(f"La palabra Javascript no esta incluida: {no_esta_incluida}")

# Mayusculas y minusculas
mayusculas = texto.upper()
minusculas = texto.lower()
print(mayusculas)
print(minusculas)

# Espacios en blanco al inicio y final
espacios = "     Este es el texto   "
sin_espacios = espacios.strip()
print(sin_espacios)

# Obtener una letra del texto a traves de su indice
print(texto[4]) # Primwera letra

# Obtener una parte del texto
print(texto[0:4]) # Desde el indice 0 hasta el 4, sin incluir el 4
print(texto[:4])  # Desde el inicio hasta el indice 4, sin incluir el 4
print(texto[5:])  # Desde el indice 5 hasta el final
print(texto[5:-2]) # Desde el indice 5 hasta el penultimo caracter, con negativo cuenta desde el final

curso = "Este curso es de Javascript"
print(curso.replace("Javascript", "Python"))

texto_dividido = texto.split(" ")
print(texto_dividido)

# Normalizacion

text2 = "Este texto tiene MAYUSCULAS y minusculas y necesito encontra ciertas palanras"
print("mayusculas".upper() in text2.upper())
