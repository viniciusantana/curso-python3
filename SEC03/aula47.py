"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

palavra_secreta = 'python'
palavra_escondida = '******'

print('Adivinhe qual é a palavra secreta!')
print('Regra: Você deve digitar apenas uma letra por vez!')

tentativas = 0

while True:
    print(' ')
    letra = input('Digite uma letra(0 para sair): ').lower()
    if letra == '0':
        print('Bye bye')
        break
    
    if(len(letra) != 1):
        print('você deve digitar apenas uma letra!')
        continue
    
    '''
    if palavra_secreta.count(letra) >= 1:
        print(f'A letra "{letra}" está na palavra secreta')
    else:
        print(f'A letra "{letra}"  não está na palavra secreta')
    '''

    nova_palavra = ''

    for i in range(len(palavra_secreta)):
        if palavra_secreta[i] == letra:
            nova_palavra += letra
        else:
            nova_palavra += palavra_escondida[i]
    
    palavra_escondida = nova_palavra

    print('Palavra: ',palavra_escondida)

    tentativas += 1
    print(f'Número de tetativas: {tentativas}')

    if palavra_escondida == palavra_secreta:
        print('Parabéns Você completou o jogo')
        break

