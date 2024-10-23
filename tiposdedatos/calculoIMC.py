#Este programa calcula el IMC (indice de masa personal) de cada persona
peso=float(input('Introduce tu peso en Kg'))
altura=float(input('Introduce tu altura en m'))
IMC=round(peso/(altura**2),2)
print(f'Tu IMC sera de {IMC}')
if (IMC>=30):
    print("Tienes obesidad")
else:
    if (IMC>=25):
        print("Tienes sobrepeso")
    else: 
        if (18.5<=IMC<=24.9):
            print("Tienes un indice de masa corporal normal")
        else:
            print("Tienes insuficiencia ponderal")