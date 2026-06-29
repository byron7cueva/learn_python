# Set
# Es una coleccion no ordenada, mutable y que no admite elementos duplicados.
# Se define usando llaves {}.
# Son conjuntos

s = {1, 2 , 3}

# Agrega un elemento
s.add(4)

# Elimina, da error si no existe
s.remove(2)

# Elimina sin error si no existe
s.discard(10)

# Elimina un elemento aleatorio
s.pop()

# Vacia el set
s.clear()

A = {1, 2, 3}
B = {3, 4, 5}

# Union
print(A | B)
print(A.union(B))

# Interseccion
# Busca elementos que tengan los dos Sets
print(A & B)
print(A.intersection(B))

# Diferencia
# Los elementos que esten en A, pero no en B
print(A - B)
print(A.difference(B))

# Diferencia simetrica
# Busca elementos que no estan en ambos
print(A ^ B)
print(A.symmetric_difference(B))