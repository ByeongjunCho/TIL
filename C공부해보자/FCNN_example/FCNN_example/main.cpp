#include "VectorND.h"

void main()
{

	int a[] = { 1,2,3 };
	double b[] = { 3,4,5 };


	VectorND<double> vec1(3);
	vec1[0] = 1;
	vec1[1] = 2;
	vec1[2] = 3;
	VectorND<double> vec2(vec1);
	std::cout << vec1 << std::endl;

}