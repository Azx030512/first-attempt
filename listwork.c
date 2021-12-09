#include<stdio.h>
#include"insert.h"
#include"delete.h"
#include"modify.h"
#include"query.h"
#define ARRAY_SIZE(array) ((int) (sizeof(array)/sizeof(array[0])))
int main()
{
	int a[50];
	int n;
	printf("Enter thr element number n:\n");
	scanf("%d",&n);
	printf("Enter a query in turn \n");
	int i;
	for(i=0;i<n;i++){
		scanf("%d",&a[i]);
	}
	void sort(a[],int n);
	sort(a,n);
	int choice;
	while(1){
		printf("[1] Insert\n[2] Delete\n[3] Modify[4] Query[Other option] End");
		scanf("%d",&choice);
		switch(choice){
			case 1:insert(a[],n);break;
			case 2:adelete(a[],n);break;
			case 3:modify(a[],n);break;
			case 4:query(a[],n);break;
		}
		if(choice<1||choice>4){
			break;
		}
	}
}









