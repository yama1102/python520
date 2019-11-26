#!/usr/bin/python3

#######
## Exercicio condidional composta
#######

# Criar uma variavel idade onde recebe uma
# idade via linha de comando, validar se essa
# pessoa pode beber ou não, caso possa, atribuir
# ao valor de uma variável embreagado o valor true, senão false

idade = int(input('Qual é a sua idade: '))

# Criar validação se a pessoa babeu para atribuir a variável
# embriagado como True ou False


# Criar uma validação com elif para que se a idade for menor
# que 0 anos, a pessoa seja invalida

if idade < 0:
    print('invalida')
elif idade >= 18:
    # if's validam se variável tem conteúdo
    bebida = input('bebeu? se sim y se não n : ').strip().lower()
    if bebida == 'y':
        embriagado = True
    else:
        embriagado = False
else:
    embriagado = False

# Criar uma validação para que se a pessoa tiver carteira de
# motorista, ela possa dirigir. Porém
# Criar condicional para que se a pessoa estiver embriagada,
# mostrar uma mensagem que ela não pode dirigir 

# carteira = input('Você tem carteira de motorista?').strip().title() # y para sim e n para não
# embriagada = input('Você está embriagada?').strip().title() # y para sim e n para não

# if carteira == 'Não' or embriagada == 'Sim':
#     print('Não pode dirigir')
# else:
#     print('Pode dirigir')

# if habilitação == 'y':
#     habilitação = True
# else:
#     habilitação = False

if 'embriagado' in globals():

    if habilitação and not embriagado:
        print('Vocẽ pode dirigir')
    else:
        print('Vocẽ não pode dirigir')

