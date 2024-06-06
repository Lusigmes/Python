# read() #readline() #readlines()
arquivo = open(file='file.txt', mode='r', encoding='utf-8') #'ascii' #UnicodeDecodeError

print(arquivo.read(), "\n") #ler e retorna string completa
# print(arquivo.readline(),"\n") #ler e retorna primeira linha
# print(arquivo.readlines() ,"\n") #ler e retorna lista de string com todas linhas sem formatação, util para iterar

while len(linhas := arquivo.readline()): #operador walrus := : atribui valores a uma variavel como parte de uma expressao(usar o valor atribuido imediatamente apos atribui-lo)
    print( f"{len(linhas)}:", linhas)

arquivo.close()

