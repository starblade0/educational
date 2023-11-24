from random import uniform
from random import randrange

compra1 = randrange(1, 100)
compra2 = randrange(100, 500)
compra3 = uniform(compra1, compra2)
compra3 = round(compra3, 2)
print(f'Preço total: {compra3}')

# Solicitar ao usuário o valor do troco
troco = float(input("Digite o valor do troco: "))

# Lista de valores de notas e moedas disponíveis
valores = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05]

# Iterar sobre os valores e contar as notas/moedas necessárias
for valor in valores:
    quantidade = troco // valor
    troco -= quantidade * valor

    if quantidade > 0:
        if valor >= 1:
            print(f"{int(quantidade)} notas de {valor}")
        else:
            print(f"{int(quantidade)} moedas de {valor:.2f}")
