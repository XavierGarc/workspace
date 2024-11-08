trabajadores = {
"nombre": "Susana",
"edad": 26,
"salario": 1500,
"ciudad": "Vinaroz"
}
print('Vamos a eliminar nombre y salario:')
del trabajadores['nombre']
del trabajadores['salario']
print(f'Ahora la lista es {trabajadores}')