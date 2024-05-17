import functools

def dupl(func):
    @functools.wraps(func)
    def envelope(*args, **kwargs):
        
        #func(*args, **kwargs)
        resultado = func(*args, **kwargs)
        return resultado
        
    return envelope

@dupl
def aprender(tecnologia):
    print(f"Estou aprendendo {tecnologia.upper()}!")
    return tecnologia.upper()

resultado = aprender("Python")
#aprender(resultado)   
print(resultado)
print(aprender.__name__) 