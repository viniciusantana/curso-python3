import random

nove_digitos = ''
for i in range(9):
  nove_digitos += str(random.randint(0, 9))

print(nove_digitos)
cpf_input = nove_digitos
cpf = cpf_input.replace('.', '').replace('-', '')

multiplicador = 10
soma1digito = 0
soma2digito = 0

for i in cpf:
  if multiplicador < 2:
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

print(f'CPF GERADO: {nove_digitos}{primeiroDigito}{segundoDigito}')

# Gabarito/aula:
"""
import random

for _ in range(100):
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))

    contador_regressivo_1 = 10

    resultado_digito_1 = 0
    for digito in nove_digitos:
        resultado_digito_1 += int(digito) * contador_regressivo_1
        contador_regressivo_1 -= 1
    digito_1 = (resultado_digito_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    dez_digitos = nove_digitos + str(digito_1)
    contador_regressivo_2 = 11

    resultado_digito_2 = 0
    for digito in dez_digitos:
        resultado_digito_2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1
    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

    print(cpf_gerado_pelo_calculo)
"""
