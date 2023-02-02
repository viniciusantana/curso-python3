# Seção 03: Iniciando na programação com Python
- Lógica de programação básica

## Aulas
### Introdução ao bloco
- [x] 13. O que vamos aprender? Devo seguir essa seção? 2m
- [x] 14. Me ajude a produzir conteúdo gratuito (texto)
- [x] 15. Criando meu primeiro módulo Python (*.py) 4m
```
Ao criar uma pasta/arquivo não utilizar espaços, acentos ou iniciar com números
```
- [x] 16. O interpretador do Python + comentários de código. [aula1.py](aula1.py) 4m 
- [x] 17. Docstrings como comentários. [aula1.py](aula1.py) 5m
- [x] Teste 1: Sobre comentários (prova)

###  Tipos de dados e função print
- [x] 18. A função print. [aula2.py](aula2.py) 12m
- [x] 19. Tipo str (string) - Introdução aos tipos de dados [aula3.py](aula3.py) 9m
- [x] Teste 2: Sobre print e str (prova)
- [x] 20. Tipo int e float (números) - Introdução aos tipos de dados [aula4.py](aula4.py) 11m
- [x] 21. Tipo bool (boolean) - Introdução aos tipos de dados [aula5.py](aula5.py) 7m
- [x] Teste 3: Sobre int, float e bool
- [x] 22. Coerção de tipos [aula6.py](aula6.py) (convertendo um tipo para outro) 13m
- [x] 23. Introdução às variáveis em Python [aula7.py](aula7.py) 12m
- [x] 24. Exercício com variáveis e tipos de dados [aula8.py](aula8.py) 3m
- [x] 25. Solução - exercício com variáveis e tipos de dados [aula8.py](aula8.py) 4m

### Operadores aritméticos
- [x] 26. Introdução aos operadores aritméticos  [aula9.py](aula9.py)(matemática) 11m
- [x] 27. Concatenação (+) e repetição (*) com operadores aritméticos [aula10.py](aula10.py) 3m
- [x] 28. Precedência entre os operadores aritméticos [aula11.py](aula11.py) 7m
- [x] 29. Exercício de programação - Cálculo do IMC (Índice de Massa Corpórea) + Ellipsis [aula12.py](aula12.py) 3m
- [x] 30. Solução exercício de programação - Cálculo do IMC[aula12.py](aula12.py) 2m

### Formatação de strings
- [x] 31. Uma introdução às f-strings (formatação de strings) [aula13.py](aula13.py) 6m
- [x] 32. Formatação de strings com o método format [aula14.py](aula14.py) 12m
- [x] Teste 4: Teste seus conhecimentos

### Condicionais, input e operadores relacionais
- [x] 33. Usando a função input para coletar dados do usuário [aula15.py](aula15.py)  9m
- [x] 34. Introdução aos blocos de código + if / elif / else (condicionais) [aula16.py](aula16.py). 11m
- [x] 35. if, elif e else: entendendo o fluxo do interpretador em condicionais [aula17.py](aula17.py) 11m
- [x] 36. O Debugger do VS Code e o interpretador do Python lendo os códigos[aula18.py](aula18.py) 8m
- [x] 37. Operadores relacionais (de comparação) em Python 7m [aula19.py](aula19.py) 
- [x] 38. Exercício de programação com if e comparação [aula20.py](aula20.py)  3m
- [x] 39. Solução - Exercício de programação com if e comparação [aula20.py](aula20.py) 3m

### Operadores lógicos
- [x] 40. Operador Lógico "and" [aula21.py](aula21.py) 12m
- [x] Teste 5: Sobre and
- [x] 41. Operador Lógico "or" [aula22.py](aula22.py) 8m
- [x] 42. Operador lógico "not" [aula23.py](aula23.py) 4m
- [x] 43. Operadores in e not in [aula24.py](aula24.py) 7m
- [x] Teste 6: Teste seu conhecimento

