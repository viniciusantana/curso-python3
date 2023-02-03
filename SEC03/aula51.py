"""
Introdução ao empacotamento e desempacotamento
"""

# Gera erro:
# ------------------------------------------
# 1) Não há variáveis suficientes para os valores:
# too many values to unpack
# nome1, nome2 = ['Maria', 'Helena', 'Luiz'] 
#
# 2) não há valores suficientes para as variáveis:
# not enough values to unpack
# nome1, nome2, nome3, nome4 = ['Maria', 'Helena', 'Luiz'] 
# ------------------------------------------

# corretos:
_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
_, _, nome2, *_ = ['Maria', 'Helena', 'Luiz']
nome3, *_ = ['Maria', 'Helena', 'Luiz']


print(nome, nome2, nome3)