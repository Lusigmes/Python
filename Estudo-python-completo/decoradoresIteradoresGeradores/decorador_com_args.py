import functools #resolve a instrospecção ao decorar uma função
def duplicar(func):
    
    @functools.wraps(func)
    def msg(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return msg

@duplicar
def aprender(tecnologia):
    print(f"Estou aprendendo a tecnologia {tecnologia}")
    return tecnologia.upper()

tecnologia = aprender("Python")
print(tecnologia)
print(aprender.__name__)