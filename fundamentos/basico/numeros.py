import random

x = 1
y = 2.5
z = 1j

# Ver el tipo de dato
print(type(x))
print(type(y))
print(type(z))

positivo = 5.5
negativo = -5.5

imaginario = -1j

# Casting
xf = float(x)
print(type(xf))
print(xf)

ye = int(y)
print(type(ye))
print(ye) # Trunca el valor al cambiar de flotante a entero

entero = 5
flotante = 5.5
entero_complejo = complex(entero)
flotante_complejo = complex(flotante)

print(type(entero_complejo))
print(entero_complejo)

print(type(flotante_complejo))
print(flotante_complejo)

# Numero aleatorios, pero el 10 no esta incluido
print(random.randrange(1,10))