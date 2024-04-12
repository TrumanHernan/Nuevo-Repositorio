# 04-Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

numero = int(input("Ingrese un número entero: "))
if numero % 2 != 0:
    print("El número es impar.")
else:
    print("El número es par.")
    
# EXPLICACION DEL OPERADOR MODULO
# el operador modulo % se utiliza para obtener el residuo de una division, en este caso se utiliza para determinar si un numero es par o impar, ya que si el residuo de la division de un numero entre 2 es distinto a 0, entonces el numero es impar, de lo contrario es par.