# Escreva um programa para determinar se um número inteiro A é divisível por um outro número inteiro B. 
# Ambos os números inteiros devem ser fornecidos pelo usuário.
numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite um número: "))
if numero1 % numero2 == 0:
    print('É divisível')
else:
    print('Não é divisível')