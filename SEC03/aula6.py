# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
#  tipos imutáveis e primitivos:
# str, int, float, bool
print(int('1'), type(int('1')))
print(type(float('1') + 1))
print(bool(' '))
# print(11 + 'b') => ERROR não soma int + str 
print(str(11) + 'b')
"""
1 <class 'int'>
<class 'float'>
True
11b
"""
