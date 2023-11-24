print('Calculadora de Números amigos. \n')
a = int(input('Digite o número A : '))
b = int(input('Digite o número B : '))
divisor = 2

divisores_a = [1]
divisores_b = [1]

# Testagem divisores A

while divisor < a:
    if a % divisor == 0:
        divisores_a.append(divisor)
    divisor += 1

# Testagem divisores B

divisor = 2
while divisor < b:
    if b % divisor == 0:
        divisores_b.append(divisor)
    divisor += 1

# Calculo de números amigos

if sum(divisores_a) == b and sum(divisores_b) == a:
    print('\nSão números amigos!\n')
else:
    print('\nSão números normais!\n')


print(f'Divisores de A = {divisores_a} \nDivisores de B = {divisores_b}')
print(f'Soma divisores A = {sum(divisores_a)} \nSoma divisores B = {sum(divisores_b)}')
