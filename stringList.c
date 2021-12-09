#include<stdio.h>
int main()
{
	int i,flag=0;
	char ch;
	const char *color[5]={"red","blue","yellow","green","black"};
	const char **pc;
	pc=color;
	printf("Input a letter:");
	ch=getchar();
	for(i=0;i<5;i++){
		if(**(pc+i)==ch){
			flag=1;
			puts(*(pc+i));
		}
	}
	/*printf("%c",*(*(color)+2));*/
	if(flag==0){
		printf("Not Found\n");
	}
	return 0;
}
