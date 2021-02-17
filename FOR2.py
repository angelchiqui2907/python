#MOSTRAR NÚMEROS PARES DE 1 A 100

for contador in range(1, 101):
    div=(contador%2)
    if div == 0:
        print("Hola asir", contador)
    
print("fin de programa")


#MOSTRAR NÚMEROS POSITIVOS Y NEGATIVOS DE UN RANGO QUE EL USUARIO INTRODUCE

num1=int(input("Escribe un numero de inicio: "))
num2=int(input("Escribe un numero de final: "))

for contador in range(num1, num2+1):
    if contador > 0:
        print(contador ,"es positivo")
    elif contador < 0:
        print(contador ,"es negativo")
print("fin de programa")


#ALGORITMO QUE MUESTRE LA TABLA DE MULTIPLICAR DE TODOS LOS NUMEROS DEL 1 AL 10

for contador in range(1, 11):
    for multi in range (1,11):
        multi2=(contador*multi)
        print (contador,"*",multi,"=",multi2)
print("fin de programa")