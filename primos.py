print('Verificador de Número Primo')
x = int(input('Digite um valor: '))
y = 2
primo = True

if x < 2 :
    print('Números menores ou iguais a 1 não podem ser primos.')
    exit()

while y <= x//2:
    if x % y == 0:
        primo = False
        break
    y += 1

if primo is True:
    print('É primo')
else:
    print('Não é primo')
