// 10989
// 계수정렬 사용 

#include <stdio.h>

using namespace std;


int main(void){
	int n;
	scanf("%d", &n);
	int count[10000] = {0};
	
	for(int i = 0; i < n; i++){
		int num;
		scanf("%d", &num);
		count[num - 1]++;
	}
	for(int i = 0; i < 10000; i++){
		for(int j = 0; j < count[i]; j++){
			printf("%d\n", i + 1);
		}
	}
	
}
