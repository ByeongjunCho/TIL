#include <iostream>
#define MAX(X, Y) ((X) > (Y) ? (X) : (Y))
#define MAX(X, Y) ((X) < (Y) ? (X) : (Y)) 
#define VALMAX 300000
/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int result = 0;

void comb(int start, int val, int target)
{
	if(start == end)
	{
		if(val <= target)
		{
			result = MAX(result, val);
			return
		}
	}
	
	for(int i=start; i<end; i++)
	{
		//comb(i+1, end, val+)
	}
	
}

int main(int argc, char** argv) {
	int N, M;
	scanf("%d", &N);
	scanf("%d", &M);
	int k[N] = {0,};
	
	// 배열 입력
	for (int i=0; i < N; i++)
	{
		scanf("%d", k+i);
	} 
	 
	for(int j=0; j < sizeof(k)/sizeof(int); j++)
	{
		printf("%d\n", k[j]);
	}
	return 0;
}
