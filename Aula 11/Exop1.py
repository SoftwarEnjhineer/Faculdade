# Ler uma lista de 5 números inteiros e mostre cada número juntamente de sua posição na lista

lista=[]

i = 1

while i <= 5:

  number_add_list = int(input('Digite um número inteiro: '))
  lista.append(number_add_list)

  i += 1


i = 0

while i <= 4:

  print(f'Número {lista[i]}, posição {i}')

  i += 1
