class CuentaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self._saldo = 0.0

    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            print("Deposito realizado")

    # Metodo Getter publico
    def obtener_saldo(self):
        return self._saldo
    

cuenta = CuentaBancaria("Juan")
cuenta.depositar(100)
print(cuenta.obtener_saldo())