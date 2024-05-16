
import os

def ingresar_datos():
    try:
        nombre = input("Ingrese el Nombre del trabajador: ")
        while not nombre or len(nombre) > 30:
            print("El nombre no puede estar vacío ingrese algo porfavor(Max 30 Letras).")
            nombre = input("Ingrese el nombre del trabajador: ")
        
        sueldo_base = float(input("Ingrese el sueldo base del trabajador: "))
        while sueldo_base <= 0:
            print("El sueldo base debe ser un valor mayor a cero.")
            sueldo_base = float(input("Ingrese el sueldo base del trabajador: "))
        
        horas_extras = float(input("Ingrese el número de horas extras trabajadas en el mes: "))
        while horas_extras < 0:
            print("Las horas extras deben ser un valor numérico positivo.")
            horas_extras = float(input("Ingrese el número de horas extras trabajadas en el mes: "))
        
        return nombre, sueldo_base, horas_extras
    except ValueError:
        print("Ha ocurrido un error. Asegúrese de ingresar un valor numérico para el sueldo base y las horas extras.")
        return 

def calcular_liquidacion(sueldo_base, horas_extras):
    try:
        pago_horas_extras = horas_extras * (sueldo_base / 180) * 1.5
        total_ingresos_brutos = sueldo_base + pago_horas_extras
        descuento_fonasa = total_ingresos_brutos * 0.07
        descuento_afp = total_ingresos_brutos * 0.1
        sueldo_liquido = total_ingresos_brutos - (descuento_fonasa + descuento_afp)
        return pago_horas_extras, total_ingresos_brutos, descuento_fonasa, descuento_afp, sueldo_liquido
    except ZeroDivisionError:
        print("Error: No se pueden calcular las horas extras debido a una división por cero.")
        return 

def mostrar_liquidacion(nombre, sueldo_base, pago_horas_extras, total_ingresos_brutos, descuento_fonasa, descuento_afp, sueldo_liquido):
    print("\n----- Liquidación de Sueldo -----")
    print(f"Nombre del trabajador: {nombre}")
    print(f"Sueldo base: ${sueldo_base:.0f}")
    print(f"Horas Extras: {pago_horas_extras:.0f}")
    print(f"Total sueldo bruto: {total_ingresos_brutos:.0f}")
    print (f"Descuento Fonasa: {descuento_fonasa:.0f}")
    print(f"Descuento AFP: {descuento_afp:.0f}")
    print(f"Sueldo Liquido: {sueldo_liquido:.0f}")

def generar_archivo(nombre,sueldo_base,pago_horas_extras,total_ingresos_brutos,descuento_fonasa,descuento_afp,sueldo_liquido):
    try:
        with open(f"{nombre}_liquidacion_sueldo_liquido.txt","w") as archivo:
            archivo.write("----- Liquidación de Sueldo -----\n")
            archivo.write(f"Nombre del trabajador: {nombre}\n")
            archivo.write(f"Sueldo base: ${sueldo_base:,.0f}\n")
            archivo.write(f"Horas Extras: {pago_horas_extras:,.0f}\n")
            archivo.write(f"Total sueldo bruto: {total_ingresos_brutos:,.0f}\n")
            archivo.write(f"Descuento Fonasa: {descuento_fonasa:,.0f}\n")
            archivo.write(f"Descuento AFP: {descuento_afp:,.0f}\n")
            archivo.write(f"Sueldo liquido: {sueldo_liquido:,.0f}\n")
        print("\nSe ha generado el archivo de liquidación de sueldo.\n")
    except:
        print("Error: No se pudo generar el archivo de liquidación de sueldo.\n")

try:
    nombre, sueldo_base, horas_extras = ingresar_datos()

    pago_horas_extras, total_ingresos, descuento_fonasa, descuento_afp, sueldo_neto = calcular_liquidacion(sueldo_base, horas_extras)

    mostrar_liquidacion(nombre, sueldo_base, pago_horas_extras, total_ingresos, descuento_fonasa, descuento_afp, sueldo_neto)

    generar_archivo(nombre, sueldo_base, pago_horas_extras, total_ingresos, descuento_fonasa, descuento_afp, sueldo_neto)

except Exception as e:
    print(f"Ha ocurrido un error: {e}")
