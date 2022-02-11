/****************************************************************
  Name:Jeswin Antony M                             Class:S3 IT
  Roll No:20                                       Date:6/12/2021
	
							 Insertion Sort
  ****************************************************************/
						


//						
#include<stdio.h>
#include<conio.h>

main()
{
	int a,i,j,key;
	printf("enter the size of array \n");
	scanf("%d",&a);
	int arr[a];
	printf("enter the elements of array  \n");
	for(i=0;i<a;i++)
	{
		scanf("%d",&arr[i]);	
	}
	for(i=1;i<a;i++)
	{
		key=arr[i];
		j=i-1;
		while(arr[j]>key&&j>=0)
		{
			arr[j+1]=arr[j];
			j--;
		}
		arr[j+1]=key;
	}
		printf("the sorted array \n");
	for(i=0;i<a;i++)
	 	printf("%d ",arr[i]);
	getch();
}	

/*********************************
	Sample Output
enter the size of array
6
enter the elements of array
10
5
-4
0
5
3
the sorted array
-4 0 3 5 5 10
***********************************/	
		
	
