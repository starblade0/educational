print('Conversor Celsius/Fahrenheit')
print('Você quer converter Celsius ou Fahrenheit para a outra forma?')
tipo = int(input('0 - Celsius \n1 - Fahrenheit '))
graus = int(input('Quantos graus? : '))

# Formula = (1 °C × 9/5) + 32 = 33,8 °F

if tipo == 0:
    C = graus
    F = (C*9/5)+32
    print(f'{F}º Fahrenheit = {C}º Celsius')
else:
    F = graus
    C = (F-32)/1.8
    print(f'{C}º Celsius = {F}º Fahrenheit')
