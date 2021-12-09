#include<stdio.h>
#include<string.h>
#include<math.h>

int iPrime(int n)
{

	int sqrtNum;
	int m = 1;
	if (2 > n||(2 != n&&n%2 == 0))
	{
		m = 0;
		return m;
	}
	sqrtNum = sqrt(n);
	int j;
	for (j = 3; j <= sqrtNum; j++)
	{
		if (0 == n % j )
		{
			m = 0;
			break;
		}
	}
	return m;
}

int main()
{
	int N;
	scanf("%d",&N);
	int i;
	for (i = 2; i <= N / 2; i++)
	{
		int j = N - i;
		if (iPrime(i) && iPrime(j))
		{
			printf("%d = %d + %d",N,i,j);
			break;
		}
	}
	return 0;
}

