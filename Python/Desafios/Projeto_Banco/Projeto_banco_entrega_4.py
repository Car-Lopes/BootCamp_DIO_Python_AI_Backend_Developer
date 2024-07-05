from abc import ABC
from datetime import datetime
import textwrap
from pathlib import Path

ROOT_PATH = Path(__file__).parent

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
        except IndexError:
            raise StopIteration
        finally:
            self._index += 1

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
        self.indice_conta = 0

    def realizar_transacao(self, conta, transacao):
        if len(conta.historico.transacoes_do_dia()) >= 5:
            print("\n Voçê excedeu o numero de transacoes permitidas para hoje!")
            return
        
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta) 


class PessoaFisica(Cliente):
    def __init__(self,nome, dt_nascimento, cpf, endereco):
        super().__init__(endereco)              
        self.nome = nome
        self.dt_nascimento = dt_nascimento
        self.cpf = cpf 
    '''
    def __str__(self):
        return f"""\
            Nome:\t{self.nome}
            cpf:\t\t{self.cpf}
        """   '''
    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}:('{self.nome}', '{self.cpf}')>"

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
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
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\nOperação falho! Voçê não tem saldo suficiente")
        
        elif valor > 0:
            self._saldo -= valor
            print("\nSaque Realizado com sucesso!")
            return True
        
        else:
            print("\nOperação falho! O valor informado é invalido.")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n Deposito realizado com sucesso! ")

        else: 
            print("\n Operação falhou! O valor informado é invalido.")
            return False

        return True    
    
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__] #Saque.__name__ #ou "Saque"]
        )    

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\nOperação falho! O valor do saque excedeu o limite.")

        elif excedeu_saques:
            print("\nOperação falhou! Numero maximo de saques excedido")    

        else:
            return super().sacar(valor)
        
        return False
    
    @classmethod
    def nova_conta(cls, cliente, numero, limite, limite_saques):
        return cls(numero, cliente, limite, limite_saques)
    
    def __repr__(self):
        return f"<{self.__class__.__name__}: ('{self.agencia}', '{self.numero}', '{self.cliente.nome}', '{self.saldo}')>"

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
            Saldo:\t\tR$ {self.saldo:.2f}
        """

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def add_transacoes(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            }
        )    

    def gerar_relatorio(self, tipo_transacao=None):
        for transacao in self._transacoes:
            if tipo_transacao is None or transacao["tipo"].lower() == tipo_transacao.lower():
                yield transacao


    def transacoes_do_dia(self):
        data_atual = datetime.now().date() 
        transacoes = []
        for transacao in self._transacoes:
            data_transacao = datetime.strptime(transacao["data"], "%d-%m-%Y %H:%M:%S").date()
            if data_atual == data_transacao:
                transacoes.append(transacao)

        return transacoes                   

class Transacao(ABC):
    @property
    
    def valor(self):
        pass

    @classmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        #super().__init__()
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.add_transacoes(self)    

class Deposito(Transacao):
    def __init__(self, valor):
        #super().__init__()
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.add_transacoes(self) 

def log_transacao(func):
    def envelope(*args, **kwargs):
        resultado = func(*args, **kwargs)
        #print(f"{datetime.now()}: {func.__name__.upper()}")
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open(ROOT_PATH / "log.txt", "a") as arquivo:
            arquivo.write(
                f"[{data_hora}] Funcao '{func.__name__.upper()}' executada com argumentos {args} e {kwargs}. retornou {resultado}\n " 
            )
        #print(f"{data_hora}: {func.__name__.upper()}")  
        return resultado

    return envelope

def menu():
    menu = """
\t========== MENU ===========

    \t[1]\t Depositar
    \t[2]\t Sacar
    \t[3]\t Extrato
    \t[4]\t Novo Usuário
    \t[5]\t Listar contas
    \t[6]\t Nova Conta
    \t[7]\t Listar Usuário
    \t[0]\t Sair
\t===========================
    => """
    return input(textwrap.dedent(menu))


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\nCliente não possui conta!")
        return
    
    
    return cliente.contas[0] 

@log_transacao
def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes) 
    
    if not cliente:
        print("\n Cliente não encontrado!")
        return
    
    valor = float(input("Informe o valor do depósito:"))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

@log_transacao
def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes) 
    
    if not cliente:
        print("\n Cliente não encontrado!")
        return
    
    valor = float(input("Informe o valor do saque:"))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

@log_transacao
def extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n Cliente não encontrado!")
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print("\n =========== EXTRATO ============")
    extrato = ""
    tem_transacao = False
    for transacao in conta.historico.gerar_relatorio(tipo_transacao="Deposito"):
        tem_transacao = True
        extrato += f"\n{transacao['data']}\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    for transacao in conta.historico.gerar_relatorio(tipo_transacao="Saque"):
        tem_transacao = True
        extrato += f"\n{transacao['data']}\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"    

    if not tem_transacao:
        extrato = "Não foram relizados movimentações" 
        

    """       
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizados movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR${transacao['valor']:.2f}"
     """       

    print(extrato)
    print(f"\nSaldo: \n\tR$ {conta.saldo:.2f}")
    print(f"==================================\n")  
    #print(datetime.now())

          


@log_transacao
def criar_cliente(clientes):
    cpf = input("Iforme o CPF (somente numero): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n ja existe cliente com esse CPF!")
        return
    
    nome = input("Informe o nome completo: ")
    dt_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro-nro-bairro-cidade-estado): ")

    cliente = PessoaFisica(nome=nome, dt_nascimento=dt_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print("\nCliente cadastrado com sucesso!")

@log_transacao
def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente (somente numero): ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n cliente não encontrado, fluxo de criação encerrado")
        return
    
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta, limite=500, limite_saques=50)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\nConta Criado com Sucesso")

@log_transacao
def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))

@log_transacao
def listar_clientes(clientes):
    for cliente in clientes:
        print("=" * 100)
        print(textwrap.dedent(str(cliente)))


def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            depositar(clientes)

        elif opcao == "2":
           sacar(clientes)
            

        elif opcao == "3":
            extrato(clientes)

        elif opcao == "4":
            criar_cliente(clientes)    

        elif opcao == "5":
            listar_contas(contas)     

        elif opcao == "6":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)         

        elif opcao == "7":
            listar_clientes(clientes) 

        elif opcao == "0":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()        