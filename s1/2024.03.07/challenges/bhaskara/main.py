from calc import bhaskara, delta
import utils

def main():
    # Aviso para que o sistema funcione melhor
    print('Para que o sistema funcione bem, você precisa primeiramente \n'+'manipular sua equação até que fique assim: `AX² + BX + C = 0´')

    utils.print_separator()
    
    # Insere os termos a equação principal
    a = utils.print_equacao() 
    b = utils.print_equacao(a) 
    c = utils.print_equacao(a, b) 
    
    utils.print_separator()

    # Mostra a equação final
    print('>>>Sua equação é: ', end='')
    utils.print_equacao(a, b, c)
    
    utils.print_separator()

    # Faz os cálculos
    d = delta(a, b, c) 
    res = bhaskara(a, b, d)

    if res['error']: 
        return print(res['error'])
        
    # Mostra resultado final
    print(f'X¹ é igual a: {res['x1']}')
    print(f'X² é igual a: {res['x2']}')

if __name__ == '__main__':
    main()
