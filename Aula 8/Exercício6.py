# 6- Faça um programa que peça que o usuário informe um número inteiro N, e
# apresente o somatório de 1 até N.
# Exemplo:
# N = 3
# Resultado = 1+2+3 = 6
# N = 5
# Resultado = 1+2+3+4+5 = 15

numero = int(input('Digite um número: '))

soma = 0

i = 1
while i <= numero:
    soma = soma + i
    i = i + 1
    
print(soma)