"""
08-En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

Nivel	Puntuación
Inaceptable	0.0
Aceptable	0.4
Meritorio	0.6 o más
Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.
"""



dinero = 2.400
nombre = input("Ingrese el nombre del empleado: ")
puntos = float(input("Ingrese la puntuación del empleado: "))

if puntos == 0.0:
    nivel = "Inaceptable"
    cantidad = 0.00
elif puntos == 0.4:
    nivel = "Aceptable"
    cantidad = dinero * puntos
elif puntos >= 0.6:
    nivel = "Meritorio"
    cantidad = dinero * puntos
else:
    nivel = "Puntuación inválida"
    cantidad = 0.00

print(f"{nombre} Su nivel de rendimiento es: {nivel}")
print(f"{nombre} Su cantidad de dinero recibida: {float(cantidad)} €")

# EXPLICACION DEL PROGRAMA 
# Se pide al usuario que ingrese el nombre del empleado y la puntuación obtenida por el empleado.
# Se define una variable dinero con un valor de 2.400 y este se multiplica por la puntuación obtenida por el empleado. y es el resultado de nuestro programa.