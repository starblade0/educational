print('Sequência de Fibonacci')
inpt = int(input('Digite um número: '))
bit = 2

fibonacci = [1, 2]

while bit <= inpt:
    next = fibonacci[-1] + fibonacci[-2]
