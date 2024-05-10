class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Iniciando a classe")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instancia da classe")    


    def falar(self):
        print("AUAU")


def criar_cachorro():
    c1 = Cachorro("Zeus", "Branco e Preto", False)
    print(c1.nome)


c = Cachorro("Chappie", "amarelo")
c.falar()  

criar_cachorro()

print("Ola Mundo")

del c

print("Ola Mundo")
print("Ola Mundo")
print("Ola Mundo")

