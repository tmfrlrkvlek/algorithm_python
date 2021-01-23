// 2178
// bfs

#include <stdio.h>
#include <queue>

using namespace std;


int main(void){
	
	int n, m;
	scanf("%d %d", &n, &m);
	// 노드 & 간선 정보 저장 
	int nodenum = n * m;
	int map[nodenum];
	// 노드 별 p1부터의 거리 저장 
	int dist[nodenum]={1, 0};
	
	// 간선 정보 입력 
	for(int i = 0; i < nodenum; i++){
		scanf("%1d", &map[i]);
	}
	
	// 방문해야할 노드 저장 & 시작 노드 p1으로 지정 
	queue<int> queue({0});

	// queue가 비어있을때까지 반복 
	while(!queue.empty()){
		// queue에 들어온 지 가장 오래된 노드 now에 입력 
		int cur = queue.front();
		// queue에 들어온 지 가장 오래된 원소 삭제 
		queue.pop();
		
		// 현재 위치가 p2면 기록한 거리 출력 후 종료 
		if (cur == nodenum - 1){
			printf("%d", dist[cur]);
			return 0;
		}else{
			// 인접노드 idx 저장 
			int array[4] = {-1, -1, -1, -1};
			if(cur >= m) array[0] = cur - m; 			// 위 노드 
			if(cur < nodenum - m) array[1] = cur + m;	// 아래 노드 
			if(cur % m != 0) array[2] = cur - 1;		// 좌측 노드 
			if(cur % m != m - 1) array[3] = cur + 1;	// 우측 노드 
			for(int i = 0; i < 4; i++){
				int idx = array[i];
				// 해당 노드로 이동이 불가능하거나 해당 노드에 이미 방문한 적 있으면 continue 
				if(idx == -1 || map[idx] == 0 || dist[idx] != 0) continue; 
				//해당 노드까지의 거리 = 이전 노드까지의 거리 + 1
				dist[idx] = dist[cur] + 1;
				// queue에 추가 
				queue.push(idx);
			}
		}
	}
}
