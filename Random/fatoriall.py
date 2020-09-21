def Fatorial(n):
	r = n - 1
	while r > 0:
		n = n * r
		r = r - 1
	return n

print(Fatorial(5))