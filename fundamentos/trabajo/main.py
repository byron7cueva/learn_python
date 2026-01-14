from menu import mostrar_menu
from pedidos import pedir_cafe
from historial import ver_historial

def main():
    while True:
        # Mostrar el menu del cafe que se va ofrecer
        mostrar_menu()
        opcion = input("Selecciona una opcion: ")
    
        if opcion == "1":
            # Pedir un cafe
            pedir_cafe()
        elif opcion == "2":
            # Ver el historial
            ver_historial()
        elif opcion == "3":
            # Saludar
            print("\n Muchas gracias por haber tomado nuestro riquisimos cafes")
            break
        else:
            print("Opcion invalida, por favor indique una de la opciones sugeridas")

# Cuando se utiliza modulos se debe asegurar que el punto de inicio sea el que nosotros deseamos

# Se debe igualar al nombre del archivo
if __name__ == "__main__":
    main()