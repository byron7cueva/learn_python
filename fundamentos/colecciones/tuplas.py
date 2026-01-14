# Tuples
# Coleccion ordenada e inmutable de elementos que permiten duplicados

tecnologias = ("Python", "Javascript", "Go", "Python")
print(tecnologias)

# Acceder a a los elementos a traves del indice
print(tecnologias[1])

print(len(tecnologias))

print(type(tecnologias))

# Definir una tupla con un solo elemento
fruta = ("Manzana",)
print(type(fruta))

tupla = ("Python", 1, True)
print(tupla)
print(type(tupla))

# Desempaquetar
x, y, z = tupla
print(x)
print(y)
print(z)

# Unir dos tuplas
tupla1 = (1,2,3)
tupla2 = (4,5,6)

tupla3 = tupla1 + tupla2
print(tupla3)

# Duplicar los datos de una tupla
print(tupla * 2) # Los elementos van estar 2 veces


for item in tupla:
    print(item)

# Modificar
print("======================")
tupla_a_modificar = ("Pyhton", "Javascript", "Go")
print(tupla_a_modificar)
lista_comodin = list(tupla_a_modificar)
print(lista_comodin)
lista_comodin.append("ReactJs")
tupla_a_modificar = tuple(lista_comodin)
print(tupla_a_modificar)