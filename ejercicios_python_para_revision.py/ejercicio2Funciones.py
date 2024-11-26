#2. Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
vocales=['a','e','i','o','u']
letra = input('Dime una letra y yo te diré si es una vocal ')
def vocal_o_no(letra):
    if letra in vocales:
        print('Es una vocal')
    else:
        print('Eso no es una vocal')

vocal_o_no(letra)