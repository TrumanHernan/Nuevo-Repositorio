# 06-Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

nombre = input("Ingrese su nombre: ").upper() 
sexo = input("Ingrese su sexo (M/F): ").upper() 

if (sexo == "M" and nombre < "M") or (sexo == "F" and nombre > "N"):
    grupo = "A"
else:
    grupo = "B"

print("Usted pertenece al grupo", grupo)

# EXPLICACION DEL METODO UPPER()
# Convierte el nombre y el sexo a mayúsculas para que no sea sensibles a minisculas.  
# y asi mejoramos el programa



