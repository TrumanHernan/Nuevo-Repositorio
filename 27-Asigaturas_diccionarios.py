# 27-Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.

asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5} 

print(f"La asignatura Matematicas tiene {asignaturas['Matemáticas']} créditos")
print(f"La asignatura Fisica tiene {asignaturas['Física']} créditos")
print(f"La asignatura Qumica tiene {asignaturas['Química']} créditos")

# EXPLICACION DEL PROGRAMA
# utiliza un diccionario llamado asignaturas para almacenar el número de créditos de tres materias escolares.
# Las claves del diccionario son los nombres de las asignaturas y los valores son los créditos correspondientes a cada una.
# El programa luego imprime la cantidad de créditos para cada asignatura utilizando f-strings, que permiten insertar valores de variables directamente dentro de las cadenas de texto. Se accede a los valores del diccionario mediante la sintaxis asignaturas['NombreDeLaAsignatura'], donde 'NombreDeLaAsignatura' es la clave que corresponde a la materia deseada.
#Como resultado, el programa muestra tres líneas de texto, cada una informando al usuario cuántos créditos tiene cada una de las asignaturas listadas en el diccionario. Por ejemplo, la salida para Matemáticas sería "La asignatura Matemáticas tiene 6 créditos".