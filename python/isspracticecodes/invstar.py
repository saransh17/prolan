n=int(input("Enter the number of levels : "))

for i in range(1,n+1):
	for k in range(i-1):
		print(" ", end = " ")
	l = 2*(n-i) + 1
	for j in range(l):
		print("*", end = " ")
	print()
