// 14425

#include <stdio.h>
#include <iostream>
#include <string>
#include <unordered_set>
using namespace std;

int main(void){

    unordered_set<string> us;
    int n, m;
    scanf("%d %d", &n, &m);

    for(int i = 0; i < n ; i++){
        std::string s;
        cin >> s;
        us.insert(s);
    }

    int count = 0;
    for(int i = 0; i < m ; i++){
        std::string s;
        cin >> s;
        if(us.find(s) != us.end()) count++;
    }
    printf("%d", count);
}