class Pessoa:
	def __init__(self, nome=None, idade=None):
		self.nome = nome
		self.idade = idade


	@classmethod #transforma em metodo de classe
	def criar_por_nascimento(cls, ano, mes, dia, nome):
		#print(cls)
		idade = 2024 - ano
		return cls(nome, idade)
		# return Pessoa(nome, idade)

	@staticmethod #converte função em metodo estatico
	def verificar_maioridade(idade):
		return idade >= 18

#Pessoa().criar_por_nascimento(1997,11,28,"Nome") - cria instancia -> acessa e executa metodo -> cria uma nova instancia dentro do metodo

p2 = Pessoa.criar_por_nascimento(1997, 1, 15,"Jao") 
print(p2.nome, p2.idade )



print(Pessoa.verificar_maioridade(18))
print(Pessoa.verificar_maioridade(10))