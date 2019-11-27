#!/usr/bin/python3

'''Exercicio Funções

Essa aula a gente fala sobre criações de funções'''
#####
## Exercício Funções
#####

# Criar uma função de soma que retorna a soma de dois valores
# Criar uma função de subtração que retorna a subtração de dois valores
# Criar uma função de multiplicação que retorna a multiplicação de dois valores
# Criar uma função de divisão que retorna a divisão de dois valores
# Criar uma função que gera raiz quadrada de um número x

# Como fazer documentação da sua função
def soma(x,y):
    ''' Função de soma

    Este modulo realiza soma com dois valores, e retorna o valor.'''
    print(__doc__)
    return x + y

def subtracao(x,y):
    return x - y

def multiplicacao(x,y):
    return x * y

def divisao(x,y):
    if y = 0
        raise ZeroDivisionError('Não tem como cara')
    return x / y

def raiz_quadrada(x):
    if x < 0:
        #raise ValueError('Não tem como fazer isso com esse número')
        x **= 0.5
        return complex(n1)
    else:
        return x ** 0.5

soma()
# print(soma(1,2))
# print(subtracao(1,2))
# print(multiplicacao(1,2))
# print(divisao(1,2))
# print(raiz_quadrada(2))