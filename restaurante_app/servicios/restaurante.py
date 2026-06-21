
from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    def __init__(self, nombre_restaurante: str):
        
        self.nombre_restaurante = nombre_restaurante
        self.lista_productos = []  
        self.lista_clientes = []   

    def registrar_producto(self, producto: Producto):
        
        self.lista_productos.append(producto)
        print(f"[Sistema] Producto registrado con éxito: {producto.nombre}")

    def registrar_cliente(self, cliente: Cliente):
        
        self.lista_clientes.append(cliente)
        print(f"[Sistema] Cliente registrado con éxito: {cliente.nombre}")

    def mostrar_menu(self):
        
        print(f"\n--- MENÚ DE {self.nombre_restaurante.upper()} ---")
        if not self.lista_productos:
            print("El menú está vacío.")
        for prod in self.lista_productos:
            print(prod)  

    def mostrar_clientes(self):
        
        print(f"\n--- BASE DE DATOS DE CLIENTES ---")
        if not self.lista_clientes:
            print("No hay clientes registrados.")
        for cli in self.lista_clientes:
            print(cli)  