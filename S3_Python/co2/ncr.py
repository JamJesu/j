"""**********************************************************
 Name:Jeswin Antony M                         Class:S3 IT
  Roll No:20                                  Date:17-12-2021

		              nCr
***********************************************************"""
def fact(n):
	res=1;
	for x in range (2,n+1):
		res=res*x
	return res
def ncr(n,r):
	print(fact(c)/(fact(r)*fact(c-r)))
c=int(input("enter the N \n"))
r=int(input("enter the R \n"))
ncr(c,r)

"""
        Sample Output
enter the N 
5
enter the R 
3
10.0
"""
        
