#*************************************************************
# Name:Jeswin Antony M                         Class:S3 IT
#  Roll No:20                                   Date:
#
#		      ELEMENT IN LIST
#**************************************************************
list1=[]
n=int(input("enter the length of list \n"))
for i in range(0,n):
	a=input("enter the element \n")
	list1.append(a)
b=input("enter the element to be searched \n")
flag=0
for i in range(0,n):
	if(list1[i]==b):
		print("element found at ",i+1)
		flag=1
if(flag==0):
	print("element not found")

#          SAMPLE OUTPUT
#enter the length of list
#5
#enter the element
#7
#enter the element
#4
#enter the element
#3
#enter the element
#2
#enter the element
#1
#enter the element to be searched
#4
#element found at  2



