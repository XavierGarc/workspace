#Ejercicio para crear un rectangulo con asteriscos
altura = int(input('Introduce la altura: '))
anchura = int(input('Introduce la anchura: '))
for i in range(altura):
    for j in range(anchura):
        print('*',end=' ')
    print()