N = float(input())
cem = 0
cinq = 0
vinte = 0
dez = 0
cinco = 0
dois = 0
um = 0
Mcinq = 0
Mvcinco = 0
Mdez = 0
Mcinco = 0
Mum = 0

if N >= 100:
    cem = int(N/100)
    N = N - (100 * cem)

if N >= 50:
    cinq = int(N/50)
    N = N - (50 * cinq)

if N >= 20:
    vinte = int(N/20)
    N = N - (20*vinte)

if N >= 10:
    dez = int(N/10)
    N = N - (10*dez)

if N >= 5:
    cinco = int(N/5)
    N = N - (5*cinco)

if N >= 2:
    dois = int(N/2)
    N = N - (2*dois)

""" *************************"""

if N >= 1:
    um = int(N)
    N = N - um

if N >= 0.5:
    Mcinq = int(N/0.5)
    N = N - (0.5 * Mcinq)

if N >= 0.25:
    Mvcinco = int(N/0.25)
    N = N - (0.25 * Mvcinco)

if N >= 0.1:
    Mdez = int(N/0.1)
    N = N - (0.1*Mdez)

if N >= 0.05:
    Mcinco = int(N/0.05)
    N = N - (0.05*Mcinco)

if N >= 0.01:
    Mum = int(N/0.01)
    N = N - (0.01*Mum)

print("NOTAS:")
print(str(cem) + " nota(s) de R$ 100.00")
print(str(cinq) + " nota(s) de R$ 50.00")
print(str(vinte) + " nota(s) de R$ 20.00")
print(str(dez) + " nota(s) de R$ 10.00")
print(str(cinco) + " nota(s) de R$ 5.00")
print(str(dois) + " nota(s) de R$ 2.00")

print("MOEDAS:")
print(str(um) + " moeda(s) de R$ 1.00")
print(str(Mcinq) + " moeda(s) de R$ 0.50")
print(str(Mvcinco) + " moeda(s) de R$ 0.25")
print(str(Mdez) + " moeda(s) de R$ 0.10")
print(str(Mcinco) + " moeda(s) de R$ 0.05")
print(str(Mum) + " moeda(s) de R$ 0.01")

