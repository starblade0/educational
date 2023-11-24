print('Calculadora de fatorial')
x = int(input('Insira um numero inteiro : '))
n1 = 1
resultado = 1

while n1 <= x:
    resultado *= n1
    n1 += 1
print(resultado)
