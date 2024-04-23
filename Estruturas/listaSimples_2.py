class No:
    def __init__(self, dado=0, nxt=None):
        self.dado = dado
        self.next = nxt

class ListaSimples:
    def __init__(self):
        self.start = None

    def empty(self):
        return self.start is None
    
    def sizze(self):
        current = self.start
        tam = 0
        while current is not None:
            tam += 1
            current = current.next
        return tam
    
    def insert_start(self, dado):
        novo = No(dado, self.start)
        self.start = novo
        
    def printar(self):
        current = self.start
        while current is not None:
            print(current.dado, end=(" -> "))
            current = current.next
        print("**void**")

    def insert_end(self, dado):
        novo = No(dado)
        if self.empty():
            self.start = novo
        else:
            current = self.start
            while current.next is not None:
                current = current.next
            current.next = novo
    
    def search_dado(self, data):
        print("S")
            
    def delete_start(self):
        if not self.empty():
            removido = self.start.dado
            self.start = self.start.next
            return removido
        else:
            raise IndexError("Lista Vazia")
        
         
    def delete_end(self):
        if not self.empty():
            if self.start.next is None:
                removido = self.start.dado
                self.start = None
            else:
                current = self.start         
                while current.next.next is not None:
                    current = current.next
                removido = current.next.dado
                current.next = None       
            return removido
        else:
            raise IndexError("Lista Vazia")
        
lista = ListaSimples()
print(lista.empty())
print(lista.sizze())
lista.printar()

lista.insert_start(12)
lista.insert_start(53)
lista.insert_start(31)
lista.insert_start(0)
lista.insert_start(0)
lista.insert_start(0)
lista.insert_end(31)
lista.insert_end(518)
lista.insert_end(1)
lista.insert_end(00)
lista.insert_end(00)
lista.insert_end(00)
lista.printar()
print(lista.sizze())

lista.delete_start()
lista.delete_start()
lista.delete_start()
lista.delete_end()
lista.delete_end()
lista.delete_end()
lista.printar()
print(lista.sizze())
