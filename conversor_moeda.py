print('Conversor de Moedas')
print('Que moeda será convertida?\n1 - Real\n2 - Dólar\n3 - Euro')
tipo = int(input('Digite aqui : '))
print('Para qual moeda será convertida?\n1 - Real\n2 - Dólar\n3 - Euro')
convert = int(input('Digite aqui : '))
qntd = float(input('Quanto dinheiro? Utilize ponto flutuante como vírgula : '))

# 1 - Real /// 2 - Dólar /// 3 - Euro

# Preços Moedas (USD)

USD = 1
BRL = 4.9
EUR = 0.92

# Conversão REAL para X

if tipo == 1:
    if convert == 1:
        print(f'BRL {round(qntd, 2)} = BRL {round(qntd, 2)}')
    if convert == 2:
        USD = qntd / BRL
        print(f'BRL {round(qntd, 2)} = USD {round(USD, 2)}')
    if convert == 3:
        EUR = (qntd / BRL) * EUR
        print(f'BRL {round(qntd, 2)} = EUR {round(EUR, 2)}')

# Conversão de DÓLAR para X

if tipo == 2:
    if convert == 1:
        print(f'USD {round(qntd, 2)} = BRL {round(BRL, 2)}')
