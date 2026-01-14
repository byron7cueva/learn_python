# Operadores aritmeticos
x = 5
y = 10

# Suma
print("Suma ", x + y)

# Resta
print("Resta ", x - y)

# Multiplicacion
print("Multiplicacion ", x * y)

# Division
print("Division ", y / x)

# Modulo (Resto)
print("Modulo", y % x)

# Potencia
print("Potencia", y ** 5)

# Division entera, no nos devuelve el decimal
print("Division entera", y // x)


par = 7
print(f"{par} es par ", par % 2 == 0)


# Precedencia de operadores
# 1 Parentesis
# 2 Exponentes
# 3 Multiplicaciones, Divisiones, Divisiones enteras y restos
# 4 Sumas y restas
# 5 Comparaciones de identidad y pertenencia
# 6 Logicos


# Operadores de asignacion
x = 5

# Sumar y asignar
x += 3
x -= 3
x *= 3
x /= 3
x %= 2
print(x)


y = 20
y //= 2
y **= 3
print(y)

# Walrus :=
# Permite asignar un valor a una variable desde la llamada de un metodo
print(z := 3)
print(z)

'''
Operadores de Comparacion
'''
x = 5
y = 3
z = 5

print(x == y) # Igual
print(x != y) # Distinto
print(x > y) # Mayor
print(x < y) # Menor
print(x >= y) # Mayor o igual
print(x <= y) # Menor o igual

'''
Operadores Logicos
'''
print(x > y and y > z)
print(x > y or y > z)
v = True
print(not(v))