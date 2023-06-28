class Conta:
    numero_conta = 0

    def __init__(self, cliente, agencia):
        self.numero = Conta.numero_conta + 1
        Conta.numero_conta += 1
        self.cliente = cliente
        self.agencia = agencia
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

    def transferir(self, conta_destino, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            conta_destino.saldo += valor
        else:
            print("Saldo insuficiente.")

    def consultar_saldo(self):
        return self.saldo
