#Escreva um programa que indique se um número inteiro digitado pelo 
#usuário está no intervalo de 20 a 90 (20 e 90 não estão na faixa de valores).
numero = int(input('Digite um número inteiro: '))
if (numero >20) and (numero <90):
    print('Correto :D')
else:
    print('Errado')