#include<stdio.h>
#define MAXN 8
double a[MAXN][MAXN];
double check1(double a[][8],int n)
{
	int i,j;
	int found=1;
	for(j=0;j<n;j++){
		for(i=j;i<n;i++){
			if(a[i][j]!=0){
				found=0;
			}
		}
	}
	return found;
}
double check2(double a[][8],int n,int k)
{
	int i,j;
	double cal;
	int found=1;
	for(i=k+1;i<n;i++){
		if(a[i][k]!=0){
			found=0;
		}
		if(found==0){
			cal=1.0*a[i][k]/a[k][k];
			for(j=0;j<n;j++){
				a[i][j]=a[i][j]-cal*a[k][j];
				printf("process\n");
			}
		}
	}
	return 0;

}
int main()
{
	int n,i,j;
	printf("Please enter a n level ÐÐÁÐÊ½\n");
	printf("Enter n as the length and width:\n");
	scanf("%d",&n);
	printf("Then enter the numbers in turn\n");
	double a[MAXN][MAXN];
	for(i=0;i<n;i++){
		for(j=0;j<n;j++){
			scanf("%lf",&a[i][j]);
		}
	}
	int number=0;
	while(check1(a,n)==0&&number<1){
		for(j=0;j<n;j++){
			check2(a,n,j);
		}
		number++;
	}
	double result=1;
	for(i=0;i<n;i++){
		result=result*a[i][i];
	}
	for(i=0;i<n;i++){
		for(j=0;j<n;j++){
			printf("%.5lf  ",a[i][j]);
		}
		printf("\n");
	}
	printf("result=%lf",result);
	return 0;
}
