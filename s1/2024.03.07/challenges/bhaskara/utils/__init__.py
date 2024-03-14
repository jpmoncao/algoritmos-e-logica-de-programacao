from time import sleep

def print_equacao(a=None,b=None,c=None):
    empty_key = '\033[32m_\033[m'

    if a is None:
        str_equacao = f'{empty_key}² + BX + C = 0'
    elif b is None:
        str_equacao = f'{a if a != 1 else ""}X² + {empty_key}X + C = 0'
    elif c is None:
        str_equacao = f'{a if a != 1 else ""}X² + {b if b != 1 else ""}X + {empty_key} = 0'
    else:    
        print(f'{a if a != 1 else ""}X² + {b if b != 1 else ""}X + {c} = 0')
        return sleep(2)

    print(str_equacao)
    return int(input('>>> '))

def print_separator(length=30):
    return print('-' * length)