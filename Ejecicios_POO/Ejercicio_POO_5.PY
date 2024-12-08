class Usuario:
    def __init__(self, nombre, apellido, edad, correo, ciudad):

        #Inicializa los atributos del usuario.

        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.correo = correo
        self.ciudad = ciudad
        self.intentos_inicio = 0

    def describir_usuario(self):

        #Muestra un resumen de la información del usuario.

        print(f"Perfil del usuario:")
        print(f"  Nombre: {self.nombre} {self.apellido}")
        print(f"  Edad: {self.edad}")
        print(f"  Correo: {self.correo}")
        print(f"  Ciudad: {self.ciudad}")

    def saludar_usuario(self):

        #Muestra un saludo personalizado para el usuario.

        print(f"¡Hola, {self.nombre}! Espero que tengas un gran día.")

    def incrementar_intentos_inicio(self):

        #Incrementa el número de intentos de inicio de sesión en 1.

        self.intentos_inicio += 1

    def restablecer_intentos_inicio(self):

        #Restablece el número de intentos de inicio de sesión a 0.

        self.intentos_inicio = 0

# Crear una instancia de la clase Usuario
usuario = Usuario("Ana", "Pérez", 29, "ana.perez@example.com", "Madrid")

# Incrementar intentos de inicio de sesión varias veces
usuario.incrementar_intentos_inicio()
usuario.incrementar_intentos_inicio()
usuario.incrementar_intentos_inicio()

# Mostrar el número de intentos después de incrementarlos
print(f"Número de intentos de inicio: {usuario.intentos_inicio}")

# Restablecer el número de intentos de inicio de sesión
usuario.restablecer_intentos_inicio()

# Mostrar el número de intentos después de restablecerlos
print(f"Número de intentos de inicio tras el restablecimiento: {usuario.intentos_inicio}")
