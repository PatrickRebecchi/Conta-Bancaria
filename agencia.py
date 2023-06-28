from conta import Conta

class Agencia:
    def __init__(self, numero):
        self.numero = numero
        self.contas = []

    def criar_conta(self, cliente):
        conta = Conta(cliente, self)
        self.contas.append(conta)
        return conta

    def buscar_conta(self, numero):
        for conta in self.contas:
            if conta.numero == numero:
                return conta
        return None