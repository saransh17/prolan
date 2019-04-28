def disarium(n):
	i = 0
	ini = n 
	ans = 0
	le = n
	while le > 0 :
		i+=1
		le = le // 10
	while n > 0 :
		rem = n % 10
		ans += pow(rem,i)
		i-=1
		n = n // 10
	if ans == ini : 
		print("Disatrium number!!!")
	else:
		print("Not a disarium number!!!")

def armstrong(n):
	le = n
	ini = n
	i = 0
	ans = 0
	while le > 0 :
		i+=1
		le = le // 10
	while n > 0 :
		rem = n % 10
		ans += pow(rem,i)
		n = n // 10
	if ans == ini :
		print("armstrong number!!!")
	else:
		print("not an armstrong number!!!")

def happy(n):
	print("happy function")

n=int(input("Enter the number : "))

disarium(n)
armstrong(n)
happy(n)