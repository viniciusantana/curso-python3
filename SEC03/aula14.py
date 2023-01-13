a = 'AAAAA'
b = 'BBBBBB'
c = 1.1

'''

# retorna os argumentos em sequencia dentro de format

formato = 'a={} b={} c={}'.format(a, b, c)

print(formato) # a=AAAAA b=BBBBB c=1.1
'''

string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c # nome1, nome2 e nome3 são parâmetros nomeados
)

print(formato) # b=BBBBBB a=AAAAA a=AAAAA c=1.10

'''
# Pegando pelo indice 0, 1 e 2.... retorna a sequência a, b, c

string = 'a={0} b={1} c={2:.2f}' 
formato = string.format(a, b, c)

print(formato) # a=AAAAA c=1.10 b=BBBBB
'''

'''
# Pegando pelo indice 0 2 e 1.... retorna a sequencia a, c, b

string = 'a={0} c={2:.2f} b={1}'
formato = string.format(a, b, c)

print(formato) # a=AAAAA c=1.10 b=BBBBB

'''

'''
# retorna dependendo da sequencia dentro format
string = 'a={} b={} c={}'
formato = string.format(a, b, c)

print(formato) # a=AAAAA b=BBBBB c=1.1
'''

'''
# Gera erro por naõ ter argumento correcpondente
string = 'a={} b={} c={} d={}'
formato = string.format(a, b, c)

print(formato) # a=AAAAA b=BBBBB c=1.1
'''
a = 1 + 'a'