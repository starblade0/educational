print('Soma de todos os anteriores')
x = int(input('Dê o valor que deverá ser somado a todos os números naturais anteriores : '))
resultado = (x+1)*(x//2)
print(f'O resultado da soma é : {resultado}')

if x < 0:
    print('Por favor, insira um valor positivo para a soma.')
