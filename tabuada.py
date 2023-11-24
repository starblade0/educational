print('Tabuada do 1 ao 10')
x = 1

while x <= 10:
    y = 1
    while y <= 10:
        print(f'{x} x {y} = {x*y}')
        y += 1
    x += 1
    print('-----------------')