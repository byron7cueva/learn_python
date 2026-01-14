# String
comillas_simples = 'Este es un texto'
comillas_dobles = "Este es otro texto"
comillas_triples = '''Texto con comillas triples'''

print(comillas_simples)
print(comillas_dobles)
print(comillas_triples)

# Enteros
a = 1
print(a)

# Flotantes
b = 1.5
print(b)

# Complejos
c = 3 + 5j
print(c)

# Lista
# Es una coleccion ordenada y mutable de elementos, en el cual
# cada elemento tiene un indice.

list = [0, 1, 2, 3, 4, 5]

# Tuplas
# Son colecciones ordenadas pero son inmutables, los elementos no
# Son inmutables

tuple = ("a", "b", "c")

# Diccionarios
# Es una coleccion ordenada de pares clave - valor
# Es mutable
# Ordenada quiere decir que tiene una posicion puntual y vamos a poder
# acceder a traves de un indice para poderlo modificarlo
# Los elementos se pueden repetir

dictionary = {
    "nombre": "Byron",
    "edad": 37,
    "ciudad": "Otavalo"
}

# Conjuntos (Set)
# Es una coleccion desordenada
# Es mutable
# Los elementos van a ser unicos
# Ignora todos los elementos repetidos
# No podemos acceder a traves del indice porque no tiene una posicion clara
conjunto = {1,1,2,2,3}
print(conjunto)


# Booleanos
boolean_verdadero = True
bolean_falso = False
