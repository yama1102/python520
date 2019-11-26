#!/usr/bin/python3

######
## Tratando Exceçoes
######

# try: # tente
#     print('Divisão de dois valores')
#     numero1 = int(input('Digite um número a ser dividido: '))
#     numero2 = int(input('Digite outro número a ser dividido: '))
#     print(numero1 / numero2)
# except ValueError as e: # Exceção
#     print('Insira Somente Números', e)
# except ZeroDivisionError as e:
#     print('Impossível dividir por 0', e)
# except Exception as e:
#     print('Erro na execução do programa', e)
# finally:
#     print('Saindo do Script')

# nulo = None

###########
### Lançando Exceções
###########

# try:
opcao = input('Não digite 5: ')
if opcao == '5':
    raise ValueError('Eu falei para vocẽ não digitar 5')    
# except ValueError as e:
#     print('Deu erro: ', e)
