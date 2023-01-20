"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input('Digite uma hora atual entre 0 e 23: ')
try:
  # hora_float = float(hora) # Para aceitar a hora em fração até 23.9
  hora_int = int(hora)
  if hora_int >= 0 and hora_int < 12:
    print('Bom dia')
  elif hora_int >= 12 and hora_int < 18:
    print('Boa tarde')
  elif hora_int >= 18 and hora_int < 24:
    print('Boa noite')
  else:
    print(f'A hora digitada tem que ser um número de 0 a 23')
except:
  print('O valor digitado tem que ser um número inteiro entre 0 e 23')