from pedidos import ARCHIVO_PEDIDOS

def ver_historial():
    try:
        print("\n Historial de pedidos")
        with open(ARCHIVO_PEDIDOS, "r", encoding="utf-8") as archivos:
            pedidos = archivos.readlines()
            # Si hai pedidos
            if pedidos:
                # Recorrer los pedidos con el indice y el elemento, pero que inicie desde 1
                for i, pedido in enumerate(pedidos, 1):
                    print(str(i) + ". " + pedido.strip())
            else:
                print("Aun no hay ningun pedido")
    except FileNotFoundError:
        print("\n Todavia no existe un historial de pedidos")