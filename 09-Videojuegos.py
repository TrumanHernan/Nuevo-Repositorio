# 09-Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

edad = int(input("ingresa tu edad: "))
if edad >= 0 and edad < 4:
    print("Puedes entrar gratis.")
elif edad > 3 and edad < 19:
    print("Debes pagar 5€.")
elif edad > 18:
    print("Debes pagar 10€.")
else:
    print("Edad no valida.")
    
# EXPLICACION DEL CODIGO
# El programa solicita al usuario que ingrese su edad y luego muestra el precio de la entrada correspondiente. Si el cliente tiene menos de 4 años, puede entrar gratis. Si tiene entre 4 y 18 años, debe pagar
