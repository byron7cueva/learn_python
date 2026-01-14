x = 5
y = 3
z = 10

if x > y:
    print(f"{x} es mayor a {y}")
else:
    print(f"{x} no es mayor a {y}")

if x > y:
    print(f"{x} es mayor a {y}")
elif x == y:
    print(f"{x} es igual a {y}")
else:
    print(f"{x} es menor a {y}")


if x > y and x > z:
    print(f"{x} es mayor a {y} y mayor a {z}")
elif x == y:
    print(f"{x} es igual a {y}")
else:
    print("Ninguna de las condiciones anteriores se cumplio")


a = "Python"
b = "Javascript"
c = "Python"

if a == c:
    print(f"{a} es igual a {c}")
else:
    print(f"{a} no es igual a {c}")


if a == c:
    if a == b:
        print(f"{a} es igual a {c} y igual a {b}")
    else:
        print(f"{a} es igual a {c} pero es distinto a {b}")
else:
    print(f"{a} no es igual a {c}")


e = 10
f = 10

if e == f:
    pass # Ignorar la estructura hasta definir que compartamiento se va dar