# 25- Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

nombre = input("Escriba su nombre: ")
edad =int(input("Escriba su edad: "))
direccion = input("Escriba su dirección: ")
telefono =int(input("Escriba su teléfono: "))

informacion = {'nombre': nombre, 'edad': edad, 'direccion': direccion, 'telefono': telefono}

print(f"{nombre} Tiene {edad} Años, vive en {direccion} y su numero de telefono es {telefono}")

# EXPLICACION DEL PROGRAMA
# Solicita al usuario que ingrese su nombre, edad, dirección y teléfono, y luego almacena esa información en un diccionario llamado informacion. Finalmente, imprime un mensaje con todos los datos ingresados, formateados en una cadena de texto.

# El programa hace uso de la función input() para obtener los datos del usuario y los convierte al tipo apropiado (la edad y el teléfono se convierten a enteros con int()). Luego, estos datos se almacenan en un diccionario donde cada clave corresponde a un tipo de información (nombre, edad, dirección, teléfono). Por último, se utiliza una f-string (cadena de texto formateada) para mostrar la información de una manera legible.