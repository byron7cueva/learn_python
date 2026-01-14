ARCHIVO_PEDIDOS = "pedidos.txt"

def pedir_cafe():
    print("\n Elige el cafe que prefieras:")
    print("1: Expreso")
    print("2: Cappuccino")
    print("3: Latte")
    print("4: Americano")

    opcion = input("Opcion: ")

    cafes = {
        "1": "Expresso",
        "2": "Cappuccino",
        "3": "Latte",
        "4": "Americano"
    }

    # solo con el nombre del diccionario devuelve las keys
    if opcion in cafes:
        cafe_elegido = cafes[opcion]
        print("Has pedido un ", cafe_elegido, "Preparando tu cafe!")

        with open(ARCHIVO_PEDIDOS, "a", encoding="utf-8") as archivo:
            archivo.write(cafe_elegido + "\n")
    else:
        print("La Opcion no es valida por favor intenta nuevamente")
