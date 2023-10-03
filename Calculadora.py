#primer numero
n1 = int(input("Dame un numero: "))
print(n1)

#segundo numero
n2 = int(input("Dame otro numero: "))
print(n2)

print("¿Qué quieres hacer")
print("1---Sumar")
print("2---Restar")
print("3---Multiplicar")
print("4---Dividir")

operacion = input()

salida = "El resultado es {}"

#SUMA modificada
if operacion == "Sumar" or operacion == "sumar" or operacion == "1" :
    print(salida.format(int(n1+n2)))

#RESTA
if operacion == "Restar" or operacion == "restar" or operacion == "2" :
    print(salida.format(int(n1-n2)))

#MULTIPLICACIÓN
if operacion == "Multiplicar" or operacion == "multiplicar" or operacion == "3" :
    print(salida.format(int(n1*n2)))

#DIVISIÓN
if operacion == "Dividir" or operacion == "dividir" or operacion == "4" :
    print(salida.format(int(n1/n2)))
