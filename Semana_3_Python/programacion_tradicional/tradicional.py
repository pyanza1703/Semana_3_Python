
def registrar_mascota():
  
    print("--- REGISTRO DE MASCOTA (Enfoque Tradicional) ---")
    
    
    nombre = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie (ej. Perro, Gato): ")
    edad = input("Ingrese la edad de la mascota: ")
    
    
    return nombre, especie, edad


def mostrar_mascota(nombre, especie, edad):
   
    print("\n--- INFORMACIÓN DE LA MASCOTA REGISTRADA ---")
    print(f"Nombre:  {nombre}")
    print(f"Especie: {especie}")
    print(f"Edad:    {edad} años")


def main():
    
    
    nom, esp, ed = registrar_mascota()
    
    
    mostrar_mascota(nom, esp, ed)



if __name__ == "__main__":
    main()