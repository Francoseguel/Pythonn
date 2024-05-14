
saldo = 500000
while True:
    print("Seleccione una opcion\n")
    print("1. Ver mi saldo")
    print("2. Retirar mi saldo")
    print("3. Salir")
    try:
        opcion = int(input("\nSeleccione una opción (1 al 3): "))
    except:
        print("\nElije alguna de las opciones\n")
    else:
        if opcion == 1:
            print(f"\nTiene un saldo de ${saldo}\n")
            continu = int(input("1) para volver atrás\n2) para salir\nElija una opcion: "))
            if continu==2:
                print("Cierre de sesión exitoso, adiós")
                break
        elif opcion == 2:
            print("\nTransferencia realizada\n")
            continu = int(input("1) para volver atrás\n2) para salir\nElija una opcion: "))
            if continu==2:
                print("Cierre de sesión exitoso, adiós")
                break
        elif opcion == 3:
            print("Saliendo....")
            break
          