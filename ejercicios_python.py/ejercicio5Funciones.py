#5. Escribir dos funciones que permitan calcular: La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
#La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
#Escribe un programa principal con un menú donde se pueda elegir la opción de
#convertir a segundos, convertir a horas, minutos y segundos o salir del programa.

def segundos_a_resto ():
    segundos = input(int(print('Dime el numero de segundos a tranformar: ')))
    pr_segundos = segundos
    pr_minutos = segundos/60
    pr_horas = segundos/3600
    print(f'Los segundos proporcionados són equivalentes a {pr_segundos} segundos, {pr_minutos} minutos y {pr_horas} horas')

def