#En este ejercicio crearemos una lista que ordene los elementos por orden alfabetico
cantidad=int(input('Digame cuantas palabras tendremos: '))
nom=[]
for i in range (1,cantidad+1):
    nombre=input(f'Digame la palabra {i}: ')
    nom.append(nombre)
print(f'La lista creada es {nom}')
print(f'La lista ordenada es : {sorted(nom)}')