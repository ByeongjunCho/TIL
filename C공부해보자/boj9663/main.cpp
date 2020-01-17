// น้มุ 9663 N-Queen 
#include <iostream>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int queen(int k, int *col, int **chess, int size, int *result)
{
	if(k==size)
	{
		*result += 1;
		return 0;
	}
	
	for(int j=0; j<size; j++)
	{
		if(col[j] || checkQueen(k, j, size, chess)){
			continue;
		}
		col[j] = 1;
		chess[k][j] = 1;
		queen(k+1, col, chess, size, result);
		col[j] = 0;
		chess[k][j] = 0;

	}
	return 0;
}

int checkQueen(int y, int x, int size, int** chess)
{
	int tmpy = y;
	int tmpx = x;
	
	while(tmpy>=0 && tmpx>=0)
	{
		if(chess[tmpy][tmpx])
		{
			return 1;
		}
		tmpy -= 1;
		tmpx -= 1;
	}
	while(tmpy<size && tmpx<size)
	{
		if(chess[tmpy][tmpx])
		{
			return 1;
		}
		tmpy += 1;
		tmpx += 1;
	}
	
	return 0;
}
int main(int argc, char** argv) {
	int N;
	scanf("%d", &N);
	int chess[N][N] = {{0,},};
	int col[N] = {0,};
	int result = 0;
	int *resultPtr;
	resultPtr = &result;
	
	queen(0, col, chess, N, result);
	printf("%d", result);
	return 0;
}
