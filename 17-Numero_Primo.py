# 17-Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

# Forma 1 con el ciclo while
n = int(input("Introduce un número entero positivo mayor que 2: "))
i = 2
while n % i != 0:
    i += 1
if i == n:
    print(str(n) + " es primo")
else:
    print(str(n) + " no es primo")

# Forma 2 con el ciclo for
n = int(input("Introduce un número entero positivo mayor que 2: "))
for i in range(2, n):
    if n % i == 0:
        break
if (i + 1)  == n:
    print(str(n) + " es primo")
else: 
    print(str(n) + " no es primo")
    
# EXPLICACION DEL CODIGO
# En ambas formas, el programa determina si el número ingresado por el usuario es primo verificando si tiene divisores distintos de 1 y de sí mismo.