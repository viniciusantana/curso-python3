# .count('x') => conta a qtd de caracteres x em uma string 
# .lower() => converte tudo para minuscula
# .upper() => converte tudo para maiuscula

# Minha resolução
while True:
  frase = input('Digite uma frase: ').lower()
  i = 0
  letra_mais_repetida = ''
  qtd_repeticao_letra = 0

  while i < len(frase):
    letra_atual = frase[i]
    # print(letra_atual, frase.count(letra_atual))

    if frase.count(letra_atual) > qtd_repeticao_letra:
      letra_mais_repetida = letra_atual
      qtd_repeticao_letra = frase.count(letra_atual)
    
    i += 1
  
  print('A Letra mais repetida foi: ', letra_mais_repetida, f'Repetida {qtd_repeticao_letra}x')

  sair = input('Quer sair? [s]im: ').lower().startswith('s')

  if sair is True:
    break


# Resolução do instrutor:

frase = 'aaaooo'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ': # <= Faltou esse detalhe na minha resolução
        i += 1
        continue

    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)