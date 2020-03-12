from sys import stdin

for line in stdin:
	list_str = line.split()
	list_int = map(int, list_str)

	total, qnt = list_int

	voltaram = input().split()
	voltaram = list(map(int, voltaram))

	if total == qnt:
		print("*")
		continue

	for num in range(1, total+1):
		if num not in voltaram:
			print(num, end=' ')
	print()
