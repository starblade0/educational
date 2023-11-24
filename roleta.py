from random import randrange

# Geração de número aleatório
x = randrange(1, 6)
y = int(input('Adivinhe o número inteiro escolhido pela máquina entre 1 a 6: '))

# Possíveis respostas caso não cumpra parâmetros
if y > 6:
    print('Burro, é até 6.')
if y < 0:
    print('Não pode menos que zero cabeção.')

# Erro
if x == y:

    print('Acertou! A máquina realmente escolheu {}.'.format(x))

# Acerto
else:
    print('Errou!')
    print('A máquina escolheu {}.'.format(x))
