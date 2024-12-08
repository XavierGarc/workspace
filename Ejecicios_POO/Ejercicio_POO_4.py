class Restaurante:
    def __init__(self, nombre_restaurante, tipo_cocina):

        #Inicializa los atributos del restaurante.

        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina
        self.numero_servido = 0  # Valor predeterminado

    def describir_restaurante(self):

        #Muestra la información sobre el restaurante.

        print(f"El restaurante '{self.nombre_restaurante}' ofrece una cocina de tipo '{self.tipo_cocina}'.")

    def abrir_restaurante(self):

        #Muestra un mensaje indicando que el restaurante está abierto.

        print(f"El restaurante '{self.nombre_restaurante}' está abierto!")

    def mostrar_numero_servido(self):

        #Muestra el número de clientes atendidos.

        print(f"El restaurante ha servido a {self.numero_servido} clientes.")

    def establecer_como_servido(self, numero):

        #Establece un nuevo valor para el número de clientes atendidos.

        if numero >= self.numero_servido:
            self.numero_servido = numero
        else:
            print("No se puede reducir el número de clientes atendidos.")

    def incrementar_numero_servido(self, incremento):

        #Incrementa el número de clientes atendidos.

        if incremento > 0:
            self.numero_servido += incremento
        else:
            print("El incremento debe ser un número positivo.")

# Crear una instancia de la clase
restaurante = Restaurante("El Gourmet Español", "cocina mediterránea")

# Mostrar el número inicial de clientes atendidos
restaurante.mostrar_numero_servido()

# Cambiar el valor de numero_servido y mostrarlo
restaurante.establecer_como_servido(25)
restaurante.mostrar_numero_servido()
