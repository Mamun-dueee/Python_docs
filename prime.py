# Finding prime numbers..........

for n in range(2, 10):
	for x in range(2, n):
		if n%x == 0:
			print(n, 'is equals', x , '*', n//x)
			break
			
	else:
		print(n, 'is a prime number')
