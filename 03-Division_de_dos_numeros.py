# 03-Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    print("la division de los dos numeros es: ", num1 / num2)
    
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
    
finally:
    print("estoy usando el manejo de excepciones para evitar errores.")