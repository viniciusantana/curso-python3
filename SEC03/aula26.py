"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variavel = 'ABC'
print(f'{variavel}') # ABC
print(f'{variavel: >10}') #          ABC
print(f'{variavel: <10}.') # ABC          .
print(f'{variavel: ^10}.') #    ABC       .
print(f'{1000.4873648123746:0=+10,.1f}') # +001,000.5
print(f'O hexadecimal de 1500 é {1500:08X}') # O hexadecimal de 1500 é 000005DC 
print(f'{variavel!r}') # 'ABC'