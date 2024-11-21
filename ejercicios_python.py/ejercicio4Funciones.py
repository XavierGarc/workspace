#4. Diseñar una función que calcule el área y el perímetro de una circunferencia. Utiliza dicha función en un programa principal que lea el radio de una circunferencia y muestre su área y perímetro.

radio = int(input('Dime el radio de la circumferencia: '))
π = 3.14

def calculo_magnitudes(radio):
    perimetro = 2*π*radio
    area = 2*π*(radio)**2
    print(f'El perimetro será igual a {perimetro} y el area será igual a {area}')

calculo_magnitudes(radio)