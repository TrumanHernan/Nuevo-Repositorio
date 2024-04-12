# 16-Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
contraseña = "truman"

while  True:
    eleccion = input("Introduce la contraseña: ").lower()
    if eleccion == contraseña:
        print("Contraseña correcta")
        break
    else:
        print("Contraseña incorrecta")
      
    
# EXPLICACION DEL CODIGO
# el programa le pide al usuario que ingrese una contraseña y verifica si coincide con la contraseña preestablecida. Si la contraseña es incorrecta, le informa al usuario y le pide que vuelva a intentarlo. Si la contraseña es correcta, el programa informa al usuario y termina.
    
