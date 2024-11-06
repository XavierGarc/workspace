#En este ejercicio crearemos una lista que ordene los elementos por orden alfabetico
elementos_lista = int(input('Cuantos elementos tendra nuestra lista? '))
numero = 0
lista = []
while numero != elementos_lista:
    lista = int(input('Introduce uno de los elementos de la lista: '))
    elementos_lista = elementos_lista-1
print(sorted(lista))