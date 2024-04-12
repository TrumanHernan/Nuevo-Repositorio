# 30-Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.

def nombre():
    nombre = input("Escribe tu nombre: ")
    return nombre

funcion = nombre()
print(f"¡Hola {funcion}!")

# EXPLICACION DEL PROGRAMA
# El programa solicita al usuario que ingrese su nombre, lo almacena y luego imprime un saludo personalizado con ese nombre.

# manera alternativa CONTINUE
# Definimos una función que imprime un saludo personalizado
def saludar():
    # Pedimos al usuario que ingrese su nombre
    nombre_usuario = input("Escribe tu nombre: ")
    # Imprimimos el saludo con el nombre del usuario
    print(f"¡Hola {nombre_usuario}!")

# Llamamos a la función para ejecutar el saludo
saludar()

# EXPLICACION DEL PROGRAMA
# En esta versión alternativa, la función saludar se encarga de pedir el nombre del usuario y de imprimir el saludo en un solo paso, sin necesidad de devolver el nombre y usar una variable adicional fuera de la función. Esto simplifica el flujo del programa al combinar la entrada y la salida en la misma función.
