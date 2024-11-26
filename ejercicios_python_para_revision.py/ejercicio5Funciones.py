# Función para convertir horas, minutos y segundos a segundos 
def convertir_a_segundos(horas, minutos, segundos): 
    segundos_totales = horas * 3600 + minutos * 60 + segundos 
    print(f"El tiempo total en segundos es: {segundos_totales}") 
 
# Función para convertir segundos a horas, minutos y segundos 

def convertir_a_hms(segundos): 
    horas = segundos // 3600 
    segundos_restantes = segundos % 3600 
    minutos = segundos_restantes // 60 
    segundos_finales = segundos_restantes % 60 
    print(f"El tiempo es: {horas} horas, {minutos} minutos y {segundos_finales} segundos") 

while True: 
    print("Menú:") 
    print("1. Convertir a segundos") 
    print("2. Convertir a horas, minutos y segundos") 
    print("3. Salir") 
    opcion = input("Elige una opción: ") 
     
    if opcion == "1": 
        horas = int(input("Introduce las horas: ")) 
        minutos = int(input("Introduce los minutos: ")) 
        segundos = int(input("Introduce los segundos: ")) 
        convertir_a_segundos(horas, minutos, segundos) 

    elif opcion == "2": 
        segundos = int(input("Introduce el tiempo en segundos: ")) 
        convertir_a_hms(segundos) 

    elif opcion == "3": 
        print("Adiós") 
        break 

    else: 
        print("Opción no válida. Intentalo de nuevo. >:( )") 