#!/usr/bin/python3

###########
## Exercicio de excessões
###########

# Criar uma tela de cadastro de usuário em uma lista
# Essa tela não pode aceitar figuras políticas que geram polêmica
# ex = Bolsonaro, Lula, Adolf Hitler, Tiririca
# Esse Loop é infinito, onde só acaba quando colocado uma figura pública

#lista = []
# try:
# while(True):
#     x = input('Cadastra o nome; ')
#     if x = 'Bolsonaro':
#     raise ValueError
#     elif x = 'Lula':
#     raise ValueError
#     elif x = 'Adolf Hitler':
#     raise ValueError
#     elif x = 'Tiririca':
#     raise ValueError
# else lista.append(x)
# except ValueError:
#         break

# Arrays de nomes de figura publica
# bolsonaro = [
#     'bolsonaro',
#     'bozo',
#     'bolsanario',
#     'bonoliro',
#     'facista'
# ] 
# lula = [
#     'lula',
#     'mula',
#     '9 dedos',
#     'nove dados',
#     'ladrão',
#     'luladrão'
# ]
# hitler =[
#     'adolf hitler',
#     'hitler',
#     'fuhr',
#     'bigodin',
#     'nazista',
#     'argentino'
# ]
# tiririca =[
#     'tiririca',
#     'palhaço',
#     'florentina'
# ]

# #Atribuindo todas as figuras publicas para uma lista
# figuras_publicas = [bolsonaro, lula, hitler, tiririca]

# # Atribuindo todos os apelidos a um arquivo de texto
# for figura in figuras_publicas:
#     for apelido in figura:
#         with open('politicos.txt','a') as arquivo:
#             arquivo.write(apelido + '\n')

#print(figuras_publicas)

#definido lista de nomes
lista_nomes = []

with open('politicos.txt','r') as arquivo:
    figuras_publicas = arquivo.readlines()
figuras_publicas = [apelido.replace('\n','') for apelido in figuras_publicas]

with open('nomes.txt','r') as nomes:
    lista_nomes = [nomes.replace('\n','') for nome in nomes.readlines()]
try:
    while True:
        #requisição pelo nome
        nome = input('Digite um nome: ').lower().strip()

        # para cada figura publica, vou validar o nome digitado

        if nome in figuras_publicas:
            cad_figura_existe = True
        else:
            cad_figura.existe = False
        #Criando lógica para cadastro
        if cad_figura_publica: 
            raise ValueError('Você tentou inserir uma figura pública')
        elif nome in lista_nomes:
            print('nome já existe')
        elif nome == 'visualizar':
            for nome_cadastrado in lista_nomes:
                print(nome_cadastrado,end= ', ')
            print('\n')
        else:
            print('\n'*100)
            with open ('nomes.txt','a') as nome:
                nome.write(nome + '\n')
            print('Cadastro Realizado')
            
except Exception:
    print('Vocẽ tentou cadastrar uma figura pública')
    print(lista_nomes)
