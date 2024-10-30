#Programa que nos dirá el numero mas pequeño, el mas grande y la media de todos los introducidos
numeros=int(input('Introduce con cuantos numeros vamos a trabajar:'))
numero=int(input(f'Dime el numero 1: '))
menor = numero
mayor = numero
suma = numero
for i in range(2, numeros+1):
    numero = int(input(f'Dime el numero {i}: '))
    suma += numero
    if numero > mayor:
        mayor=numero
    elif numero < menor:
        menor = numero

print(f'El numero mas pequeño es: {menor}')
print(f'El numero mas pequeño es: {mayor}')
print(f'La media es: {suma/numeros}')
