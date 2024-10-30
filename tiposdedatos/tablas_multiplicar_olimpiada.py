#Programa que decideix si un numero és prim o no i que calcule un nombre de primers consecutius
t = int(input('Indica el nombre de casos que cal processar: '))
for i in range (0,t):
    k = int(input('Introdueix un nombre entre 0 i 100: '))
    n = int(input('Introdueix un nombre sencer entre 1 i 100000: '))
    if k == 0:
        if (n % 2 == 0):
            print('NO')
        else:
            print('SI')