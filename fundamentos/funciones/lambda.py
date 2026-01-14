# Lambda: Es una funcion pequena y anonima que puede tener muchos argumentos pero solo una expresion
# Es una funcion anonima
x = lambda a : a + 10
print(x(5))

sumar = lambda a, b : a + b
print(sumar(4, 5))

# Fabricar funciones
def mi_funcion(n):
    return lambda a: a * n

duplicador = mi_funcion(2)
triplicador = mi_funcion(3)

print(duplicador(5))
print(triplicador(5))