// 1260
// 그래프 탐색 dfs, bfs 문제 

#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;

// 각 노드 방문 여부 
bool *checked;
// 간선 정보 
int first[10000] = {0}; 
int second[10000] = {0};
int m;

void dfs(int start){
	if(checked[start] == true){
		return;
	}else{
		checked[start] = true;
		printf("%d ", start + 1);
		int array[m + 2] = {0};
		int idx = 0;
		// 해당 노드와 연결되어 있는 노드 array에 모음 
		for(int i =0; i < m; i++){
			if(first[i] == start + 1){
				array[idx++] = second[i];
			}
			if(second[i] == start + 1){
				array[idx++] = first[i];
			}
		}
		// array 오름차순 정렬 
		sort(array, array + idx);
		// dfs 재귀적으로 진행 
		for(int i = 0; i < idx; i++){
			dfs(array[i] - 1);
		}
	}
	return;
}

void bfs(int start){
	printf("\n");
	// 방문해야할 노드들 누적 
	vector<int> queue;
	queue.push_back(start + 1);
	// 방문해야할 노드가 더이상 없을 때 까지 반복 
	while(queue.size() != 0){
		// queue에 들어온 지 가장 오래된 노드 now에 입력 
		int now = queue[0] - 1;
		// queue에 들어온 지 가장 오래된 원소 삭제 
		queue.erase(queue.begin());
		// 이미 방문한 노드면 생략 
		if(checked[now] == true){
			continue;
		}else{	
		// 이미 방문한 노드가 아니면 탐색 진행 
			int st = queue.size();
			checked[now] = true;
			printf("%d ", now + 1);
			// 해당 노드와 연결되어 있는 노드를 array에 모음 
			for(int i =0; i < m; i++){
				if(first[i] == now + 1){
					queue.push_back(second[i]);
				}
				if(second[i] == now + 1){
					queue.push_back(first[i]);
				}
			}
			// 방금 추가한 노드들만 오름차순 정렬 
			sort(queue.begin() + st, queue.end());
		}
	}
}

int main(void){
	// n 정점의 개수, m 간선의 개수, 탐색을 시작할 정점의 번호 start 입력 
	int n, start;
	scanf("%d %d %d", &n, &m, &start);
	checked = new bool[n];
	// 간선 정보 입력 
	for(int i = 0; i < m; i++){
		int n1, n2;
		scanf("%d %d", &n1, &n2);
		first[i] = n1;
		second[i] = n2;
	}
	// checked 초기화 
	for(int i = 0; i < n; i++){
		checked[i] = false;
	}
	// dfs
	dfs(start - 1);
	// checked 초기화 
	for(int i = 0; i < n; i++){
		checked[i] = false;
	}
	// bfs
	bfs(start - 1);
	return 0;
}
