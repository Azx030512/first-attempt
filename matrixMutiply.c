#include<stdio.h>
int main()
{
	int length1,width1,length2,width2,length3,width3;
	int i,j,m;
	printf("Please input the length and width of the two matrix seperately\n");
	printf("Give you an examplebelow.\n");
	printf("           		width        \n			4 0 1 3 5\n			5 9 7 -1 3\n		length  4 7 3 1 0\n			5 4 8 1 6\n");
	printf("Input the first matrix's length and width\n");
	scanf("%d%d",&length1,&width1);
	printf("Input the second matrix's length and width\n");
	scanf("%d%d",&length2,&width2);
	printf("Then enter the matrix's element in turn\n");
	length3=length1;
	width3=width2;
	int a[length1][width1],b[length2][width2],c[length3][width3];
	for(i=0;i<length1;i++){
		for(j=0;j<width1;j++){
			scanf("%d",&a[i][j]);
		}
	}
	printf("Then enter the next matrix's element in turn\n");
	for(i=0;i<length2;i++){
		for(j=0;j<width2;j++){
			scanf("%d",&b[i][j]);
		}
	}
	for(i=0;i<length3;i++){
		for(j=0;j<width3;j++){
			int result=0;
			for(m=0;m<width2;m++){
				result=result+a[i][m]*b[m][j];	
			}
			c[i][j]=result;
		}
	}
	for(i=0;i<length3;i++){
		for(j=0;j<width3;j++){
			printf("%d ",c[i][j]);
		}
		printf("\n");
	}
}
	

