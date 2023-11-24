print('Calculadora de Números amigos. \n')
a = int(input('Digite o número A : '))
b = int(input('Digite o número B : '))
divisor = 2  # Começamos com 2, pois 1 já está na lista

divisores_a = [1]  # 1 é sempre um divisor próprio
divisores_b = [1]

### Testagem divisores A

while divisor < a:
    if a % divisor == 0:
        divisores_a.append(divisor)
    divisor += 1

print(divisores_a, divisores_b)
