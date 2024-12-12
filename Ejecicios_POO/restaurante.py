from Ejercicio_POO_4 import restaurante 
# Crear una instancia de la clase
restaurante = Restaurante("El Gourmet Español", "cocina mediterránea")
# Mostrar el número inicial de clientes atendidos
restaurante.mostrar_numero_servido()
# Cambiar el valor de numero_servido y mostrarlo
restaurante.establecer_como_servido(25)
restaurante.mostrar_numero_servido()