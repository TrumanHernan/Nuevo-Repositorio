# 20-Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.



# Crea una lista con nombres de asignaturas escolares
asignatura = ["matematicas", "fisica", "quimica", "historia", "lengua"]

# pedimos al usuario que ingrese cada una de las notas de cada asignatura accediendo a ellas mediante su indice que empieza desde 0 y guardamos cada nota en una variable
n1 =float(input(f"tu nota en {asignatura[0]}: "))
n2 =float(input(f"tu nota en {asignatura[1]}: "))
n3 =float(input(f"tu nota en {asignatura[2]}: "))
n4 =float(input(f"tu nota en {asignatura[3]}: "))
n5 =float(input(f"tu nota en {asignatura[4]}: "))

print("----------------------------------------------------------------")

# imprimimos un mensaje con el nombre de la asignatura igualmente accediendo a ellas mediante su indice. y la nota que el usuario ingreso guardada en sus respectivas las variables
print(f"Tu nota en {asignatura[0]} es: {n1}")
print(f"Tu nota en {asignatura[1]} es: {n2}")
print(f"Tu nota en {asignatura[2]} es: {n3}")
print(f"Tu nota en {asignatura[3]} es: {n4}")
print(f"Tu nota en {asignatura[4]} es: {n5}")