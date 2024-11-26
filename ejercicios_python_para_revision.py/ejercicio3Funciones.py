#3. Definir una funcion llamada histograma() que tome una lista de números enteros e imprima un histograma en la pantalla. Ejemplo: histograma([4, 9, 7]) debería imprimir lo siguiente:

def histograma(lista):
    for i in lista:
        print('*'*int(i))

lista_numeros = input('Introduce una lista de numeros separados por comas: ').split(',')

histograma(lista_numeros)