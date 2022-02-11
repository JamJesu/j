/****************************************************************
  Name:Jeswin Antony M                           Class:S3 IT
  Roll No:20                                     Date:29/11/2021
	
							Binary search
  ***************************************************************/
						
#include<stdio.h>
#include<conio.h>

main()
{
	int a,val,i,pos=-1;
	printf("enter the size of array \n");
	scanf("%d",&a);
	int arr[a];
	printf("enter the elements of array in sorted  \n");
	for(i=0;i<a;i++)
	{
		scanf("%d",&arr[i]);	
	}
	printf("enter the elements to be searched \n");
	scanf("%d",&val);
	int low=0,high=a,mid;
	while(low<=high)
	{
		mid=(low+high)/2;
		if(arr[mid]==val)
		{
			pos=mid;
			printf("The element is found at %d and location at %d \n",mid+1,mid);
			break;
		}
		else if(arr[mid]>val)
			high=mid-1;
		else
			low=mid+1;
	}
	if(pos==-1)
	{
			printf("value not found");
	}
	getch();
}

/*Sample Output:
enter the size of array
5
enter the elements of array in sorted
1
2
3
4
5
enter the elements to be searched
3
The element is found at 3 and location at 2
*/			
			
		
		

	
