# 05- Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

edad = int(input("Ingrese su edad: "))
ingresos = float(input("Ingrese sus ingresos mensuales: "))

mensaje = "Tienes que tributar." if edad > 16 and ingresos >= 1000 else "No tienes que tributar."

print(mensaje)

# Mejora del codigo con el operador ternario haciendo el codigo mas corto.  