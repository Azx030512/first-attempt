#include<stdio.h>
#include"devidesearch.h"
void adelete(int a[],int *p)
{
	int value;
	int index;
	int i;
	printf("Please input an value\n");
	scanf("%d",&value);
	extern void devidesearch(int a[],int n,int value);
	index=devidesearch(a,*p,value);
	if(index=-1){
		return ;
	}else{
		*p--;
		for(i=index;i<(*p)+1;i++){
			a[i]=a[i+1];
		}
	}
}
