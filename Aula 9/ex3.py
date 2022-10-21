# 3) Crie um programa que vai ler vários números e colocar em uma list. Depois disso, mostre:
# a) Quantos números foram digitados.
# b) A list de valores, ordenada de forma decrescente.
# c) Se o valor 5 foi digitado e está ou não na list.

list = []

choice = 'S'
while choice == 'S':

    number = int(input('Digite o número que será adicionado a lista: '))

    choice = input('Gostaria de continuar adicionando números? (s/n): ').upper()

    list.append(number)
    list.sort()
    list.reverse()

print(f'Números digitados na lista: {len(list)}')

print(f'A lista em ordem descrescente: {list}')

if 5 in list:
    print('Contém o número 5 na lista')
else:
    print('Não contém o número 5 na lista')
