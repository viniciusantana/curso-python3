"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3
lista = [10, 20, 30, 40]
print(lista)
lista.append('Luiz') 
print(lista) # [10, 20, 30, 40, 'Luiz']

nome = lista.pop()
print(lista) # [10, 20, 30, 40]

lista.append(1233)
print(lista) # [10, 20, 30, 40, 1233]

del lista[-1]
print(lista) # [10, 20, 30, 40]

# lista.clear() # []

lista.insert(0, 5) 
print(lista) # [5, 10, 20, 30, 40]

lista.insert(3, 5) 
print(lista) # [5, 10, 20, 5, 30, 40] 

print(lista[4])