#include<stdio.h>
int dividesearch(int a[],int n,int value)
{
	int i=0,j=n-1;
	int mid;
	while(i<j){
		mid=(i+j)/2;
		if(a[mid]==value){
			return mid;
		}else if(a[mid]<value){
			i=mid+1;
		}else if(a[mid]>value){
			j=mid-1;
		}
	}
	if(i>=j){
		printf("Not found\n");
		return -1;
	}
	
}
