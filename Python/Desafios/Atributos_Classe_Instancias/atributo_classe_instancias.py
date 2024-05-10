class Estudante:
    escola = "Dio"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula


    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"
    

def mostrar_valore(*objs):
    for obj in objs:
        print(obj)


aluno1 = Estudante("Gui", 1)   
aluno2 = Estudante("Guilher", 2)
mostrar_valore(aluno1, aluno2)

print()
Estudante.escola = "Python"
aluno1.matricula = 3 
mostrar_valore(aluno1, aluno2)

print()
aluno3 = Estudante("Car", 4)
aluno3.escola = "Mob"
mostrar_valore(aluno1, aluno2, aluno3)
