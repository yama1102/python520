#!/usr/bin/python3

#input('Digite qual o caminho a ser seguido: ')

#a = 'engarrafado'
#b = 'livre'

#if a == 'engarrafado':
  # print('Melhor ir pela b')
#else:
  # print('Indo pelo Caminho a')

#########
### Estrutura de condicional 
#########

# nome = input('Digite seu nome: ').strip().title()
# sobrenome = input ('Digite seu sobrenome; ').strip().title()

# if nome == 'Daniel':
#     print('Olá professor')
# print('Seja bem vindo')

#########
### Estrutura condicional composta
#########

# if nome == 'Daniel':
#     print(f'Bem vindo Professor {nome}')
# else:
#     print(f'Bem vindo Aluno {nome}')
# print('Você pode utilizar a plataforma')

#########
### Comparando duas condições
#########

# if nome == 'Daniel' and sobrenome == 'Silva': # pode-se utilizar o 'or'
#     print(f'Bem vindo Professor {nome}')
# else:
#     print(f'Bem vindo Aluno {nome}')
# print('Você pode utilizar a plataforma')

##########
## Condicionais Encadeadas
##########

# if nome == 'Daniel':
#     if sobrenome == 'Silva':
#         print('Olá professor')
#     else:
#         print('Você é Daniel, Mas não é professor')
# else:
#     print(f'Olá Aluno {nome}')

###########
## Condicionais Aninhadadas
##########

nome = input('Digite seu nome: ').strip().title()

# Consegue fazer validação em mais de um fator
# com comportamento diferente
if nome == 'Daniel':
    print(f'Seu nome é muito bonito, {nome}')
elif nome == 'Juliana':
    print(f'Seu nome é bem legal, {nome}')
elif nome == 'Jorge':
    print(f'Seu nome é muito feio, {nome}')
else:
    print(f'Seu nome é bem normal, {nome}')
