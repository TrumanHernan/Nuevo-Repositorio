"""
07-Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

Renta	Tipo impositivo
Menos de 10000€	5%
Entre 10000€ y 20000€	15%
Entre 20000€ y 35000€	20%
Entre 35000€ y 60000€	30%
Más de 60000€	45%
Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
"""

renta = float(input("Ingrese su renta anual: "))

if renta < 10000:
    tipo_impositivo = 5
elif renta < 20000:
    tipo_impositivo = 15
elif renta < 35000:
    tipo_impositivo = 20
elif renta < 60000:
    tipo_impositivo = 30
else:
    tipo_impositivo = 45

print("El tipo impositivo que le corresponde es:", tipo_impositivo, "%")

# otra forma de hacerlo es usando la condicional match

renta = float(input("Ingrese su renta anual: "))

match renta:
    case renta if renta < 10000:
        tipo_impositivo = 5
    case renta if renta < 20000:
        tipo_impositivo = 15
    case renta if renta < 35000:
        tipo_impositivo = 20
    case renta if renta < 60000:
        tipo_impositivo = 30
    case _:
        tipo_impositivo = 45

print("El tipo impositivo que le corresponde es:", tipo_impositivo, "%")
