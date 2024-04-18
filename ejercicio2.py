#Ejercicio2
añoNacimiento = int(input("Dime en que año naciste: "))
mesNacimiento = int(input("Dime que mes naciste(en numero): "))
diaNacimiento = int(input("Dime que dia naciste: "))

fechaActual = (2024,4,18)
edad = fechaActual[0] - añoNacimiento

if (fechaActual[1], fechaActual[2]) < (mesNacimiento, diaNacimiento):
    edad -= 1
print("la edad es: ", edad)
