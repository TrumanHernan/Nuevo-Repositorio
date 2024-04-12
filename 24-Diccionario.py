# 24-Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

diccionario = {'dollar':'$', 'euro':'€', 'yen':'¥'}
print (diccionario)
opcion = input("Introduce una divisa: ")

#La instrucción match evalúa la variable opcion después de convertirla a minúsculas (para hacer la comparación insensible a mayúsculas/minúsculas) y la compara con varios casos posibles: "dollar", "euro" y "yen". Si la variable coincide con alguno de los casos, se imprime el símbolo de la divisa correspondiente. Si no coincide con ninguno de los casos, se imprime un mensaje de aviso.
match opcion.lower():

    case "dollar":
        print(diccionario['dollar'])
    case "euro":
        print(diccionario['euro'])
    case "yen":
        print(diccionario['yen'])
    case _:
        print("No se encuentra la divisa")
        
    # El programa guarda un diccionario con las divisas y sus símbolos, después pregunta al usuario por una divisa y muestra su símbolo o un mensaje de aviso si la divisa no está en el diccionario. con el uso de la instruccion match  (introducida en Python 3.10) para el manejo de casos, similar a un switch en otros lenguajes de programación.