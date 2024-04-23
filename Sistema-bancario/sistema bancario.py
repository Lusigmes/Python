menu = '''

	[d] Depositar
	[s]	Sacar
	[e]	Extrato	
	[0]	Sair

	'''

saldo = 0
extrato = ""
numero_saque = 0
saque_limite = 500
QUANTIDADE_LIMITE_SAQUE = 3

# iniciando o sistema bancário
while True:
	selecione = input(menu+"-> ")
	#deposito
	if selecione == 'd':
		valor_deposito = float(input("Digite o valor do depósito: "))
		print("\n")
		if valor_deposito > 0:
			saldo += valor_deposito
			extrato += f"     Deposito: R$ {valor_deposito:.2f}\n"
			print(saldo)

		else:
			print("Não é possível realizar depósito de um valor negativo!\n")
	#saque
	elif selecione == 's':
		valor_saque = float(input("Digite o valor do saque: "))
		print("\n")
		
		saldo_excedido = valor_saque > saldo #verifica se o valor do saque é maior q o saldo
		limite_excecido = valor_saque > saque_limite #verifica se o valor do saque é maior que o limite de 500
		saque_excedido = numero_saque >= QUANTIDADE_LIMITE_SAQUE #verifica se a quantidade de saque é maior que a quantidade limite de 3 saques diarios
		if saldo_excedido:
			print("Falha!! Saldo insuficiente.")
		elif limite_excecido:
			print("Falha!! Valor do saque excedeu o limite de R$500.")
		
		elif saque_excedido:
			print("Falha!! Limite de saque diarios (3) atingido.")
	
		elif valor_saque > 0:
			saldo -= valor_saque
			numero_saque += 1
			extrato += f"     Saque: R$ {valor_saque:.2f}\n"
			print(saldo)
		
		else:
				print("Falha!!")
			
	#extrato
	elif selecione == 'e':
		print("\n*****************************")
		print("Não houve transações." if not extrato else extrato)
		print(f"\n		Saldo: R${saldo:.2f}") #imprimir a variavel saldo no formato ai e com 2 casas decimais
		print("*****************************")

	#sair
	elif selecione == '0':
		print("Deseja finalizar seu acesso?")
		finalizar = input("      Sim[s] ou Não[n]\n   -> ")
		if finalizar == 's':
			break
		else:
			continue
	else:
		print("Operador inválido, tente novamente!")

#print(menu)




















