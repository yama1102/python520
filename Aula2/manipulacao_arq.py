#!/usr/bin/python3

#########
## Manipulando Arquivos com python
#########

### Abrir um arquivo para mododificação
##### Método Não Recomendado ######
# ponteiro = open('nomedoarquivo.txt','a') #Abre um ponteiro para escrita de arquivos
                                          # escrita de arquivos, o modo utilizado é o read plus (r+)
                                          # que serve para leitura e escrita. Possuimos varios
                                          # modos de acesso, por exemplo:
                                          # w = sobrescrita
                                          # r = somente leitura
                                          # + = abre um arquivo para atualização (acresenta e modifica)
                                          # a = complemento
                                          # x = criação
                                          # este método não é recomendado porque o ponteiro sempre
                                          # necessita ser encerrado com "close", isso foi substituido
                                          # com a adição do comando "with" (mostraremos em breve)
# ponteiro.write('Olá mundo\n')
# ponteiro.read()
# ponteiro.close()

##### Método Usual###
# Arquivo em modo de escrita
with open('nomedoarquivo2.txt','w') as arquivo:
    arquivo.write('Olá mundo/n')
    arquivo.writeline(['banana\n','maça\n'])
# Arquivo em modo de leitura
with open('nomedoarquivo2.txt','r') as arquivo:
    letras = arquivo.readlines() # read apenas ler

    print(letras)
