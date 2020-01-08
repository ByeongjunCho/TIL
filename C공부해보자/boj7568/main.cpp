#include <iostream>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	int N;
	scanf("%d",&N);
	
	int **peoples = new int*[N];
	int ranks[N] = {0,};
	
	for(int i=0; i<N; i++)
	{
		peoples[i] = new int[2];	
	}
	
	for(int cnt=0; cnt<N; cnt++)
	{
		scanf("%d %d", peoples[cnt], peoples[cnt]+1);
	}
	
	for(int i=0; i<N; i++)
	{
		for(int j=0; j<N; j++)
		{
			if((peoples[i][0] < peoples[j][0]) && (peoples[i][1] < peoples[j][1])){
				ranks[i] += 1;
			}
		}
	}
	for(int cnt=0; cnt<N; cnt++)
	{
		if(cnt==N-1){
			printf("%d", ranks[cnt]+1);
		}
		else{
			printf("%d ", ranks[cnt]+1);
		}
		
	}
	
	
	for(int j=0; j<N; j++)
	{
		delete[] peoples[j];
	}
	delete[] peoples;
	return 0;
}
