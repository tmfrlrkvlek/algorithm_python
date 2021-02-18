// 11652

#include <stdio.h>
#include <iterator>
#include <unordered_map>
using namespace std;

int main(void){
    unordered_map<long long, long long> hm;
    int n;
    scanf("%d", &n);
    while(n--){
        long long c;
        scanf("%lld", &c);
        unordered_map<long long, long long>::iterator cnt = hm.find(c);
        if(cnt != hm.end()){
            hm[c] = cnt->second + 1;
        }else{
            hm.insert(make_pair(c, 1));
        }
    }
    long long k, v = 0;
    for(auto i : hm){
        if(i.second >= v){
            if(i.second == v && i.first > k) continue;
            k = i.first;
            v = i.second;
        }
    }
    printf("%lld", k);
}
