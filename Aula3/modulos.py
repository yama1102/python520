#!/usr/bin/python3

### Importando nosso proprio modulo
#import modulos.calculadora as calculadora # primeiro jeito
# from modulos.calculadora import * #somar, subtrai
# soma = somar(1,2)
# print(soma)

# print(subtrai(9,1))
# print(multiplica(3,9))

import random # modulo nativo que trata operações de aleatoriedade
import os #possibilita usar funcionalidades do sistema operacional
import sys # acessar variaveis de sistema e alguns parametros especificos
import datetime # cuida de data e hora
import json # codificar e/ou decodificar um arquivo no formato JSON
import csv # trabalha com planilhas

# modulo os
# print(os.listdir('/home/developer'))
# print(os.rename('nomeErrado.txt', 'nomeCerto.txt'))
# os.system('sudo systemctl restart apache2')
# print(random.randint(1,90))

# modulo sys
# print(sys.platform)
# print(sys.builtin_module_names)
# print(sys.argv)
# sys.exit()
# print('Hello')

# print(datetime.datetime.now())
# print(datetime.timedelta(7))
# print(datetime.time(14,0,0))
# print(datetime.date(2019,5,4))

#exemplo prático
# acesso = datetime.datetime(2019,1,22,00,00,00)
# atual = datetime.datetime(2019,1,26,1,1,00)

# print(atual - acesso)
# print(atual)
# if (atual - acesso).total_seconds() > 3600:
#     print('seu token exprirou')
# else:
#     print('acesso liberado')

#jason
print(json.dumps({
    "nome":"Daniel",
    "sobrenome":"Silva"
    },indent=4))

print(json.loads('{"nome":"Daniel","sobrenome":"Silva"}'))

