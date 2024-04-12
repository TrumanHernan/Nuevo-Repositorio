# 21-Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

loteria = []

a = float(input("Introduce un número: "))
b = float(input("Introduce otro número: "))
c = float(input("Introduce otro número: "))
d = float(input("Introduce otro número: "))
e = float(input("Introduce otro número: "))

loteria.append(a)
loteria.append(b)
loteria.append(c)
loteria.append(d)
loteria.append(e)

loteria.sort()
  
print(loteria)

# EXPLICACION DEL CODIGO
# Solicita al usuario que ingrese cinco números, los agrega a una lista llamada loteria con el metodo append(), ordena la lista en orden ascendente con el metodo sort() y luego imprime la lista ordenada.

print("\n---Codigo mejorado de Continue---\n")

# Aquí hay una versión mejorada del código que utiliza un bucle para solicitar los números y agregarlos a la lista, lo que reduce la repetición del código. Además, he agregado comentarios en español y explicaciones:

# Crea una lista vacía llamada 'loteria'
loteria = []

# Utiliza un bucle para pedir al usuario que introduzca cinco números
for i in range(5):
    # Solicita al usuario un número y lo convierte a float antes de agregarlo a la lista 'loteria'
    numero = float(input(f"Introduce el número {i+1}: "))
    loteria.append(numero)

# Ordena la lista 'loteria' en orden ascendente
loteria.sort()

# Imprime la lista 'loteria' ordenada
print("Los números de la lotería ordenados son:", loteria)
