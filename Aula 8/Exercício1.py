# Exemplo 1
i = 1

while i < 10:
    print(i)
    i = i+1
print('Fim')


# Exemplo 2
resposta = 'S'

while resposta == 'S':
    numero = int(input('Digite um valor: '))
    resposta = (input('Quer continuar? [S/N] ')).upper()
print('Fim')


# Exemplo 3
n = 1

while n != 0:
    n = int(input('Digite um valor: '))
print('Acabou')


# Exemplo 4
n = 1

par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n %2 == 0:
        par = par+1 
    else:
        impar = impar+1
print('Quantidade de números pares:',par)
print('Quantidade de números impares:',impar)
