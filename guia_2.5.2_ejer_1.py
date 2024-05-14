
puntos = 100000

while True:
    print("Seleccione una opcion")
    print("1. Ver mis puntos")
    print("2. Gastar mis puntos")
    print("3. Salir")
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        print(f"Sus puntos son de {puntos}")
    elif opcion == 2:
        print("Seleccione el producto a canjear")
        print("1.- Gift Card de $10.000, valor de 10.000 puntos")
        print("2.- Secadora de pelo, valor de: 25.000 puntos")
        print("3.- Disco duro portátil, valor de: 30.000 puntos")
        continu = int(input("Seleccione la opción"))
        if continu==1:
            puntos = puntos-10000
            print(f"Canje exitoso, le quedan: ${puntos} puntos")
        elif continu==2:
            puntos = puntos-25000
            print(f"Canje exitoso, le quedan: ${puntos} puntos")
        elif continu==3:
            puntos = puntos-30000
            print(f"Canje exitoso, le quedan: ${puntos} puntos")
            break
    elif opcion == 3:
        print("Saliendo....")
        break        
    
    
    
    


