# 2) Crie um programa onde o usuário possa digitar vários valores numéricos e
# cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será
# adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 

list = []

choice = 'S'

while choice == 'S':

    number = input('Digite um valor a ser adicionado: ')

    choice = input('Gostaria de continuar adicionando números? (s/n): ').upper()

    if number not in list:
        list.append(number)
        list.sort()

print(list)
