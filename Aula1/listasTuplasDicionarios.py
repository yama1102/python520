#!/usr/bin/python3
import random

# #contagem de lista começa sempre do 0
# #contagem regressiva começa com -1 
# lista = ['Arroz','Feijão','Óleo','Sal','Açucar','Temperos']
# #          0        1        2     3       4         5
# #          -6       -5       -4    -3      -2        -1

# lista3d = [
#         [ 2 , 3 , 4 , 5 ],
#         [ 3 , 4 , 5 , 5 ],
#         [ 7 , 5 , 7 , 8 ]
#         ]

# #Adicionar um item no final da lista
# lista.append('Carne')
# #Adicionar um item no determinado indice da lista 
# lista.insert(0,'Sabão em pó')

# #remove o elemento pelo indice
# # lista.pop(0)

# #Ordena a lista em ordem alfabetica/numerica
# lista.sort()

# #reverte a ordem
# lista.reverse()

# #remove o primeiro indice encontrado com o seguinte valor
# lista.remove('Sabão em pó')

# #mostra quantidade de elementos
# print(len(lista))

# #Procura o primeiro indice da ocorrência
# print(lista.index('Açucar'))

# #Conta quantidade de indices x no array
# print(lista.count('Arroz'))

# #Sobrescreve elemento em determinado indice
# lista[3] = 'Maça'

# print(lista)

###########
## Tuplas
###########

#primeiro método para criar tuplas
# tupla = ('Maça','Banana','Laranja','Abacaxi','Uva')
# print(type(tupla))

# #segundo método para criar tuplas
# tupla2 = 'valor1',2,True,2j
# print(type(tupla2))

# #Acessando indices de uma tupla
# print(tupla[3])
# print(tupla[1:4])
# print(tupla[-2])

# #Converter tupla para lista
# lista_da_tupla = list(tupla)
# print(type(lista_da_tupla))

# print(tupla)

# tupla = (['Indice 1'],'Nome')
# tupla[0].insert(1,'Indice 2')
# print(tupla)

############
###Dicionarios
############

#Criando um dicionário
# apresentacoes = {
#     'Paulista' : 'Salve',
#     'Carioca' : 'Vai Flamengo',
#     'Pirata' : 'Argh',
#     'Mineiro' : 'Pão de queijo',
#     'Acre' : 'Barulhos de Dinossauro',
# }

# #Acessando índices em um dicionário
# print(apresentacoes['Paulista'])

# #Criando um dicionário com multi-valores internos
# linguagem_favorita = {
#     'Daniel' : {
#         'linguagem' : 'Python',
#         'Tempo de experiência' : 4
#     },
#     'Olympio' : {
#         'limguagem' : 'R',
#         'limguagem2' : 'VBA',
#         'Tempo de experiência' : 10
#     },
# }

# valores = {'nome': 'Daniel', 'Sobrenome': 'Silva'}
# print(linguagem_favorita.get('Daniel')['linguagem'])
# #acesso a todas as chaves
# print(linguagem_favorita.keys())
# #acesso aos valores
# print(linguagem_favorita.values())
# #acesso aos itens
# print(linguagem_favorita.items())

############
###Números
############

#Operações matemáticas
somar = 2 + 2
print( 2 + 2, 'Retornando o valor de 2 + 2')
print(somar, 'Retornando o Somar')

subtrair = somar - 2 # somar retorna um tipo inteiro
print(subtrair, 'Retornando o Subtrair')

multiplicar = subtrair * 3 #subtrair também retorna um tipo inteiro
print(multiplicar, 'Retornando o Multiplicar')

divisão = multiplicar / 5 #multiplicar também retorna um tipo inteiro
print(divisão, 'Retornando o dividir') # Retorna um valor de ponto flutuar

potencia = 2 ** 6
print(potencia, 'Retornando o valor da potencia')
raiz = 2 ** 0.5 
print(raiz, 'Retornando o valor da raiz')

letras = 'abcdefghijk' + 'lmnopqrstuvwxyz'
print(float(input('Digite um numero: '))+float(input('Digite outro numero: ')))

