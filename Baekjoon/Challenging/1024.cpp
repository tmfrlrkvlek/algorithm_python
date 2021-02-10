// 1024
#include <stdio.h>

int main(void){

    long long num;
    long long len;
    scanf("%lld %lld", &num, &len);
    while((num % len != 0) && len <= 100){
        len++;
    }
    if(len > 100 || num / len < ( len / 2 )){
        printf("-1");
        return 0;
    }
    for(long long i = -(len / 2); i <= len / 2; i++){
        printf("%lld ", num/len + i);
    }
}


// 18 3
// --> 5 6 7
// 20 5
// --> 3 4 5 6 7
// 30 3
// --> 9 10 11
// 23 5

