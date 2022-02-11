/****************************************************************
  Name:Jeswin Antony M                            Class:S3 IT
  Roll No:20                                      Date:29/11/2021
	
							Linear search
  ****************************************************************/
						

#include<stdio.h>
#include<conio.h>

main()
{
	int a,e,i,pos=0;
	printf("enter the size of array \n");
	scanf("%d",&a);
	int arr[a];
	printf("enter the elements of array \n");   
	for(i=0;i<a;i++)
	{
		scanf("%d",&arr[i]);	
	}
	printf("enter the elements to be searched \n");
	scanf("%d",&e);
	for(i=0;i<a;i++)
	{
		if(arr[i]==e)
		{
			printf("the element found at %d and loction at %d  \n",i+1,i);
			pos++;
		}
	}
	if(pos==0)
	{
		printf("element not found \n");
	}
	
	getch();
	
	
}
/*Sample Ouput:
enter the size of array
5
enter the elements of array
4
3
2
8
1
enter the elements to be searched
4
the element found at 1 and loction at 0
*/


