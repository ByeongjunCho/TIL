#include <iostream>
#define MAX(X, Y) ((X) > (Y) ? (X) : (Y))
#define MIN(X, Y) ((X) < (Y) ? (X) : (Y)) 
/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int result = 0;
int N, M;
int *arr;
int comb(int k, int cnt, int val)
{
	if (result == M || val > M){
		return 0;
	}
	if(cnt == 3)
	{
		if (val <= M){
			result = MAX(result, val);	
		}
		return 0;
	}
	
	for(int i = k; i < N; i++)
	{
		comb(i+1, cnt+1, val+arr[i]);
	}
	return 0;
}

int main(int argc, char** argv) {
	scanf("%d", &N);
	scanf("%d", &M);
	
	arr = new int[N];
	
	// 배열 입력
	for (int i=0; i < N; i++)
	{
		scanf("%d", arr+i);
	} 
	comb(0, 0, 0);
	printf("%d", result);
	return 0;
}
