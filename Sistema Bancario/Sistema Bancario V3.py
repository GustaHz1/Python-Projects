from abc import ABC, abstractclassmethod, abstractproperty
 
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    #Função para realizar transações
    def efetuar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    #Função para adicionar uma nova conta a lista de contas, utilizando o .append
    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    #Por meio do SUPER(). estou chamando a função da classe pai CLIENTE, com ela eu posso utilizar a variavel endereço
    def __init__(self, endereco, nome, data_nascimento, cpf):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


    pass


class Conta:
    def __init__(self, numero, cliente, saldo = 0):
        self._saldo = saldo
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente 
        self._historico = Historico()

    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

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
    def historico(self):
        return self._historico

    #A função realiza uma operação uma adição na variavel salod, com a quantidade de entrada da variavl valor
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            return True 
        return False

    #A função realiza uma operação de subtração na variavel saldo, com a quantidade de entrada da variavel valor
    def sacar(self, valor):
        if valor > 0 and valor <= self._saldo:
            self._saldo -= valor
            return True
        return False

    #A função percorre o saldo atual e o retorna 
    def obter_saldo(self):
        return self._saldo


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            return super().sacar(valor)

        return False


class Historico:
    def __init__(self):
        self._transacoes = []

    #Utilizamos property para trabalhar com um valor privado
    @property
    def transacoes(self):
        return self._transacoes
    
    #Função para adicionar uma transação em forma de dicionário com o tipo e valor, na lista _transacoes
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "Tipo": transacao.__class__.__name__,
                "Valor": transacao.valor,
            }
        )


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
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

