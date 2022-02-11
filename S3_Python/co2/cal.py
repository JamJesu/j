"""*************************************************************
 Name:Jeswin Antony M                         Class:S3 IT
  Roll No:20                                  Date:17-12-2021

		        Calculator
**************************************************************"""
def add(a,b):
	print("Sum:",a+b)
def sub(a,b):
	print("Subtraction:",a-b)
def multi(a,b):
	print("Multiplication:",a*b)
def div(a,b):
	print("Division:",a/b)
def exp(a,b):
	print("Exponent:",a**b)
i=1
while(i==1):
	a=int(input("Enter the first number \n"))
	b=int(input("Enter the Second number \n"))
	print("enter 1.Add")
	print("enter 2.Subtraction")
	print("enter 3.Multiplication")
	print("enter 4.Division")
	print("enter 5.Exponent")
	c=int(input())
	if(c==1):
		add(a,b)
	elif(c==2):
		sub(a,b)
	elif(c==3):
		multi(a,b)
	elif(c==4):
		div(a,b)
	elif(c==5):
		exp(a,b)
	c=int(input("Enter 1 to repeat,Enter 2 to exit \n"))
	i=c
"""
        Sample Output
        Enter the first number 
10
Enter the Second number 
5
enter 1.Add
enter 2.Subtraction
enter 3.Multiplication
enter 4.Division
enter 5.Exponent
4
Division: 2.0
Enter 1 to repeat,Enter 2 to exit 
2
Enter the first number 
5
Enter the Second number 
2
enter 1.Add
enter 2.Subtraction
enter 3.Multiplication
enter 4.Division
enter 5.Exponent
3
Multiplication: 10
Enter 1 to repeat,Enter 2 to exit 
1
Enter the first number 
4
Enter the Second number 
2
enter 1.Add
enter 2.Subtraction
enter 3.Multiplication
enter 4.Division
enter 5.Exponent
1
Sum: 6
Enter 1 to repeat,Enter 2 to exit 
1
Enter the first number 
3
Enter the Second number 
1
enter 1.Add
enter 2.Subtraction
enter 3.Multiplication
enter 4.Division
enter 5.Exponent
2
Subtraction: 2
Enter 1 to repeat,Enter 2 to exit 
1
Enter the first number 
3
Enter the Second number 
3
enter 1.Add
enter 2.Subtraction
enter 3.Multiplication
enter 4.Division
enter 5.Exponent
5
Exponent: 27
Enter 1 to repeat,Enter 2 to exit 
"""
