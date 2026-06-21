
from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.cliente import Cliente

def ejecutar_sistema():
    print("====================================================")
    print("   INICIANDO SIMULACIÓN DEL SISTEMA DE RESTAURANTE  ")
    print("====================================================\n")
    
    
    mi_restaurante = Restaurante("Sabores del Pacífico")
    
    
    print("--- Pasando Objetos a la Capa de Servicios ---")
    prod1 = Producto("Ceviche de Camarón", 12.50)
    prod2 = Producto("Arroz Marinero", 15.00)
    prod3 = Producto("Batido de Guanábana", 3.50)
    
    
    mi_restaurante.registrar_producto(prod1)
    mi_restaurante.registrar_producto(prod2)
    mi_restaurante.registrar_producto(prod3)
    
    
    print("\n--- Registrando Clientes del Sistema ---")
    cliente1 = Cliente("Luis Narváez", "0956781234")
    cliente2 = Cliente("María Elena Ruiz", "1712345678")
    
    
    mi_restaurante.registrar_cliente(cliente1)
    mi_restaurante.registrar_cliente(cliente2)
    
    
    mi_restaurante.mostrar_menu()
    mi_restaurante.mostrar_clientes()
    
    print("\n====================================================")
    print("         DEMOSTRACIÓN COMPLETADA CON ÉXITO          ")
    print("====================================================")


if __name__ == "__main__":
    ejecutar_sistema()
