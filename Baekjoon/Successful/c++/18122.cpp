// 18122

// 내 알고리즘
// n = (pow(2, n + 2) - 5) % 1000000007;

#include <stdio.h>
#include <cmath>

using namespace std;

int main(void){
	int n;
	long long k = 1; 
	scanf("%d", &n);
	while (n != -2) {
		k = (k * 2)% 1000000007;
		n--;
	}
	printf("%lld", k - 5);
}

// best code

// #include <stdio.h>
// typedef long long ll;
// #define DIVNUM 1000000007

// using namespace std;

// int main(void){
// 	int n;
// 	scanf("%d", &n);
// 	n += 2;
// 	ll k = 1; 
// 	ll x = 2;
// 	while(n){ 
// 		if(n & 1) k = (k * x) % DIVNUM;
// 		x = (x * x) % DIVNUM;
// 		n >>= 1;
// 	}
// 	printf("%lld", (k - 5 + DIVNUM) % DIVNUM);
// }


