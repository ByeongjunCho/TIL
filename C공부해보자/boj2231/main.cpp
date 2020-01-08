#include <iostream>
#define MAX 1000000
/* run this program using the console pauser or add your own getch, system("pause") or input loop */
/* 백준 2231 - 분해합 */

int divideArr[MAX] = {0,};
// 분할합 리턴하는 함수 
int divSum(int num)
{	
	int tmp = num;
	int sum = num;
	while(tmp){
		sum += tmp%10;
		tmp /= 10;
	}
	return sum;
}

int getDivMin(int num)
{
	int tmp = num;
	int numCount = 0;
	int firstNum = 0;
	int result = 0;
	while(tmp){
		numCount += 1;
		firstNum = tmp%10;
		tmp /= 10;
	}
	
	for(int i = num-(9*(numCount-1) + firstNum); i<=num; i++){
		result = divSum(i);
		if(result == num)
			return i; 
	}
	
	return 0;
} 

int main(int argc, char** argv) {
	int N;
	scanf("%d", &N);
	printf("%d", getDivMin(N));
	return 0;
}
