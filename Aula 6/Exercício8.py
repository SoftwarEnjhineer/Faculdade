# (h) Retornar uma substring da string S1. Para isso o usuário 
# deve informar a partir dequal posição deve ser criada a 
# substring e qual é o tamanho da substring.

string1 = input('Digite um texto: ')
inicio = int(input('De qual posição a substring deve ser iniciada? '))
tamanhoString = int(input('Qual o tamanho da string? '))
print(string1[inicio:tamanhoString])