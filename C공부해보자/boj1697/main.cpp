#include <iostream>
#include <deque>

#define MAXSIZE 100000
/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int 
int bfs(int start, int target)
{
	int cnt = 0;
	std::deque<int> q;
	q.push_back(start);
	while(!q.empty())
	{
		cnt += 1;
		int current = q.front();
		q.pop_front();
		if(0 <= current+1 <= MAXSIZE)
		{
			if(current+1 == target)
				return cnt;
			q.push_back(current+1);
		}
		if(0 <= current-1 <= MAXSIZE)
		{
			q.push_back(current-1);
			if(current-1 == target)
				return cnt;
		}
		
		if(0 <= current*2 <= MAXSIZE)
		{
			q.push_back(current*2);
			if(current*2 == target)
				return cnt;
		}
	}
	
}

int main(int argc, char** argv) {
	int N, K;
	std::ios::sync_with_stdio(false);
	std::cin >> N >> K;
	bfs(N, K);
	//std::cout << bfs(N, K);
	
	return 0;
}
