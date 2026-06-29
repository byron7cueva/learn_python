# Funcion Lambda
duplicar_lambda = lambda n: n * 2

print(duplicar_lambda(5))

# -----------------------------------------------------------------------------
# map()
# Aplica una función a cada elemento de una secuencia.
numeros = [1, 2, 3, 4, 5]

#Usando map y una lambda para duplicar cada numero
numeros_duplicados_map = map(lambda x: x * 2, numeros)
# Transformando a una lista
print(list(numeros_duplicados_map))

# Usando la forma Pythonica: List Comprehension
numeros_duplicados_lc = [x * 2 for x in numeros]
print(numeros_duplicados_lc)

# -----------------------------------------------------------------------------
# filter
# Filtra una secuencia, dejando solo los elementos que cumplen una condición.

# Usando filter y una lambda para obtener solo los numeros pares
numeros_pares_filter = filter(lambda x: x % 2 == 0, numeros)
print(list(numeros_pares_filter))

# Forma Pythonica: List Comprehension con if
numeros_pares_lc = [x for x in numeros if x % 2 == 0]
print(numeros_pares_lc)