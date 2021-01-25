// InsertionSort·Î ±¸Çö 
#include<iostream>
using namespace std;

int main(void){
	int n, temp;
	cin >> n;
	int *array = new int[n];
	cin >> array[0];
	for(int i = 1; i < n; i++){
		cin >> array[i];
		int j = i;
		while((array[j] < array[j - 1])&&(j > 0)){
			temp = array[j];
			array[j] = array[j - 1];
			array[j - 1] = temp;
			j--;
		}
	}
	for(int i = 0; i < n; i++){
		cout << array[i] << endl;
	}
}
