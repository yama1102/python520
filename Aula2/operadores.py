#!/user/bin/python3

############
### Operadores Aritiméticos
############

# Variáveis por numenclatura podem ter no
# máximo 16 Caractéres
num1 = 6 # Número 1
num2 = 8 # Número 2

adicao = num1 + num2 # Adição
subtracao = num1 - num2 # Subtração
multiplicacao = num1 * num2 # Multiplicação
divisao = num1 / num2 # Divisão
result_div_int =  num1 // num2 # Resultado de uma divisão inteira
resto_div_int = num1 % num2  # Resto de uma divisão inteira (Módulo)

# Operadores de Forma Abreviada
# Paga o Valor Atual do Número e realiza um cálculo
# Atribuindo o resultado a variável

numero = 1
numero += 3 # 1 + 3         numero = numero + 3
numero -= 3 # 4 - 3         numero = numero - 3
numero *= 4 # 1 * 4         numero = numero * 4
numero /= 2 # 4 / 2         numero = numero / 2
numero //= 2 # 2 // 2 = 1   numero = numero // 2
numero %= 2 # 2 % 2 = 0     numero = numero % 2

########
### Operadores Relacionais
########

# Operadores relacionais servem para comparação entre fatores
# Retorna Valores Booleanos (True e False)
numero1 = 6
numero2 = 9
numero3 = numero1

print(numero1 == numero2) # False
print(numero1 != numero2) # True
print(numero1 < numero2) # True
print(numero1 <= numero2) # True
print(numero1 > numero2) # False
print(numero1 >= numero2) # False

print(numero1 is numero3) # Compara se estão alocados no mesmo bloco de memória

lista1 = ['item 1','item2'.'item3']
print('item1' in lista) # Compara exixtência de valores em lista True


