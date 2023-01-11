"""
DocString
Python = Linguagem de programação
Tipo de tipagem = Dinâmica / Forte
str -> string -> texto
Strings são textos que estão dentro de aspas
"""
print(1234)

# Aspas simples
print('Luiz Otávio') # Saída: Luiz Otávio
print(1, 'Luiz "Otávio"') # Saída: 1 Luiz "Otávio"
#print(1, 'Luiz 'Otávio'') # <-- gera erro! tem que utilizar o escape ou inverter aspas 

# Aspas duplas
print("Luiz Otávio") # Saída: Luiz Otávio
print(2, "Luiz 'Otávio'") # Saída: 2 Luiz 'Otávio'
#print(1, "Luiz "Otávio""") # <-- gera erro! 

# Escape
print("Luiz \"Otávio\"") # Saída: Luiz "Otávio"
print("Luiz \"Otávio") # Saída: Luiz "Otávio


# r -> utilizado para expressões regulares
print(r"Luiz \"Otávio\"") # saída: Luiz \"Otávio\"