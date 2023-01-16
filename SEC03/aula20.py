valor01 = input('Digite o valor: ')
valor02 = input('Digite outro valor: ')

if valor01 > valor02:
  print('O primeiro valor é maior que o segundo')
elif valor01 < valor02:
  print('Segundo valor é maior que o primeiro')
else:
  print('Os valores são iguais')

'''
# Solução proposta:

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor >= segundo_valor:
    print(
        f'{primeiro_valor=} é maior ou igual '
        f'ao que {segundo_valor=}'
    )
else:
    print(
        f'{segundo_valor=} é maior '
        f'do que {primeiro_valor=}'
    )
'''
