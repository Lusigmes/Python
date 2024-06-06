class IterarNumeros:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0
        
    def __iter__(self):
        return self
    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except IndexError:
            raise StopIteration
        
for i in IterarNumeros(numeros=[1,2,5,6]):
    print(i)
        