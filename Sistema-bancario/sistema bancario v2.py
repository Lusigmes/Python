import textwrap

def menu():
	menu ="""\n
		|**************** Selecione a opção desejada **************|
	
		[01] [Depositar] 	                 [Criar nova conta] [04]
		[02] [Sacar] 		               [Criar novo usuário] [05]
		[03] [Exibir extrato] 	             	[Listar contas] [06]
		[00] [Sair]                           [Listar usuários] [07]
			            
							 
		|**********************************************************|

	\t\t=> """
	return input(textwrap.dedent(menu))

#base
def depositar(saldo, valor_deposito, /,  extrato):
	print("\n")
	if valor_deposito > 0:
		saldo += valor_deposito
		extrato += f"\t\t\tDeposito:\tR$ {valor_deposito:.2f}\n"
		print(f"\n\tDepósito de R$ {valor_deposito:.2f} realizado com sucesso!" )
	else:
		print("\n\tHouve uma falha na transação!\nValor inválido" )
		
	return saldo, extrato


def sacar(*, valor_saque, saldo, extrato, numero_saques, saque_limite, quantidade_limite_saques):
	print("\n")
	saldo_excedido = valor_saque > saldo #verificar se o valor do saque é maior q o saldo
	limite_excecido = valor_saque > saque_limite #verificar se o valor do saque é maior que o limite de 500
	saque_excedido = numero_saques >= quantidade_limite_saques #verificar se a quantidade de saque é maior que a quantidade limite de 3 saques diarios
	#falhas
	if saldo_excedido:
		print("\tHouve uma falha na transação!\n\tSaldo insuficiente.")
	elif limite_excecido:
		print("\tHouve uma falha na transação!\n\tValor do saque excedeu o limite de R$500 reais.")
	elif saque_excedido:
		print("\tHouve uma falha na transação!\n\tLimite de saques diário (3) atingido.")
	#realizando o saque
	elif valor_saque > 0:
		saldo -= valor_saque
		numero_saques += 1
		#print(numero_saques)
		extrato += f"\t\t\tSaque:\t\tR$ {valor_saque:.2f}\n"
		print(f"\n\tSaque de R$ {valor_saque:.2f} realizado com sucesso!" )
		
	else:
			print("\n\tHouve uma falha na transação!\nValor inválido")
			
	return saldo, extrato, numero_saques

def exibirExtrato(saldo, /,*, extrato):
	print("\n|************************ Extrato *************************|\n")
	print("\t\t\tNenhuma transação foi realizada.\n" if not extrato else extrato)
	print(f"\n\t\t\tSaldo:\t\tR${saldo:.2f}") #imprimir a variavel saldo no formato ai e com 2 casas decimais
	print("\n|**********************************************************|")

#manipulando listas
def verificarCpf(cpf, usuarios):
	verificar_cpf = [
		usuario for usuario in usuarios 
			if usuario["cpf"] == cpf
	]
	return verificar_cpf[0] if verificar_cpf else None	##
#
#
def criarUsuario(usuarios):
	cpf  = input("\n\tInsira o CPF (Somente números): ")
	cpf_existente = verificarCpf(cpf, usuarios)
	#erro: cpf ja cadastrado
	if cpf_existente: #se ja houver cadastro com o cpf verificado, retorna o usuario com o cpf verificado, senão recebe valores para novo usuario
		print(f"\n\tCPF: {cpf} já cadastrado.\n")
		return
		
	nome = input("\tInsira seu nome completo: ")
	data_nascimento = input("\tInsira sua data de nascimento (dd-mm-aa): ")
	endereco = input("\tInsira seu endereço (Rua, numero-Bairro Cidade-UC): ")
	
	#adicionar um  valor de dicionario com os valores lido, caso o cpf_existente retorne None(nenhum valor "cpf" do dicionario é igual ao cpf inseriodo no dicionario dento da lista usuarios)
	usuarios.append({"cpf":cpf, "nome":nome, "data_nascimento":data_nascimento, "endereco":endereco})
	print("\n\tCadastro finalizado com sucesso.\n\t\tObrigado pela preferência!\n")
