print(5 > 3)
v = True
f = False

print(type(v))

# Cating
# True
print(bool("Hola mundo")) # True
print(bool(123))
print(bool(["Manzana", "Pera"]))


# False
print(bool("")) # False
print(bool(0))
print(bool([]))
print(bool(None))
print(bool(()))
print(bool({}))
print(bool(set()))

# Validar si es un entero
x = 123
print(isinstance(x, int))
