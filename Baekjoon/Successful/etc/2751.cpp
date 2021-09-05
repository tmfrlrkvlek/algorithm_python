#include <stdio.h>

void swap(long long a[], long long idx1, long long idx2){
	long long temp = a[idx1];
	a[idx1] = a[idx2];
	a[idx2] = temp;
}

void heapify(long long a[], long long idx){
	long long root = 0;
	long long child = root * 2 + 1;
	while(child + 1 < idx){
		
		if(a[child] < a[child + 1]){
			child++;
		}
		if (a[root] < a[child]){
			swap(a, root, child);
			root = child;
			child = root * 2 + 1;
		}
		else return;
	}
	if (child + 1 != idx) return;
	else{
		if (a[root] < a[child]){
			swap(a, root, child);
		}
		else return;
	}
}

int main(void){
	long long num;
	scanf("%lld", &num);
	
	long long *array = new long long[num];
	
	scanf("%lld", &array[0]);
	for (long long i = 1; i < num; i++){
		scanf("%lld", &array[i]);
		long long idx = i;
		long long root = (idx - 1) / 2;
		while(idx > 0){
			if(array[idx] > array[root]){
				swap(array, idx, root);
				idx = root;
			}
			else break;
			root = (idx - 1) / 2;
		}
	}
	
	for (long long i = num - 1; i > 0; i--){
		swap(array, 0, i);
		heapify(array, i);
	}
	
	for(long long i = 0; i < num; i++){
		printf("%lld\n", array[i]);
	}
	
}

