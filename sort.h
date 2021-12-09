#include<stdio.h>
extern int n;
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


