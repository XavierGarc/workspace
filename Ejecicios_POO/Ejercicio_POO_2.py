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

# Crear tres instancias de la clase
restaurante1 = Restaurante("La Parrilla Andaluza", "cocina andaluza")
restaurante2 = Restaurante("Pasta & Pizza", "cocina italiana")
restaurante3 = Restaurante("Sushi Zen", "cocina japonesa")

# Llamar al método describir_restaurante para cada instancia
restaurante1.describir_restaurante()
restaurante2.describir_restaurante()
restaurante3.describir_restaurante()