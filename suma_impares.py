total = 0

num = int(input("Ingrese un numero: "))
numeros_pares = []                                    #Aqui mostramos los numeros pares que existen desde 0 a n

for i in range(0, num + 1):
    if i % 2 == 1:
        numeros_pares.append(i)
        total += i

print("El rango de numeros impares entre 0 y {} es: {}".format(num,numeros_pares))
print("La suma de los numeros impares entre 0 y {} es: {}".format(num, total))
