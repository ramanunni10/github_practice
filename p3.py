def fibonacci(n):
	a=0
	b=1
	print a," ",b," ",
	for h in range(n):
		c=a+b
		a=b
		b=c
		print c,"	",
n=int (raw_input("range"))
fibonacci(n)

print

