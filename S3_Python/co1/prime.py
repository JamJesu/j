#*************************************************************
# Name:Jeswin Antony M                         Class:S3 IT
#  Roll No:20                                   Date:
#
#		        PRIME NUMBER
#**************************************************************
a=int(input("enter the starting range:"))
b=int(input("enter the ending range:"))

for x in range(a,b+1):
	if (x>1):
		for y in range(2,x):
			if(x%y==0):
				break;
		else:
			print(x,"is prime \n")
#        SAMPLE OUTPUT
#enter the starting range:4
#enter the ending range:12
#5 is prime

#7 is prime

#11 is prime
