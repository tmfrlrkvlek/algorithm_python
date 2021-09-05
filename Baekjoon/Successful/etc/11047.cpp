#include <stdio.h>

int main(void){
	int N;
	long long K, sum = 0;
	
	scanf("%d %lld", &N, &K);
	int *A = new int[N];
	for(int i = 0; i < N; i++){
		scanf("%d", &A[i]);
	}
	for(int i = N - 1; i >= 0; i--){
		sum += K / A[i];
		K %= A[i];
	}
	printf("%lld", sum);
}
