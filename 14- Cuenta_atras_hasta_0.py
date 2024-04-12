# 14-Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

numero = int(input("Introduce un numero entero:\n"))
while numero > 0:
    numero -=1
    print(numero, end = ",")
    
# EXPLICACION DEL CODIGO
# pedimos numero al usuario y decimos que mientras ese numero sea mayor a 0 se ejecute el codigo donde el numero se ira restando de 1 en 1 hasta llegar a 0 y por ultimo imprimimos por pantalla y utilizamos el codigo para que se vizualize de manera horizantal  print(numero, end = ",")