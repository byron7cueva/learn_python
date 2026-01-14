# match es parecido al switch de otros lenguajes
dia = 1

match dia:
    case 1:
        print("Hoy es Lunes")
    case 2:
        print("Hoy es Martes")
    case 3:
        print("Hoy es miercoles")
    case _:
        print("No coincide con ninguna de las anteriores condiciones")