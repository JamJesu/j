a=int(input("enter the year \n"))
if(a%100==0):
	if(a%400==0):
		print("It is a leap year")
	else:
		print("Not a leap year")
elif(a%4==0):
	print("It is a leap year")
else:
	print("Not leap year")




 



