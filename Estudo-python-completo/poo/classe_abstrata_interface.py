from abc import ABC, abstractmethod,abstractproperty
# fornece segurança de polimorfimos de metodos
# caso herde a classe pai e não seja notada a existencia do metodo proposto
class ControleRemoto(ABC):

	@abstractmethod
	def ligar(self):
		print("Ligando")

	@abstractmethod
	def desligar(self):
		print("Desligando")

	@property
	@abstractproperty
	def marca(self):
		pass

class ControleTV(ControleRemoto):
	def ligar(self):
		print("Ligando a TV")
		print("Ligado")
	def desligar(self):
		super().desligar() 
		print("Desligado")
	@property
	def marca(self):
		return "LG"

class ControleArCondicionado(ControleRemoto):
	def ligar(self):
		print("Ligando o arcondicinado")
		print("Ligado")
	def desligar(self):
		super().desligar() 
		print("Desligado")
	@property
	def marca(self):
		return "LG"


controle = ControleTV()
controle.ligar()
controle.desligar()
print("Controle TV marca: ",controle.marca)

controleAr = ControleArCondicionado()
controleAr.ligar()
controleAr.desligar()
print("Controle Ar condicionado marca: ",controleAr.marca)