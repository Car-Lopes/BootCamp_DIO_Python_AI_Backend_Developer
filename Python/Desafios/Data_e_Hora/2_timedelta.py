from datetime import date, datetime, timedelta, time

tipocarro = 'G' # P, M, G
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipocarro == 'P':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou : {data_atual} e ficará pronto às {data_estimada}")
elif tipocarro == 'M':
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"O carro chegou : {data_atual} e ficará pronto às {data_estimada}")
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"O carro chegou : {data_atual} e ficará pronto às {data_estimada}")


print(date.today() - timedelta(days=1))    

resultado = datetime(2024, 5, 21, 10, 19, 20) - timedelta(hours=1)
print(resultado.time())

print(datetime.now().date())