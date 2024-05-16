# retornar função de função
def calcular(op):
    def somar(a,b):
        return a+b
    def subtrair(a,b):
        return a-b
    if op == "+":
        return somar
    else:
        return subtrair
    
resultado = calcular("+")(1,2)
resultado2 = calcular("-")(2,1)
print(resultado)
print(resultado2)
print("*"*50)