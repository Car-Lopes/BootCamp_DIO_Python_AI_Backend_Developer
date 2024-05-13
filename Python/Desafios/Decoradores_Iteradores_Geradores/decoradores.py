def mensagem(nome):
    print(f'executando nome')
    return f'oi {nome}'

def mensagem_longa(nome):
    print('executando a mensagem longa')
    return f'Ola tudo bem com voçê {nome}?'

def executar(funcao, nome):
    print("Executando executar")
    return funcao(nome)

print(executar(mensagem, "joao"))
print(executar(mensagem_longa, "Carlos"))