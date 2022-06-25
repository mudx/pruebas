
# Funcion que recibe un parametro y Genera n pares segun lo introducido por el usuario

def pairs_generator(n):
    pairs = []
    counter = 0
    number = 0

    while counter < n:
        if number % 2 == 0:
            pairs.append(number)
            counter += 1
        number += 1
    return pairs

n = int(input("Ingrese los numeros pares a generar: "))
if n > 0:
    pairs = pairs_generator(n)
    print(pairs)
    print('cantidad de pares: ', len(pairs))
else:
    print('El numero debe ser positivo')
