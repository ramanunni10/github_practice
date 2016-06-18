a=0
b=1
n=int (raw_input("range"))

print a," ",b," ",
for h in range(n):
	c=a+b
	a=b
	b=c
	print c,"	",
print

