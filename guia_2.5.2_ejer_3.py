#CargaTarjetaBip
sw = 1
saldo = 0

while sw == 1:
    print("1. Ver mi Saldo")
    print("2. Cargar Saldo")
    print("3. Salir")
    
    op = int(input("Seleccione una opción: "))

    try:
        if 0 < op < 4:
            if op == 1:
                print(f"Tiene un saldo de {saldo}")
                continu = int(input("Presione 1 para volver atrás, presione 2 para salir: "))
                
                if continu == 2:
                    print("Cierre de sesión exitoso, adiós")
                    sw = 0

            elif op == 2:
                print("¿Cuánto desea cargar?")
                print("1.- $1.000")
                print("2.- $5.000")
                
                continu = int(input("Seleccione la opción: "))
                
                if continu == 1:
                    saldo += 1000
                    print(f"Carga exitosa, su saldo es de: ${saldo}")
                elif continu == 2:
                    saldo += 5000
                    print(f"Carga exitosa, su saldo es de: ${saldo}")

            elif op == 3:
                print("Muchas gracias por ocupar el servicio, adiós")
                sw = 0

        else:
            print("Selección fuera de rango")

    except ValueError:
        print("Ingreso Erróneo")