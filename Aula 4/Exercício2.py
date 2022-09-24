#Escreva um programa que leia um número inteiro e informe se ele é divisível por 3 e por 7. 
numero = int(input('Digite um número inteiro: '))
if (numero %3 == 0) and (numero %7 == 0) :
    print('É divisível')
else:
    print('Não é divisível')