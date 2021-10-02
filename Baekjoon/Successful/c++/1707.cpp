// 1707
// dfs 

#include <stdio.h>
#include <vector>

using namespace std;
vector<int> *graph;

int *checked;

bool dfs(int num, int before){
	// 해당 노드가 이전 노드와 같은 값이면 이분 그래프가 아님. 
	if(checked[num] == before){
		return false;
	}else if(checked[num] == 0){	// 해당 노드를 방문한 적 없으면 
		// 해당 노드에 이전 노드와 다른 값 입력 
		if(before == 1) checked[num] = 2;
		else checked[num] = 1;
		// 해당 노드에 연결되어 있는 간선 수만큼 반복 
		for(int i = 0; i < graph[num].size(); i++){
			// 만약 dfs한 return 값이 false면 false 반환 
			if(!dfs(graph[num][i], checked[num])){
				return false;
			}
		}
		// 모든 인접한 노드에 대한 dfs return값이 true면 true 반환 
		return true;
	}
	// 해당 노드를 방문한 적 있으면 true 반환 
	return true;	
}

int main(void){
	
	// test case 개수 입력 
	int k;
	scanf("%d", &k);
	
	// test case 개수만큼 반복 
	while(k--){
		// 노드 수, 간선 수 입력 
		int v, e;
		scanf("%d %d", &v, &e);
		// 방문 여부, 노드 종류 저장 
		checked = new int[v + 1]{0};	// 0 : 방문 x, 1, 2: 노드 종류 
		// 간선 정보 입력 
		graph = new vector<int>[v + 1];
		for(int i = 0; i < e; i++){
			int n1, n2;
			scanf("%d %d", &n1, &n2);
			graph[n1].push_back(n2);
			graph[n2].push_back(n1);
		}
		// 이분 그래프 판별 결과 저장 
		bool result = true;
		// 모든 노드에 대해 반복 
		for(int i = 1; i < v + 1; i++){
			// 아직 방문한 적 없으면 dfs 진행 
			if(checked[i] == 0){
				// 최종 return 값이 false면 NO 출력 후 break 
				if(!(result = dfs(i, 2))) {
					printf("NO\n");
					break;
				}
			}
		}
		// 최종 return값이 true면 YES 출력 
		if(result) printf("YES\n");
	}
}
