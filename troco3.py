from random import randrange
from random import uniform

c1 = randrange(1, 500)
c2 = randrange(1, 500)
c3 = uniform(c1, c2)
c3 = round(c3, 2)

trocos = [200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05]

print(f'O total da compra foi: {c3}')
pagto = float(input('Insira o valor pago: '))
troco = pagto - c3

if pagto < c3:
    print(f'Há um débito de {round(troco, 2)}')

else:
    print(f'Troco a ser devolvido: {round(troco, 2)}')
    for valor in trocos:
        quantidade = troco//valor
        troco -= quantidade*valor

        if quantidade > 0:
            if valor >= 2:
                print(f'{int(quantidade)} notas de {valor}')
            else:
                print(f'{int(quantidade)} moedas de {valor:.2f}')
