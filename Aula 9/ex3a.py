# 3) Crie um programa que vai ler vários números e colocar em uma list. Depois disso, mostre:
# a) Quantos números foram digitados.
# b) A list de valores, ordenada de forma decrescente.
# c) Se o valor 5 foi digitado e está ou não na list.

list = []

choice = 'S'
while choice == 'S':

    number = input('Digite os números: ')
    list.append(number)
    list.sort()
    list.reverse()

    choice = input('Gostaria de continuar adicionando números? (s/n): ').upper()

if '5' in list:
    print('Contém 5 na lista')
else:
    print('Não contém 5 na lista')

print(f'A lista contém: {len(list)} componentes')
print(f'A lista em ordem descrescente: {list}')
