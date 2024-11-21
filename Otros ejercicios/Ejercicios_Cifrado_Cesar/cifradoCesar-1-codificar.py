alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def codifica(texto,desplazam):
    texto_cifrado=''
    for letra in texto:
        position = alfabeto.index(letra)
        nueva_posicion = (position+desplazam)%27
        nueva_letra = alfabeto[nueva_posicion]
        texto_cifrado += nueva_letra
    print(f'El texto codificado es {texto_cifrado}')
def descodifica(texto,desplazam):
    texto_cifrado=''
    for letra in texto:
        position = alfabeto.index(letra)
        nueva_posicion = (position+desplazam)%27
        nueva_letra = alfabeto[nueva_posicion]
        texto_cifrado += nueva_letra
    print(f'El texto decodificado es {texto_cifrado}')
direccion = input("Escribe 'codifica' para codificar o 'decodifica' para decodificar: ")
texto = input("Escribe tu mensaje: ").lower()
desplazam = int(input("Escribe un número para el desplazamiento: "))
if direccion == 'codifica':
    codifica(texto,desplazam)
elif dirección == 'decodifica':
    decodifica(texto,desplazam)

#TODO-1: Crea una funcion llamada 'codifica' que coja el 'texto' y 'desplazamiento' como entradas.

    #TODO-2: Dentro de la función 'codifica', desplaza cada letra del 'texto' hacia adelante en el alfabeto
    # la cantidad desplazam e imprime el texto codificado.  
    #ejemplo: 
    #texto_plano = "hola"
    #desplazamiento = 5
    #texto_cifrado = "mtqf"
    #print output: "El texto codificado es mtqf"
# Ayuda: indice de una lista en Python: https://www.w3schools.com/python/ref_list_index.asp  

#TODO-3: Llama a la función codifica y pasa lo que ha introducido el usuario. 
# Deberías ser capaz de probar el código y codificar un mensaje. 
