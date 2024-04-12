"""
 26-Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

Fruta	Precio
Plátano	1.35
Manzana	0.80
Pera	0.85
Naranja	0.70
"""

frutas = {'platano':'1.35', 'manzana':'0.80', 'pera':'0.85', 'naranja':'0.70'}
print(frutas,"\n")
op = input("Elige una fruta: ")
kilos = float(input("Cuantos kilos: "))

if op == 'platano':
    precio = float(frutas['platano'])*kilos
    print(f"el precio de {kilos} kilos de {op} es de {precio}")

elif op == 'manzana':
    precio = float(frutas['manzana'])*kilos
    print(f"el precio de {kilos} kilos de {op} es de {precio}")

elif op == 'pera':
    precio = float(frutas['pera'])*kilos
    print(f"el precio de {kilos} kilos de {op} es de {precio}")

elif op == 'naranja':
    precio = float(frutas['naranja'])*kilos
    print(f"el precio de {kilos} kilos de {op} es de {precio}")
    
else:
    print("La fruta no esta entre las opciones")
    
# EXPLICACION DEL PROGRAMA
# Este programa en Python permite al usuario calcular el precio de una cantidad de frutas seleccionada. Primero, se define un diccionario frutas que contiene el nombre de distintas frutas como claves y sus precios por kilo como valores. El programa muestra este diccionario al usuario.

# Luego, el usuario debe elegir una fruta ingresando su nombre y la cantidad de kilos que desea comprar. El programa recoge estos datos a través de la función input() y los almacena en las variables op (para la fruta) y kilos (para la cantidad), respectivamente.

# A continuación, el programa utiliza una serie de condicionales if y elif para verificar qué fruta ha elegido el usuario. Dependiendo de la elección, se calcula el precio multiplicando el precio por kilo (obtenido del diccionario) por la cantidad de kilos ingresada. El resultado se imprime en pantalla con un mensaje que indica el precio total de la compra.

# Si el usuario ingresa una fruta que no está en el diccionario, el programa ejecutará el bloque else y mostrará el mensaje "La fruta no está entre las opciones".

# Este programa es un ejemplo simple de cómo utilizar diccionarios y condicionales para procesar la entrada del usuario y proporcionar una salida basada en esa entrada.
