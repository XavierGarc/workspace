def leer_fecha(dia, mes, año): 

    dia = int(input("Introduce el día: ")) 
    mes = int(input("Introduce el mes: ")) 
    año = int(input("Introduce el año: ")) 

def es_bisiesto(año, bisiesto): 

    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0): 

        bisiesto = True 
    else: 
        bisiesto = False 
def dias_del_mes(mes, año, bisiesto, dias_mes): 

    if mes == 2: 
        if bisiesto: 
            dias_mes = 29 
        else: 
            dias_mes = 28 
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11: 
        dias_mes = 30 
    else: 
        dias_mes = 31 

def calcular_dia_juliano(dia, mes, año, bisiesto, dia_juliano): 
    dia_juliano = dia 
    for mes_anterior in range(1, mes): 
        dias_mes = dias_del_mes(mes_anterior, año, bisiesto, dias_mes) 
        dia_juliano += dias_mes 

print("Cálculo del Día Juliano") 
dia, mes, año = leer_fecha() 
bisiesto = es_bisiesto(año, False) 
dias_mes = dias_del_mes(mes, año, bisiesto) 
if 1 <= mes <= 12 and 1 <= dia <= dias_mes:   
    dia_juliano = 0 
    dia_juliano = calcular_dia_juliano(dia, mes, año, bisiesto, dia_juliano) 
    print(f"El día juliano de la fecha {dia}/{mes}/{año} es: {dia_juliano}") 
else: 
    print("La fecha introducida no es valida.")