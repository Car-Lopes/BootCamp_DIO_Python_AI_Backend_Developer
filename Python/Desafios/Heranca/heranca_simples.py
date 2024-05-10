class Veiculo:
    def __init__(self, cor, placa, rodas):
        self.cor = cor
        self.placa = placa
        self.rodas = rodas

    def ligar_motor(self):
        print("Ligando o motor")

  #  def __str__(self):
   #     return self.cor    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Motocicleta(Veiculo):
    pass            

class Caminhao(Veiculo):
    def __init__(self, cor, placa, rodas, carregado):
        super().__init__(cor, placa, rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

moto = Motocicleta("Preta", "ABC-1234", 2)
print(moto)
moto.ligar_motor()
print()

caminhao = Caminhao("roxo", "gfd-8712", 8, True)
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao)

