# 5- Escreva um programa que calcula e imprime a potência (X elevado a N) de 2 números
# positivos informados pelo usuário. Obs: utilizar somente as operações
# aritméticas básicas (multiplicação, divisão, soma e subtração).


x = int(input('Digite o número base: '))
n = int(input('Digite o expoente: '))

potencia = 1
i = 0

while i != n:
    potencia = potencia * x
    i = i + 1
    
print(potencia)