#
#
def listarUsuarios(usuarios):
	if usuarios:
		print("\n\t\t\t\tUsuários cadastrados\n")
	else:
		print("\n\t\t\t\tNenhum usuário cadastrado.\n")
		return
		
	for usuario in usuarios:
		perfil = f"""
			\t\t\tPerfil de {usuario["nome"]}
			\t\tCPF: {usuario["cpf"]}
			\t\tNome: {usuario["nome"]}
			\t\tData de nascimento: {usuario["data_nascimento"]}
			\t\tEndereço: {usuario["endereco"]}
 		"""
		print("*" * 60)
		print(textwrap.dedent(perfil))
		print("*" * 60)
#
#
def criarConta(agencia, numero_conta, usuarios):
	cpf  = input("\n\tInsira o CPF (Somente números): ")
	cpf_existente = verificarCpf(cpf, usuarios) #usuario
	#sucesso: cpf válido
	if cpf_existente: #SE HOUVER ALGUM VALOR EM cpf_existente[0] cpf_existente = usuario com cpf válido
		print("\n\tConta bancária criada com sucesso.\n\t\tObrigado pela preferência!\n")
		return {"agencia":agencia, "numero_conta":numero_conta, "usuario":cpf_existente}
		
	print(f"\n\tUsuário de CPF {cpf} não cadastrado.\n")
#
#
def listarContas(contas):	
	if contas:
		print("\n\t\t\tContas bancárias cadastradas\n")
	else:
		print("\n\t\t\t\tNenhuma conta bancária cadastrada.\n")
		return
		
	for conta in contas:
		perfil = f"""
			\t\t\tTitular da conta: {conta["usuario"]["nome"]}
			\t\tAgência: {conta["agencia"]}
			\t\tNumero da conta: {conta["numero_conta"]}
			\t\tCPF vínculado: {conta['usuario']['cpf']}
 		"""
		print("*" * 60)
		print(textwrap.dedent(perfil))
		print("*" * 60)
#
#
#
#
#
def main():
	QUANTIDADE_LIMITE_SAQUE = 3
	AGENCIA = "000X"
	saldo = 0
	extrato = ""
	numero_saques = 0
	saque_limite = 500
	usuarios = []
	contas = []
	


	while True:
		opcao = menu()
	
		if opcao == "01":#depositar
			valor_deposito = float(input("\n\tInsira o valor do depósito: "))
			
			saldo, extrato = depositar(saldo,valor_deposito,extrato=extrato)
			
		elif opcao == "02":#sacar
			valor_saque = float(input("\n\tInsira o valor do saque: "))
		
			saldo, extrato, numero_saques = sacar(valor_saque=valor_saque, saldo=saldo, extrato=extrato, numero_saques=numero_saques, saque_limite=saque_limite, quantidade_limite_saques=QUANTIDADE_LIMITE_SAQUE,)
			
		elif opcao == "03":#exibir extrato
			exibirExtrato(saldo,extrato=extrato)
			#argumento posicional saldo(positional) / e * argumento nomeado(keyword) extrato
		elif opcao == "04":#criar nova conta bancária
			numero_conta = len(contas)+1
			conta_nova = criarConta(AGENCIA, numero_conta,usuarios)
			
			if conta_nova: #nao insere conta com valor None na lista contas
				contas.append(conta_nova)
			
		elif opcao == "05":#criar novo usuario
		 criarUsuario(usuarios)
			
		elif opcao == "06":#listar contas bancarias no sistema
		 listarContas(contas)
			
		elif opcao == "07":
		 listarUsuarios(usuarios)
		
			
		elif opcao == "00":#salir
			
			print("\t\t\nDeseja realmente finalizar seu acesso?")
			finalizar = input("\t\t\tSim[y] ou Não[n]\n   -> ")
			if finalizar == 'y':
				print("\t\t\nObrigado por usar nosso sistema, volte sempre!")
				break
			else:
				continue
			
		else:
				print("\tOperação inválida!\n\tTente novamente!")


main()