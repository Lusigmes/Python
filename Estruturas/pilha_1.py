class Pilha:
    def __init__(self):
        self.items = []
        print("OK")
    
    def empty(self):
        return len(self.items) == 0   
    
    def sizze(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)
        print(item,"empilhado.")
        
    def pull(self):
        if not self.empty():
            return self.items.pop()
        else:
            raise IndexError("Pilha vazia")
    
    def topo(self):
        if not self.empty():
            return self.items[-1]
        else:
            raise IndexError("Pilha vazia")
    
pilha = Pilha()

print("Vazio: ",pilha.empty())
print("Tamanho: ",pilha.sizze())

pilha.push(19)
pilha.push(11)
pilha.push(100)

print("Topo:", pilha.topo())
print("Tamanho:",pilha.sizze())
 
removido = pilha.pull()
print("Removido:", removido)
print("Topo:", pilha.topo())
print("Tamanho:",pilha.sizze())
