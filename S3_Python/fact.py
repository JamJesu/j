a=int(input("enter the number \n"))
f=1
if(a<0):
	print("no factorial for negative value")
else:
	while(a>0):
		f=f*a
		a=a-1
	print("the factorial",f)

 


