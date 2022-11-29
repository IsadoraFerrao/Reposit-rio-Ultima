# variavel = porta nomes 

calculadora = 0
numero1 = 10
numero2 = 4

# soma -> + 
calculadora = numero1+numero2
print(calculadora)

# subtracao -> -
calculadora = numero1-numero2
print(calculadora)

# multiplicacao -> *
calculadora = numero1*numero2
print(calculadora)

# divisao -> /
calculadora = numero1/numero2
print(f'divisao comum: {calculadora}')

# divisao inteira -> //
calculadora = numero1//numero2
print(f'divisao inteira - resolvendo divisao : {calculadora}')

# potencia -> **
calculadora = numero1**numero2 
print(calculadora)

# modulo -> %
calculadora = numero1%numero2
print(calculadora)


# INT = NUMERO INTEIRO (10, 2, 4, 5, 6, 200, 5000)
# FLOAT = NUMERO DECIMAL (10.0, 2.0, 4.0, 500,2)
# STR = tipo textual ('texto', 'frutas', 'palavras')

frase = "Hoje e dia de aula de python"
print(frase)

numero_decimal = 5
print(float(numero_decimal))

numero_decimal = int(6.9)
print(numero_decimal)

# IF = se
# ELSE = senão

numero = 10
if numero == 10:
    print('Numero e 10')
else:
    print('numero e diferente de 10')

# operadores
# ==  -> igual
# != -> diferente de
if 5 != 5:
    print('numeros sao diferentes')
else:
    print('numeros sao iguais')

# < -> menor
# > -> maior
numero = 10
if numero > 10:
    print('numero e maior que 10')
else:
    print('numero e igual ou menor que 10')
# >= -> maior igual

#como definimos as listas
# lista = []
# for = para

frutas = ['Banana','Uva','Manga','Morango']

#for fruta in frutas: # para cada elemento da lista frutas
    #print(fruta) #mostre o nome da fruta

# while = enquanto
numero = 2
while numero == 2:
    print('repetiu uma vez')
    numero = 0

# dada a lista nomes = ['Isadora', 'Alan', 'Sherlon', 'Danilo', 'Aline']
# mostrem cada um dos nomes da lista, um nome por vez
# a saida deve conter "olá professor(a), nome"

#funcoes

def apresentacao():
    print('Ola, esta e uma funcao')

