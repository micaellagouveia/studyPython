from collections import Counter

N = int(input())
lista = []

for i in range(N):
    x = int(input())
    lista.append(x)

lista.sort()
ocorrencia = Counter(lista)

for num, repeticao in ocorrencia.items():
    print(str(num) + " aparece " + str(repeticao) + " vez(es)")