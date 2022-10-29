# Ler uma lista de 4 notas, em seguida o programa deve exibir as notas e as médias
list = []

i = 0

while i <= 3:

    number_add_list = float(input('Digite um número inteiro: '))
    list.append(number_add_list)

    soma = sum(list)

    i += 1

print(soma / 4)