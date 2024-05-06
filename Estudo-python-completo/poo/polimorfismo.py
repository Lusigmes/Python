class Passaro:
    def voar(self):
        print('Voando')

class Galinha(Passaro):
    def voar(self):
        print("galinha nao voa")

class Pato(Passaro):
    def voar(self):
        super().voar()

class Aviao(Passaro):
    def voar(self):
        print("decolando")

def plano_voo(obj):
    obj.voar()



plano_voo(Aviao())
plano_voo(Galinha())
plano_voo(Pato())