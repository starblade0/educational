from random import uniform
from random import randrange
r1 = randrange(1, 100)
r2 = randrange(100, 500)
r3 = uniform(r1, r2)
r3 = round(r3, 2)

print('Troco: {}'.format(r3))

n100 = r3//100
print('{} notas de 100'.format(n100))
r3 = r3 - (n100*100)

n50 = r3//50
print('{} notas de 50'.format(n50))
r3 = r3 - (n50*50)

n20 = r3//20
print('{} notas de 20'.format(n20))
r3 = r3 - (n20*20)

n10 = r3//10
print('{} notas de 10'.format(n10))
r3 = r3 - (n10*10)

n5 = r3//5
print(f'{n5} notas de 5')
r3 = r3 - (n5*5)

n2 = r3//2
print(f'{n2} notas de 2')
r3 = r3 - n2*2

m1 = r3//1
print(f'{m1} moedas de 1')
r3 = r3 - m1*1

m50 = r3//0.5
print(f'{m50} moedas de 0.5')
r3 = r3 - m50*0.5

m25 = r3//0.25
print(f'{m25} moedas de 0.25')
r3 = r3 - m25*0.25

m10 = r3//0.10
print(f'{m10} moedas de 0.10')
r3 = r3 - m10*0.1

m5 = r3//0.05
print(f'{m5} moedas de 0.05')
r3 = r3 - m5*0.05
