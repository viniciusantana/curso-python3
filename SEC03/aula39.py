"""
Iterando strings com while
"""
#       012345678910
nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321
tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
print(nome[3])

nova_string = ''
nova_string += '*L*u*i*z* *O*t*á*v*i*o'

# Minha solução:

nome2 = input('Digite seu nome: ')
tamanho_nome = len(nome2)
nova_string2 = ''

incremento = 0
while incremento < tamanho_nome:
  nova_string2 += '*' + nome2[incremento]
  incremento += 1

print(nova_string2)

# SOLUÇÂO DO INSTRUTOR

"""
Iterando strings com while
"""
#       012345678910
# nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321


nome = 'Maria Helena'  # Iteráveis

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*' # O meu resultado é diferente por casa disso
print(novo_nome)