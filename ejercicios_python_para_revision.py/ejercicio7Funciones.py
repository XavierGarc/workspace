# Función para calcular el MCD usando el método de Euclides 

def calcular_mcd(numero_mayor, numero_menor): 
    while numero_menor != 0: 
        resto = numero_mayor % numero_menor 
        numero_mayor, numero_menor = numero_menor, resto 
    print(f"El MCD es: {numero_mayor}") 
print("Cálculo del MCD (Máximo Común Divisor)") 
primer_numero = int(input("Introduce el primer número: ")) 
segundo_numero = int(input("Introduce el segundo número: ")) 
if primer_numero > 0 and segundo_numero > 0: 
    if primer_numero < segundo_numero: 
        primer_numero, segundo_numero = segundo_numero, primer_numero  
    calcular_mcd(primer_numero, segundo_numero) 
else: 
    print("Por favor, introduce números enteros.") 