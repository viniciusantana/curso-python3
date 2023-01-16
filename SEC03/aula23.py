# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True
senha = input('Senha: ')

if not senha:
  print('você não digitou nada')

# ------------------

print(not True)  # False
print(not False)  # True

print(not 1)  # False
print(not 0)  # True
