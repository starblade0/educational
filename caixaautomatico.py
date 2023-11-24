print('Caixa automático :')
sacar = int(input('Por favor, insira a quantidade que deseja sacar: '))

notas = [200, 100, 50, 20, 10, 5, 2]

print('O saque será de = {}'.format(sacar))
for nota in notas:
    retirado = sacar//nota
    if retirado > 0:
        print(f'{retirado} de R${nota}')
        sacar -= nota * retirado

if sacar > 0:
    print('Não foi possível retirar todo o valor necessário do saque.')
