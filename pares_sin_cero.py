
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
    print(pairs[1:])
    print('cantidad de pares: ', len(pairs[1:])) #Aqui usando [1:] quito el cero inicial de la cadena... pero tambien corta el string... 
else:
    print('El numero debe ser positivo')
    
    
    # Este codigo no esta terminado, lamentablemente no pude quitar el 0 inicial de mi codigo sin hacer un recorte de este mismo.
    # Cuando el usuario ingresa un numero para generar los pares, ejemplo: 4,
    # el codigo en vez de mostrar 4 numeros muestra 3, ya que no encontre la forma de quitar el cero y tomar el siguiente numero de la cadena..
