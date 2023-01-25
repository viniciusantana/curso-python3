"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""

"""

lista = ['Maria', 'Helena', 'Luiz']

posicao = 0
for nome in lista:
    print(posicao, nome)
    posicao += 1
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João') # ['Maria', 'Helena', 'Luiz', 'João']


indices = range(len(lista))
# len(lista) => 4
# range(len(lista)) => (0:3)

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))