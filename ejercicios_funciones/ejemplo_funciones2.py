def minimo(a, b):
    if a < b:
        print(f'El mínimo de {a} y {b} es {a}')
    elif b < a:
        print(f'El mínimo de {a} y {b} es {b}')
    else:
        print('Los dos números son iguales')


numero1 = int(input('Introduce el numero 1:'))
numero2 = int(input('Introduce el numero 1:'))
minimo(numero1,numero2)