def dupl(func):
    def envelope(*args, **kwargs):
        resultado = func(*args, **kwargs)
        return resultado
        
    return envelope

@dupl
def aprender(tecnologia):
    print(f"Estou aprendendo {tecnologia}!")
    return tecnologia.upper()

resultado = aprender("Python")
aprender(resultado)   
print(aprender.__name__) 