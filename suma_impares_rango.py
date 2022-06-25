min = int(input("Ingrese el numero inicial: "))
max = int(input("Ingrese el numero final: "))


suma = 0


print("Los numeros impares en el rango ingresado es:\n")
while min <= max:
    if min % 2 == 1: #El codigo es igual que el de generador de pares... pero cambiamos de 0 a 1 para diferenciar entre pares e impares.
        print(min, end=',')
        suma = suma + min
    min+=1

print("\n\n\nEl resultado de la suma de los numeros impares es: {}".format(suma))
