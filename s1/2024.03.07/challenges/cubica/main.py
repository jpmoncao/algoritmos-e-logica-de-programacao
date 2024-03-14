from calc import bhaskara, delta
import utils

def main():
    try:
        # Aviso para que o sistema funcione melhor
        print('Para que o sistema funcione bem, você precisa primeiramente \n'+'manipular sua equação até que fique assim: `y= AX³ + BX² + CX + D´')

        utils.print_separator()
        
        # Insere os termos a equação principal
        a = utils.print_equacao() 
        b = utils.print_equacao(a) 
        c = utils.print_equacao(a, b) 
        d = utils.print_equacao(a, b, c) 
        
        utils.print_separator()

        # Mostra a equação final
        print('>>>Sua equação é: ', end='')
        utils.print_equacao(a, b, c)
        
        utils.print_separator()

        # Faz os cálculos
        d = delta(a, b, c) 
        res = bhaskara(a, b, d)
        
        # Mostra resultado final
        print(f'X¹ é igual a: {res['x1']}')
        print(f'X² é igual a: {res['x2']}')
    except Exception as err:
        raise err.args

if __name__ == '__main__':
    main()
