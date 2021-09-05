// 1024
#include <stdio.h>

int main(void){

    long long num;
    long long len;
    scanf("%lld %lld", &num, &len);
    
    for(long long l = len; l <= 100; l++ ){
        long long start = num - l * (1 + l) / 2;
        if(start % l == 0 && start / l + 1 >= 0){
            start = start / l;
            for(long long i = 1; i <= l; i++){
                printf("%lld ", start + i);
            }
            return 0;
        }
    }
    printf("-1");
    return 0;
}

// start + 1 + start + 2 + start + 3 ... start + len
// start * len + (1 + len ) * len / 2 = num
// start len = num - (1 + len) * len / 2
// start = num / len - (1 + len) / 2