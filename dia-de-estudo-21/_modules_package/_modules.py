# Added numbers:
def _add(x, y):
    return x + y

# Creates new functions:
def create_functions(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna

# Multiply numbers:
def mult(x, y):
    return x * y