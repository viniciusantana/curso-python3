"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""

"""

string = 'vinicius'
string[3] = 'abc' # gera erro pois 'vinicius' é imutável
print(string)
"""

stringb = 'luiz otavio'
outra_variavel = f'{stringb[0:3]}ABC{stringb[4:]}'
print(stringb)
print(outra_variavel)


string = '1000'
print(string.zfill(10))