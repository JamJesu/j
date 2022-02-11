#*************************************************************
# Name:Jeswin Antony M                         Class:S3 IT
#  Roll No:20                                   Date:
#
#		          ADDITION OF TWO MATRIX
#**************************************************************
A=[]
B=[]
print("Enter the rows and columns of matrix")
row=int(input("Rows"))
column=int(input("columns"))
print("enter 1st matrix")
for i in range(0,row):
	r=[]
	for j in range(0,column):
		a=int(input())
		r.append(a)
	A.append(r)
for i in range(0,row):
	print(A[i])
print("enter 2nd matrix")
for i in range(0,row):
	r=[]
	for j in range(0,column):
		a=int(input())
		r.append(a)
	B.append(r)
for i in range(0,row):
	print(B[i])
result=[]
for i in range(0,row):
	r=[]
	for j in range(0,column):
		z=A[i][j]+B[i][j]
		r.append(z)
	result.append(r)
print("The result matrix")
for i in range(0,row):
	print(result[i])
"""     SAMPLE OUTPUT
Enter the rows and columns of matrix
Rows2
columns2
enter 1st matrix
1
2
3
4
[1, 2]
[3, 4]
enter 2nd matrix
1
1
1
1
[1, 1]
[1, 1]
The result matrix
[2, 3]
[4, 5]
"""







