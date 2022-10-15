
lista = []

for i in range(0,4):

    n = input('Digite um valor a ser adicionado: ')
    
    if n not in lista:
        lista.append(n)
        lista.sort()

print(lista)