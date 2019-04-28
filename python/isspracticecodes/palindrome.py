n=int(input("Enter the number please:"))
temp=n
rev=0

while(temp>0):
	rev = rev * 10 + (temp%10)
	temp = temp//10
	print(temp)

if(n==rev):
	print("Palindrome!!!")
else:
	print("Not a Palindrome!! :(")