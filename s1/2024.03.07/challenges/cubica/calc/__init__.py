from math import sqrt

def delta(a, b, c):
    try:
        return b**2 - 4 * a * c
    except Exception as err: 
        raise Exception(err)

def bhaskara(a, b, delta):
    try:
        if delta < 0:
            raise Exception("error": "A equação não possui raízes reais.")
        elif delta < 0:
            raise Exception("error": "A raiz é igual a 0.")
        else:
            x1 = ((b * -1) + sqrt(delta)) / (2 * a)
            x2 = ((b * -1) - sqrt(delta)) / (2 * a)
            return {"x1":x1, "x2":x2}
    except Exception as err: 
        raise Exception(err)