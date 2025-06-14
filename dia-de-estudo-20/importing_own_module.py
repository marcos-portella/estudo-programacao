from _modules_package import _modules
import _modules_package
print('Este módulo se chama', __name__)
# print('Este módulo se chama', __name__)
print(_modules._add(2, 3)) # Usando o nome do arquivo para chamar a função
print(_modules_package._add(2, 3)) # Usando o nome da pasta para chamar a função 

