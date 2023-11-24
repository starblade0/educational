from random import randrange

x = randrange(1, 100)
y = 0
print('A máquina randomizou um número entre 1 e 100!')
print('Qual valor que você acha que é?')
while x != y:

    ans = int(input())

# Erro >
    if x > ans:
        print('Mais!')

# Erro <
    elif x < ans:
        print('Menos!')

# Acerto
    if x == ans:
        print('Acertou miserável!')
        exit()
