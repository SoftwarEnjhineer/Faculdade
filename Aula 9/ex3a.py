# 3) Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# a) Quantos números foram digitados.
# b) A lista de valores, ordenada de forma decrescente.
# c) Se o valor 5 foi digitado e está ou não na lista.

lista = []

escolha = 'S'
while escolha == 'S':

    n = input('Digite os números: ')
    lista.append(n)
    lista.sort()
    lista.reverse()

    escolha = input('Gostaria de continuar adicionando números? (s/n): ').upper()

if '5' in lista:
    print('Contém 5 na lista')
else:
    print('Não contém 5 na lista')

print(len(lista))
print(lista)
