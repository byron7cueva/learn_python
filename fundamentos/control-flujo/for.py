palabra = "Python"

for letra in palabra:
    print(letra)

frutas = ["Manzana", "Naranja", "Kiwi"]

for fruta in frutas:
    print(fruta)

# Break
print("==Break==")
for fruta in frutas:
    if fruta == "Naranja":
        break
    print(fruta)

# Break
print("==Continue==")
for fruta in frutas:
    if fruta == "Naranja":
        continue
    print(fruta)

# Else
# Se ejecuta una vez que termine el bucle
print("==Else==")
for fruta in frutas:
    if fruta == "Naranja":
        continue
    print(fruta)
else:
    print("Termino de recorrer el for")

print("--------------------------------")
# Rango
# Comienza desde 0 y termina hasta el numero que indicamos pero sin incluirlo
for i in range(10):
    print(i)

# Inicia en el 3 y termina en 4
for i in range(3,5):
    print(i)

# Inicia desde 0 y termina en 10 sin incluirlo, pero solo va de 2 en 2
for i in range(0,10,2):
    print(i)

# Bucle anidado
adjetivos = ["Rica", "Saludable"]
for adjetivo in adjetivos:
    for fruta in frutas:
        print(fruta, adjetivo)

for fruta in range(10):
    pass