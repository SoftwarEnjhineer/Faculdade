# 2) Crie um programa onde o usuário possa digitar vários valores numéricos e
# cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será
# adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 

lista = []

escolha = 'S'

while escolha == 'S':

    n = input('Digite um valor a ser adicionado: ')

    escolha = input('Gostaria de continuar adicionando números? (s/n): ').upper()

    if n not in lista:
        lista.append(n)
        lista.sort()

print(lista)
