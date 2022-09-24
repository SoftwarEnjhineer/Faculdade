#1. Faça um programa que leia uma string S1 e após isso mostre um menu com as seguintes opções:
#(a) Imprimir o tamanho da string S1;

string1 = input('Digite a um texto: ')
print('O tamanho da string é:',len(string1) - (string1.count(' ')))