anos =int(input('A quantos anos você fuma? '))
cigarrosDia =int(input('Quantos cigarros fuma por dia? '))
precoCarteira = float(input('Quantos custa a carteira? '))
carteira = 20 #Quantidade de  cigarros na carteira
gasto = (anos*365 * cigarrosDia * precoCarteira) / carteira
print('Valor gasto: R$ {}' .format(gasto))