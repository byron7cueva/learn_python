year = input("Cual es tu edad? ")

try:
    year_int = int(year)
    print(f"Su edad es {year_int}")
except:
    print("La edad es incorrecta o no es un valor valido")