from agencia import Agencia
from conta import Conta
import tkinter as tk
from tkinter import messagebox, simpledialog

class Interface:
    def __init__(self, master):
        self.agencia = Agencia("001")
        self.conta_atual = None

        self.master = master
        self.master.title("Banco XYZ")

        self.label_info = tk.Label(master, text="")
        self.label_info.pack()

        self.frame_acoes = tk.Frame(master)
        self.frame_acoes.pack()

        self.botao_criar_conta = tk.Button(self.frame_acoes, text="Criar conta", command=self.criar_conta)
        self.botao_criar_conta.pack(side=tk.LEFT)

        self.botao_acessar_conta = tk.Button(self.frame_acoes, text="Acessar conta", command=self.acessar_conta)
        self.botao_acessar_conta.pack(side=tk.LEFT)

        self.botao_sair = tk.Button(self.frame_acoes, text="Sair", command=self.sair)
        self.botao_sair.pack(side=tk.LEFT)

        self.frame_conta = tk.Frame(master)
        self.label_saldo = tk.Label(self.frame_conta, text="")
        self.label_saldo.pack()

        self.botao_depositar = tk.Button(self.frame_conta, text="Depositar", command=self.depositar)
        self.botao_depositar.pack(side=tk.LEFT)

        self.botao_sacar = tk.Button(self.frame_conta, text="Sacar", command=self.sacar)
        self.botao_sacar.pack(side=tk.LEFT)

        self.botao_transferir = tk.Button(self.frame_conta, text="Transferir", command=self.transferir)
        self.botao_transferir.pack(side=tk.LEFT)

        self.botao_consultar_saldo = tk.Button(self.frame_conta, text="Consultar Saldo", command=self.consultar_saldo)
        self.botao_consultar_saldo.pack(side=tk.LEFT)

        self.botao_voltar = tk.Button(self.frame_conta, text="Voltar", command=self.voltar)
        self.botao_voltar.pack(side=tk.LEFT)

        self.frame_acoes.pack_forget()
        self.frame_conta.pack_forget()

    def iniciar(self):
        self.frame_acoes.pack()

    def criar_conta(self):
        self.frame_acoes.pack_forget()
        self.frame_conta.pack()

        numero_conta = tk.simpledialog.askinteger("Criar Conta", "Digite o número da conta:")
        nome = tk.simpledialog.askstring("Criar Conta", "Digite o nome do cliente:")
        cliente = {"nome": nome}
        conta = self.agencia.criar_conta(numero_conta, cliente)
        self.conta_atual = conta
        messagebox.showinfo("Bem-vindo", f"Bem-vindo(a), {nome}! Sua conta {numero_conta} foi criada com sucesso.")
        self.atualizar_info()

    def acessar_conta(self):
        self.frame_acoes.pack_forget()
        self.frame_conta.pack()

        numero_conta = tk.simpledialog.askinteger("Acessar Conta", "Digite o número da conta:")
        conta = self.agencia.buscar_conta(numero_conta)

        if conta:
            self.conta_atual = conta
            self.atualizar_info()
        else:
            messagebox.showerror("Erro", "Conta não encontrada.")
            self.voltar()

    def sair(self):
        self.master.quit()

    def depositar(self):
        valor = tk.simpledialog.askfloat("Depositar", "Digite o valor a ser depositado:")
        self.conta_atual.depositar(valor)
        self.atualizar_info()

    def sacar(self):
        valor = tk.simpledialog.askfloat("Sacar", "Digite o valor a ser sacado:")
        self.conta_atual.sacar(valor)
        self.atualizar_info()

    def transferir(self):
        numero_destino = tk.simpledialog.askinteger("Transferir", "Digite o número da conta de destino:")
        conta_destino = self.agencia.buscar_conta(numero_destino)

        if conta_destino:
            valor = tk.simpledialog.askfloat("Transferir", "Digite o valor a ser transferido:")
            self.conta_atual.transferir(conta_destino, valor)
            self.atualizar_info()
        else:
            messagebox.showerror("Erro", "Conta de destino não encontrada.")

    def consultar_saldo(self):
        saldo = self.conta_atual.consultar_saldo()
        messagebox.showinfo("Saldo", f"Saldo disponível: {saldo}")

    def voltar(self):
        self.frame_conta.pack_forget()
        self.frame_acoes.pack()
        self.conta_atual = None

    def atualizar_info(self):
        numero_conta = self.conta_atual.numero
        saldo = self.conta_atual.consultar_saldo()
        self.label_info.config(text=f"Conta atual: {numero_conta}")
        self.label_saldo.config(text=f"Saldo disponível: {saldo}")
