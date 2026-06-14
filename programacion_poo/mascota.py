class Mascota:
    
    def __init__(self, nombre, especie, edad):
        # Atributos (Datos del objeto)
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def mostrar_informacion(self):
        """Método para mostrar los atributos del objeto."""
        print(f"Nombre: {self.nombre} | Especie: {self.especie} | Edad: {self.edad} años")

    def hacer_sonido(self):
        """Método que simula el sonido según la especie (Abstracción)."""
        especie_clean = self.especie.lower()
        if "perro" in especie_clean:
            print(f"{self.nombre} dice: ¡Guau guau!")
        elif "gato" in especie_clean:
            print(f"{self.nombre} dice: ¡Miau miau!")
        else:
            print(f"{self.nombre} hace un sonido nativo de su especie.")