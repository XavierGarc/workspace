# Proyecto sobre estructuras de datos en python: Listas, tuplas, diccionarios y conjuntos 
# Sistema de Bases de Datos para almacenar información de usuarios
# En este proyecto usarás listas y diccionarios
# Partiremos de la definición del diccionario para almacenar la base de datos (usuarios).
# De cada usuario se guardará su apellido y 4 campos: nombre, ocupacion, aficiones y edad

#Empieza definiendo el diccionario "usuarios"
usuarios = {
    'Rovira':{
                'nombre':'Xavier',
                'ocupacion':'Estudiante',
                'aficiones':['salir','Videojuegos','Mates'],
                'edad': 17
    }
}

# A continuación habrá un bucle en donde se evalúe la entrada del usuario 
# Dentro del bucle se le darán al usuario 4 opciones: listar usuarios, añadir un usuario, borrar un usuario, buscar un usuario
# Dependiendo de lo que conteste el usuario se hará lo que dice esa opción.

while True:
    elige_opcion = input("1 - listar usuarios, 2 - añadir un usuario, 3 - borrar un usuario, 4 - buscar un usuario, 5 - guardar en un fichero, 6 - salir: ")
    match elige_opcion:
        case '1':
            print('Listado de todos los usuarios: ')
            for clave,valor in usuarios.items():
                 print(f'{clave}: {valor}')
            print()
        case '2':
            apellido = input('Introduce el apellido: ')
            if apellido in usuarios:
                print('El usuario ya existe.\n')
            else:
                nombre = input('Introduce el nombre: ')
                ocupación = input('Introduce la ocupación: ')
                aficiones = input('Introduce las aficiones separados por comas: ').split(',')
                edad = int(input('Introduce la edad: '))
                usuarios[apellido] = {
                    'nombre': nombre,
                    'ocupacion': ocupación,
                    'aficiones': aficiones,
                    'edad': edad
                }
        case '3':
            print('Estos són los usuarios: ')
            print(f'{usuarios}')
            nombre_borrado  = input('Cual deseas eliminar? ')
            if nombre_borrado in usuarios:
                del usuarios[nombre_borrado]
                print(f'Se ha eliminado al usuario {apellido}\n')
            else:
                print('Ese usuario no existe')
        case '4':
            buscar = input('Que usuario quieres buscar?: ')
            if buscar in usuarios:
                print(f'Estos son los datos del usuario {buscar}:')
                print(f'{usuarios[buscar]}')
            else:
                print('Ese usuario no existe')
        case '5':
            with open('ejercicios_ficheros/usuarios.dat', 'w') as f:
                for clave,valor in usuarios.items():
                    f.write(clave + '\n')
                    f.write(str(valor)+'\n')
        case '6':
            break