#include<stdio.h>
int search(int list[],int n,int x)
{
	int i,r=-1;
	for(i=0;i<n;i++){
		if(list[i]==x){
			r=i;
		}
	}
	return r;
}
void sort(int list[],int left,int right)
{
	if(left>=right){
		return ;
	}
	int i=left;
	int j=right;
	int key=list[left];/*key is acting like an empty bottle*/
	while(i<j)
	{
		while(i<j&&key<=list[j]){
			j--;
		}
		list[i]=list[j];/*three bottle:key list[i] list[j] complete the mission*/
		while(i<j&&list[i]<=key){
			i++;
		}
		list[j]=list[i];
	}
	list[i]=key;
	sort(list,left,i-1);
	sort(list,i+1,right);
}

int main()
{
	int i;
	int list[20],n;
	int index;
	int x;
	printf("Enter digits number n:\n");
	scanf("%d",&n);
	for(i=0;i<n;i++){
		scanf("%d",&list[i]);
	}
	printf("Please input a number you want search\n");
	scanf("%d",&x);
	index=search(list,n,x);
	printf("The index of %d is %d\n",x,index);
	sort(list,0,n-1);
	printf("After quicksort the list is:\n");
	for(i=0;i<n;i++){
		printf("%4d",list[i]);
	}
	return 0;
	
	
	
}
