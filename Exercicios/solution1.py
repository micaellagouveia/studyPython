from collections import Counter

while True:
	num_bilhetes, num_pessoas = map(int, input().split())

	if num_bilhetes==0 and num_pessoas == 0:
		break

	list_pessoas = list(map(int, input().split()))
	histogram = Counter(list_pessoas)

	clonados = 0

	for k, v in histogram.items():
		if v>1:
			clonados+=1

	print(clonados)
