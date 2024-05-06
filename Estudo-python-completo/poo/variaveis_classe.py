class Estudante:
	instituicao = "UFC" # variavel de classe são gerais

	def __init__(self, nome, matricula):
		self.nome = nome
		self.matricula = matricula

	def __str__(self) -> str: # variaveis de obj, possui uma variavel por obj
		return f"Nome: {self.nome} - {self.matricula} - {self.instituicao}"


def get_valores(*objs):
	for obj in objs:
		print(obj)

aluno1 = Estudante("Jao",1234)
aluno2 = Estudante("Peter",2345,)
get_valores(aluno1, aluno2)
Estudante.instituicao = "FADAT"
aluno3 = Estudante("Clark", 123456)
get_valores(aluno1, aluno2, aluno3)