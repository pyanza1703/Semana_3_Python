
from mascota import Mascota

def main():
    print("--- GESTIÓN DE MASCOTAS (Enfoque Orientado a Objetos) ---\n")
    
    
    print("Ingresar datos para la primera mascota:")
    nom1 = input("Nombre: ")
    esp1 = input("Especie: ")
    edad1 = input("Edad: ")
    
    mascota1 = Mascota(nom1, esp1, edad1)
    
    print("\n" + "-"*40 + "\n")
    
    
    print("Ingresar datos para la segunda mascota:")
    nom2 = input("Nombre: ")
    esp2 = input("Especie: ")
    edad2 = input("Edad: ")
    
    mascota2 = Mascota(nom2, esp2, edad2)
    
    
    print("\n==============================================")
    print(" EJECUTANDO MÉTODOS Y MOSTRANDO INFORMACIÓN")
    print("==============================================")
    
    print("\nResultados Mascota 1:")
    mascota1.mostrar_informacion()
    mascota1.hacer_sonido()
    
    print("\nResultados Mascota 2:")
    mascota2.mostrar_informacion()
    mascota2.hacer_sonido()


if __name__ == "__main__":
    main()