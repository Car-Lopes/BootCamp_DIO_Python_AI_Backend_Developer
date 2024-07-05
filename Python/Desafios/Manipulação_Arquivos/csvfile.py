import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

#Escrevendo um CSV
''' 
try:
    with open(ROOT_PATH / "csvfile.csv", "w", newline='') as csvfile:
        escritor = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        escritor.writerow(['id', 'nome'])
        escritor.writerow(['1', 'Maria'])
        escritor.writerow(['2', 'joao'])
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")
except AttributeError as exc:
    print(f"Erro ao escrever o arquivo. {exc}")    '''


#Lendo um CSV
try:
    with open(ROOT_PATH / "csvfile.csv", "r", newline='') as csvfile:
        leitor = csv.reader(csvfile, quoting=csv.QUOTE_ALL)
        for row in leitor:
            print(row)
except IOError as exc:
    print(f"Erro ao ler o arquivo. {exc}")
except AttributeError as exc:
    print(f"Erro ao ler o arquivo. {exc}")
