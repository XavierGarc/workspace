class Restaurante:
    def __init__(self, nombre_restaurante, tipo_cocina):

        #Inicializa el nombre del restaurante y el tipo de cocina.
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina

    def describir_restaurante(self):

         #Muestra la información sobre el restaurante.

        print(f"El restaurante '{self.nombre_restaurante}' ofrece una cocina de tipo '{self.tipo_cocina}'.")

    def abrir_restaurante(self):

        #Muestra un mensaje indicando que el restaurante está abierto.

        print(f"El restaurante '{self.nombre_restaurante}' está abierto!")

# Crear una instancia de la clase
restaurante = Restaurante("El Gourmet Español", "cocina mediterránea")

# Llamar a los métodos
restaurante.describir_restaurante()
restaurante.abrir_restaurante()