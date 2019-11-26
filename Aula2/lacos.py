#!/usr/bin/python3

######
## Laço de Repetição
######


######
## Laço while
######
# Este laço executa enquanto uma condição for verdadeiro

# i = 0
# while( i < 10): # Enquanto i for menor que 10
#     print(i)    # mostra valor de i
#     i += 1      # i = i + 1
    #repete

# Como fazer controle de um loop while

# i = 0
# while(True):

#     i += 1
#     if i == 10:
#         break
#     if i == 5:
#         continue
#     print('Teóricamente, um loop infinito',i)

# Continue retoma do começo a execução de um loop
# i = 10             # Iterador regressivo
# while i > 0:       # enquanto i < 0
#     i -= 1         # i = i-1
#     if i % 2 == 1: 
#         continue
#     print (i)

#############
### Laço for
#############
# Percorre itens em determinado alcance de valores

# for(i=0;i<10;i++){}

# lista = []
# for i in range (1000): # começa do 1, vai até o 100 de 2 em 2
#     lista.append(i)
# print(lista)
# percorrer uma lista
# for i in lista:
#     if i % 2 == 0:
#         print(f'\033[31m{i}\033[0m', 'par')
#     if i % 2 == 1:
#         print(f'\033[32m{i}\033[0m', 'impar')
# percorrer um dicionario
# dicionario = {
#     'nome':'Daniel',
#     'sobrenome':'Silva'
#     }
#for i in dicionario:
#   print(dicionario[i])

# for chave,valor in dicionaro.items():
#     print(chave)
#     print(valor)

# Enumerando itens de uma lista
# lista = ['item1','item2','item3','item4','item5','item6','item7']
# print(list(enumurate(lista)))
# for indice,valor in enumerate(lista):
#     print(indice)

# list comprehension (compreensão de listas)

lista = [x*2 for x in range(1,101)]
print(lista)