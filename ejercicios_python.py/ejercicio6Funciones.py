def login(usuario, contrasena, intentos, max_intentos): 
    if usuario == "usuario1" and contrasena == "asdasd": 
        print("Login exitoso") 
        intentos = max_intentos + 1 
    else: 
        print("Nombre de usuario o contraseña incorrectos.") 
        intentos += 1 
        print(f"Intentos realizados: {intentos}/{max_intentos}") 
    return intentos 

intentos = 0 
max_intentos = 3 

while intentos < max_intentos: 
    usuario = input("Introduce el nombre del usuario: ") 
    contrasena = input("Introduce la contraseña: ") 
    intentos = login(usuario, contrasena, intentos, max_intentos) 
    if intentos > max_intentos: 
        break 

if intentos <= max_intentos: 
    print("Has superado el máximo de intentos.") 