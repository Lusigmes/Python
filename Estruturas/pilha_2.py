class No:
    def __init__(self, dado=0, nxt=None):
        self.dado = dado
        self.next = nxt
        
class Pilha:
    def __init__(self):
        self.topo = None
        self.sizze = 0
    
    def empty(self):
        return self.sizze == 0
    
    def get_size(self):
        return self.sizze
    
    def get_topo(self):
        if not self.empty():
            return self.topo.dado
        else:
            raise IndexError("Pilha vazia")
    
    def push(self, item):
        novo = No(item, self.topo)
        self.topo = novo
        self.sizze += 1
        print(item,"empilhado.")
        
    def pull(self):
        if not self.empty():
            removido = self.topo.dado
            self.topo = self.topo.next
            self.sizze -= 1
            return removido
        else:
           raise IndexError("Pilha vazia")
       
    def printar(self):
        if not self.empty():
            current = self.topo
            while current is not None:
                print(current.dado, end=" -> ")
                current = current.next
        else:
            print("Pilha vazia")            
    
    
pilha = Pilha()
print("Vazio:", pilha.empty())
print("Tamanho:", pilha.get_size())

pilha.push(15)
pilha.push(225)
pilha.push(31)
pilha.push(51)
print("Topo:", pilha.get_topo())
print("Tamanho:", pilha.get_size())
    

print(pilha.pull(),"desempilhado.")
print("Topo:", pilha.get_topo())
print("Tamanho:", pilha.get_size())

pilha.printar()