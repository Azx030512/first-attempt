#include<stdio.h>
#include<string.h>
void fsort(char color[][20],int n);
int main(void)
{
	int i;
	char pcolor[5][20];
	for(i=0;i<5;i++){
		scanf("%s",pcolor[i]);
	}
	fsort(pcolor,5);
	for(i=0;i<5;i++){
		printf("%s ",pcolor[i]);
	}
	return 0;
}
void fsort(char color[][20],int n)
{
	int k,j;
	char *temp;
	for(k=1;k<n;k++){
		for(j=0;j<n-k;j++){
			if(strcmp(color[j],color[j+1])>0){
				strcpy(temp,color[j]);
				strcpy(color[j],color[j+1]);
				strcpy(color[j+1],temp);
			}
		}
	}
}
