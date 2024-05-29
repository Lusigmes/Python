# Construção das classes

from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime


class ContasIterador:
    def __init__(self, contas):
        self.contas = contas
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            conta = self.contas[self._index]
            return f"""\
                Agência:\t{conta.agencia}
                Número:\t\t{conta.numero}
                Titular:\t{conta.cliente.nome}
                Saldo:\t\tR$ {conta.saldo:.2f}
            """
        except StopIteration as e:
            print(f"ERRO: [{e}]")
            raise StopIteration
        finally:
            self._index += 1


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
        self.indice_conta = 0

    def realizar_transacao(self, conta, transacao):
        if len(conta.extrato.transacoes_diarias()) >= 2:
            print("\nNuméro total (10) de transações diárias excedidas!")
            return

        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: ('{self.nome}','{self.cpf}')>"


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._extrato = Extrato()

    @classmethod
    def criar_conta(cls, cliente, numero):
        return cls(numero, cliente)

    # property transforma um atributo privado _ em getter
    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def extrato(self):
        return self._extrato

    def sacar(self, valor):
        saldo = self.saldo
        saldo_excedido = valor > saldo

        if saldo_excedido:
            print("\n OPERAÇÃO FALHA!! SALDO INSUFICIENTE.")
        elif valor > 0:
            self._saldo -= valor
            print("\n SAQUE REALIZADO COM SUCESSO!!")
            return True
        else:
            print("\n OPERAÇÃO FALHA!! VALOR INVÁLIDO.")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n DEPÓSITO REALIZADO COM SUCESSO!!")
        else:
            print("\n OPERAÇÃO FALHA!! VALOR INVÁLIDO.")
            return False

        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saque=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saque = limite_saque

    def sacar(self, valor):
        numero_saques = len(
            [
                transacao
                for transacao in self.extrato.transacoes
                if transacao["tipo"] == Saque.__name__
            ]
            # [transacao for transacao in self.extrato.transacoes if transacao["tipo"] == "Saque"]
        )

        limite_excedido = valor > self._limite
        saques_excedidos = numero_saques >= self._limite_saque

        if limite_excedido:
            print("\n OPERAÇÃO FALHA!! VALOR DO SAQUE EXCEDE O LIMITE.")
        elif saques_excedidos:
            print("\n OPERAÇÃO FALHA!! NÚMERO TOTAL DE SAQUES EXCEDIDO.")
        else:
            return super().sacar(valor)

        return False

    def __str__(self) -> str:
        return f"""
                Agência:\t{self.agencia}
                C/C:\t\t{self.numero}
                Titular:\t{self.cliente.nome}
        """

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: ('{self.agencia}', '{self.numero}', '{self.cliente.nome}'>"


class Extrato:
    def __init__(self):
        self._trasacoes = []

    @property
    def transacoes(self):
        return self._trasacoes

    def adicionar_transacao(self, transacao):
        self._trasacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )

    def gerador_relatorio(self, tipo_transacao=None):
        for transacao in self._trasacoes:
            if (
                tipo_transacao is None
                or transacao["tipo"].lower() == tipo_transacao.lower()
            ):
                yield transacao

    def transacoes_diarias(self):
        data_atual = datetime.utcnow().date()
        transacoes = []
        for transacao in self._trasacoes:
            data_transacao = datetime.strptime(
                transacao["data"], "%d-%m-%Y %H:%M:%S"
            ).date()

            if data_atual == data_transacao:
                transacoes.append(transacao)
        return transacoes


# def transacoes_diarias(self): #compressão de listas
# data_atual = datetime.now(datetime.UTC).date()
# return [transacao for transacao in self._transacoes if datetime.strptime(transacao["data"], "%d-%n-%Y %H:%M:%S").date() == data_atual]


class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_saque = conta.sacar(self.valor)

        if sucesso_saque:
            conta.extrato.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_deposito = conta.depositar(self.valor)

        if sucesso_deposito:
            conta.extrato.adicionar_transacao(self)
