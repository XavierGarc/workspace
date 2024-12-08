class Usuario:
    def __init__(self, nombre, apellido, edad, correo, ciudad):

        #Inicializa los atributos del usuario.

        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.correo = correo
        self.ciudad = ciudad

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

# Crear varias instancias de la clase Usuario
usuario1 = Usuario("Ana", "Pérez", 29, "ana.perez@example.com", "Madrid")
usuario2 = Usuario("Carlos", "Gómez", 35, "carlos.gomez@example.com", "Barcelona")
usuario3 = Usuario("Lucía", "Fernández", 42, "lucia.fernandez@example.com", "Valencia")

# Llamar a los métodos para cada usuario
usuarios = [usuario1, usuario2, usuario3]

for usuario in usuarios:
    usuario.describir_usuario()
    usuario.saludar_usuario()
    print()  # Separador entre usuarios
