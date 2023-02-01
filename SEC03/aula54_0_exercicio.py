lista_compras = []

while True:
  print('Selecione uma opção:')
  opcao = input('[i]inserir [a]pagar [l]istar [s]air: ')

  if opcao == 's':
    print(f'Bye Bye!\n')

    break
  elif opcao == 'i':
    item = input('Digite item: ')
    lista_compras.append(item)
    print(f'Item adicionado!\n')
  elif opcao == 'a':
    indice = input('Digite o indice do item: ')
    if indice.isdigit() and int(indice) < len(lista_compras):
      lista_compras.pop(int(indice))
    else:
      print(f'Indice invalido!\n')
  elif opcao == 'l':
    print('Lista de compras:')
    for index, item in enumerate(lista_compras):
      print(f'{index}. {item}') 
  else:
    print(f'Opção invalida!\n')