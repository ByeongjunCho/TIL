#include <iostream>
using namespace std;

// �ð� �ʰ��� �ȵ�
int comicbook(int *p, int N)
{
	int count = 0;  // ī��Ʈ ����
	int idx = 0;  // �ε��� ����
	int k = 1; // ��ȭå ��

	while (true)
	{
		if (idx == N) { // �ε����� �ѹ��� ���Ҵٸ� idx�� 0���� ��ȯ
			idx = 0;   
			count += 1;
			if (k == N+1) break;
		}


		if (p[idx] == k) // ��ȭå�� ã�Ҵٸ�
		{
			k += 1;  // ���� ��ȭå�� ã�� ���� +1�� �Ѵ�.
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
	return 0;//��������� �ݵ�� 0�� �����ؾ��մϴ�.
}