#include<stdio.h>
int main(void)
{
	int i,flag=0;
	char ch;
	const char *color[5]={"red","blue","yellow","green","black"};
	printf("Input a letter:");
	ch=getchar();
	for(i=0;i<5;i++){
		if(*color[i]==ch){
			flag=1;
			puts(color[i]);
		}
	}
	printf("%s",color[1]);
	if(flag==0){
		printf("Not found\n");
	}
	return 0;
}
