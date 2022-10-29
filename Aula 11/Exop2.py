# Ler uma lista de 10 números reais e mostre na ordem inversa

list = []

i = 0

while i <= 10:

    number_add_list = float(input('Digite um número inteiro: '))
    list.append(number_add_list)

    list.reverse()

    i += 1

print(list)
