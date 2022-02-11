"""**********************************************************
 Name:Jeswin Antony M                        Class:S3 IT
 Roll No:20                                  Date:17-12-2021

		        Fibonacci
***********************************************************"""
def fib(n):
	if(n<=1):
		return(n)
	else:
		return((fib(n-1)+fib(n-2)))
z=int(input("enter the nth number"))
for x in range(0,z):
	print(fib(x)) 
"""
        Sample Output
enter the nth number5
0
1
1
2
3
"""
