


def registar_cliente():
    print("\n --- REGISTRANDO NUEVO CLIENTE ---")
    




def listar_cliente():
    print("\n --- LISTANDO CLIENTES ---")

def Eliminar_cliente():
    print("\n --- ELIMINANDO UN CLIENTE ---")

def Registar_pedido():
    print("\n --- REGISTRANDO PEDIDO ---")

def Listar_pedidos_de_un_cliente():
    print("\n --- LISTA DEL CLIENTE ---")

def Guardar_venta():
    print("\n --- GUARDANDO VENTA DEL CLIENTE ---")

def Listar_ventas_realizadas():
    print("\n --- LISTA DE VENTAS REALIZADAS ---")

def menu():
    while true:
        print("1. Registrar un cliente")
        print("2. Listar cliente")
        print("3. Eliminar un cliente")
        print("4. Registrar un pedido")
        print("5. Listar pedidos de un cliente")
        print("6. Guardar una venta")
        print("7. Listar las ventas realizadas por cliente")
        print("8. Salir")

        op = input("Eliga una opcion: ")
        if op == "1":
            registar_cliente()
        elif op =="2":
            listar_cliente()
        elif op =="3":
            Eliminar_cliente()
        elif op =="4":
            Registar_pedido()
        elif op=="5":
            Listar_pedidos_de_un_cliente()
        elif op=="6":
            Guardar_venta()
        elif op=="7":
            Listar_ventas_realizadas()
        elif op =="8":
            print("Saliendo del programa...*")
            break