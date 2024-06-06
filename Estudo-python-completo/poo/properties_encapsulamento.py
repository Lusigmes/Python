class Person:
	def __init__(self, cpf=None, birth=None):
		self._cpf = cpf
		self._birth = birth

	@property #retorna a propriedade encapsulada tipo get
	def cpf(self):
		return self._cpf or 0
 	#def get_cpf(self) return self._cpf
	@property
	def age(self):
		_current_year = 2024
		return _current_year - self._birth 

 	#def get_age(self) return 2024 - self._birth

	@cpf.setter # insere valor na propriedade encapsulada
	def cpf(self, value):
		# _cpf = self._cpf or 0
		# _value = value or 0
		self._cpf = value

	@cpf.deleter # remove o valor da propriedade encapsulada
	def cpf(self):
		self._cpf = 0

#pode ser uasdo propriedade @atributo.setter caso tenha uma lógica para proteger o atributo, caso contrario deixar público

pessoa = Person(14124, 1997)
print(pessoa.cpf)

pessoa._cpf = 546846
print(pessoa.cpf)

del pessoa.cpf
print(pessoa.cpf) 

print(f"Meu cpf é {pessoa.cpf} e minha idade é {pessoa.age}")

#