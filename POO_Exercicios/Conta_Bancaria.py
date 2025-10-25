class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        return self.saldo

    def sacar(self, valor):
        self.saldo -= valor
        return self.saldo

    def mostrar_saldo(self):
        return self.saldo

conta1 = ContaBancaria('Guilherme', 5000)
conta2 = ContaBancaria('Cassia', 30000)

conta1.depositar(100)
conta1.sacar(100)
print(conta1.mostrar_saldo())