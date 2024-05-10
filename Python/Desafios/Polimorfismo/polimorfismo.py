class Passaro:
    def voar(self):
        print("Voando...")


class Pardal(Passaro):
    def voar(self):
        super().voar()



class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")


class Arara(Passaro):
    def voar(self):
       super().voar()



def plano_voo(obj):
    obj.voar() 


p1 = Pardal()
p2 = Avestruz()

plano_voo(p1)
plano_voo(p2)
plano_voo(Arara())