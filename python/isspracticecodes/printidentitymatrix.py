n=int(input("Enter the dimension : "))
i=0
j=0
while(i<n):
	while(j<n):
		if(i==j):
			print("1 ",end = " ")
		else:
			print("0 ",end = " ")
		j=j+1
	print("\n")
	j=0
	i=i+1