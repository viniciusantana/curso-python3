# Precedência entre os operadores aritméticos:

# 1. (n + n)
# 2. **
# 3. * / // % 
# 4. + -
# Operadores de mesma precedência são executados da esquerda para direita
conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_1)
