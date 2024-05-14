#Numero complejo
numeroComplejo = 1j
print(type(numeroComplejo))

#Datos de tipo rango (range)
coordenada = range (0,11)
print (coordenada)

#Datos set () es para conjuntos
numeros = {2,5,7,8,9}
numeros.add(14)
print (numeros) 

"""
tipo de dato Frozenset: Es una coleccion inmutable parecida a un set, NO SE PUEDE MODIFICAR

"""
frutas = frozenset({"Arandanos","Frutilla","Manzana","Melon"})
print(frutas)
print(type(frutas))

"""
Tipo de dato bytes: es un tipo de dato inmutable(NO SE PUEDEN MODIFICAR O AGREGAR) parten desde el 0 hasta el 255

"""
#Crear un objeto a partir de un bytes

variableBytes = bytes("Hola que sucede realmente","utf-8") #utf-8 es un formato de codificacion Unicode e ISO
print(variableBytes)

#Crear un texto a partir de número bytes

b = bytes([72,111,108,97])
print(b)

#byteArray

c = bytearray("Hola k pa","utf-8")
print(c)

#Modificar bytearray

c[0] = 83

print(c)

#Datos de tipo none es un tipo de dato unico que no representa un valor
VariableNone = None
print(VariableNone)

#Para solo imprimir desde un inicio a final parte desde el num 0
hola = "Hola bitch"
print(hola[5:10])
print(hola[:5])