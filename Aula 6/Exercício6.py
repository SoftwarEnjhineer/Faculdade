#(f) Substituir a primeira ocorrência do caractere C1 da string S1 pelo caractere C2
#Os caracteres C1 e C2 serão lidos pelo usuário;

string1 = input('Digite a um texto: ')
sc1 = input('Digite o caracter que será substituído: ')
sc2 = input('Digite o caracter que deseja substituir: ')
print(string1.replace(sc1,sc2,1))