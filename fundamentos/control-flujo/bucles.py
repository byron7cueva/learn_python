# while
i = 0

while i < 10:
    print(i)
    i += 1

# Romper el ciclo
j = 0
while j <= 10:
    print(j)
    if j == 5:
        break
    j += 1

# Saltar un paso
k = 0
while k <= 10:
    k += 1
    if k == 5:
        continue
    print(k)

# Capturar cuando termina
a = 0
while a < 10:
    a += 1
    if a == 5:
        continue
    print(a)
else:
    print("Dejo de ser menor a 10")