arquivo = open(
    "Python/Desafios/Manipulação_Arquivos/teste.txt", "w"
)

arquivo.write("Escrevendo um novo arquivo.")
arquivo.writelines("Python")

arquivo.close()