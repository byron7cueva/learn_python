# Listas
# Son modificable y permiten duplicados
frutas = ["Manzana", "Naranja", "Mandarina", "Naranja"]
print(frutas)
print(type(frutas))

# Acceder con el indice
print(frutas[1])

frutas[1] = "Banana"
print(frutas)

# Se puede mesclar los tipos de dato
lista = ["Byron", 7, True]
print(lista)
print(type(lista))

# Saber cuantos elementos tiene la lista
print(len(lista))

# Obtener una parte de la lista
print(frutas[0:2]) # Desde la posicion 0 hasta el 2, pero no esta incluido
print(frutas[:2]) # Desde el inicio hasta el 2, pero el 2 no esta incluido
print(frutas[1:]) # Desde la posicion 1 hasta el final

# Valida si ese valor esta en la lista
if "Manzana" in frutas:
    print("La Manzana esta dentro de frutas")

vehiculos = ["Auto", "Moto", "Avion"]

# Metodos
# Append: Agregar un elemento al final de la lista
vehiculos.append("Barco")
print(vehiculos)

# Insert: Permite agregar un elemento pero indicando la posicion en dode vamos a agregar el elemento
# Esto hace que el siguiente elemento corra una posicion
vehiculos.insert(1, "Bicicleta")
print(vehiculos)

# Remove: Remueve un elemento de la lista
# Remueve el elemento pero recorre la lista
vehiculos.remove("Auto")
print(vehiculos)

# Pop
# Remueve de acuerdo al indice
vehiculos.pop(1)
print(vehiculos)

# Sort
# Ordena los elementos
vehiculos.sort()
print(vehiculos)

# Reverse
# Ordena la lista de forma invertida
vehiculos.reverse()
print(vehiculos)

# Unir lista
coleccion1 = [1,2,3]
coleccion2 = [4,5,6]

coleccion3 = coleccion1 + coleccion2
print(coleccion3)

# Agrega una coleccion a otra, modificando la primera
coleccion1.extend(coleccion2)
print(coleccion1)