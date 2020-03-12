from sys import stdin
from collections import Counter

for line in stdin:

    d = {}
    vTotal = []
    vX = []

    total, voltar = line.split()

    total = int(total)
    voltar = int(voltar)


    for i in range(1,total+1):
        vTotal.append(i)
    
    x = input()
    vX = x.split()
    vX = list(map(int,vX))

    vTotal = vTotal + vX

    ocorrencia = Counter(vTotal)

    morreu = []

    for chave,valor in ocorrencia.items():
        if(valor == 1):
            print(chave, end = " ")
    
    if voltar == total:
        print("*", end="")
    
    print()


