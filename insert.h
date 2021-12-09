#include<stdio.h>

void insert(int a[],int *p)
{
	int value;
	printf("Please input the value you want to insert\n");
	scanf("%d",&value);
	a[*p]=value;
	*p++;
	extern void sort(int a[],int left,int right);
	sort(a,0,*p);
	
}
