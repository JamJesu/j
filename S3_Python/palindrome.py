n=int(input("enter the number"))
temp=n
rev=0
while(n>0):
	a=n%10
	rev=(rev*10)+a
	n=int(n/10)
if(temp==rev):
	print("the number is palindrome")
else:
	print("the number is not palindrome")

	
		