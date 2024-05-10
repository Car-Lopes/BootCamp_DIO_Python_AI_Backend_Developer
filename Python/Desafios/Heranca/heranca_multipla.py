class Animal:
    def __init__(self, patas):
        self.patas = patas
        

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"    

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw): 
        self.cor_pelo = cor_pelo
        super().__init__(**kw)
        

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)

class Cachorro(Mamifero):
    pass


class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Ornitorrinco(Mamifero,Ave):
    pass


gato = Gato(patas=4, cor_pelo="Preto")
print(gato)
print()

ornitorrinco = Ornitorrinco(patas=2, cor_pelo="Azul", cor_bico="Azul")
print(ornitorrinco)


class Foo:
    def hello(self):
        print(self.__class__.__name__.lower())


class Bar(Foo):
    def hello(self):
        return super().hello()


bar = Bar()
bar.hello()