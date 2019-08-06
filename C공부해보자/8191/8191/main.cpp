#include <iostream>
using namespace std;

// 시간 초과로 안됨
int comicbook(int *p, int N)
{
	int count = 0;  // 카운트 변수
	int idx = 0;  // 인덱스 변수
	int k = 1; // 만화책 권

	while (true)
	{
		if (idx == N) { // 인덱스가 한바퀴 돌았다면 idx를 0으로 변환
			idx = 0;   
			count += 1;
			if (k == N+1) break;
		}


		if (p[idx] == k) // 만화책을 찾았다면
		{
			k += 1;  // 다음 만화책을 찾기 위해 +1을 한다.
		}
		
		idx += 1;
		

	}
	return count;
}

int main(int argc, char** argv)
{
	int test_case;
	int T;
	
	cin >> T;
	
	for (test_case = 1; test_case <= T; ++test_case)
	{
		int N;
		cin >> N;
		int *p = new int[N];
		for (int i = 0; i < N; i++)
		{
			cin >> p[i];
		}

		cout << "#" << test_case << " " << comicbook(p, N) << endl;
		delete[] p;
	
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}