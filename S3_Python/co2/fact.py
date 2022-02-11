"""*************************************************************
 Name:Jeswin Antony M                         Class:S3 IT
  Roll No:20                                  Date:17-12-2021

		        Factorial
**************************************************************"""
def fact(n):
	if(n==1):
		return(1)
	elif(n==0):
		return(1)
	elif(n<=0):
		print("No factorial for negative number")
	else:
		return(n*fact(n-1))
	
a=int(input("Enter the number \n"))
print(fact(a))
""" Sample Output
Enter the number5
120
"""
