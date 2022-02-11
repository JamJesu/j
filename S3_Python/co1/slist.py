#*************************************************************
# Name:Jeswin Antony M                         Class:S3 IT
#  Roll No:20                                   Date:
#
#		    AVERAGE AND SQUARE OF N NUMBERS
#**************************************************************
list1=[]
n=int(input("enter the length of list \n"))
print("Enter the values")
for i in range(0,n):
	a=int(input())
	list1.append(a)
sum=0
for i in range(0,n):
	sum=sum+float(list1[i])
avg=sum/n
print("average :",avg)
for i in range(0,n):
	sq=float(list1[i])
	print("The square of",sq,"=",sq*sq)

#        SAMPLE OUTPUT
#enter the length of list
#5
#Enter the values
#1
#2
#3
#4
#5
#average : 3.0
#The square of 1.0 = 1.0
#The square of 2.0 = 4.0
#The square of 3.0 = 9.0
#The square of 4.0 = 16.0
#The square of 5.0 = 25.0
