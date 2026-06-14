
class CuentaBancaria:
    
    def __init__(self, titular, saldo_inicial, tipo_cuenta):
        self.titular = titular         
        self.saldo = saldo_inicial     
        self.tipo_cuenta = tipo_cuenta  

    
    def mostrar_informacion(self):
        print(f"\n--- Cuenta de {self.titular} ---")
        print(f"Tipo de cuenta: {self.tipo_cuenta}")
        print(f"Saldo disponible: ${self.saldo}")

    
    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
        else:
            print("El monto a depositar debe ser mayor a cero.")


cuenta1 = CuentaBancaria("Carlos Mendoza", 1500, "Ahorros")
cuenta1.mostrar_informacion()
cuenta1.depositar(100)
cuenta1.mostrar_informacion()

print("-" * 30)


cuenta2 = CuentaBancaria("Ana Rodríguez", 2800, "Corriente")
cuenta2.mostrar_informacion()
cuenta2.depositar(700)
cuenta2.mostrar_informacion()