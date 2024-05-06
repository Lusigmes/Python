class Animal:
        
    def __init__(self, name, n_paws):
        self.name = name
        self.n_paws = n_paws 

        print("Create class")
        
    
    def __del__(self):
        print("Destroy class")

    def __str__(self):
        return f"{self.__class__.__name__} : {' || '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class TalkAbout:
    def talk(self):
        return "Olá Mundo!"
class Mamifero(Animal):
    def __init__(self, pelage, **kw):
        self.pelage = pelage
        super().__init__(**kw)


class Ave(Animal):
    def __init__(self, feather, **kw):
        self.feather = feather        super().__init__(**kw)


class Ornitorrinco(Mamifero, Ave, TalkAbout):
    def __init__(self, **kw):
        super().__init__(**kw)

    # def __init__(self, name, n_paws, pelage, feather):
    #     super().__init__(name=name, n_paws=n_paws, pelage=pelage, feather=feather)

        # print(Ornitorrinco.mro())

roberto = Ornitorrinco(name="roberto", n_paws=4, pelage="Prerto", feather="branco")
print(roberto)
print(roberto.talk())