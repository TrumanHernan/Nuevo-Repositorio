# 15-Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
n = 0
numero = int(input("Introduce un numero entero: "))
while n < 10:
    n +=1
    print(numero , " X " , n, " = ", numero * n)
    
# EXPLICACION DEL PROGRAMA
# El bucle while se repite incrementando n en cada iteración hasta que n llega a 10. En cada iteración, se imprime la correspondiente línea de la tabla de multiplicar del número ingresado por el usuario.

