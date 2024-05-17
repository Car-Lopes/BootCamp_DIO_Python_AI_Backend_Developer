def MeuGerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2 


for i in MeuGerador(numeros=[1, 2, 3]):
    print(i)     