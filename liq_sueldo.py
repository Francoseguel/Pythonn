# Función para calcular el sueldo base
def calcular_sueldo_base(horas_trabajadas, valor_hora):
    return horas_trabajadas * valor_hora

# Función para calcular las horas extras
def calcular_horas_extras(horas_extras, valor_hora):
    return horas_extras * (valor_hora * 1.5)  # Se pagan con un 50% de recargo

# Función para calcular el bono por antigüedad
def calcular_bono_antiguedad(anios_trabajados, bono_anual):
    return anios_trabajados * bono_anual

# Función para calcular las cotizaciones previsionales
def calcular_cotizaciones(sueldo_bruto):
    AFP = sueldo_bruto * 0.1  # Cotización para el sistema de AFP
    salud = sueldo_bruto * 0.07  # Cotización para salud
    seguro_cesantia = sueldo_bruto * 0.006  # Seguro de cesantía
    return AFP, salud, seguro_cesantia

# Función para calcular los impuestos
def calcular_impuestos(sueldo_bruto):
    impuesto_mensual = 0
    if sueldo_bruto > 500000:  # Ejemplo de tramo impositivo, puede variar según la legislación actual
        impuesto_mensual = (sueldo_bruto - 500000) * 0.08  # Impuesto del 8% sobre el exceso de 500,000 CLP
    return impuesto_mensual

# Función para calcular el sueldo líquido
def calcular_sueldo_liquido(sueldo_bruto, AFP, salud, seguro_cesantia, impuestos):
    sueldo_liquido = sueldo_bruto - (AFP + salud + seguro_cesantia + impuestos)
    return sueldo_liquido

# Datos de ejemplo
horas_trabajadas = 180
valor_hora = 5000
horas_extras = 10
anios_trabajados = 3
bono_anual = 100000

# Cálculos
sueldo_base = calcular_sueldo_base(horas_trabajadas, valor_hora)
extra = calcular_horas_extras(horas_extras, valor_hora)
bono_antiguedad = calcular_bono_antiguedad(anios_trabajados, bono_anual)
sueldo_bruto = sueldo_base + extra + bono_antiguedad
AFP, salud, seguro_cesantia = calcular_cotizaciones(sueldo_bruto)
impuestos = calcular_impuestos(sueldo_bruto)
sueldo_liquido = calcular_sueldo_liquido(sueldo_bruto, AFP, salud, seguro_cesantia, impuestos)

# Crear y escribir en el archivo de texto
with open("liquidacion_sueldo.txt", "w") as archivo:
    archivo.write("Detalle de la Liquidación de Sueldo\n")
    archivo.write("===================================\n")
    archivo.write(f"Sueldo Base: ${sueldo_base}\n")
    archivo.write(f"Horas Extras: ${extra}\n")
    archivo.write(f"Bono por Antigüedad: ${bono_antiguedad}\n")
    archivo.write(f"Sueldo Bruto: ${sueldo_bruto}\n")
    archivo.write("Descuentos:\n")
    archivo.write(f"- AFP: ${AFP}\n")
    archivo.write(f"- Salud: ${salud}\n")
    archivo.write(f"- Seguro de Cesantía: ${seguro_cesantia}\n")
    archivo.write(f"- Impuestos: ${impuestos}\n")
    archivo.write("-----------------------------------\n")
    archivo.write(f"Sueldo Líquido: ${sueldo_liquido}\n")

print("Se ha generado el archivo 'liquidacion_sueldo.txt' con la información de la liquidación de sueldo.")
