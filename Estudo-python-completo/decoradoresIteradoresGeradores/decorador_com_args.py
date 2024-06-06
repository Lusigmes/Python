import functools #resolve a instrospecção ao decorar uma função
def duplicar(func):
    @functools.wraps(func) # mantem o nome da função que usa o decorador duplicar
    def duplicada(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return duplicada

@duplicar
def aprender(tecnologia):
    print(f"Estou aprendendo a tecnologia {tecnologia}")
    return tecnologia.upper()

tecnologia = aprender("Python")
print(tecnologia)
print(aprender.__name__) # functools garante que retorne o nome da função "aprender" inves de "duplicada"