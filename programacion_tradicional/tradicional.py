def registrar_mascota():
    """Función para solicitar los datos de la mascota por teclado."""
    print("--- Registro de Mascota (Programación Tradicional) ---")
    nombre = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie (ej. Perro, Gato): ")
    edad = int(input("Ingrese la edad de la mascota: "))
    
    # Retornamos los datos agrupados en un diccionario
    return {
        "nombre": nombre,
        "especie": especie,
        "edad": edad
    }

def mostrar_informacion(mascota):
    """Función para mostrar la información organizada de la mascota."""
    print("\n--- Información de la Mascota ---")
    print(f"Nombre:  {mascota['nombre']}")
    print(f"Especie: {mascota['especie']}")
    print(f"Edad:    {mascota['edad']} años")

# Flujo principal del programa
if __name__ == "__main__":
    # Registramos la mascota y guardamos el diccionario retornado en una variable
    nueva_mascota = registrar_mascota()
    
    # Pasamos la variable como argumento a la función de visualización
    mostrar_informacion(nueva_mascota)