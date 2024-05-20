# Simular operação bancária

# import desafio_poo
import textwrap
from desafio_banco_classes import Transacao, Deposito, Saque, Cliente, PessoaFisica, Conta, ContaCorrente, ContasIterador, Extrato
import datetime
import functools

def menu():
    menu = """\n
    **************** MENU ****************
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuario
    [q]\tSair
    **************************************
    => """
    return input(textwrap.dedent(menu))

def filtrar_cliente_por_cpf(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None    
            
def recuperar_conta_por_cliente(cliente):
    if not cliente.contas:
        print("\nO CLIENTE NÃO POSSUI CONTA!")
        return

    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]


def log_transacoes(funcao): #decorador
    # @functools.wraps(funcao)
    def conteudo(*args, **kwargs):
        resultado = funcao(*args, **kwargs)
        # print(f"{datetime.datetime.now()}: {funcao.__name__.upper()}")
        print(f"{datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')} -> {funcao.__name__.upper()}")
        return resultado
    
    return conteudo
    
@log_transacoes
def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente_por_cpf(cpf, clientes)
    
    if not cliente:
        print("\nCLIENTE NÃO ENCONTRADO!!")
        return
    
    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)
    
    conta = recuperar_conta_por_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)
    
@log_transacoes
def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente_por_cpf(cpf, clientes)
    
    if not cliente:
        print("\nCLIENTE NÃO ENCONTRADO!!")
        return
    
    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)
    
    conta = recuperar_conta_por_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)
    
@log_transacoes
def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente_por_cpf(cpf, clientes)
    
    if not cliente:
        print("\nCLIENTE NÃO ENCONTRADO!!")
        return
    
    conta = recuperar_conta_por_cliente(cliente)
    if not conta:
        return
    
    print("\n******************* EXTRATO *******************")
    extrato = ""
    possui_transacao = False
    # for transacao in conta.extrato.gerador_relatorio(tipo_transacao="saque"):
    # for transacao in conta.extrato.gerador_relatorio(tipo_transacao="deposito"):
    for transacao in conta.extrato.gerador_relatorio():
        possui_transacao = True   
        extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}\n\t{transacao['data']}"
    
    if not possui_transacao:
        extrato = "NÃO HOUVE MOVIMENTAÇÕES!"
    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("\n******************* EXTRATO *******************")

@log_transacoes
def criar_cliente(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente_por_cpf(cpf, clientes)
    
    if cliente:
        print("\nCLIENTE JÁ CADASTRADO!!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, numero - bairro - cidade/sigla estado): ")
    
    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    clientes.append(cliente)
    
    print("\nCLIENTE CRIADO COM SUCESSO!!")
    
@log_transacoes
def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente_por_cpf(cpf, clientes)
    
    if not cliente:
        print("\nCLIENTE NÃO ENCONTRADO!!")
        return
    
    conta = ContaCorrente.criar_conta(cliente=cliente,numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)
    
    print("\nCONTA CRIADA COM SUCESSO!!")
    
    
def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))
        
def banco():
    clientes = []
    contas = []
    
    while True:
        opcao = menu()
        
        if opcao == "d":
            depositar(clientes)
        
        elif opcao == "s":
            sacar(clientes)
            
        elif opcao == "e":
            exibir_extrato(clientes)
            
        elif opcao == "nu":
            criar_cliente(clientes)
            
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
            
        elif opcao == "lc":
            listar_contas(contas)
            
        elif opcao == "q":
            break
        
        else:
            print("OPÇÃO INVÁLIDA!! TENTE NOVAMENTE.")
            
banco()