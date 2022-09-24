#print("A média dos valores digitados é", sum( [ int(input("Informe o valor "+str(x+1) )) for x in range(10) ] )/10 ) 

#Faça um programa que leia 10 inteiros e imprima sua média.

valores = 0

for i in range(0, 10):
 valores += int(input('Digite os valores: '))
  
print('A média é ' + format(valores/10, '.0f'))

#d = 0
#for i in range(0, 10):
#  n = int(input('Digite: '))
#  d += n
#  print(f'o resultado é: {d/10}')
