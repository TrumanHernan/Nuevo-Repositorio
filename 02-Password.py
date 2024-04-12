# 02-Escribir un programa que almacene la cadena de caracteres en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

password = "contraseña"  

user_input = input("Introduce la contraseña: ")

if user_input.lower() == password.lower():  
    print("La contraseña es correcta.")
else:
    print("La contraseña es incorrecta.")
    

# EXPLICACION DEL METODO LOWER    
# el metodo lower permite convertir la cadena de caracteres en minisculas, para que no importe si el usuario ingresa la contraseña en mayusculas o minusculas.