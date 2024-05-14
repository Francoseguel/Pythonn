saldo = 100000
while True:
    print("Bienvenido al Banco Duoc, selecciona una opcion\n")
    print("1.- Consultar Saldo")
    print("2.- Retirar Dinero")
    print("3.- Salir\n")

    opcion = input("Selecciona una opcion del (1 al 3): ")
    if opcion == "1":
        print(f"\nTu saldo es de {saldo}\n")
    elif opcion == "2":
        cantidad_retiro = float(input("Ingrese la cantidad a retirar: $"))
        if cantidad_retiro <= saldo:
            saldo -= cantidad_retiro
            print(f"Haz retirado ${cantidad_retiro}\nTu nuevo saldo es de: ${saldo}")
        else:
            print("Saldo insuficiente.")
    elif opcion == "3":
        print("Gracias por utilizar el Cajero")
        break
    else:
        print("Opcion no valida, selecciona una opcion valida")
