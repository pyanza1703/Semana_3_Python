class Cliente:
    def __init__(self, nombre: str, cedula: str):
        
        self.nombre = nombre
        self.cedula = cedula

    def __str__(self):
    
        return f"Cliente: {self.nombre} (C.I: {self.cedula})"