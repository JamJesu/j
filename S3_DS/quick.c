/****************************************************************
  Name:Jeswin Antony M                            Class:S3 IT
  Roll No:20                                      Date:13/12/2021
	
						 Quick Sort
  ****************************************************************/
#include<stdio.h>
#include<conio.h>
void qs(int a[],int f,int l)
{
	int p,i,j,temp;
	if(f<l)
	{
		p=f;
		i=f;
		j=l;
		while(i<j)
		{
			while(a[i]<=a[p]&&i<l)
				i++;
			while(a[j]>a[p]&&j>f)
				j--;
			if(i<j)
			{
				temp=a[i];
				a[i]=a[j];
				a[j]=temp;
			}
			else
			{
			
				temp=a[p];
				a[p]=a[j];
				a[j]=temp;
			}
		}
	qs(a,f,j-1);
	qs(a,j+1,l);
	}
	
}
main()
{
	int n,i;
	printf("enter the no of elements: \n");
	scanf("%d",&n);
	int a[n];
	printf("enter the elements: \n");
	for(i=0;i<n;i++)
		scanf("%d",&a[i]);
	qs(a,0,n-1);
	printf("the sorted array \n");
	for(i=0;i<n;i++)
		printf("%d ",a[i]);
}
/*******************************
	Sample Output:	
enter the no of elements:
5
enter the elements:
0
1
-4
3
8
the sorted array
-4 0 1 3 8
********************************/

