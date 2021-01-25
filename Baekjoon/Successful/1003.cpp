// 1003
// recursive function

#include <stdio.h>

using namespace std;

int* countFibonacci(int num){
	int* arr = new int[2]{0};
	if (num == 0){
		arr[0]++;
	}else if(num == 1){
		arr[1]++;
	}else{
		arr = countFibonacci(num - 1);
		int temp = arr[1];
		arr[1] += arr[0];
		arr[0] = temp;
	}
	return arr;
}

int main(void){
	
	int t;
	scanf("%d", &t);
	while(t--){
		int n;
		scanf("%d", &n);
		int *arr = countFibonacci(n);
		printf("%d %d\n", arr[0], arr[1]);
	}
}
