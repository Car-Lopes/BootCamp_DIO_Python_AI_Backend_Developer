import textwrap

def menu():
    menu = """
\t========== MENU ===========

    \t[1]\t Depositar
    \t[2]\t Sacar
    \t[3]\t Extrato
    \t[4]\t Novo Usuário
    \t[5]\t Listar contas
    \t[6]\t Novo Conta
    \t[7]\t Listar Usuário
    \t[0]\t Sair
\t===========================
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n Depósito relaizado com sucesso!")
    else:
        print("\nOperação falhou! O valor informado é inválido.") 

    return saldo, extrato     

def saque(*, saldo, valor, extrato, limite, numero_saque, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > saldo
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\nOperação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("\nOperação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("\nOperação falhou! Número máximo de saques excedido.")
        
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n Saque Realizado com Sucesso!")

    else:
        print("\nOperação falhou! O valor informado é inválido.")

    return saldo, extrato 


def extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_usuario(usuarios):
    cpf = input("Iforme o CPF (somente nuemro): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\n ja existe usuario com esse CPF!")
        return
    
    nome = input("Informe o nome completo: ")
    dt_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro-nro-bairro-cidade-estado): ")

    usuarios.append({"nome": nome, "data_nascimento": dt_nascimento, "cpf": cpf, "endereco": endereco})

    print("\nUsuario cadastrado com sucesso!")




def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Iforme o CPF (somente nuemro): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\n Conta criada com sucesso!")
        return {"agencia":agencia, "numero_conta":numero_conta, "usuario":usuario}
    
    print("\n Usuario não encontrado, fluxo de criação de conta encerrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agencia: \t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}  
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def listar_usuarios(usuarios):
    for usuario in usuarios:
        linha = f"""\
            Cpf: \t {usuario['cpf']}
            Nome: \t {usuario['nome']}
        """
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saque=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
            

        elif opcao == "3":
            extrato(saldo, extrato=extrato)

        elif opcao == "4":
            criar_usuario(usuarios)    

        elif opcao == "5":
            listar_contas(contas)     

        elif opcao == "6":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios) 

            if conta:
                contas.append(conta)         

        elif opcao == "7":
            listar_usuarios(usuarios) 

        elif opcao == "0":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()        