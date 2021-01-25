#include <stdio.h>
#include <algorithm>

using namespace std;

int main(void){
	int N, L;
	scanf("%d %d", &N, &L);
	int *H = new int[N];
	
	for(int i = 0; i < N; i++){
		scanf("%d", &H[i]);
	}
	sort(H, H + N);
	for(int i = 0; i < N; i++){
		if(H[i] <= L){
			L++;
		}else{
			break;
		}
	}
	printf("%d", L);
}
