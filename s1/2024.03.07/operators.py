from math import sqrt

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

print('-=' * 30)

print(f'{n1} + {n2}: {n1 + n2}')
print(f'{n1} - {n2}: {n1 - n2}')
print(f'{n1} * {n2}: {n1 * n2}')
print(f'{n1} / {n2}: {n1 / n2}')
print(f'mod({n1}, {n2}): {n1 % n2}')
print(f'{n1} ^ {n2}): {n1 ** n2}')
print(f'raiz de {n1}: {sqrt(n1)}')
print(f'raiz de {n2}: {sqrt(n2)}')