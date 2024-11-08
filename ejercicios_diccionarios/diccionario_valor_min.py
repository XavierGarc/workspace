notas = {
 'Matemáticas': 7,
 'Física': 8,
 'Historia': 9
}
minimo = 10
for i in notas:
    if i.value() < minimo:
        asignatura=i.key()
print(f'El minimo es: {minimo}')