### Interpolação e formatação de strings
- [x] 44. Interpolação de string com % em Python [aula25.py](aula25.py) 7m
- [x] 45. Formatação de strings com f-strings [aula26.py](aula26.py) 10m
- [x] 46. Fatiamento de strings e a função len [aula27.py](aula27.py)  11m
- [x] 47. Exercício: teste seu conhecimento até aqui [aula28.py](aula28.py) 3m
- [x] 48. Solução - Exercício: teste seu conhecimento até aqui [aula28.py](aula28.py) 5m

### Introdução ao try e except

<details><summary>Anotações</summary>
<p>

- try -> tentar executar o código e caso ocorra um erro passa par o except
- except -> ocorreu algum erro ao tentar executar

```
try:
    ...
except:
    ...
```
- A função `isdigit(X)` verifica se uma entrada 'X' é um número e retorna True ou False
- CONSTANTE = "Variáveis" que não vão mudar, sendo declarado em maiusculo
```
variavel = 10
CONTANTE = 10 
```
- Flag (Bandeira) - Marcar um local
- None = Não valor
- is e is not = é ou não é (tipo, valor, identidade)
- id = Identidade
- A função `id(X)` retorna o local na memória de uma variável 'X'
```
variavel = "a"
print(id(variavel)) # retorna local na memoria
```


</p>
</details>

- [x] 49. Introdução ao try e except para capturar erros (exceptions)[aula29.py](aula29.py) 15m
- [x] 50. Parte 1: Variáveis, constantes e complexidade de código [aula30.py](aula30.py) 7m
- [x] 51. Parte 2: Variáveis, constantes e complexidade de código [aula30.py](aula30.py) 9m
- [x] 52. id - A identidade do valor que está na memória [aula31.py](aula31.py) 3m
- [x] 53. Flags, is, is not e None [aula31.py](aula31.py) 11m
- [x] 54. Exercícios - Enunciados aula32_exercicio[[01]](aula32_exercicio01.py) [[02]](aula32_exercicio02.py) [[03]](aula32_exercicio03.py).py 4m
- [x] 55. Solução 1 dos Exercícios - Enunciados [aula32_solucao01.py](aula32_solucao01.py) 6m
- [x] 56. Solução 2 dos Exercícios - Enunciados [aula32_solucao02.py](aula32_solucao02.py)  7m
- [x] 57. Solução 3 dos Exercícios - Enunciados [aula32_solucao03.py](aula32_solucao03.py)  5m


### Estrutura de repetição while

<details><summary>Anotações</summary>
<p>

- Documentação tipos: https://docs.python.org/pt-br/3/library/stdtypes.html
- Olhar métodos de string na documentação acima.
- Imutáveis que vimos: str, int, float, bool
- Operadores de atribuição:

```
=   +=   -=   *=   /=   //=   **=   %=
```

- While (boleano):

```
while true:
    ...
    continue <=> deixa de executar restante do código e retorna ao início do while
    ...
    break <=> Sai do while

```
- Função `string.lower()` retorna string em minuscula
- Função `string.upper()` retorna string em maiuscula
- Função `string.startswith('X')` retorna True/False se string começar com `X`
- Função `string.count('X')` retorna a quantidade de vezes que `X` aparece em uma string
- Pegar erro e imprimir:
```
try:
    ...
except Exception as error:
    print(error)
```

</p>
</details>

- [x] 58. Conversa - tipos built-in, documentação, tipo imutáveis, métodos de string [aula33.py](aula33.py) 15m 
- [x] 59. while e break - Estrutura de repetição (Parte 1) [aula34.py](aula34.py) 10m
- [x] 60. while - Condição em detalhes [aula35.py](aula35.py) 9m
- [x] 61. Operadores de atribuição com operadores aritméticos [aula36.py](aula36.py) 5m
- [x] 62. while + continue - pulando alguma repetição [aula37.py](aula37.py) 8m
- [x] 63. while + while (laços internos)[aula38.py](aula38.py) 8m
- [x] 64. Exercício guiado com while [aula39.py](aula39.py)4m
- [x] 65. Solução do exercício guiado com while [aula39.py](aula39.py) 6m
- [x] 66. Exercício guiado - Calculadora - Parte 1 [aula40.py](aula40.py) 9m
- [x] 67. Exercício guiado - Calculadora - Parte 2 [aula40.py](aula40.py) 9m
- [x] 68. Exercício guiado - Calculadora - Parte 3 [aula40.py](aula40.py) 5m
- [x] 69. while / else (recurso peculiar do Python) [aula41.py](aula41.py) 5m
- [x] 70. while - Qual letra apareceu mais vezes na frase? (Iterando strings com while) [aula42.py](aula42.py) 14m
- [x] 71. DEBUGGER: while - Qual letra apareceu mais vezes na frase? [aula42.py](aula42.py) 7m
- [x] Teste 7: Teste

