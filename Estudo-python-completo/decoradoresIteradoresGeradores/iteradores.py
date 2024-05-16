#contém um numero contavel de valores que podem ser iterados
# metodos especiais para iteração __next__() e __iter__() 
# raise - finaliza iteração
class FileIterator:
    def __init__(self, filename):
        self.file = open(filename)
        
    def __iter__(self):
        return self
    def __next__(self):
        line = self.file.readline()
        if line != '':
            return line
        else:
            self.file.close()
            raise StopIteration
        

for line in FileIterator('file.txt'):
    print(line)
