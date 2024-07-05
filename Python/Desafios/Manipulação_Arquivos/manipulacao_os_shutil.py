import os
import shutil
from pathlib import Path

#Criando arquivo dinamico
ROOT_PATH = Path(__file__).parent
#print(__file__)

#Criando um novo diretorio
#os.mkdir(ROOT_PATH / "novo-diretorio")

#Criando novo arquivo
#arquivo = open(ROOT_PATH / "novo.txt", "w")
#arquivo.close()

#Renomeando arquivo
#os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "alterando.txt")

#removendo arquivo
#os.remove(ROOT_PATH / "novo.txt")

#movendo para outro diretorio
shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / "novo-diretorio" / "novo.txt")