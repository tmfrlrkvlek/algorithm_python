#include <stdio.h>

int main(void){
	int L, P, V, sum = 0, count = 0;
	scanf("%d %d %d", &L, &P, &V);
	while(V != 0){
		
		sum += (V / P) * L;
		V %= P;
		if(V / L > 0){
			sum += L;
		}else{
			sum += V;
		}
		printf("Case %d: %d\n", ++count, sum);
		sum = 0;
		scanf("%d %d %d", &L, &P, &V);
	} 
}
