#Este programa contentdrá una lista, nos pedirá un elemento de esta y eliminará ese elemento
numero_elementos = int(input('Dime cuantos elementos tendrá nuestra lista: '))
lista = []
for i in range (1,numero_elementos+1):
    palabra = input(f'Digame la palabra {i}: ')
    lista.append(palabra)
print(f'La lista creada es: {lista}')
eliminar = input('Palabra a eliminar: ')
while eliminar in lista:
    lista.remove(eliminar)
print(f'La lista ahora es: {lista}')