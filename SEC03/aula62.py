"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14
Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O segundo dígito do CPF é 0
"""

cpf_input = '746.824.890-70'
cpf = cpf_input.replace('.', '').replace('-', '')

multiplicador = 10
soma1digito = 0
soma2digito = 0

for i in cpf:
  if multiplicador < 2:
    # soma2digito += int(i) * ( multiplicador + 1 )
    break
  if i.isdigit():
    soma1digito += int(i) * multiplicador
    soma2digito += int(i) * ( multiplicador + 1 )
    multiplicador -= 1

primeiroDigito = (soma1digito * 10) % 11
primeiroDigito = 0 if primeiroDigito > 9 else primeiroDigito

soma2digito += primeiroDigito * 2
segundoDigito = (soma2digito * 10) % 11
segundoDigito = 0 if segundoDigito > 9 else segundoDigito

print(primeiroDigito, segundoDigito)


