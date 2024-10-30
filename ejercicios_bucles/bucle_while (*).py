#Este programa adivinará un numero, nos pedira un rango y irá diciendo si es mayor o menor
import random
valor_minimo = int(input('Introduce el valor mínimo: '))
valor_maximo = int(input('Introduce el valor máximo: '))
secreto = random.radint(valor_minimo,valor_maximo)
print(f'A ver si adivinas un numero entre {valor_minimo} y {valor_maximo}')
intento = 1
num_intento = int(input('Dime un numero: '))
if num_intento == secreto:
    print('¡Felicidades, has acertado el numero!')
    print('Solo te ha costado {intento} intentos')
elif num_intento < secreto:
    print('Uf,prueba con un numero mas grande')
    intento = intento+1
else:
    print('Alaa, prueba con un numero mas pequeño')
    intento = intento+1
