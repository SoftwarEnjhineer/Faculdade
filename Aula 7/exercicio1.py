#Escrever um programa que o usuário digite 5 valores, um de cada vez, e conta quantos destes 
#valores são negativos, imprimindo esta informação na tela.

count = 0

for i in range(0, 5):
  n = int(input('Digite os números: ')) 
  if n < 0:
    count += 1

print(f'valores negativos: {count}')
