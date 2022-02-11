#include<stdio.h>
#include<conio.h>
main()
{
	int n,i,key,j;
	printf("enter the no of elements \n");
	scanf("%d",&n);
	int a[n];
	printf("enter the elements \n");
	for(i=0;i<n;i++)
		scanf("%d",&a[i]);
	for(i=1;i<n;i++)
	{
		key=a[i];
		j=i-1;
		while(key<a[j]&&j>=0)
		{
				a[j+1]=a[j];
				j--;
		}
		a[j+1]=key;
	}
	printf("the sorted array \n");
	for(i=0;i<n;i++)
	{
			printf("%d ",a[i]);
	}
	getch();
			
	
}
