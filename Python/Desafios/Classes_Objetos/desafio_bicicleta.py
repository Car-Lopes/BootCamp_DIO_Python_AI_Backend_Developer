class Bicicleta:
    # pass - vazia
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("BI BI...")

    def parar(self):
        print("Freiar")

    def correr(self):
        print("Vrummmmm")  
    """
    def __str__(self):
        return f"BICICLETA: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"
    """

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    

bicicleta1 = Bicicleta("vermelha", "caloi", 2022, 1200)         
bicicleta1.buzinar()
bicicleta1.parar()
bicicleta1.correr()

print(bicicleta1.cor, bicicleta1.modelo)


bicicleta2 = Bicicleta("azul", "monark", 2000, 600)  
bicicleta2.buzinar()
Bicicleta.buzinar(bicicleta2)

print(bicicleta2.cor, bicicleta2.modelo)
print(bicicleta2)
print(bicicleta1)
