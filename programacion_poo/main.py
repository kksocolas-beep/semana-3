# Importamos la clase Mascota desde el archivo mascota.py
from mascota import Mascota

def ejecutar_sistema_poo():
    print("--- Gestión de Mascota (POO) ---\n")
    
    # Instanciación: Creamos el primer objeto de la clase Mascota
    mascota1 = Mascota("Max", "Perro", 3)
    
    # Instanciación: Creamos el segundo objeto de la clase Mascota
    mascota2 = Mascota("Luna", "Gato", 2)
    
    # Ejecución de métodos para el objeto 1
    print("Mascota 1:")
    mascota1.mostrar_informacion()
    mascota1.hacer_sonido()
    
    print("-" * 30)
    
    # Ejecución de métodos para el objeto 2
    print("Mascota 2:")
    mascota2.mostrar_informacion()
    mascota2.hacer_sonido()

if __name__ == "__main__":
    ejecutar_sistema_poo()