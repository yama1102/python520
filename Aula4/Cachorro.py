class Animal:
    nome = 'Animal'
    cabeca = 1

    def __init__(self):
        pass

    def viver(self):
        print('Estou vivo')

class Cachorro(Animal):
    _DNA = 'Cachorro'
    '''Abstração de um cachorro

    Cria um cachorro, baseado nos conceitos definidos em sala'''
    def __init__(self, nome, idade, cor, raca='Vira-lata', porte='Médio'):
        #Atributos Obrigatórios para existir um cachorro
        self.nome = nome
        self.idade = idade
        self.cor = cor
        self.raca = raca
        self.porte = porte
        # Atributos padrão para cada cachorro
        self.patas = 4
        self.orelhas = 2
        self.focinho = True # Valores únicos como true e false
        self.lingua = True
        self.olhos = 2
        self.rabo = True
        print(f'Cachorro {nome}, Construindo com sucesso!')
    
    #O que faz - Métodos

    def latir(self):
        if self.lingua:
            print(f'{self.nome} Au Au Au')
        else:
            print('....')
    
    def comer(self):
        print('Comendo...')

    def cheirar(self):
        if self.focinho:
            print('Cheirando')
        else:
            print('Não está cheirando')

    def cagar(self):
        print('Cagando...')
    
    def dormir(self):
        print('Dormindo...')
    
    def __del__(self):
        print(f'Descanse em paz {self.nome}')
    
    def __str__(self):
        return 'Constroi um cachorro'



