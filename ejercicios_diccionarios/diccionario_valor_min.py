notas = {
 'Matemáticas': 7,
 'Física': 8,
 'Historia': 9
}
minimo = 10
for asignatura,nota in notas:
    if nota < minimo:
        asignatura_min=asignatura
print(f'El minimo es: {asignatura_min}')
