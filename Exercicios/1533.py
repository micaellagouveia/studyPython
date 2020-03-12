N = 1
K = []
d = {}

while (N):
    N = int(input())
    if not N :
        break
    s = input()
    s = s.split()

    K = list(map(int, s))

    for pos, val in enumerate(K):
        d[val] = pos + 1

    K.sort()
    posicao = d[K[-2]]

    print(posicao)

