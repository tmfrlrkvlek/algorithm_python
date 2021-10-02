// 1012
// dfs

#include <stdio.h>

using namespace std;

int m, n, k;
bool** map;

void dfs(int i, int j){
	// 방문한 노드 이동불가 처리 
	map[i][j] = false;
	
	// 인접노드 idx 저장
	int array[4][2] = {{-1, -1},{-1,-1},{-1,-1},{-1,-1}};
	if(i > 0) {array[0][0] = i - 1; array[0][1]= j;} 				// 위 노드 
	if(i < n - 1) {array[1][0] = i + 1; array[1][1] = j;}			// 아래 노드 
	if(j != 0) {array[2][0] = i; array[2][1] = j - 1;}			// 좌측 노드 
	if(j != m - 1) {array[3][0] = i; array[3][1] = j + 1;}		// 우측 노드 
	for(int p = 0; p < 4; p++){
		// 해당 노드에 이미 방문한 적 있으면 continue 
		if(array[p][0] == -1) continue; 
		// 해당 노드로 이동이 가능하면 dfs 실행 
		if(map[array[p][0]][array[p][1]] == 1){
			dfs(array[p][0], array[p][1]);
		}
	}
}


int main(void){
	
	int T;
	scanf("%d", &T);		//test case 개수 입력 
	
	// test case 개수만큼 반복 
	while(T--){
		
		// 가로길이, 세로길이, 배추 개수 입력 
		scanf("%d %d %d", &m, &n, &k);
		 
		map = new bool*[n];
		for(int i = 0; i < n; i++){
			map[i] = new bool[m]{false};
		} 
		
		
		// 배추 위치 입력 
		for(int i = 0; i < k; i++){
			int x, y;
			scanf("%d %d", &x, &y);
			map[y][x] = true;
		}
		
	
		int sum = 0;	// 필요한 지렁이 개수 
		// 모든 칸 방문 
		for(int i = 0; i < n; i++){
			for(int j = 0; j < m; j++){
				// 배추가 있는 위치면 dfs 실행 
				if(map[i][j]) {
					dfs(i, j);
					sum++;
				}
			}
		}
		// 필요한 지렁이의 개수 출력 
		printf("%d\n", sum);
		
	} 
	
}

