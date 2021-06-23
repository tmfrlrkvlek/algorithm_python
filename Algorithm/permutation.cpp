#include <stdio.h>
#include <algorithm>

int main(){
	int A[] = {1, 2, 3};
	do {
		printf("%d %d %d\n", A[0], A[1], A[2]);
	}while(std::next_permutation(A, A+3));
}