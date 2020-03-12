from collections import Counter

while True:
    entrada = input()
    entrada = entrada.split()
    entrada = map(int, entrada)

    N, M = entrada

    if N == 0 and M == 0:
        break

    pacote = input()
    pacote = pacote.split()
    pacote = list(map(int, pacote))

    ocorrencia = Counter(pacote)

    repetidos = 0

    for ingresso, repeticao in ocorrencia.items():
        if repeticao > 1:
            repetidos += 1

    print(repetidos)
