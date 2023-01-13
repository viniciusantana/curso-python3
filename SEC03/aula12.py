# Exercício de programação - Cálculo do IMC (Índice de Massa Corpórea) + Ellipsis

nome = 'vinicius'
altura = 1.69
peso = 75
# IMC = Peso ÷ (Altura × Altura)
imc = peso / (altura * altura)

print(nome, 'mede', str(altura) + 'm', 'e pesa', str(peso) + 'kg' )
print('Seu IMC atual é:')
print(imc)

'''
# SOLUÇÃO PROPOSTA:

nome = 'Luiz Otávio'
altura = 1.80
peso = 95
imc = peso / altura ** 2

print(nome, 'tem', altura, 'de altura,',)
print('pesa', peso, 'quilos e seu imc é',)
print(imc)

# Luiz Otávio tem 1.80 de altura,
# pesa 95 quilos e seu IMC é
# 29.320987654320987

'''