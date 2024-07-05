#Abrindo e lendo o arquivo
arquivo = open("Python\Desafios\Manipulação_Arquivos\lorem.txt", "r")

print(arquivo.read())
#print(arquivo.readline()) #chama uma linha por vez 
#print(arquivo.readlines()) #retorna uma lista 

'''
for linha in arquivo.readlines():
    print(linha) '''

#dica
#while len(linha := arquivo.readline()):
#    print(linha)

arquivo.close()