### Estrutura de repetição for e tipo List
<details><summary>Anotações</summary>
<p>

-----------------
#### For:
- for/in sting:
```

for letra in texto:
    print(letra)
```

- range -> range(start, stop, step)
```
for numeros in range(0, 5)
    print(numero) # 0 1 2 3 4

for numeros in range(0, 5, 2)
    print(numero) # 0 2 4 6 8

for numeros in range(len('palavra'))
    print(numero) # 0 1 2 3 4 5 6

```
- range(len(string)) 
- break - pode ser usado para sair do loop
- continue - pode ser usado para para um loop e ir ao próximo
- else - pode ser usado após finalizar o loop caso não seja usado o break



#### Funcionamento do for (74):
- Iterável -> str, range, etc `(__iter__)`
- Iterador -> quem sabe entregar um valor por vez
- next -> me entregue o próximo valor
- iter -> me entregue seu iterador

```
texto = 'Luiz'  # iterável
iterador = iter(texto)  # iterator -> retorna um local na memoria
letra = next(iteratador) # retorna a letra: L
letra = next(iteratador) # retorna a letra: u
letra = next(iteratador) # retorna a letra: i
letra = next(iteratador) # retorna a letra: z
letra = next(iteratador) # retorna ERRO: StopIteration
```

#### Lista
- Tipo list - Mutável
- Suporta vários valores de qualquer tipo
- Conhecimentos reutilizáveis - índices e fatiamento
- Métodos úteis:
    - append - Adiciona um item ao final
    - insert - Adiciona um item no índice escolhido
    - pop - Remove do final ou do índice escolhido
    - del - apaga um índice
    - clear - limpa a lista
    - extend - estende a lista
    - `+ -` concatena listas
    - copy - serve para copiar uma lista para outra variável
- CRUD
    - Create/Criar
    - Read/Ler:
    - Update/Alterar
    - Delete/Apagar
- Criar indice com `for/in` +  `range(len(lista))`: ver [aula50.py](aula50.py)
-----------------

</p>
</details>

- [x] 72. Introdução ao for / in - estrutura de repetição para coisas finitas [aula43.py](aula43.py) 9m
- [x] 73. range + for para usar intervalos de números [aula44.py](aula44.py) 8m
- [x] 74. Como o for funciona por baixo dos panos? (next, iter, iterável e iterador)[aula45.py](aula45.py) 15m
- [x] 75. O que aprendemos com while também funciona no for (continue, break, else, etc)[aula46.py](aula46.py) 5m
- [x] 76. Exercício - Jogo da palavra secreta [aula47.py](aula47.py) 5m
- [x] 77. Sobre exercícios - não saber é normal 3m
- [x] 78. (Parte 1) Solução do exercício - Jogo da palavra secreta [aula47gabarito.py](aula47gabarito.py) 8m
- [x] 79. (Parte 2) Solução do exercício - Jogo da palavra secreta [aula47gabarito.py](aula47gabarito.py) 8m
- [x] 80. Tipo list - Introdução às listas mutáveis em Python [aula48_1.py](aula48_1.py) 10m
- [x] 81. Alterando uma lista com índices, del, append e pop (Tipo list) [aula48_2.py](aula48_2.py) 14m
- [x] 82. Inserindo itens em qualquer índice da lista com insert [aula48_3.py](aula48_3.py) (Tipo list) 9m
- [x] 83. Concatenando e estendendo listas em Python [aula48_4.py](aula48_4.py) 5m
- [x] 84. Cuidados com tipos de dados mutáveis - list e copy  [aula48_5.py](aula48_5.py)8m
- [x] 85. for in com tipo list [aula49.py](aula49.py) 2m
- [x] 86. Exercício - exiba os índices da lista [aula50.py](aula50.py)(aula com solução) 4m

