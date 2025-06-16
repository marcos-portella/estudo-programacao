def type_int_float(func):
    def internal(*args, **kwargs):
        for arg in args:
            e_int_float(arg)
        resultado = func(*args, **kwargs)
        return resultado
    return internal

def e_int_float(param):
    if not isinstance(param, int|float):
        raise TypeError('add a int or float')
    

# Added numbers:
@type_int_float
def _add(x, y):
    return x + y


# Creates new functions:
def create_functions(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna

# Multiply numbers:
@type_int_float
def _mult(x, y):
    return x * y


