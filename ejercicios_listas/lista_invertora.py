#Este programa creará una lista, nos nombrará la lista normal y su versión invertida
numero_elementos = int(input('Dime cuantos elementos tendrá nuestra lista: '))
lista = []
lista_invertida = []
for i in range (1,numero_elementos+1):
    palabra = input(f'Digame la palabra {i}: ')
    lista.append(palabra)
    for i in range (numero_elementos, 0, -1):
        lista_invertida.append(palabra)
print(f'La lista creada es: {lista}')
print(f'La lista invertida es: {lista_invertida}')