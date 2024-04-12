# 13-Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

n = 0
numero = int(input("Introduce un numero entero: "))
while n < numero:
    n+=1
    if n % 2 == 0:
        continue
    print(n, end=",")
    
# EXPLICACION DEL CODIGO
# inicializamos variable n en 0 que se va ir incrementando en 1 en 1 cada vez que el ciclo se repite y pedimos el numero a introducir por el usuario
# con el ciclo while decimos que se repita mientras n sea menor al numero introducido por pantalla
# luego mediante una condicion decimos que si n encuentra un numero par continue osea omita los numeros pares y continue con la salida en este caso solo mostraria numeros los impares
# por ultimo mediante print(n, end=",")imprimimos por la consola el resultado...  
# end="," esta parte del codigo sirve para poder imprimirlo de manera horizontal ya que python esta determinado de manera vertical


    
    