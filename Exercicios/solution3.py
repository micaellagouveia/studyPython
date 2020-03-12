from collections import Counter

qnt = int(input())
histograma = Counter()

for _ in range(qnt):
	num = int(input())
	histograma[num] += 1

for k, v in sorted(histograma.items()):
	print(k, "aparece", v, "vez(es)")