### Empacotamento e Desempacotamento

<details><summary>Anotações</summary>
<p>

- Tipo tupla - Uma lista imutável
    - Tupla: `tupla = 1, 2, 3` ou `tupla = (1, 2, 3)`
    - Lista: `lista = [1, 2, 3]`
- A função `tuple(L)` converte uma lista `L` em uma tupla
- A função `list(T)` converte uma tupla `T` em uma lista
- `enumerate(lista)` - enumera iteráveis (índices) aula53
    - Ex:`enumerate(['a', 'b']) => [(0, 'a'), (1, 'b')]`
    - Ao ser usado ele fica vazio no final.
    - Pode ser convertido para lista/tupla com `list(T)` / `tuple(L)`
- Try/Except
    - `except ValueError:` erro no valor/tipo
    - `except IndexError:` erro de indice (indice não existente)
    - `except Exception:` exceção (qualquer outro erro)
- Imprecisão de ponto flutuante
    - Causa problemas em operações com numeros decimais.
    - Ex: 0.1 + 0.7 = 0.799999....
    - para resolver esse problema pode se usar a função `round(num, casas-dcimais)`;
    - Importar a biblioteca `import decimal` e usar `decimal.Decima('0.1')`.
    - Olhar aula51.py .
- Métodos String
    - split - divide uma string e transforma em (list) `str.split()`
    - join - une em uma string `str.join(str/list/tupla)`
    - strip - corta o espaço no final e no começo se tiver.
- Interpretador do Python
    - `python --version` ou `python -V` (ver a versão do python)
    - `python mod.py` (executa o mod)
    - `python -u` (unbuffered) Descarrega o buffer
    - `python -m mod` (lib mod como script)
    - `python -c 'cmd'` (comando)
    - `python -i mod.py` (interativo com mod)
    - `python --help` (ajuda)
- Desempacotamento  96 -> [aula59.py](aula59.py)


-----------------

</p>
</details>

- [x] 87. Introdução ao empacotamento e desempacotamento [aula51.py](aula51.py) 7m
- [x] 88. Tipo tuple [aula52.py](aula52.py) (tuplas) 5m
- [x] 89. enumerate para enumerar valores de iteráveis (pegar índices) [aula53.py](aula53.py)  12m
- [x] 90. Exercício - crie uma lista de compras com listas [Meu Exercício](aula54_0_exercicio.py) 4m
- [x] 91. Solução do exercício - crie uma lista de compras com listas [Gabarito](aula54_1_solucao.py) (com try / except) 11m
- [x] 92. Imprecisão dos números de ponto flutuante + round e decimal.Decimal [aula55.py](aula55.py)  9m
- [x] 93. split, join e strip são métodos muito úteis da str [aula56.py](aula56.py) 12m
- [x] 94. Listas dentro de listas (iteráveis dentro de iteráveis) [aula57.py](aula57.py) 8m
- [x] 95. Detalhes sobre o interpretador do Python [aula58.py](aula58.py)  17m
- [x] 96. Desempacotamento em chamadas de funções [aula59.py](aula59.py) 7m
- [x] 97. Operação ternária com Python (if e else de uma linha) [aula60.py](aula60.py) 7m
- [x] 98. Exercício - Gerar o primeiro dígito de um CPF com Python [aula61.py](aula61.py)  10m
- [ ] 99. Solução do exercício - Gerar o primeiro dígito de um CPF com Python 9m
- [ ] 100. Exercício - Gerar o segundo dígito de um CPF com Python 4m
- [ ] 101. Solução do exercício - Gerar o segundo dígito de um CPF com Python9m
- [ ] 102. Possíveis problemas e soluções para nosso algoritmo do CPF 14m
- [ ] 103. Criando um gerador de CPFs com nosso algoritmo e Python