def printmatrix(arr,r,c):
	print("array is:")
	for i in range(r):
		for j in range(c):
			print(arr[i][j],end = " ")
		print()


def transpose(arr,r,c):
	print("in transpose")
	for i in range(r):
		for j in range(c):
			print(arr[j][i],end = " ")
		print()

r=int(input("Enter the length : "))
c=int(input("Enter the breadth: "))

matrix = []

for i in range(r):
	a = []
	for j in range(c):
		a.append(int(input()))
	matrix.append(a)

printmatrix(matrix,r,c)

q=1
while(q != 4):
	q=int(input("Enter the choice number\n1.transpose\n2.add\n3.multiply\n4.exit"))
	if(q == 1):
		transpose(matrix,r,c)
	elif(q == 2):
		add(matrix,anotherone,r,c)#add two matrices is the same as traversing them while adding them in the loop
	elif(q == 3):
		mult(matrix,anotherone,r,c,p)#mat[i][j]=+a[i][k]*b[k][j]
	else:
		break
