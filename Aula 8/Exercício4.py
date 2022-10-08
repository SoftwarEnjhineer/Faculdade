# 4- Faça um programa que imprima na tela a quantidade números entre 1 à 100 que são divisíveis por 5.

i = 1
soma = 0

while i < 101:
    if i %5 == 0:
        soma += 1
    i = i+1
    
print(soma)