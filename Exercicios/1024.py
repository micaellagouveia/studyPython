def desloc (s, n, all=False):
    r = ""
    for c in s:
        if(c.isalpha() or all):
            r += chr(ord(c) + n)
        else:
            r += c
    return r

x = int(input())

for i in range(x):
    s = input()
    tam = len(s)

    s = desloc(s,3)
    s = s[::-1]

    tam = tam//2


    s = s[:tam] + desloc(s[tam:],-1, all=True)

    print(s)
