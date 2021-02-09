// 1024
#include <stdio.h>

int main(void){

    long long num;
    long long len;
    scanf("%lld %lld", &num, &len);
    while(num % 2 == 0 && len % 2 == 0 && len <= 100){
        len++;
    }
    if(len + 1> 100){
        printf("-1");
    }else{
        for(long long i = -(len/2); i <= len/2; i++){
            printf("%lld ", num/len + i);
        } 
    }
}