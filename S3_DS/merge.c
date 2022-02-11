/****************************************************************
  Name:Jeswin Antony M                            Class:S3 IT
  Roll No:20                                      Date:13/12/2021
	
						 Merge Sort
  ****************************************************************/
#include<stdio.h>
#include<conio.h>
int a[20],b[20],i;
void merge(int low,int mid,int high)
{
	int l1,l2,i;
	for(l1=low,l2=mid+1,i=low;l1<=mid&&l2<=high;i++)
	{
		if(a[l1]<a[l2])
			b[i]=a[l1++];
		else
			b[i]=a[l2++];
			
	}
	while(l1<=mid)
		b[i++]=a[l1++];
	while(l2<=high)
		b[i++]=a[l2++];
	for(i=low;i<=high;i++)
		a[i]=b[i];
	
}
void sort(int low,int high)
{
		int mid;
		if(low<high)
		{
			mid=(low+high)/2;
			sort(low,mid);
			sort(mid+1,high);
			merge(low,mid,high);
			
			
		}
}
main()
{
	int q,i;
	printf("enter the no of elements:");
	scanf("%d",&q);
	printf("enter the elements \n");
	for(i=0;i<q;i++)
	{
		scanf("%d",&a[i]);
	}
	sort(0,q-1);
	printf("the sorted \n");
	for(i=0;i<q;i++)
		printf("%d ",a[i]);
	
}
/*******************************
	Sample Output:
enter the no of elements:5
enter the elements
0
-2
5
2
8
the sorted
-2 0 2 5 8
********************************/


