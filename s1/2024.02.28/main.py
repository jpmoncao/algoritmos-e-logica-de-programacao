from math import sqrt

print('Para que o sistema funcione bem, você precisa primeiramente \n'+	'separar equação até que fique assim: `AX² + BX + C = 0´')

a = int(input('Termo A (sem o X²): '))
b = int(input('Termo B (sem o X): '))
c = int(input('Termo C: '))

delta = b**2 - 4 * a * c

if delta < 0:
    print("A equação não possui raízes reais.")
else:
    x1 = ((b * -1) + sqrt(delta)) / (2 * a)
    x2 = ((b * -1) - sqrt(delta)) / (2 * a)
    print(f'X¹ é igual a: {x1}')
    print(f'X² é igual a: {x2}')

print('=)')