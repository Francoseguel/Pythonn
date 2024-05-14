edad = int(input("Indiqueme su edad: "))

if edad >= 18:
    print("Usted es mayor de edad")
elif edad > 0 and edad < 18:
    print ("Usted es menor de edad")
else:
    print("Su edad es incorrecta porfavor, volver a ingresarla.")