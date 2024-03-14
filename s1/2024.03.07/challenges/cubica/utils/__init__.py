from time import sleep

def print_equacao(a=None,b=None,c=None,d=None):
    try:
        empty_key = '\033[32m_\033[m'

        if a is None:
            str_equacao = f'y = {empty_key}³ + BX² + CX + D'
        elif b is None:
            str_equacao = f'y = {a if a != 1 else ""}X³ + {empty_key}X² + CX + D'
        elif c is None:
            str_equacao = f'y = {a if a != 1 else ""}X³ + {b if b != 1 else ""}X² + {empty_key}X + D'
        elif d is None:
            str_equacao = f'y = {a if a != 1 else ""}X³ + {b if b != 1 else ""}X² + {c if c != 1 else ""}X + {empty_key}'
        else:    
            str_equacao = f'y = {a if a != 1 else ""}X³ + {b if b != 1 else ""}X² + {c if c != 1 else ""}X + {d}'
            return sleep(2)

        print(str_equacao)
        return int(input('>>> '))
    except Exception as err: 
        raise Exception(err)

def print_separator(length=30):
    return print('-' * length)