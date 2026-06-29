# Bucle For, Range y Continue

# range(3) genera secuencia: 0, 1, 2. EL rango inicia desde 0 por lo cual no va tomar en cuenta el 3
print("Inicio del bucle FOR")
for i in range(3):
    print(f"Paso {i}")

# Ejemplo de contrinue solo imprime impares
# Tambien en range podemos definir desde donde empieza. En este caso le digo que empiece en 1
for number in range(1, 6):
    if number % 2 == 0:
        continue
    print(f"Impar: {number}")