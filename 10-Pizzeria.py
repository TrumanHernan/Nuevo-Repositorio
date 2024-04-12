"""
10-La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva. 
"""

pizza = input("quieres una pizza vegetariana o no vegetariana: ").lower()

if pizza == "vegetariana":
    ingredientes = ["mozzarella", "tomate", "Pimiento", "tofu"]
    print(f"La opcion eligida a sido: {pizza} y los ingredientes son: {ingredientes}")
elif pizza == "no vegetariana":
    ingredientes = ["mozzarella", "tomate", "Peperoni", "jamón", "salmón"]
    print(f"La opcion eligida a sido: {pizza} y los ingredientes son: {ingredientes}")
else:
    print("ERROR!!! escribe correctamente la opcion a eligir.")
    
# EXPLICACION DEL PROGRAMA:
# El programa solicita al usuario que elija entre una pizza vegetariana o no vegetariana. depende de la eleccion se muestra la pizza elegida y los ingredientes que lleva.
# Si el usuario no elige ninguna de las dos opciones, se muestra un mensaje de error.
# y tenenemos el formato de la cadena de caracteres f"{}" para mostrar el mensaje de salida. en lugar de tener que concatenar las cadenas de caracteres utilizando la coma y de esta manera sea un codigo mas legible.  
# tenemos el metodo lower() para convertir la cadena de caracteres en minusculas y asi no importa si el usuario ingresa la opcion en mayusculas o minusculas.
