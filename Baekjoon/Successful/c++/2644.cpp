// 2644
// bfs

#include <stdio.h>
#include <vector>
#include <queue>

using namespace std;


int main(void){
	
	int n, p1, p2, m;
	scanf("%d", &n);
	scanf("%d %d", &p1, &p2);
	scanf("%d", &m);
	// 노드 & 간선 정보 저장 
	vector<int> family[n + 1];
	// 노드 별 p1부터의 거리 저장 
	int dist[n + 1]={0};
	
	// 간선 정보 입력 
	for(int i = 0; i < m; i++){
		int n1, n2;
		scanf("%d %d", &n1, &n2);
		family[n1].push_back(n2);
		family[n2].push_back(n1);
	}
	
	// 방문해야할 노드 저장 & 시작 노드 p1으로 지정 
	queue<int> queue({p1});

	// queue가 비어있을때까지 반복 
	while(!queue.empty()){
		// queue에 들어온 지 가장 오래된 노드 now에 입력 
		int cur = queue.front();
		// queue에 들어온 지 가장 오래된 원소 삭제 
		queue.pop();
		
		// 현재 위치가 p2면 기록한 거리 출력 후 종료 
		if (cur == p2){
			printf("%d", dist[cur]);
			return 0;
		}else{
			int max = family[cur].size();
			// 해당 노드에 연결되어 있는 간선 수만큼 반복 
			for(int i = 0; i < max; i++){
				// 연결되어있는 노드 번호  
				int p = family[cur][i];
				// 해당 노드에 이미 방문한 적 있으면 continue 
				if(dist[p] != 0) continue;
				//해당 노드까지의 거리 = 이전 노드까지의 거리 + 1
				dist[p] = dist[cur] + 1;
				// queue에 추가 
				queue.push(p);
			}
			// 해당 노드 간선 정보 초기화 더이상 필요 없음 
			family[cur].clear();
		}
	}
	// 두 노드가 연결되어 있지 않을 경우 -1 출력  
	printf("%d", -1);
}
