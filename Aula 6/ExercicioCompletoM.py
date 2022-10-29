string1 = input('Digite a um texto: ')

print('==== Menu de opções ====\n')
print('Opção 1: Imprimir o tamanho da string')
print('Opção 2: Comparar a string 1 com string 2')
print('Opção 3: Concatenar a string 1 com a string 2')
print('Opção 4: Imprimir a string 1 de forma reversa')
print('Opção 5: Contar quantas vezes um caractere aparece na string 1')
print('Opção 6: Substituir a primeira ocorrência do caractere 1 da string 1 pelo caractere 2')
print('Opção 7: Verificar se uma string 2 é substring de 1')
print('Opção 8: Retornar uma substring da string 1\n')

opcaoMenu = int(input('Digite o número correspondente da opção que deseja aplicar: '))
if (opcaoMenu == 1):
    print('O tamanho da string sem espaços é:',len(string1) - (string1.count(' ')))
elif (opcaoMenu == 2):
    string2 = input('Forneça um segundo texto: ')
    if (string1 == string2):
        print('As strings são iguais')
    else:
        print('As string são diferentes')
elif (opcaoMenu == 3):
    string2 = input('Forneça segundo um texto: ')
    print(f'Concatenação das frases: {string1 + string2}')
elif (opcaoMenu == 4):
    print('A string invertida fica assim:',string1 [::-1])
elif (opcaoMenu == 5):
    caracter1 = input('Digite o carácter que deseja contar: ')
    print(f'Esse caracter aparece: {str(string1.count(caracter1))} vezes')
elif (opcaoMenu == 6):
    caracterSubstituido = input('Digite o carácter que será substituído: ')
    caracter_substituto = input('Digite o caracter que deseja substituir: ')
    print(string1.replace(caracterSubstituido,caracter_substituto,1))
elif (opcaoMenu == 7):
    string2 =input('Digite uma segunda string: ')
    if (string2 in string1):
        print('É sub string')
    else:
        print('Não é substring')
elif (opcaoMenu == 8):
    inicioSubstring = int(input('De qual posição a substring deve ser iniciada? '))
    tamanhoString = int(input('Qual o tamanho da string? '))
    print(string1[inicioSubstring:tamanhoString])