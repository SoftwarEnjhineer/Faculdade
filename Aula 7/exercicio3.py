#Faça um programa que leia um número inteiro positivo N e imprima todos os números
#naturais de 0 até N em ordem decrescente.

valor = int(input('Digite um valor positivo: '))

if (valor > 0):
    for i in range(valor, -1, -1):
        print(i)