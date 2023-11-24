def soma(x, y):
    return(x + y)

def subtracao(x, y):
    return(x - y)

def multiplicacao(x, y):
    return(x * y)

def divisao(x, y):
    return(x / y)

def potencia(x, y):
    return(x ** y)

print('Calculadora Básica:')
print('Qual o tipo de operação?\n 1- Soma\n 2 - Subtração\n 3 - Multiplicação\n 4 - Divisão\n 5 - Potenciação')
op = int(input('Digite : '))
a = float(input('Digite o valor A : '))
b = float(input('Digite o valor B : '))

if op == 1:
    x = soma(a, b)
    print(x)
if op == 2:
    x = subtracao(a, b)
    print(x)
if op == 3:
    x = multiplicacao(a, b)
    print(x)
if op == 4:
    x = divisao(a, b)
    print(x)
if op == 5:
    x = potencia(a, b)
    print(x)
