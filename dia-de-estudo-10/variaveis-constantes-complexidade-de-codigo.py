"""
CONSTANTE = "Variáveis" que não vão mudar em letra maiúscula para os outros entenderem
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

velocidade = 60  # velocidade atual do carro
local_carro = 107  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

velocidade_do_carro_passou_radar_1 = velocidade > RADAR_1


carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE)


if velocidade_do_carro_passou_radar_1:
    print('Carro está acima do limite de velocidade')
else:
    print('Carro abaixo do limite de velocidade')

if carro_passou_radar_1:
    print('Carro passou pelo radar')
else:
    print('Carro não passou pelo radar')

if carro_passou_radar_1 and velocidade_do_carro_passou_radar_1:
    print('Caroo multado em radar 1')
else:
    print('Carro não multado')