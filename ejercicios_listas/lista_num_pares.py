n=int(input('Digame un número: '))
lista=[]

for i in range(1,n+1):
    if i%2==0:
        lista.append(i)
print(f'{lista}')