# 01-Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

# Mejora del codigo con el operador ternario.  
edad = int(input("Ingrese su edad: "))
mensaje = "Eres mayor de edad." if edad >= 18 else "Eres menor de edad."
print(mensaje)
