COMISSAO = 15 / 100

nome = input('Digite o nome do vendedor: ')
salario_minimo = float(input('Digite o salário mínimo: R$'))
valor_vendas = float(input('Digite o valor das vendas mensais: R$'))

print(f'O vendedor(a) {nome} ganhará um total de R${salario_minimo + (valor_vendas * COMISSAO / valor_vendas * 100) }')
