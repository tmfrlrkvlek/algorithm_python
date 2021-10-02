#include <stdio.h>

int main(void){
	int N, distance;
	long long price, total = 0;
	scanf("%d", &N);
	int *L = new int[N - 1];
	long long *P = new long long[N];
	for (int i = 0; i < N - 1; i++){
		scanf("%d", &L[i]);
	}
	scanf("%lld", &P[0]);
	price = P[0];
	distance = L[0];
	for (int i = 1; i < N; i++){
		scanf("%lld", &P[i]);
		if(P[i] < price || i == N - 1){
			total += price * distance;
			distance = L[i];
			price = P[i];
		}else{
			distance += L[i];
		}
	}
	printf("%lld", total);
}
