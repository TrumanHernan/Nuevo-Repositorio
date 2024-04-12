# 28-Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

diccionario_vacio = {}

# nombre, edad, sexo, teléfono, correo electrónico,
nombre = input("Escriba su nombre: ")
edad =int(input("Escriba su edad: "))
sexo = input("Escriba su sexo: ")
telefono =int(input("Escriba su teléfono: "))
correo = input("Escriba su correo: ")

# MANERAS DE AGREGAR CLAVE-VALOR A UN DICCIONARIO
diccionario_vacio.update({'nombre': nombre, 'edad': edad, 'sexo': sexo, 'telefono': telefono, 'correo': correo})

diccionario_vacio['nombre'] = nombre
diccionario_vacio['edad'] = edad
diccionario_vacio['sexo'] = sexo
diccionario_vacio['telefono'] = telefono
diccionario_vacio['correo'] = correo

print(diccionario_vacio)

# EXPLICACION DEL PROGRAMA
"""
Este programa en Python comienza creando un diccionario vacío llamado diccionario_vacio. Luego, solicita al usuario que ingrese su información personal: nombre, edad, sexo, teléfono y correo electrónico, y guarda estas entradas en variables.

Después, el programa muestra dos maneras diferentes de agregar pares clave-valor al diccionario vacío:

Utilizando el método update(), que toma un diccionario como argumento y agrega los pares clave-valor de ese diccionario al diccionario_vacio. En este caso, se crea un diccionario con las claves 'nombre', 'edad', 'sexo', 'telefono' y 'correo', y se les asignan los valores correspondientes ingresados por el usuario.

Asignando valores directamente a las claves utilizando la sintaxis de corchetes []. El programa asigna cada valor ingresado por el usuario a su respectiva clave en el diccionario_vacio. Esto sobrescribe los valores que se agregaron previamente con el método update().

Finalmente, el programa imprime el diccionario_vacio con todos los pares clave-valor agregados.

Es importante notar que, debido a que el programa utiliza ambas maneras de agregar contenido al diccionario, la segunda manera (usando la sintaxis de corchetes) sobrescribirá cualquier dato que se haya agregado con el método update(). Esto significa que al final del programa, el diccionario contendrá la información ingresada por el usuario, pero los pares clave-valor habrán sido agregados dos veces, la segunda sobrescribiendo a la primera.
"""

