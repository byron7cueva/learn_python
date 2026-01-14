# Conjuntos (Set)
# Coleccion no ordenada de elementos unicos (No se puede acceder por indice)
# Si se puede modificar el conjunto pero no un elemento
# Los elementos duplicados se eliminan o son ignorados

frutas = {"Manzana", "Naranja", "Mandarina", "Naranja"}
print(frutas)
print(type(frutas))
print(len(frutas))

conjuntos = {"Python", 156, True}
print(conjuntos)
print(type(conjuntos))

# Recorrer
for item in conjuntos:
    print(item)


print("Manzana" in frutas)
print("Pera" not in frutas)

# Agregar elementos
# Add
frutas.add("Pera")
print(frutas)

# Update: Agregar mas de un elemento
# Agregar listas, tuplas y conjuntos
frutas_tropicales = {"Pina", "Mango"}
frutas.update(frutas_tropicales)
print(frutas)

# Eliminar
frutas.remove("Mango")
print(frutas)
# frutas.remove("Banana") # Al no haber en la lista genera un error

# Discard
frutas.discard("Pera")
print(frutas)
frutas.discard("Banana") # Si hai lo elemina, caso contrario no da error

# Elimina un elemento aleatorio
frutas.pop()
print(frutas)

# Vacias
frutas.clear()
print(frutas)

print("============")
print("Operaciones entre conjuntos")
a = {"a", "b", "c"}
b = {"c", "d", "e"}

# Union
c = a.union(b)
print(c)

# Interseccion
i = a.intersection(b)
print(i)

# Diferencia
d = a.difference(b)
print(d)