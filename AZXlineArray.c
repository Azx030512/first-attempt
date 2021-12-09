#include<stdio.h>
#include<stdlib.h>
#include<string.h>
struct lineArray{
	int number;
	struct lineArray *next;
}*head,*node,*end;
int main()
{
	int number;
	char name[10];
	printf("Please input number of student:\n");
	scanf("%d",&number);
	/*printf("Than enter the name:\n");
	scanf("%s",name);*/
	head->number=number;
	/*strcpy(head->name,name);*/
	end=head;
	while(number!=0){
		printf("Input the number:\n");
		scanf("%d",name);
		node=(struct lineArray*)malloc(sizeof(struct lineArray));
		node->number=number;
		end->next=node;
		end=node;
	}
	end->next=NULL;
	return 0;
}
