from analizador import text_utils
# from analizador.text_utils import a_mayusculas
# import analizador.text_utils as text_utils

mi_frase = "La modularidad es la clave del software profesional"

print(text_utils.contar_palabras(mi_frase))
print(text_utils.a_mayusculas(mi_frase))