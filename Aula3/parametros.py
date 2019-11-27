#!/usr/bin/python3

'''Parametros python - Título

Esta aula, nós analisamos como criar e documentar funções'''
######
### Parâmetros de função
######

# def retorna_pessoa(nome,idade=99):
#     print(f'Nome: {nome}\nidade: {idade}')

# retorna_pessoa(nome='Daniel',idade=19)


### Especificar tipo de parâmetro e retorno



# def retorna_valor_int(inteiro : int) -> int:
#     ''' Função com anotação de tipo
    
#     Se refere a função que possui tipos especificos e
#     mostram na sua sintaxe de construção o que é necessário,
#     sempre tem que pular uma linha'''
#     inteiro = int(inteiro)
#     return int(inteiro)

#print(retorna_valor_int('i'))



### args e Kwargs
# print('ola','mundo',',','prazer','sou','Daniel')

### Criando uma função que recebe multiplos valores
def funcao_multi_valores(parametros_estaticos,*argumento_variavel):
    print(parametros_estaticos, 'parametro estático')
    print(argumento_variavel)
    # Fazendo acesso aos parâmetros
    # for argumento in argumento_variavel:
    #     print(argumento)

# funcao_multi_valores('valor estático obrigatório',
#                     'Daniel','Andressa','João','Ana',
#                     'Paula','Lucas','Leonardo','Pedro')

## Argumentos com palavra chave - kwargs

def parametros_chave_valor(**dados):
    if dados['nome'] == 'Daniel':
        print('Acesso Negado')
    else:
        print('Permitido')

# Execução - metodo 1
# print('Metodo 1')
# parametros_chave_valor(nome='Daniel',sobrenome='Silva',
#                         idade=19,sexo='Masculino')

# Execução 
# print('Metodo 2')
dados_requisicao = {'nome':'Daniel',
                    'Sobrenome':'Silva',
                    'Profissão':'Operador de empilhadeira'}
# parametros_chave_valor(**dados_requisicao)

## Decoradores de função
# uma função que modifica o valor de outra

#declara uma função com uma variavel funcao obrigatória
def mudaCor(retorno_funcao):
    def modificaAzul(retorno_funcao):
        return f'\033[94m{retorno_funcao}\033[0m' 
    return modificaAzul

@mudaCor
def log(texto):
    return texto

print(log('oi'))