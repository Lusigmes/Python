def gerar_numeros(numeros: list[int]):
    # contador += 1
    for numero in numeros:
        yield numero * 2
        
for i in gerar_numeros(numeros=[2,4,5,6]):
    print(i)