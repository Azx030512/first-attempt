#include<stdio.h>
#include<stdlib.h>
int bubble(int *p,int n)
{
	int i,j,t;
	if((p=(int *)calloc(n,sizeof(int)))==NULL){
		printf("Not able to allocate the room.\n");
		exit(1);
	}
	for(i=1;i<n;i++){
		for(j=0;j<n-i;j++){
			if(p[j]<p[j+1]){
				t=p[j];
				p[j]=p[j+1];
				p[j+1]=t;
			}
		}
	}
	return 0;
}
int main(void)
{
	int i;
	int b[]={0,1,2,3,4,5,6,7,8,9};
	int c[]={65,4684,-85,12,65,45};
	bubble(b,10);
	bubble(c,6);
	for(i=0;i<10;i++){
		printf("%d ",b[i]);
	}
	printf("\n");
	for(i=0;i<6;i++){
		printf("%d ",c[i]);
	}
	return 0;
}
