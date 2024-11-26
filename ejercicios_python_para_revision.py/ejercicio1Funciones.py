#1. Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
a = int(input('Dime cual será el primer número '))
b = int(input('Dime cual será el segundo número '))
c = int(input('Dime cual será el tercer número '))
def max_de_tres(a,b,c):
    if a > b and a > c:
        print(f'El número màs grande es el {a}')
    elif b > a and b > c:
        print(f'El número màs grande es el {b}')
    elif c > a and c > b:
        print(f'El número màs grande es el {c}')
    elif a == b and c == b:
        print('los 3 son iguales')
    else:
        print('No se que has hecho animal')

max_de_tres(a,b,c)