// baekjoon 16964
#include <stdio.h>
#include <vector>
#include <queue>

using namespace std;

// 정점 개수 N, 정점 1~ n까지 번호가 매겨져있는 양방향 그래프 

// 같은 깊이의 순서 변경 관련 에러 해결 못한 상태. 

queue<int> answers;

void DFS(int x, vector<int> graph[], bool checked[]) {
    if (checked[x] == true || answers.back()==-1) {
        return;
    }
    checked[x] = true;
    int ans = answers.front();
    answers.pop();
    if(ans != x){
    	printf("0");
    	answers.push(-1);
    	return;
	}
    // x를 방문
    for (int i = 0; i < graph[x].size(); i++) {
    	int idx = graph[x][i];
        if (checked[idx] == false) {
            DFS(idx, graph, checked);
        }
    }
}

int main(void){
	int n;
	scanf("%d", &n);
	vector<int> graph[n + 1];
	bool checked[n] = {false};
	
	for (int i = 0; i < n - 1; i++){
		int n1, n2;
		scanf("%d %d", &n1, &n2);
		graph[n1].push_back(n2);
		graph[n2].push_back(n1);
	}
	
	for(int i = 0; i < n; i++){
		int ans;
		scanf("%d", &ans);
		answers.push(ans);
	}
	
	DFS(1, graph, checked);
	
	if(answers.back()!=-1){
		printf("1");
	}
	
}
