# 29-Escribir una función que muestre por pantalla el saludo ¡Hola amiga! cada vez que se la invoque.

def hola_amiga():
    return "¡Hola amiga!"
funcion = hola_amiga()
print(funcion)
print(funcion)
print(funcion)

print("-----------------------------------------")

# EXPLICACION DEL PROGRAMA
# Este programa define una función llamada hola_amiga que no toma ningún argumento y simplemente devuelve la cadena de texto "¡Hola amiga!". Luego, la función se llama y se almacena el resultado en la variable funcion. Finalmente, se imprime el contenido de la variable funcion tres veces.
# Una forma alternativa de escribir este programa podría ser:
def hola_Amiga():
    print("¡Hola amiga!")

hola_Amiga()
hola_Amiga()
hola_Amiga()

# EXPLICACION DEL PROGRAMA
# En esta versión, la función hola_amiga se encarga de imprimir el mensaje directamente cada vez que se llama, en lugar de devolverlo y luego imprimirlo desde fuera de la función. Esto elimina la necesidad de almacenar el resultado en una variable y simplifica un poco el código.