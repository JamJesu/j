a=int(input("enter the first number \n"))
b=int(input("enter the second number \n"))
c=int(input("enter the third number \n"))
if(a>b and a>c):
	print(a,"is largest")
elif(b>c):
	print(b,"is largest")
else:
	print(c,"is largest")
if(a<b and a<c):
	print(a,"is smallest")
elif(b<c):
	print(b,"is smallest")
else:
	print(c,"is smallest")
 


