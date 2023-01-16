"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
# print(variavel[início:fim:passos])
# passos = de quantos em quantos caracteres vai pular
print(variavel[5]) # u
print(variavel[-4]) # u


print(variavel[4:]) # mundo
print(variavel[4:8]) # mund

print(variavel[0:5]) # olá m
print(variavel[:5]) # olá m

print(len(variavel)) # 9
print(len(variavel[3])) # 1

print(variavel[0:9:1]) # olá mundo
print(variavel[::1]) # olá mundo
print(variavel[0:9:2]) # oámno
print(variavel[::2]) # oámno


print(variavel[::-1]) # odnum álO
print(variavel[0:9:-1]) #  **não exibe nada
print(variavel[-1:-10:-1]) # odnum álO