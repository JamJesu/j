/****************************************************************
  Name:Jeswin Antony M                            Class:S3 IT
  Roll No:20                                      Date:6/12/2021
	
							 Selection Sort
  ****************************************************************/
						


//			
#include<stdio.h>
#include<conio.h>

main()
{
	int a,i,pos=-1,temp,j;
	printf("enter the size of array \n");
	scanf("%d",&a);
	int arr[a];
	printf("enter the elements of array  \n");
	for(i=0;i<a;i++)
	{
		scanf("%d",&arr[i]);	
	}
	for(i=0;i<a-1;i++)
	{
			pos=i;
			for(j=i+1;j<a;j++)
			{
				if(arr[pos]>arr[j])
					pos=j;
			}
			if(pos!=i)
			{
				temp=arr[i];
				arr[i]=arr[pos];
				arr[pos]=temp;
			}
			
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
-3
0
-4
8
1
3
the sorted array
-4 -3 0 1 3 8
***********************************/


	
