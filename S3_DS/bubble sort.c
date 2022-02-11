/****************************************************************
  Name:Jeswin Antony M                            Class:S3 IT
  Roll No:20                                      Date:29/11/2021
	
						 Bubble Sort
  ****************************************************************/
#include<stdio.h>
#include<conio.h>

main()
{
	int a,val,i,pos=-1,temp,j;
	printf("enter the size of array \n");
	scanf("%d",&a);
	int arr[a];
	printf("enter the elements of array  \n");
	for(i=0;i<a;i++)
	{
		scanf("%d",&arr[i]);	
	}
	for(i=a;i>0;i--)
	{
		for(j=0;j<i-1;j++)
		{
			if(arr[j]>arr[j+1])
				{
					temp=arr[j];
					arr[j]=arr[j+1];
					arr[j+1]=temp;                                                                        
					 
				
				}
		}
	}
	printf("the sorted array \n");
	for(i=0;i<a;i++)
	 	printf("%d ",arr[i]);
	getch();
	
}

/******************************
	Sample Ouput:
enter the size of array
6
enter the elements of array
-5
0
5
6
3
2
the sorted array
-5 0 2 3 5 6
******************************/

	
		
