want_greet = 'S'  # importante dar un valor inicial
MAX_GREETS = 4
num_greets = 0
while want_greet == 'S':
    print('Hola qué tal! ;)')
    num_greets +=1
    if num_greets == MAX_GREETS:
        print('Pesao')
        break
    want_greet = input('¿Quiere otro saludo? [S/N] ')
    if not want_greet == 'S' or 'N' :
        want_greet = 'S'
    else:
        while want_greet == 'S':
            print('Hola qué tal! ;)')
            num_greets +=1
    want_greet = input('¿Quiere otro saludo? [S/N] ')
        
print('Que tenga un buen día')