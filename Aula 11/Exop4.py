# Ler um vetor com 20 idades e exibir a maior e a menor idade

list = []

i = 0

while i <= 20:

    age = int(input('Digite uma idade para adicionar a lista: '))
    list.append(age)

    i += 1

greater_Number = max(list)

print(f'a maior idade é: {greater_Number}')
