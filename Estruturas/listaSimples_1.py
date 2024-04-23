class ListaSimples:
    def __init__(self):
        self.lista = []
        
    def empty(self):
        return len(self.lista) == 0
    
    def sizze(self):
        return len(self.lista)
    
    def printar(self):
        if not self.empty():
            print(" -> ".join(map(str, self.lista)))
        else:
            print("Lista Vazia")
            
    def insert_start(self, dado):
        self.lista.insert(0, dado)
        
    def insert_end(self, dado):
        self.lista.append(dado)
            
    def delete_start(self):
        if not self.empty():
            return self.lista.pop(0)
        else:
            raise IndexError("Lista Vazia")
                            
    def delete_end(self):        
        if not self.empty():
            return self.lista.pop()
        else:
            raise IndexError("Lista Vazia")


lista = ListaSimples()

print("Vazia:", lista.empty())
print("Tamanho:", lista.sizze())
lista.printar()

lista.insert_start(12)
lista.insert_start(24)
lista.insert_start(1)
lista.insert_start(1)
lista.insert_start(1)
lista.insert_end(44)
lista.insert_end(12)
lista.insert_end(156)
lista.insert_end(1)
lista.insert_end(1)
lista.insert_end(1)
lista.printar()

lista.delete_start()
lista.delete_start()
lista.delete_start()
lista.delete_end()
lista.delete_end()
lista.delete_end()
lista.printar()