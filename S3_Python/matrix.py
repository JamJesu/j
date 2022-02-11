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
print(A)
print("enter 2nd matrix")
for i in range(0,row):
	r=[]
	for j in range(0,column):
		a=int(input())
		r.append(a)
	B.append(r)
print(B)
result=[]
for i in range(0,row):
	r=[]
	for j in range(0,column):
		z=A[i][j]+B[i][j]
		r.append(z)
	result.append(r)
print("The result matrix")
print(result)








