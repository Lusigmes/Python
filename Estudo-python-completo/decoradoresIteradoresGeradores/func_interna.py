# função interna
def pai():
    print("func pai")
    
    def f1():
        print("func f1")
    def f2():
        print("func f2")
    f1()
    f2()

pai()
print("*"*50)

