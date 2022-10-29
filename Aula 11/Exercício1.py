# Mostre as seguintes listas, derivadas de:

list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# Intervalo de 1 a 9
print(list[1:10])

# Intervalo de 8 a 13
print(list[8:14])

# Números pares
print(list[0::2])

# Números ímpares
print(list[1::2])

# Todos os múltiplos de 2, 3 e 4

i = 0

list_Multiple2 = []
list_Multiple3 = []
list_Multiple4 = []

while i <= 15:

    if list[i] %2 == 0:
        list_Multiple2.append(i)
    
    if list[i] %3 == 0:
        list_Multiple3.append(i)

    if list[i] %4 == 0:
        list_Multiple4.append(i)
    i +=1

print('Números múltiplos de 2:',list_Multiple2)
print('Números múltiplos de 3:',list_Multiple3)
print('Números múltiplos de 4:',list_Multiple4)

# Lista reversa

print('lista inversa:',list[::-1]) # método 1 para inverter

list.reverse() # método 2 para inverter
print('lista inversa:',list)