num1 = 0
num2 = 1
n = int(input("Ingrese el numero deseado para imprimir la serie: "))
print(num1, end=', ')
print(num2, end=', ')

for i in range(n-2):
    num3 = num1 + num2
    if i == n-3:
        print(num3)
    else:
        print(num3, end=', ')
        num1=num2
        num2=num3

# La simpleza de este codigo imprime la secuencia fibonacci usando un numero ingresado por el Usuario
# Se puede realizar de muchas maneras.. para este caso yo uso el bucle "for" para iterar los numeros.
# En los otros codigos, hago uso de while para mostrar las diferencias.
