#Este programa adivinará un numero, nos pedira un rango y irá diciendo si es mayor o menor
import random
valor_minimo = int(input('Introduce el valor mínimo: '))
valor_maximo = int(input('Introduce el valor máximo: '))
secreto = random.randint(valor_minimo,valor_maximo)
print(f'A ver si adivinas un numero entre {valor_minimo} y {valor_maximo}')
intento = 1
num_intento = int(input('Dime un numero: '))
while num_intento != secreto:
    if num_intento < secreto:
        num_intento = int(input('Uf,prueba con un numero mas grande '))
    else:
        num_intento = int(input('Uf,prueba con un numero mas pequeño '))
    intento = intento+1
print('Exacto, ese era el numero en que estaba pensando')
print(f'Y solo te ha costado {intento} intentos')